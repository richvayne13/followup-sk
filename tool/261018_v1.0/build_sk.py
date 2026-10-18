# -*- coding: utf-8 -*-
"""
build_sk.py
SK하이닉스 양산기술 지원 맞춤형 심층 꼬리질문 & 방어 답변 대시보드 빌드 파이프라인.
"""

import json
import os
import sys
import traceback

from ui_engine import render_dashboard_html, render_master_markdown
from sk_modules_part1 import SK_MODULES_PART1
from sk_modules_part2 import SK_MODULES_PART2

BASE_DIR = r"C:\Work\꼬리질문_SK"
RESULT_DIR = os.path.join(BASE_DIR, "result", "261018_v1.0")
LIVE_URL = "https://richvayne13.github.io/followup-sk/"


def main():
    try:
        os.makedirs(RESULT_DIR, exist_ok=True)
        modules = SK_MODULES_PART1 + SK_MODULES_PART2

        html = render_dashboard_html(
            page_title="SK하이닉스 양산기술 면접 심층 꼬리질문 & 100점 방어 답변 마스터 대시보드",
            sidebar_title="SK하이닉스 양산기술 꼬리질문",
            sidebar_subtitle="Context 전 항목 기반 압박 꼬리질문 & 방어 바이블",
            header_badge="🔥 SK하이닉스 양산기술(P&T / FAB) 실전 면접 완벽 대비",
            header_title="SK하이닉스 양산기술 심층 꼬리질문 & 100점 방어 답변 대시보드",
            header_desc=(
                "<code>context/현대자동차_경력면접대비.docx</code>에 수록된 모든 경력·프로젝트(웹게이지 미세라인 EMA·동적임계치, "
                "Die Shim 100:1 웜기어·LVDT 전동화, 100만 장 Burr 이원화 Valley·1×7 Bridge Kernel 비전 엔진, IPQC 월 40시간 자동화, "
                "New-form factor 양산 셋업, 본·기·함·구 AI 프로토콜, 건조·기계요소 물리)를 <strong>SK하이닉스 양산기술 직무 관점</strong>으로 "
                "완벽히 매핑하여 총 <strong>8개 핵심 파트 · 36개 실전 꼬리질문과 방어 답변</strong>으로 구축했습니다."
            ),
            accent_primary="#38bdf8",
            modules=modules,
            storage_prefix="followup_sk"
        )

        root_html = os.path.join(BASE_DIR, "index.html")
        res_html = os.path.join(RESULT_DIR, "index.html")
        for p in (root_html, res_html):
            with open(p, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"[OK] Generated {p} ({len(html):,} bytes)")

        md = render_master_markdown(
            title="SK하이닉스 양산기술 심층 꼬리질문 & 방어 답변 마스터 보고서",
            live_url=LIVE_URL,
            local_path=root_html,
            modules=modules
        )
        md_path = os.path.join(RESULT_DIR, "261018_sk_followup_master.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)
        with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
            f.write(md)
        with open(os.path.join(BASE_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
            f.write("\n")
        print(f"[OK] Generated {md_path}")

    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
