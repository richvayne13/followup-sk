# -*- coding: utf-8 -*-
"""
ui_engine.py
심층 꼬리질문 & 방어 답변 인터랙티브 HTML 대시보드 및 마스터 보고서(MD) 생성 엔진.
"""

import re
from datetime import datetime


def render_dashboard_html(
    page_title: str,
    sidebar_title: str,
    sidebar_subtitle: str,
    header_badge: str,
    header_title: str,
    header_desc: str,
    accent_primary: str,
    modules: list,
    storage_prefix: str = "followup_sk"
) -> str:
    total_modules = len(modules)
    total_qas = sum(len(m.get("qas", [])) for m in modules)

    # 1. 좌측 사이드바 네비게이션 생성
    nav_items = []
    for idx, m in enumerate(modules, start=1):
        num_str = f"{idx:02d}"
        m_id = f"mod-{num_str}"
        active_cls = " active" if idx == 1 else ""
        qa_cnt = len(m.get("qas", []))
        nav_items.append(
            f'      <li class="nav-item"><a href="#{m_id}" class="nav-link{active_cls}">'
            f'<span class="nav-num">{num_str}</span>'
            f'<span class="nav-text">{m["nav_title"]} <small style="color:#38bdf8;font-weight:700;">({qa_cnt}문항)</small></span></a></li>'
        )
    nav_list_html = "\n".join(nav_items)

    # 2. 본문 모듈 섹션 생성
    sections_html = []
    global_q_idx = 1
    for idx, m in enumerate(modules, start=1):
        num_str = f"{idx:02d}"
        m_id = f"mod-{num_str}"
        sec_cls = "topic-section latest-card-highlight" if idx == 1 else "topic-section"

        summary_lis = "\n".join([f"          <li>{s}</li>" for s in m["context_summary"]])

        qa_cards = []
        for q_item in m.get("qas", []):
            q_num_str = f"Q{global_q_idx:02d}"
            global_q_idx += 1
            qa_card = f"""
          <div class="qa-card">
            <div class="qa-question-header">
              <span class="qa-badge">{q_num_str} · 심층 꼬리질문</span>
              <span class="qa-tag">{q_item.get("tag", "핵심 검증")}</span>
              <h4 class="qa-question-title">“{q_item["question"]}”</h4>
            </div>
            <div class="qa-intent-box">
              <strong>🎯 평가자 질문 의도 &amp; 방어 핵심 전략:</strong> {q_item["intent"]}
            </div>
            <div class="qa-answer-box">
              <div class="qa-answer-label">💬 실전 100점 방어 답변 (구두 전달용 완성본)</div>
              <div class="qa-answer-text">{q_item["answer"]}</div>
            </div>
          </div>"""
            qa_cards.append(qa_card)

        qa_cards_html = "\n".join(qa_cards)

        svg_block = ""
        if m.get("svg"):
            svg_block = f"""
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            {m.get("svg_title", "📊 핵심 메커니즘 & 아키텍처 도해")}
          </div>
          {m["svg"]}
        </div>"""

        base_speech_block = ""
        if m.get("base_speech"):
            base_speech_block = f"""
        <div class="base-speech-box">
          <div class="base-speech-title">🎙️ [Base Speech] 이 주제의 출발점 45초 핵심 답변 (꼬리질문 유도용 베이스)</div>
          <div class="base-speech-body">{m["base_speech"]}</div>
        </div>"""

        sec_html = f"""
    <!-- MODULE {num_str} : {m["title"]} -->
    <section class="{sec_cls}" id="{m_id}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">PART {num_str}</span>
          <span class="latest-tag">{m["badge"]}</span>
          <h2 class="topic-title">{m["title"]}</h2>
        </div>
      </div>

      <div class="interview-summary-card">
        <span class="summary-tag">📄 Context 원문 핵심 스펙 &amp; 직무 매핑 요약</span>
        <ul class="summary-list">
{summary_lis}
        </ul>
      </div>

      <div class="lecture-content">
{base_speech_block}
{svg_block}
        <h3>🔥 예상 심층 꼬리질문 &amp; 100점 방어 답변 체인 ({len(m.get("qas", []))}문항)</h3>
        <div class="qa-chain-container">
{qa_cards_html}
        </div>
      </div>
    </section>"""
        sections_html.append(sec_html)

    sections_str = "\n".join(sections_html)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>{page_title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
  <style>
    :root {{
      --bg-body: #0b0f19;
      --bg-card: #131b2e;
      --bg-sidebar: #0f172a;
      --border: #222f49;
      --text-main: #f1f5f9;
      --text-sub: #cbd5e1;
      --text-muted: #64748b;
      --accent-blue: {accent_primary};
      --accent-amber: #f59e0b;
      --accent-green: #10b981;
      --summary-bg: linear-gradient(135deg, rgba(14, 165, 233, 0.12) 0%, rgba(99, 102, 241, 0.12) 100%);
      --summary-border: #0284c7;
      --shadow-lg: 0 10px 25px -5px rgba(0,0,0,0.5);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background-color: var(--bg-body);
      color: var(--text-main);
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    body.sidebar-collapsed aside {{
      transform: translateX(-100%);
    }}

    body.sidebar-collapsed main {{
      margin-left: 0;
      max-width: 100%;
      padding: 40px 80px 100px;
    }}

    .drawer-toggle-btn {{
      background: rgba(30, 41, 59, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      border-radius: 6px;
      padding: 5px 11px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .drawer-toggle-btn:hover {{
      background: #0284c7;
      color: #ffffff;
    }}

    .drawer-float-open-btn {{
      position: fixed;
      top: 18px;
      left: 18px;
      z-index: 99;
      background: #0f172a;
      border: 1.5px solid #38bdf8;
      color: #38bdf8;
      border-radius: 8px;
      padding: 8px 16px;
      font-size: 0.88rem;
      font-weight: 800;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    }}
    body.sidebar-collapsed .drawer-float-open-btn {{
      display: inline-flex;
    }}

    aside {{
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      width: 380px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      display: flex;
      flex-direction: column;
      z-index: 50;
      box-shadow: var(--shadow-lg);
    }}

    .sidebar-header {{
      padding: 22px 20px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(30,41,59,0.5) 0%, rgba(15,23,42,0) 100%);
    }}

    .sidebar-header h1 {{
      font-size: 1.15rem;
      font-weight: 800;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .sidebar-header p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 6px;
      line-height: 1.4;
    }}

    .search-box {{
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
    }}

    .search-input {{
      width: 100%;
      padding: 9px 13px;
      background-color: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.85rem;
      outline: none;
    }}
    .search-input:focus {{
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }}

    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px 8px;
      list-style: none;
    }}

    .nav-item {{ margin-bottom: 4px; }}

    .nav-link {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 12px;
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      line-height: 1.4;
      font-weight: 500;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
    }}
    .nav-link:hover {{
      background-color: rgba(255, 255, 255, 0.05);
      color: #38bdf8;
      transform: translateX(3px);
    }}
    .nav-link.active {{
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.15), rgba(99, 102, 241, 0.05));
      color: #38bdf8;
      font-weight: 700;
      border-left: 3px solid #38bdf8;
    }}

    .nav-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: #38bdf8;
      background-color: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
      margin-top: 1px;
    }}

    .nav-text {{ flex: 1; word-break: keep-all; }}

    main {{
      margin-left: 380px;
      flex: 1;
      padding: 40px 60px 100px;
      max-width: 1280px;
      transition: all 0.3s ease;
    }}

    header.main-header {{
      margin-bottom: 44px;
      padding-bottom: 22px;
      border-bottom: 1px solid var(--border);
    }}

    .badge-top {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 14px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 20px;
      color: #38bdf8;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 14px;
    }}

    .main-title {{
      font-size: 2.05rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.3;
      margin-bottom: 10px;
    }}

    .main-desc {{
      font-size: 0.98rem;
      color: var(--text-sub);
      line-height: 1.65;
    }}

    .topic-section {{
      background-color: var(--bg-card);
      border: 5px solid #2a3d66;
      border-radius: var(--radius-lg);
      padding: 34px 38px;
      margin-bottom: 52px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
      scroll-margin-top: 25px;
      transition: all 0.25s ease;
    }}
    .topic-section:hover {{
      border-color: #38bdf8;
    }}

    .latest-card-highlight {{
      border: 5px solid #0284c7;
      background: linear-gradient(180deg, rgba(2, 132, 199, 0.08) 0%, var(--bg-card) 100%);
    }}

    .topic-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 22px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }}

    .topic-title-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .topic-badge {{
      background: linear-gradient(135deg, #0284c7, #6366f1);
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
    }}

    .latest-tag {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      color: #10b981;
      font-size: 0.76rem;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 4px;
    }}

    .topic-title {{
      font-size: 1.42rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }}

    .interview-summary-card {{
      background: var(--summary-bg);
      border: 1.5px solid var(--summary-border);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin-bottom: 24px;
    }}

    .summary-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #0284c7;
      color: #ffffff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 12px;
    }}

    .summary-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 9px;
    }}

    .summary-list li {{
      font-size: 0.94rem;
      line-height: 1.65;
      color: #e2e8f0;
      position: relative;
      padding-left: 22px;
    }}

    .summary-list li::before {{
      content: "✔";
      position: absolute;
      left: 0;
      top: 1px;
      color: #38bdf8;
      font-weight: 800;
    }}

    .summary-list li strong {{ color: #38bdf8; }}

    .base-speech-box {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(15, 23, 42, 0.85) 100%);
      border-left: 4px solid #f59e0b;
      border-radius: 0 12px 12px 0;
      padding: 18px 22px;
      margin: 18px 0 24px;
    }}

    .base-speech-title {{
      font-size: 0.92rem;
      font-weight: 800;
      color: #fbbf24;
      margin-bottom: 8px;
    }}

    .base-speech-body {{
      font-size: 0.95rem;
      color: #f8fafc;
      line-height: 1.72;
      font-weight: 500;
    }}

    .lecture-content h3 {{
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--text-main);
      margin: 26px 0 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .lecture-content h3::before {{
      content: "";
      width: 4px;
      height: 18px;
      background: #38bdf8;
      border-radius: 2px;
      display: inline-block;
    }}

    .qa-chain-container {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .qa-card {{
      background: #0d1424;
      border: 1.5px solid #263554;
      border-radius: 14px;
      padding: 22px 24px;
      transition: all 0.2s ease;
    }}
    .qa-card:hover {{
      border-color: #38bdf8;
      box-shadow: 0 6px 24px rgba(56, 189, 248, 0.15);
    }}

    .qa-question-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 12px;
    }}

    .qa-badge {{
      background: #ef4444;
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 5px;
    }}

    .qa-tag {{
      background: rgba(56, 189, 248, 0.14);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: #38bdf8;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
    }}

    .qa-question-title {{
      width: 100%;
      font-size: 1.12rem;
      font-weight: 800;
      color: #fde047;
      line-height: 1.45;
      margin-top: 4px;
    }}

    .qa-intent-box {{
      background: rgba(30, 41, 59, 0.65);
      border-left: 3px solid #38bdf8;
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 0.88rem;
      color: #cbd5e1;
      line-height: 1.6;
      margin-bottom: 14px;
    }}
    .qa-intent-box strong {{ color: #7dd3fc; }}

    .qa-answer-box {{
      background: rgba(16, 185, 129, 0.07);
      border: 1px solid rgba(16, 185, 129, 0.35);
      border-radius: 10px;
      padding: 16px 18px;
    }}

    .qa-answer-label {{
      font-size: 0.8rem;
      font-weight: 800;
      color: #34d399;
      margin-bottom: 8px;
      letter-spacing: 0.02em;
    }}

    .qa-answer-text {{
      font-size: 0.95rem;
      color: #f1f5f9;
      line-height: 1.75;
    }}
    .qa-answer-text strong {{
      color: #6ee7b7;
      font-weight: 700;
    }}

    .mobile-top-bar {{ display: none; }}
    .mobile-fab-container {{ display: none; }}
    .drawer-backdrop {{ display: none; }}

    @media (max-width: 900px) {{
      body {{ flex-direction: column !important; overflow-x: hidden !important; width: 100% !important; }}
      .mobile-top-bar {{
        display: flex !important; position: sticky; top: 0; left: 0; right: 0; height: 52px;
        background: rgba(9, 13, 26, 0.95); backdrop-filter: blur(8px); border-bottom: 1px solid #1e293b;
        padding: 0 14px; align-items: center; justify-content: space-between; z-index: 1000;
      }}
      .mobile-menu-btn {{
        display: inline-flex; align-items: center; gap: 6px; background: #1e293b; color: #38bdf8;
        border: 1px solid #334155; border-radius: 8px; padding: 6px 12px; font-size: 0.85rem; font-weight: 700; cursor: pointer;
      }}
      .mobile-header-title {{ font-size: 0.92rem; font-weight: 800; color: #f8fafc; max-width: 55vw; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
      .mobile-top-btn {{ width: 34px; height: 34px; background: #1e293b; color: #cbd5e1; border: 1px solid #334155; border-radius: 8px; cursor: pointer; }}
      aside {{
        position: fixed !important; top: 0 !important; left: 0 !important; bottom: 0 !important;
        width: 84vw !important; max-width: 320px !important; height: 100vh !important; z-index: 1200 !important;
        transform: translateX(-100%) !important; transition: transform 0.28s ease !important;
      }}
      body.drawer-open aside {{ transform: translateX(0) !important; }}
      .drawer-backdrop {{
        display: block !important; position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 1100;
        opacity: 0; pointer-events: none; transition: opacity 0.25s ease;
      }}
      body.drawer-open .drawer-backdrop {{ opacity: 1 !important; pointer-events: auto !important; }}
      main {{ margin-left: 0 !important; padding: 16px 12px 100px !important; width: 100% !important; max-width: 100vw !important; }}
      .drawer-float-open-btn {{ display: none !important; }}
      .mobile-fab-container {{ display: flex !important; position: fixed; bottom: 24px; right: 16px; gap: 8px; z-index: 950; }}
      .mobile-fab-btn {{
        display: inline-flex; align-items: center; gap: 6px; background: #0284c7; color: #fff;
        border: none; border-radius: 30px; padding: 10px 16px; font-size: 0.86rem; font-weight: 800; cursor: pointer;
      }}
      .topic-section {{ padding: 18px 14px !important; margin-bottom: 24px !important; }}
      .qa-card {{ padding: 16px 14px !important; }}
      .lecture-content div[style*="background:#090d1a"] {{ overflow-x: auto !important; }}
      .lecture-content div[style*="background:#090d1a"] svg {{ min-width: 620px; height: auto; }}
    }}
  </style>
</head>
<body>

  <div class="mobile-top-bar">
    <button class="mobile-menu-btn" onclick="openDrawer()">☰ 목차 ({total_modules}파트 · {total_qas}문항)</button>
    <div class="mobile-header-title">{sidebar_title}</div>
    <button class="mobile-top-btn" onclick="scrollToTop()">⬆</button>
  </div>

  <div id="drawerBackdrop" class="drawer-backdrop" onclick="closeDrawer()"></div>

  <div class="mobile-fab-container">
    <button class="mobile-fab-btn" onclick="openDrawer()">📑 목차 열기</button>
  </div>

  <button id="sidebarFloatOpenBtn" class="drawer-float-open-btn">📑 목차 열기</button>

  <aside>
    <div class="sidebar-header">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1>{sidebar_title}</h1>
        <button id="sidebarCollapseBtn" class="drawer-toggle-btn">◀ 접기</button>
      </div>
      <p>{sidebar_subtitle} (총 {total_modules}개 파트 · {total_qas}개 심층 Q&amp;A)</p>
    </div>
    <div class="search-box">
      <input type="text" id="searchInput" class="search-input" placeholder="키워드 검색 (예: LVDT, EMA, 웜기어, Valley, 본기함구)...">
    </div>
    <ul class="nav-list" id="navList">
{nav_list_html}
    </ul>
  </aside>

  <main>
    <header class="main-header">
      <div class="badge-top">{header_badge}</div>
      <h2 class="main-title">{header_title}</h2>
      <p class="main-desc">{header_desc}</p>
    </header>
{sections_str}
  </main>

  <script>
    const searchInput = document.getElementById('searchInput');
    const sections = document.querySelectorAll('.topic-section');
    const navLinks = document.querySelectorAll('.nav-link');

    searchInput.addEventListener('input', (e) => {{
      const keyword = e.target.value.toLowerCase();
      sections.forEach(sec => {{
        const text = sec.innerText.toLowerCase();
        sec.style.display = text.includes(keyword) ? 'block' : 'none';
      }});
    }});

    window.addEventListener('scroll', () => {{
      let current = '';
      sections.forEach(sec => {{
        const secTop = sec.offsetTop - 130;
        if (window.scrollY >= secTop) current = sec.getAttribute('id');
      }});
      navLinks.forEach(link => {{
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${{current}}`) link.classList.add('active');
      }});
    }});

    const sidebarCollapseBtn = document.getElementById('sidebarCollapseBtn');
    const sidebarFloatOpenBtn = document.getElementById('sidebarFloatOpenBtn');
    if (sidebarCollapseBtn) {{
      sidebarCollapseBtn.addEventListener('click', () => {{
        document.body.classList.add('sidebar-collapsed');
        localStorage.setItem('{storage_prefix}_collapsed', 'true');
      }});
    }}
    if (sidebarFloatOpenBtn) {{
      sidebarFloatOpenBtn.addEventListener('click', () => {{
        document.body.classList.remove('sidebar-collapsed');
        localStorage.setItem('{storage_prefix}_collapsed', 'false');
      }});
    }}
    if (localStorage.getItem('{storage_prefix}_collapsed') === 'true') {{
      document.body.classList.add('sidebar-collapsed');
    }}

    function openDrawer() {{ document.body.classList.add('drawer-open'); }}
    function closeDrawer() {{ document.body.classList.remove('drawer-open'); }}
    function scrollToTop() {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }}

    document.addEventListener('DOMContentLoaded', function() {{
      document.querySelectorAll('#navList a').forEach(function(link) {{
        link.addEventListener('click', function() {{
          if (window.innerWidth <= 900) closeDrawer();
        }});
      }});
    }});
  </script>
</body>
</html>
"""


def render_master_markdown(title: str, live_url: str, local_path: str, modules: list) -> str:
    now_str = datetime.now().strftime("%Y년 %m월 %d일")
    total_qas = sum(len(m.get("qas", [])) for m in modules)
    lines = [
        f"# [보고서] {title}",
        "",
        f"- **작성일자**: {now_str}",
        f"- **배포 대시보드**: [{local_path}](file:///{local_path.replace(chr(92), '/')})",
        f"- **온라인 라이브 URL**: [{live_url}]({live_url})",
        f"- **구성 규모**: 총 {len(modules)}개 핵심 파트 / {total_qas}개 심층 꼬리질문 & 방어 답변",
        "",
        "---",
        "",
        "## 파트별 심층 꼬리질문 & 방어 전략 총람",
        ""
    ]
    q_idx = 1
    for m_idx, m in enumerate(modules, start=1):
        lines.append(f"### PART {m_idx:02d}. {m['title']}")
        for qa in m.get("qas", []):
            lines.append(f"- **Q{q_idx:02d}. {qa['question']}**")
            lines.append(f"  - 🎯 **의도/전략**: {qa['intent']}")
            clean_ans = re.sub(r"<[^>]+>", "", qa["answer"])
            lines.append(f"  - 💬 **방어 답변**: {clean_ans}")
            q_idx += 1
        lines.append("")
    return "\n".join(lines)
