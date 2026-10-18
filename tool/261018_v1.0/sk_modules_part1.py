# -*- coding: utf-8 -*-
"""
sk_modules_part1.py
SK하이닉스 양산기술 맞춤형 심층 꼬리질문 & 방어 답변 (PART 01 ~ PART 04)
"""

SK_MODULES_PART1 = [
    {
        "badge": "지원동기 · 엔지니어링의 본질 · 도메인 전환 방어",
        "nav_title": "지원동기 & 엔지니어링의 본질 (μm ➔ nm 확장)",
        "title": "지원동기 & 엔지니어링의 본질: 마이크로(μm) 공정 성과에서 나노(nm) 반도체 양산기술로의 도약과 AI 결합",
        "context_summary": [
            "<strong>핵심 지원동기</strong>: 현업(LG에너지솔루션 전극 코터)에서 마이크로($\\mu\\text{m}$) 단위 산포를 잡아 수율을 개선한 검증된 엔지니어링 역량과 독자적인 AI 프로토콜을 결합해, 제조 기술의 극한인 <strong>나노($\\text{nm}$) 단위 SK하이닉스 초미세 메모리 양산 수율 혁신</strong>을 주도하고자 지원.",
            "<strong>내가 정의하는 엔지니어링의 본질</strong>: 작업자의 '감(숙련도)'이나 '육안'에 의존하던 불확실한 물리 현상을 <strong>데이터 알고리즘과 정밀 제어 시스템으로 정량화하여 누가 운영해도 흔들리지 않는 재현성(산포 제로, $C_{pk}$ 극대화)을 만드는 것</strong>.",
            "<strong>공정 + AI 양방향 기여</strong>: SK하이닉스가 선도하는 스마트 팹(Smart Fab) 환경에서 현장 설비 물리(HW)와 AI 자동화 파이프라인(SW)을 동시에 다룰 수 있는 하이브리드 양산기술 엔지니어."
        ],
        "base_speech": (
            "“저는 현업에서 배운 엔지니어링 역량과 저만의 AI 엔지니어링 기법을 결합해, 마이크로($\\mu\\text{m}$)를 넘어 나노($\\text{nm}$) 단위의 공정을 다뤄보고 수율 혁신을 주도하기 위해 지원했습니다. "
            "현업에서 여러 프로젝트를 통해 마이크로미터 단위의 공정 안에서 수율을 개선하며 엔지니어링의 본질을 체득했지만, 엔지니어로서 가장 극한의 물리적 한계를 다루는 '나노 단위 초미세 공정'에서 엔지니어링을 경험해 보고 싶다는 갈증이 커졌습니다. "
            "스케일이 마이크로에서 나노로 정밀해질 뿐, 데이터 기반으로 공정 산포($C_{pk}$)를 잡고 설비 이상을 제어하는 양산기술의 본질은 같기에 현업에서 검증된 문제 해결력으로 빠르게 성과를 낼 자신이 있습니다. "
            "특히 SK하이닉스는 양산 현장에 AI를 적극 도입해 스마트 팹 혁신을 선도하고 있습니다. 저 역시 AI를 단순 챗봇으로 쓰는 것을 넘어, 저만의 AI 프로토콜을 구축해 자동화 프로젝트를 진행했는데요, 이 경험을 기반으로 공정과 AI 두 가지 방면으로 기여하겠습니다.”"
        ),
        "svg_title": "📊 [마이크로(배터리 코터) ➔ 나노(SK하이닉스 FAB) 양산기술 핵심 역량 전이 아키텍처]",
        "svg": """<svg viewBox="0 0 960 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="320" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Left: Current Experience (Micro) -->
  <g transform="translate(20, 20)">
    <rect width="290" height="280" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="28" fill="#38bdf8" font-size="12" font-weight="800">1. 현업 검증 역량 (μm 전극 코터 양산)</text>
    <rect x="16" y="44" width="258" height="62" rx="6" fill="#1e293b"/>
    <text x="26" y="64" fill="#fde047" font-size="9.5" font-weight="700">✔ 기구적 숙련도 산포 제거 (HW 개조)</text>
    <text x="26" y="82" fill="#cbd5e1" font-size="8.2">• 100:1 웜기어 + LVDT 실측 위치 피드백</text>
    <text x="26" y="96" fill="#6ee7b7" font-size="8">➔ 셋업 Loss 18% ↓ / 양산 수율 0.2% ↑</text>
    <rect x="16" y="116" width="258" height="62" rx="6" fill="#1e293b"/>
    <text x="26" y="136" fill="#fde047" font-size="9.5" font-weight="700">✔ 육안·약신호의 알고리즘화 (Signal/Vision)</text>
    <text x="26" y="154" fill="#cbd5e1" font-size="8.2">• 웹게이지 EMA+동적임계치 / 100만장 Burr 선별</text>
    <text x="26" y="168" fill="#6ee7b7" font-size="8">➔ 미세라인 Loss 50% ↓ / 5ms·미검률 0%</text>
    <rect x="16" y="188" width="258" height="72" rx="6" fill="#1e293b"/>
    <text x="26" y="208" fill="#fde047" font-size="9.5" font-weight="700">✔ 나만의 AI 에이전트 워크플로우 (AX)</text>
    <text x="26" y="226" fill="#cbd5e1" font-size="8.2">• Context-Tool-Result + 본·기·함·구 빌드업</text>
    <text x="26" y="244" fill="#6ee7b7" font-size="8">➔ IPQC 검토 월 40시간(공수 100%) 완전 자동화</text>
  </g>
  <!-- Center Bridge: Essence of Engineering -->
  <g transform="translate(335, 65)">
    <rect width="290" height="190" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="22" y="30" fill="#a5b4fc" font-size="12" font-weight="800">⚡ 양산 엔지니어링의 본질 (Core Bridge)</text>
    <text x="22" y="58" fill="#ffffff" font-size="9.5" font-weight="700">“모호한 물리 현상과 작업자의 감(숙련도)을</text>
    <text x="22" y="76" fill="#fde047" font-size="9.5" font-weight="800">데이터 알고리즘 &amp; 정밀 제어 루프</text>
    <text x="22" y="94" fill="#ffffff" font-size="9.5" font-weight="700">로 정량화하여 산포(Cpk)를 통제하는 것”</text>
    <line x1="22" y1="112" x2="268" y2="112" stroke="#4338ca" stroke-width="1"/>
    <text x="22" y="134" fill="#cbd5e1" font-size="8.5">• 스케일(μm ➔ nm)이 정밀해질수록</text>
    <text x="22" y="152" fill="#38bdf8" font-size="8.5" font-weight="700">  육안 개입 불가 ➔ 센서 데이터·AI 의존도 극대화!</text>
    <text x="22" y="170" fill="#6ee7b7" font-size="8.5" font-weight="700">• HW 물리 이해 + SW 데이터 모델링 동시 보유</text>
  </g>
  <!-- Right: Target SK hynix Mass Production Engineering -->
  <g transform="translate(650, 20)">
    <rect width="290" height="280" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="28" fill="#10b981" font-size="12" font-weight="800">2. SK하이닉스 양산기술 직무 기여 (nm)</text>
    <rect x="16" y="44" width="258" height="62" rx="6" fill="#1e293b"/>
    <text x="26" y="64" fill="#34d399" font-size="9.5" font-weight="700">🎯 챔버 산포(TTTM) &amp; FDC 약신호 감지</text>
    <text x="26" y="82" fill="#cbd5e1" font-size="8.2">• 잔차 분석 + 동적 임계치(kσ) 기반 이상 조기 포착</text>
    <text x="26" y="96" fill="#94a3b8" font-size="8">• WIW / WTW / C2C 미세 공정 산포(Cpk) 극대화</text>
    <rect x="16" y="116" width="258" height="62" rx="6" fill="#1e293b"/>
    <text x="26" y="136" fill="#34d399" font-size="9.5" font-weight="700">🎯 웨이퍼 결함(ADC) &amp; 계측 데이터 모델링</text>
    <text x="26" y="154" fill="#cbd5e1" font-size="8.2">• 배경 편차 상쇄 및 모폴로지 신호 복원 역량 이식</text>
    <text x="26" y="168" fill="#94a3b8" font-size="8">• 대용량 계측 이미지/시계열 초고속 선별</text>
    <rect x="16" y="188" width="258" height="72" rx="6" fill="#1e293b"/>
    <text x="26" y="208" fill="#34d399" font-size="9.5" font-weight="700">🎯 Smart Fab 엔지니어링 자동화 표준 구축</text>
    <text x="26" y="226" fill="#cbd5e1" font-size="8.2">• 폐쇄망 안전 파이썬 도구(run.bat/GUI) 배포</text>
    <text x="26" y="244" fill="#6ee7b7" font-size="8">➔ 반복 데이터 취합 공수 제로화 &amp; 수율 분석 집중</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "본질 정의 검증",
                "question": "지원동기에서 '현장에서 엔지니어링의 본질을 체득했다'고 하셨는데, 본인이 생각하는 양산 엔지니어링의 본질이 구체적으로 무엇인가요?",
                "intent": "추상적인 미사여구인지, 아니면 실제 본인 프로젝트 경험에서 우러나온 확고한 엔지니어링 철학인지 확인하려는 질문입니다. 본인의 대표 성과 2가지(기구 전동화 + 데이터 알고리즘화)로 즉시 연결해야 합니다.",
                "answer": (
                    "제가 5년간 현장에서 렌치도 직접 쥐어보고 데이터도 뜯어보며 체득한 양산 엔지니어링의 본질은, "
                    "<strong>‘작업자의 감(숙련도)이나 육안에 의존하던 불확실한 물리 현상을, 데이터 알고리즘과 정밀 제어 시스템으로 정량화하여 누가 운영해도 흔들리지 않는 재현성(산포 제로)을 만드는 것’</strong>입니다.<br><br>"
                    "실제로 저는 두 가지 방향으로 이를 증명했습니다. 첫째, 작업자가 수동으로 다이얼게이지를 맞추며 생기던 코팅 폭 편차를 없애기 위해 <strong>100:1 고감속 웜기어와 $\\mu\\text{m}$ 단위 LVDT 변위 센서 기반의 실시간 위치 피드백 전동 제어 시스템</strong>을 구축해 셋업 Loss를 18% 줄이고 수율을 0.2% 개선했습니다. "
                    "둘째, 비전 검사기가 못 잡아 작업자 육안에 의존하던 미세라인과 실오라기 Burr 불량을 <strong>지수이동평균(EMA) 기반 동적 임계치와 $1\\times 7$ Bridge Kernel 비전 알고리즘</strong>으로 수학적 모델링하여 설비가 스스로 잡아내게 만들었습니다. "
                    "이처럼 현장의 물리 현상을 데이터와 제어 루프로 치환해 산포를 통제하는 것이 제가 체득한 엔지니어링의 본질입니다."
                )
            },
            {
                "tag": "도메인 차이 압박",
                "question": "스케일이 마이크로에서 나노로 정밀해질 뿐 양산기술의 본질은 같다고 하셨는데, 배터리 연속(Roll-to-Roll) 공정과 반도체 나노 웨이퍼 공정 사이에서 가장 크게 다른 점은 무엇이며 그 간극을 어떻게 극복하실 건가요?",
                "intent": "배터리 공정과 반도체 FAB 공정의 물리적 차이를 명확히 인지하고 있는지, 그리고 왜 나노 공정에서 본인의 강점이 더 빛을 발하는지 논리적 연결고리를 보는 질문입니다.",
                "answer": (
                    "가장 큰 차이는 <strong>‘공정 환경의 물리적 메커니즘과 직접 개입 가능 여부’</strong>라고 생각합니다. 배터리가 대기압 하에서 유체 슬러리와 열풍 건조를 다루는 연속 웹(Web) 공정이라면, 반도체는 고진공 챔버 내에서 플라즈마·광학·원자 단위 화학 반응을 다루는 매엽/배치식 초미세 박막 공정입니다. 특히 나노 공정에서는 수 옹스트롬($\\text{\\AA}$)의 두께 산포(WIW, WTW)나 열 예산(Thermal Budget), 미세 파티클 하나가 소자의 문턱전압($V_{th}$)과 누설전류를 직접 좌우합니다.<br><br>"
                    "하지만 역설적이게도 <strong>나노 진공 챔버 내부는 사람의 눈으로 볼 수도, 렌치로 수동 조작할 수도 없기 때문에 수많은 FDC 센서 시계열 데이터와 인라인 계측 프로파일에서 미세한 이상 신호(Weak Signal)를 분리해 내는 데이터 엔지니어링의 중요성이 훨씬 더 절대적</strong>입니다. "
                    "제가 현업에서 1% 미만의 미세 로딩 시프트를 잔차 분석과 동적 임계치로 잡아내고, 기구적 백래시를 센서 피드백으로 무효화했던 경험은 나노 공정의 챔버 간 산포(TTTM)와 FDC 이상 감지 업무에 가장 빠르게 안착할 수 있는 무기라고 확신합니다."
                )
            },
            {
                "tag": "이직 사유 압박",
                "question": "LG에너지솔루션에서 핵심 프로젝트 성과도 많이 내셨는데, 굳이 익숙한 배터리 도메인을 떠나 반도체로 오려는 진짜 이유가 뭔가요? 최근 배터리 업황 때문 아닌가요?",
                "intent": "도피성 이직이 아니라 엔지니어로서의 명확한 기술적 지향점(Pull Factor)이 있는지를 검증하는 질문입니다.",
                "answer": (
                    "업황 때문이 아니라, 제가 현업에서 데이터 기반 산포 제어와 AI 엔지니어링 자동화를 깊이 파고들수록 <strong>‘가장 데이터 밀도가 높고 가장 극한의 정밀도를 요구하는 무대에서 내 엔지니어링 방법론을 증명해 보고 싶다’</strong>는 기술적 갈증이 확고해졌기 때문입니다.<br><br>"
                    "배터리 코터에서 마이크로($\\mu\\text{m}$) 단위 산포를 잡고 월 40시간의 데이터 검토 자동화 및 100만 장 비전 선별 엔진을 직접 구축하면서, 하드웨어 물리와 데이터 알고리즘을 결합할 때 수율이 어떻게 바뀌는지 경험했습니다. "
                    "이제는 그 다음 단계로, 수백 개의 공정 스텝과 초미세 나노($\\text{nm}$) 산포가 맞물려 돌아가며 AI 스마트 팹 혁신이 가장 치열하게 일어나는 <strong>SK하이닉스 양산기술 최전선에서 초정밀 공정 제어와 AI 자동화의 정점</strong>을 찍어보고 싶어 지원했습니다."
                )
            },
            {
                "tag": "성과 구체성 검증",
                "question": "본인이 달성한 수율 0.2% 개선(Shim 전동화)과 0.12% 개선(미세라인 감지)이 양산 라인 전체에서 어느 정도의 재무적·실질적 임팩트를 가지는 수치인가요?",
                "intent": "수율 0.1~0.2%라는 숫자의 무게감을 아는 진짜 양산 엔지니어인지 확인하는 질문입니다.",
                "answer": (
                    "양산이 안정화된 성숙 라인에서 수율 0.1~0.2%는 단순한 소수점 숫자가 아니라 <strong>연간 수십억 원 규모의 원재료(양극재·동박/알루미늄박) 폐기 손실을 방어하는 핵심 지표</strong>입니다.<br><br>"
                    "특히 코터 공정은 배터리 원가의 70~80%를 차지하는 활물질 슬러리가 투입되는 첫 단추이기 때문에, 코터에서 발생한 셋업 Loss(18% 절감)와 연속 미세라인 Loss(50% 절감)를 줄인 것은 단순 코터 수율 향상을 넘어 후공정(롤프레스·슬리팅·조립)으로 유입되는 불량 유출 비용과 라인 정지 시간을 동시에 막아낸 고임팩트 성과였습니다. "
                    "반도체 FAB 역시 웨이퍼 한 장, 수율 0.1%가 막대한 영업이익과 직결되는 만큼, 미세 Loss 요인을 끝까지 추적해 수율을 방어하는 집요함으로 기여하겠습니다."
                )
            },
            {
                "tag": "입사 후 포부 구체화",
                "question": "입사 후 '공정과 AI 두 가지 방면으로 기여하겠다'고 하셨는데, 신입이 아닌 경력/중고신입으로 오시면 초반 3개월, 6개월, 1년 동안 각각 어떻게 적응하고 성과를 내실 계획인가요?",
                "intent": "현실적인 온보딩 및 기여 로드맵을 가지고 있는지 확인하는 질문입니다.",
                "answer": (
                    "<strong>초반 3개월</strong>은 담당 단위 공정의 설비 하드웨어 구조, 레시피 파라미터, 그리고 기존 8D 리포트 및 트러블슈팅 이력을 바닥부터 습득하며 도메인 싱크로율을 100%로 끌어올리는 데 집중하겠습니다.<br><br>"
                    "<strong>6개월 차</strong>에는 팀 내에서 매일 반복되는 인라인 계측/FDC 데이터 취합, 헌팅 노이즈 제거, 챔버 간 트렌드 비교 업무를 저만의 <strong>`Context-Tool-Result` 구조와 파이썬 자동화 대시보드(GUI/`run.bat`)</strong>로 구축해 동료 엔지니어들의 단순 반복 공수를 획기적으로 줄이겠습니다.<br><br>"
                    "<strong>1년 차 이후</strong>에는 축적된 공정 물리 이해도와 시계열 신호처리(EMA·동적 임계치·잔차 분석) 역량을 결합해, 미세 공정 산포 드리프트를 사전에 포착하는 알고리즘을 고도화하여 실질적인 양산 $C_{pk}$ 및 수율 개선 성과를 만들어 내겠습니다."
                )
            }
        ]
    },
    {
        "badge": "프로젝트 1 · 시계열 신호처리 · FDC & 가상 계측 연계",
        "nav_title": "[프로젝트 1] 웹게이지 미세라인 감지 로직 (EMA·Dynamic Threshold)",
        "title": "[프로젝트 1] 웹게이지 미세라인 감지 로직 개발: 1% 미만 약신호(Weak Signal) 포착, EMA 위상 지연 극복 및 Dynamic Threshold",
        "context_summary": [
            "<strong>문제 상황 (Issue)</strong>: 양산 코팅 라인에서 비전 검사기의 광학적 한계(조명 반사·간섭)로 잡히지 않는 고질 불량 <strong>‘미세라인’</strong>이 발생하여, 작업자 육안 음영 확인에만 의존하다 보니 지속적인 양산 Loss 발생.",
            "<strong>데이터 분석 및 핵심 솔루션 (Action)</strong>: <strong>100 Lot</strong>의 인라인 웹게이지(베타선/X-ray 스캔 두께·로딩 측정기) 데이터를 심층 분석하여 불량 부위의 <strong>1% 미만 국부적 Data Shift(Dip)</strong>를 확인. ① 신호 지연 없이 최신 추세를 반영하는 <strong>지수이동평균(EMA)</strong>으로 동적 베이스라인 추출, ② 고정 스펙 오검을 막는 <strong>Dynamic Threshold($k\\sigma$)</strong> 적용, ③ <strong>MD 방향 스캔 수와 TD 방향 포인트를 변수화(레시피화)</strong>하여 단발성 노이즈와 실제 연속 결함을 완벽히 분리.",
            "<strong>정량적 성과 (Result)</strong>: 비전 검사기보다 정밀한 감지 로직 완성 ➔ <strong>미세라인 Loss 50% 개선, 전체 양산 수율 0.12% 향상</strong> (반도체 챔버 FDC 이상 감지 및 Virtual Metrology와 100% 직결)."
        ],
        "base_speech": (
            "“양산 코팅 라인에서 비전 검사기에 잡히지 않는 고질 불량인 ‘미세라인’이 발생해 작업자 육안에만 의존하던 문제를, 인라인 웹게이지 로딩 데이터의 시계열 신호처리 로직을 신규 개발해 해결한 경험이 있습니다. "
            "100 Lot의 계측 데이터를 심층 분석한 결과, 미세라인 부위에서 1% 미만의 국부적인 Data Shift가 존재함을 발견했습니다. "
            "이를 센서 노이즈와 구분하기 위해 최근 데이터에 가중치를 두어 위상 지연을 줄인 지수이동평균(EMA)으로 동적 기준선을 세우고, 이동평균선 대비 $k\\sigma$ 이상 벗어날 때만 감지하는 Dynamic Threshold를 적용했습니다. "
            "나아가 MD 주행 방향 연속 스캔 수와 TD 폭 방향 포인트를 레시피 변수화하여 설비 인터록에 연동한 결과, 미세라인 Loss를 50% 절감하고 양산 수율을 0.12% 향상시켰습니다.”"
        ),
        "svg_title": "📊 [웹게이지 1% 미만 미세라인 검출 신호처리 파이프라인] EMA 동적 베이스라인 + 잔차(Residual) 추출 + Dynamic Threshold(kσ) + MD 연속성 필터",
        "svg": """<svg viewBox="0 0 960 310" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="310" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Left Panel: Raw Signal vs EMA Baseline -->
  <g transform="translate(20, 20)">
    <rect width="450" height="270" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">1. Raw 로딩 프로파일 vs 지수이동평균(EMA) &amp; 동적 임계치</text>
    <rect x="16" y="40" width="418" height="165" rx="6" fill="#1e293b"/>
    <!-- Fixed USL/LSL dashed -->
    <line x1="30" y1="60" x2="420" y2="60" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
    <text x="35" y="55" fill="#94a3b8" font-size="7.5">고정 스펙 USL (완만한 드리프트 시 과검 유발)</text>
    <line x1="30" y1="185" x2="420" y2="185" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
    <text x="35" y="197" fill="#94a3b8" font-size="7.5">고정 스펙 LSL (1% 미만 미세 Dip 미검 발생!)</text>
    <!-- EMA Baseline Curve -->
    <path d="M 35 115 Q 150 90 260 120 T 410 105" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="310" y="95" fill="#38bdf8" font-size="8" font-weight="700">EMA 동적 기준선 B(t)</text>
    <!-- Dynamic Threshold Lower Bound (B(t) - k*sigma) -->
    <path d="M 35 140 Q 150 115 260 145 T 410 130" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="5,3"/>
    <text x="275" y="160" fill="#fbbf24" font-size="8" font-weight="700">Dynamic Threshold (B(t) - kσ)</text>
    <!-- Local Dip (<1% Data Shift) piercing Dynamic Threshold -->
    <path d="M 185 108 L 195 168 L 205 110" fill="none" stroke="#ef4444" stroke-width="2.5"/>
    <circle cx="195" cy="168" r="5" fill="#ef4444"/>
    <text x="135" y="180" fill="#fca5a5" font-size="8.5" font-weight="800">★ 1% 미만 미세라인 Dip 포착!</text>
    <text x="16" y="225" fill="#cbd5e1" font-size="8.3">• <tspan fill="#fde047" font-weight="700">단순이동평균(SMA) 한계</tspan>: 과거 N개 균등 평균 ➔ 위상 지연((N-1)/2)으로 결함 늦게 감지</text>
    <text x="16" y="244" fill="#cbd5e1" font-size="8.3">• <tspan fill="#34d399" font-weight="700">지수이동평균(EMA) 도입</tspan>: y[n] = α·x[n] + (1-α)·y[n-1] ➔ 최신 데이터 가중치로 지연 최소화</text>
    <text x="16" y="261" fill="#6ee7b7" font-size="8">➔ 고정 공차(LSL)로는 못 잡는 1% 미만 국부 꺼짐을 동적 임계치(kσ)로 정확히 분리!</text>
  </g>
  <!-- Right Panel: 2D MD/TD Persistence Recipe & Semiconductor FDC Link -->
  <g transform="translate(490, 20)">
    <rect width="450" height="270" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12" font-weight="800">2. 노이즈 vs 실제 미세라인 구분 (MD×TD 레시피화) &amp; 반도체 연계</text>
    <rect x="16" y="40" width="418" height="125" rx="6" fill="#1e293b"/>
    <text x="28" y="60" fill="#fde047" font-size="9.5" font-weight="800">■ 왜 1회성 센서 노이즈에 오알람(과검)이 울리지 않는가?</text>
    <text x="28" y="80" fill="#cbd5e1" font-size="8.5">1) <tspan fill="#38bdf8" font-weight="700">TD(폭 방향) 포인트 그룹화</tspan>: 웹게이지가 폭 방향으로 스윙(Swing) 스캔할 때</text>
    <text x="40" y="96" fill="#94a3b8" font-size="8">특정 TD 좌표 구간에서 발생한 잔차(Residual = Raw - EMA)를 추적</text>
    <text x="28" y="116" fill="#cbd5e1" font-size="8.5">2) <tspan fill="#34d399" font-weight="700">MD(주행 방향) 연속 스캔 카운트 (N회 지속성 검증)</tspan>:</text>
    <text x="40" y="132" fill="#94a3b8" font-size="8">무작위 노이즈는 1스캔에서 소멸하지만, 실제 라인 불량은 주행 방향으로 지속됨</text>
    <text x="40" y="148" fill="#6ee7b7" font-size="8" font-weight="700">➔ 동일 TD 좌표에서 연속 N스캔 이상 동적 임계치 이탈 시에만 설비 알람 트리거!</text>
    <rect x="16" y="175" width="418" height="82" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
    <text x="28" y="196" fill="#a5b4fc" font-size="9.5" font-weight="800">🔗 SK하이닉스 양산기술 직무 직결 포인트 (FDC &amp; APC)</text>
    <text x="28" y="216" fill="#e2e8f0" font-size="8.3">• 반도체 증착/식각 챔버의 RF Power, OES 파장, 압력 시계열 데이터에서도</text>
    <text x="28" y="232" fill="#fde047" font-size="8.3" font-weight="700">  챔버 노화에 따른 완만한 Drift와 국부 Arcing/이상 신호를 분리하는 원리가 100% 동일!</text>
    <text x="28" y="248" fill="#6ee7b7" font-size="8">➔ 미세라인 Loss 50% 절감 · 수율 0.12% 개선 노하우를 FAB FDC 고도화에 즉시 이식</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "물리적 원인 검증",
                "question": "비전 카메라 검사기에는 안 잡히는 미세라인이 왜 웹게이지(두께/로딩 측정기) 데이터에서는 잡혔나요? 물리적 원리가 뭔가요?",
                "intent": "비전 검사기와 방사선(베타선/X-ray) 웹게이지의 측정 원리 차이를 정확히 이해하고 가설을 세웠는지 확인하는 질문입니다.",
                "answer": (
                    "비전 검사기는 전극 표면에 조명을 비춰 반사되는 빛의 밝기(2D 표면 반사광)를 카메라로 찍는 방식입니다. 그런데 슬롯 다이에 미세 이물이 걸리거나 유동이 흔들려 생기는 초기 ‘미세라인’은 표면이 완전히 긁혀 호일이 드러난 스크래치가 아니라, <strong>두께가 완만하게 1% 미만으로 살짝 꺼진 형태(Local Dip)</strong>여서 조명 각도와 난반사에 묻혀 비전 카메라로는 식별되지 않았습니다.<br><br>"
                    "반면 작업자가 측면에서 비스듬히 육안으로 볼 때 미세한 음영 차이가 보인다는 점에 착안해, 저는 <strong>‘음영 차이가 존재한다는 건 반드시 단위 면적당 코팅 질량(Loading Level, $\\text{g/m}^2$)의 물리적 단차가 존재한다’</strong>는 가설을 세웠습니다. 물질 투과 감쇠량을 직접 재는 웹게이지 Raw 데이터를 100 Lot 분석한 결과 실제로 1% 미만의 국부적 Data Shift를 찾아낼 수 있었습니다."
                )
            },
            {
                "tag": "신호처리 심층 검증",
                "question": "노이즈 제거를 위해 단순이동평균(SMA) 대신 지수이동평균(EMA)을 쓰셨다고 했는데, 왜 SMA를 쓰면 안 되나요? 수식이나 원리로 설명해 보세요.",
                "intent": "이력서에 적힌 '지수이동평균(EMA)'을 단순 라이브러리 호출로만 썼는지, 위상 지연(Phase Lag)과 가중치 원리를 이해하고 썼는지 검증하는 핵심 질문입니다.",
                "answer": (
                    "단순이동평균(SMA)은 과거 $N$개의 데이터를 모두 동일한 가중치($1/N$)로 평균 내기 때문에, 윈도우 크기가 커질수록 <strong>$(N-1)/2$ 스캔만큼의 심각한 위상 지연(Phase Lag, 신호 딜레이)</strong>이 발생합니다. 또한 국부적으로 급격한 결함이나 계단식 변화가 생겼을 때 반응이 느려 이미 수백 미터의 불량이 지나간 뒤에야 기준선이 따라가는 문제가 있었습니다.<br><br>"
                    "반면 <strong>지수이동평균(EMA)</strong>은 $y_t = \\alpha x_t + (1-\\alpha) y_{t-1}$ 수식처럼 <strong>가장 최근에 들어온 데이터에 높은 가중치($\\alpha$)를 부여하고 과거 데이터의 영향력은 지수함수적으로 빠르게 잊게 만드는 필터</strong>입니다. 여러 윈도우 크기와 $\\alpha$ 값을 시뮬레이션하여 고주파 센서 노이즈는 억제하면서도 위상 지연을 최소화해 실시간 검출 응답성을 극대화했습니다."
                )
            },
            {
                "tag": "통계적 임계치 검증",
                "question": "Dynamic Threshold(동적 임계치)를 적용하셨다고 했는데, 기존 고정 스펙(USL/LSL)과 무엇이 다르며 $k\\sigma$ 값은 어떻게 설정하셨나요?",
                "intent": "고정 공차(Static Spec)와 동적 임계치(Adaptive Threshold)의 통계적 차이와 과검(False Alarm) 통제 방식을 묻는 질문입니다.",
                "answer": (
                    "코팅 공정 특성상 슬러리 온도나 장력에 따라 전체적인 평균 로딩량이 정상 공차(USL/LSL) 범위 안에서 물결치듯 완만하게 오르내리는 거시적 변동이 존재합니다. 이때 고정된 절대값 기준선을 쓰면 평균 로딩량이 조금만 낮아져도 정상 구간 전체를 불량으로 오검(과검)하고, 평균 로딩량이 높을 때는 1% 미만의 미세라인 꺼짐을 놓치는 미검이 발생했습니다.<br><br>"
                    "그래서 저는 고정 스펙 대신 <strong>EMA로 추정한 실시간 동적 기준선(Baseline)을 중심으로, 국부 표준편차의 $k$배($\\text{Baseline} - k\\sigma$) 또는 $\\Delta X\\%$ 이상 급격히 떨어지는 잔차(Residual)만 잡아내는 Dynamic Threshold</strong>를 설계했습니다. 100 Lot 데이터를 기반으로 정상 산포의 99.7%를 포괄하는 $3\\sigma$ 수준을 기준으로 삼고, 모델별 노이즈 특성에 맞춰 레시피 변수로 튜닝할 수 있게 구현해 오검을 원천 차단했습니다."
                )
            },
            {
                "tag": "레시피 변수화 검증",
                "question": "MD 방향 스캔 수와 TD 방향 포인트를 변수화해서 레시피로 관리했다는 게 구체적으로 어떻게 작동하는 로직인가요?",
                "intent": "웹게이지의 지그재그 스윙(Swing) 스캔 구조(MD 주행 × TD 횡방향 스캔)를 이해하고 2차원 필터를 설계했는지 확인하는 질문입니다.",
                "answer": (
                    "웹게이지는 전극이 주행(MD)하는 동안 센서 헤드가 폭 방향(TD)으로 좌우 왕복(Swing)하며 프로파일을 측정합니다. 만약 1% 미만의 값 튐이 발생할 때마다 알람을 울리면 전기적 스파이크 노이즈 때문에 설비가 계속 멈추게 됩니다.<br><br>"
                    "하지만 <strong>단발성 노이즈는 무작위 위치에서 1번 튀고 사라지는 반면, 실제 미세라인 불량은 다이 립의 특정 폭 위치(TD 포인트)에서 주행 방향(MD)을 따라 연속적으로 이어진다</strong>는 물리적 특성이 있습니다. "
                    "따라서 폭 방향 감지 구간(TD 포인트 범위)과 주행 방향 연속 발생 횟수(MD 연속 $N$ 스캔)를 엔지니어가 모델별로 설정할 수 있도록 레시피 변수화했습니다. 동일한 TD 좌표 구간에서 연속 $N$번 이상 Dynamic Threshold를 벗어날 때만 최종 알람을 울리게 하여 노이즈 오검출을 완벽히 제거했습니다."
                )
            },
            {
                "tag": "반도체 직무 연결",
                "question": "이 웹게이지 미세라인 감지 로직 개발 경험을 SK하이닉스 양산기술 직무에서는 어디에 어떻게 적용할 수 있을까요?",
                "intent": "배터리 계측 경험을 반도체 FAB의 FDC(Fault Detection & Classification) 및 APC/SPC 산포 관리로 연결하는 능력을 평가합니다.",
                "answer": (
                    "SK하이닉스 FAB의 <strong>FDC(설비 이상 감지 및 분류) 고도화와 Virtual Metrology(가상 계측) 산포 관리</strong>에 그대로 적용할 수 있습니다.<br><br>"
                    "예를 들어 CVD/ALD 증착이나 플라즈마 식각 챔버는 PM 주기가 지남에 따라 챔버 벽면 폴리머 퇴적으로 RF 임피던스나 OES(광방출 분광) 베이스라인이 완만하게 드리프트(Drift)합니다. 이때 고정된 FDC 상·하한선만 쓰면 미세한 플라즈마 아킹(Arcing)이나 가스 유량 헌팅 같은 1% 미만의 약신호(Weak Signal) 이상을 놓치거나 과검하게 됩니다. "
                    "제가 구현했던 <strong>EMA 동적 기준선 추출 + 잔차 기반 Dynamic Threshold + 연속성 검증 로직</strong>을 적용하면 챔버 노화 추세와 무관하게 실제 이상 징후만 조기에 포착하여 대량 웨이퍼 스크랩(Scrap)을 막을 수 있습니다."
                )
            }
        ]
    },
    {
        "badge": "프로젝트 2 · 초정밀 기구 메커니즘 · Full Closed-Loop 제어",
        "nav_title": "[프로젝트 2] Die Shim Offset 전동화 (100:1 웜기어·LVDT)",
        "title": "[프로젝트 2] 슬롯 다이 Shim Offset 미세조절장치 전동화 개발: 100:1 웜기어 역구동 방지 및 LVDT 기반 기구적 백래시 무효화",
        "context_summary": [
            "<strong>문제 상황 (Issue)</strong>: 신규 New-form factor 전극 개발/양산에서 고객사의 타이트한 코팅 폭 누적공차 스펙과 $C_{pk}$를 만족해야 했으나, <strong>작업자가 수동으로 다이얼게이지를 돌려 Shim Offset을 조정하는 과정에서 발생하는 작업자 숙련도 편차와 기계적 유격(Backlash)</strong>이 초기 셋업 Loss의 핵심 병목이 됨.",
            "<strong>기구 및 제어 설계 (Action)</strong>: ① 슬러리 토출 압력에 기어가 밀리지 않는 자체 락킹(Self-locking) 특성과 초미세 이송 분해능을 위해 <strong>100:1 고감속비 웜기어(모터 $360^\\circ$ 회전 시 기어 $3.6^\\circ$ 회전 ➔ 심 $1\\,\\mu\\text{m}$ 직진)</strong>와 소형 모터 결합, ② 기어 틈새(백래시)로 인해 모터 펄스만 돌고 실제 기구부가 덜 밀리는 오차를 잡기 위해 <strong>기구부에 직접 맞닿는 고분해능 LVDT 변위 센서</strong>를 부착해 <strong>실시간 위치 피드백(Full Closed-Loop) 제어</strong> 구축.",
            "<strong>정량적 성과 (Result)</strong>: 작업자 숙련도 산포 완전 제거 및 재현성 100% 확보 ➔ <strong>조건조정 셋업 Loss 18% 개선, 전체 양산 수율 0.2% 향상</strong>."
        ],
        "base_speech": (
            "“신규 New-form factor 전극 양산 셋업 당시, 고객사의 타이트한 누적공차 스펙을 맞춰야 했으나 작업자가 수동으로 슬롯 다이 Shim Offset을 조정하며 발생하는 작업자 간 편차가 가장 큰 병목이었습니다. "
            "저는 이 숙련도 산포를 원천 제거하기 위해 미세조절장치의 전면 디지털 전동화를 주도했습니다. "
            " 먼저 슬러리 토출 압력에 기어가 역으로 밀리지 않도록 나사선 리드각 원리를 이용한 100:1 고감속비 웜기어를 채택해 모터 1회전당 $1\\,\\mu\\text{m}$ 단위의 분해능을 확보했습니다. "
            "특히 기어 유격(백래시) 때문에 모터에 100펄스를 줘도 실제로는 덜 움직이는 기계적 한계를 극복하기 위해, 기구부에 직접 닿아 실제 변위를 $\\mu\\text{m}$ 단위로 측정하는 고분해능 LVDT 센서를 부착하여 실시간 위치 피드백 제어 시스템을 완성했습니다. "
            "그 결과 작업자 산포를 완벽히 제거하여 셋업 Loss를 18% 줄이고 양산 수율을 0.2% 개선했습니다.”"
        ),
        "svg_title": "📊 [슬롯 다이 Shim Offset 전동화 아키텍처] 100:1 웜기어(Self-locking) + LVDT 실측 위치 피드백(Full Closed-Loop)을 통한 백래시 무효화",
        "svg": """<svg viewBox="0 0 960 310" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="310" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Left: Mechanical Architecture -->
  <g transform="translate(20, 20)">
    <rect width="470" height="270" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">1. 기구·센서 결합 구조: 왜 100:1 웜기어 + LVDT 풀 클로즈드 루프인가?</text>
    <!-- Block 1: Motor -->
    <rect x="20" y="55" width="110" height="75" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="32" y="80" fill="#38bdf8" font-size="9.5" font-weight="800">소형 서보/스텝 모터</text>
    <text x="28" y="98" fill="#cbd5e1" font-size="8">• 1회전 (360° 구동)</text>
    <text x="28" y="114" fill="#94a3b8" font-size="7.5">• 펄스 입력 제어</text>
    <!-- Arrow -->
    <line x1="130" y1="92" x2="160" y2="92" stroke="#38bdf8" stroke-width="2"/>
    <!-- Block 2: 100:1 Worm Gear -->
    <rect x="160" y="55" width="140" height="75" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="172" y="78" fill="#fde047" font-size="9.5" font-weight="800">100:1 고감속 웜기어</text>
    <text x="170" y="96" fill="#cbd5e1" font-size="8">• 기어 3.6° ➔ 1μm 직진</text>
    <text x="170" y="112" fill="#fca5a5" font-size="7.8" font-weight="700">⚠️ 기어 유격(Backlash) 존재</text>
    <!-- Arrow -->
    <line x1="300" y1="92" x2="330" y2="92" stroke="#f59e0b" stroke-width="2"/>
    <!-- Block 3: Die Shim & LVDT -->
    <rect x="330" y="55" width="120" height="75" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="342" y="78" fill="#34d399" font-size="9.5" font-weight="800">Die Shim 기구부</text>
    <text x="340" y="96" fill="#cbd5e1" font-size="8">• 토출압 역밀림 차단!</text>
    <text x="340" y="112" fill="#6ee7b7" font-size="8" font-weight="700">★ LVDT 직접 접촉 측정</text>
    <!-- Feedback Loop from LVDT back to Controller -->
    <path d="M 390 130 L 390 185 L 75 185 L 75 130" fill="none" stroke="#10b981" stroke-width="2.2" stroke-dasharray="5,3"/>
    <rect x="135" y="168" width="205" height="32" rx="6" fill="#064e3b" stroke="#10b981"/>
    <text x="148" y="188" fill="#6ee7b7" font-size="9" font-weight="800">◀ LVDT 실시간 실측 변위(μm) 피드백</text>
    <text x="20" y="226" fill="#cbd5e1" font-size="8.3">• <tspan fill="#fde047" font-weight="700">웜기어 채택 이유</tspan>: 나사선 리드각 원리(Self-locking)로 슬러리 토출압에 의한 역회전 밀림 원천 차단</text>
    <text x="20" y="246" fill="#cbd5e1" font-size="8.3">• <tspan fill="#34d399" font-weight="700">LVDT 채택 이유</tspan>: 모터 펄스만 믿으면 기어 틈새(백래시)만큼 덜 움직임 ➔ 끝단 실측값 도달 시까지 보정!</text>
  </g>
  <!-- Right: Semi-closed vs Full-closed comparison & Impact -->
  <g transform="translate(508, 20)">
    <rect width="432" height="270" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">2. 제어 공학적 핵심: 모터 엔코더(Semi) vs LVDT(Full Closed-Loop)</text>
    <rect x="16" y="42" width="400" height="105" rx="6" fill="#1e293b"/>
    <text x="28" y="64" fill="#f87171" font-size="9" font-weight="700">❌ 일반 모터 엔코더 제어 (Semi-Closed Loop)의 한계</text>
    <text x="28" y="82" fill="#cbd5e1" font-size="8.2">• 모터에 100펄스 인가 ➔ 모터 축은 100만큼 돌았으나 기어 틈새(Backlash) 때문에</text>
    <text x="28" y="98" fill="#fca5a5" font-size="8.2" font-weight="700">  실제 Shim은 85μm만 이동! (방향 전환 시 치명적 위치 오차 발생)</text>
    <text x="28" y="122" fill="#34d399" font-size="9" font-weight="700">✔ 본 과제 LVDT 직결 제어 (Full Closed-Loop)의 해결</text>
    <text x="28" y="138" fill="#6ee7b7" font-size="8.2">• 기구부 끝단 LVDT가 실제 100μm 이동을 확인할 때까지 추가 펄스 보정 인가!</text>
    <rect x="16" y="158" width="400" height="96" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
    <text x="28" y="180" fill="#a5b4fc" font-size="9.5" font-weight="800">🏆 정량적 성과 &amp; 반도체 장비 엔지니어링 확장성</text>
    <text x="28" y="200" fill="#fde047" font-size="8.5" font-weight="700">• 작업자 숙련도 산포 0%화 ➔ 조건조정 셋업 Loss 18% 절감, 양산 수율 0.2% ↑</text>
    <text x="28" y="218" fill="#cbd5e1" font-size="8.2">• 모터 회전수 대비 코팅폭 변화량 상관식을 실험적으로 정량화하여 HMI 레시피화</text>
    <text x="28" y="236" fill="#38bdf8" font-size="8.2" font-weight="700">• 반도체 노광/식각/패키징 장비의 초정밀 스테이지·밸브 위치 보정 원리와 100% 일치</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "기구 메커니즘 검증",
                "question": "회전운동을 직선운동으로 바꾸는 기구에는 볼스크류나 평기어(Spur Gear)도 있는데, 왜 하필 '웜기어(Worm Gear)'와 '100:1 고감속비'를 선택하셨나요?",
                "intent": "기계공학적 배경지식 없이 남이 만든 걸 쓰기만 한 건지, 실제 공정 환경(슬러리 토출 압력)과 요구 분해능을 계산해 기구 요소를 선정했는지 확인하는 질문입니다.",
                "answer": (
                    "두 가지 명확한 공학적 이유가 있었습니다.<br><br>"
                    "첫째는 <strong>‘역구동 방지(Self-locking)’</strong> 특성 때문입니다. 코팅 중 슬롯 다이 내부에는 높은 슬러리 토출 압력이 걸리는데, 마찰이 적은 일반 기어나 리드가 큰 볼스크류를 쓰면 토출 압력 때문에 기어가 거꾸로 밀려 Shim 위치가 틀어지는 현상이 발생합니다. 웜기어는 나사선의 리드각 원리(경사면을 원통으로 말아놓은 구조)를 이용해 웜이 웜휠을 돌릴 수는 있어도 반대쪽에서 밀면 절대 역회전하지 않는 Self-locking 특성이 있어 채택했습니다.<br><br>"
                    "둘째는 <strong>‘$1\\,\\mu\\text{m}$ 단위의 초미세 분해능 확보’</strong>입니다. 100:1 고감속비를 적용하면 모터가 $360^\\circ$ 한 바퀴를 돌아도 기어는 $3.6^\\circ$만 회전하고, 이를 통해 심(Shim)이 $1\\,\\mu\\text{m}$ 단위로 미세 직진 운동을 하게 되어 수동 조작으로는 불가능했던 정밀 분해능과 높은 구동 토크를 동시에 확보할 수 있었습니다."
                )
            },
            {
                "tag": "제어 루프 심층 검증",
                "question": "모터 자체에 회전수를 재는 엔코더(Encoder)나 펄스 카운터가 있을 텐데, 왜 굳이 비용과 공수를 들여 LVDT 센서를 기구부에 따로 부착하셨나요?",
                "intent": "Semi-Closed Loop와 Full Closed-Loop의 차이, 그리고 기어 백래시(Backlash)의 물리적 한계를 어떻게 극복했는지 찌르는 핵심 질문입니다.",
                "answer": (
                    "모터에 펄스를 100개 줬다고 해서 실제 기구부(Shim)가 정확히 100만큼 움직이지 않기 때문입니다. 감속기와 웜기어 이빨 사이에는 필연적으로 미세한 <strong>기계적 틈새(유격, Backlash)</strong>가 존재합니다. 특히 정방향으로 밀다가 역방향으로 살짝 뺄 때, 모터 축은 돌고 있어도 기어 틈새가 메워질 때까지 실제 Shim은 제자리에 멈춰 있는 헛도는 구간이 발생합니다.<br><br>"
                    "따라서 모터 회전수만 믿는 반폐루프(Semi-Closed Loop) 제어로는 $\\mu\\text{m}$ 단위 누적 공차를 맞출 수 없었습니다. 이를 해결하기 위해 <strong>실제 움직이는 기구부 끝단에 직접 접촉하는 고분해능 LVDT(선형 가변 차동 변압기) 변위 센서를 장착</strong>했습니다. 기어 유격이 얼마든 상관없이 LVDT가 읽은 ‘실제 물리적 이동값’이 타겟값에 도달할 때까지 모터 피드백 제어를 수행하는 <strong>완전 폐루프(Full Closed-Loop)</strong>를 구축해 백래시 오차를 완벽히 무효화했습니다."
                )
            },
            {
                "tag": "정량화 및 시운전 검증",
                "question": "심(Shim)을 $1\\,\\mu\\text{m}$ 움직인다고 해서 실제 호일에 발리는 코팅 폭이 똑같이 $1\\,\\mu\\text{m}$ 변하지는 않을 텐데, 그 상관관계는 어떻게 맞추셨나요?",
                "intent": "기구 이동량($\\Delta x$)과 실제 유체 코팅 폭 변화량($\\Delta W$) 사이의 비선형적 차이를 실험적으로 캘리브레이션했는지 묻는 실무 질문입니다.",
                "answer": (
                    "정확히 짚어주셨습니다. 슬롯 다이 내부에서 금속 Shim이 이동하는 기계적 변위량과, 토출된 슬러리 비드(Bead)가 퍼지며 형성되는 실제 전극 코팅 폭 변화량 사이에는 슬러리 점도와 코팅 갭에 따른 유체역학적 비율 차이가 존재합니다.<br><br>"
                    "그래서 하드웨어 개조 직후 수차례의 시운전 테스트를 통해 <strong>모터 회전수(및 LVDT 실측 변위 $\\mu\\text{m}$) 변화에 따른 실제 웹게이지 코팅 폭 변화량($\\text{mm}$)의 상관 데이터를 수집하여 선형 회귀 계수(Gain Table)로 정량화</strong>했습니다. 덕분에 현장 작업자는 복잡한 계산 없이 ‘코팅 폭을 몇 $\\text{mm}$ 줄이겠다’고 입력하면 시스템이 알아서 목표 LVDT 변위값으로 변환해 한 번에 안착하도록 구현했습니다."
                )
            },
            {
                "tag": "제어 안정성 검증",
                "question": "LVDT로 $1\\,\\mu\\text{m}$ 단위까지 실시간 피드백을 걸면 목표 위치 근처에서 모터가 계속 왔다 갔다 하며 떨리는 헌팅(Hunting)이나 오버슈트가 생기지 않았나요?",
                "intent": "정밀 위치 제어 시 발생하는 오버슈트(Overshoot)와 채터링/헌팅 문제를 어떻게 제어 로직으로 잡았는지 확인하는 질문입니다.",
                "answer": (
                    "초기 테스트 때 관성으로 인해 타겟값을 살짝 지나쳤다가 다시 반대로 도는 오버슈트와 미세 헌팅 현상이 있었습니다. 이를 두 가지 제어 기법으로 잡았습니다.<br><br>"
                    "첫째, <strong>2단 속도 프로파일(가감속 제어)</strong>을 적용해 목표 위치 근처까지는 빠르게 접근하고, 타겟 직전 구간에서는 저속 크립(Creep) 속도로 감속해 관성 오버슈트를 없앴습니다. "
                    "둘째, 공정 스펙에 영향을 주지 않는 극미세 허용 오차 범위(불감대, Dead-band) 안으로 LVDT 값이 들어오면 모터 구동을 즉시 정지시키고 웜기어의 Self-locking으로 위치를 고정하도록 설계해 헌팅을 완벽히 방지했습니다."
                )
            },
            {
                "tag": "반도체 설비 연결",
                "question": "비전공자(기계공학 전공 아님)로서 기계 요소와 체결 토크까지 직접 파고드셨다고 했는데, 이 경험이 SK하이닉스 양산기술에서 어떻게 도움이 될까요?",
                "intent": "`context` 문서의 '느낀점 1. 기계요소(토크렌치와 다이 뒤틀림)' 내용을 바탕으로 반도체 장비 하드웨어 관리 역량을 확인하는 질문입니다.",
                "answer": (
                    "현장에서 슬롯 다이 볼트 하나를 조일 때도 작업자 감이 아니라 토크렌치로 균일한 체결 토크를 주지 않으면 다이 바디가 수 $\\mu\\text{m}$ 뒤틀려 코팅 단차와 주름이 발생한다는 것을 몸소 겪으며, <strong>‘초정밀 공정 산포의 시작점은 결국 설비 하드웨어의 기계적 정밀도와 체결 표준화’</strong>라는 것을 배웠습니다.<br><br>"
                    "SK하이닉스 양산기술에서도 챔버 PM(예방보전) 후 샤워헤드나 정전척(ESC)의 미세 수평도, 스로틀 밸브 액추에이터의 유격 등 하드웨어적 미세 틀어짐이 웨이퍼 내 균일도(WIW Uniformity) 불량으로 이어집니다. 저는 데이터만 보는 반쪽짜리 엔지니어가 아니라, 기구적 백래시와 체결 토크 같은 하드웨어 메커니즘과 센서 피드백 데이터를 동시에 꿰뚫어 보고 설비 간 편차(TTTM)를 잡는 엔지니어로 기여하겠습니다."
                )
            }
        ]
    },
    {
        "badge": "프로젝트 3 · 컴퓨터 비전 알고리즘 · 초고속 무결점 선별",
        "nav_title": "[프로젝트 3] 100만 장 Burr 이미지 처리 비전 선별 엔진",
        "title": "[프로젝트 3] 100만 장 실오라기 Burr 이미지 처리 엔진 자체 개발: 이원화 Valley 알고리즘과 1×7 수직 Bridge Kernel을 통한 장당 5ms·미검률 0% 달성",
        "context_summary": [
            "<strong>문제 상황 (Issue)</strong>: 고객사 출하 직전 <strong>‘실오라기 형태의 Burr’</strong> 불량 이슈가 발생하여 출하 지연 위기 직면. 육안 확인이 필요한 이미지가 <strong>100만 장(그중 실제 Burr는 0.5%)</strong>에 달해 인력 전수 검사가 물리적으로 불가능한 상황.",
            "<strong>과제 설정 (Task)</strong>: ‘사람이 눈으로 음영 차이를 구분할 수 있다면 픽셀과 그레이스케일 데이터로도 구분할 수 있다’고 판단, 현장 도메인 지식을 접목한 <strong>자체 이미지 처리 엔진을 개발해 72시간 내 100만 장을 미검 0%로 전수 선별</strong>하겠다는 목표 수립.",
            "<strong>핵심 알고리즘 (Action)</strong>: ① Lot 간 조명·코팅 농도 편차로 인한 과검/미검을 막기 위해 배경 코팅 평균 그레이스케일을 실시간 추정하여 <strong>밝기 55를 기준으로 레시피를 2개로 자동 전환하는 ‘이원화 Valley 알고리즘’</strong>(절대 밝기가 아닌 상대적 음영 낙차 계산) 구축, ② 지그재그로 끊어져 미세 노이즈로 오인되는 실오라기 Burr의 기하학적 연속성을 복원하기 위해 <strong>$1\\times 7$ 수직 비대칭 Bridge Kernel 모폴로지 닫힘 연산</strong> 및 <strong>8-연결성 성분분석(20px 이상 치명 결함 포착)</strong> 설계.",
            "<strong>정량적 성과 (Result)</strong>: <strong>장당 평균 5ms 초고속 처리</strong>로 72시간 내 100만 장 전수 선별 완수, <strong>미검률 0% 달성 및 고객 출하 지연 0건</strong>으로 이슈 클로징."
        ],
        "base_speech": (
            "“고객사 출하를 앞두고 ‘실오라기 형태의 Burr’ 이슈가 발생해 100만 장의 이미지를 72시간 내에 전수 선별해야 하는 긴급 상황이 있었습니다. "
            "저는 사람이 음영 차이로 구분할 수 있다면 컴퓨터 비전 픽셀 데이터로도 모델링할 수 있다고 판단해 자체 이미지 처리 엔진을 단독 개발했습니다. "
            "표준 샘플의 그레이스케일을 분석해 경계면의 국소 음영 낙차(Valley)를 포착했는데요, 두 가지 난관을 공학적으로 돌파했습니다. "
            "첫째, Lot 간 조명과 코팅 밝기 편차로 인한 오검을 막기 위해 배경 평균 스케일 55를 기준으로 레시피를 자동 전환해 상대적 음영 낙차를 계산하는 ‘이원화 Valley 알고리즘’을 구축했습니다. "
            "둘째, 실오라기 Burr가 점선처럼 끊어져 찍히며 단순 노이즈로 누락되는 미검 문제를 해결하기 위해, 가로 노이즈는 무시하고 세로 결함 신호만 이어주는 ‘$1\\times 7$ 수직 Bridge Kernel’ 모폴로지 연산과 8-연결성 분석을 적용해 20px 이상의 치명 결함을 정확히 잡아냈습니다. "
            "그 결과 장당 5ms의 초고속 처리로 미검률 0%, 출하 지연 0건을 달성했습니다.”"
        ),
        "svg_title": "📊 [100만 장 실오라기 Burr 초고속 비전 선별 엔진 아키텍처] (A) 배경 밝기 55 기준 이원화 Valley 알고리즘 | (B) 1×7 수직 Bridge Kernel 모폴로지 연결 및 8-연결성 판정",
        "svg": """<svg viewBox="0 0 960 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="320" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Panel A: Dual Valley Algorithm -->
  <g transform="translate(20, 20)">
    <rect width="450" height="280" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">1. 이원화 Valley 알고리즘: Lot 간 조명·코팅 농도 편차 완벽 상쇄</text>
    <rect x="16" y="42" width="418" height="140" rx="6" fill="#1e293b"/>
    <!-- Bright Lot Curve -->
    <path d="M 35 65 L 160 65 L 175 110 L 190 65 L 390 65" fill="none" stroke="#fde047" stroke-width="2.2"/>
    <text x="40" y="57" fill="#fde047" font-size="8" font-weight="700">밝은 Lot (배경 평균 &gt; 55) ➔ 상대적 음영 낙차(ΔValley) 추출</text>
    <!-- Threshold 55 divider -->
    <line x1="30" y1="115" x2="410" y2="115" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="4,3"/>
    <text x="275" y="110" fill="#38bdf8" font-size="8" font-weight="800">배경 그레이스케일 기준선 = 55</text>
    <!-- Dark Lot Curve -->
    <path d="M 35 135 L 220 135 L 235 172 L 250 135 L 390 135" fill="none" stroke="#34d399" stroke-width="2.2"/>
    <text x="40" y="152" fill="#34d399" font-size="8" font-weight="700">어두운 Lot (배경 평균 ≤ 55) ➔ 저조도 맞춤형 Valley 레시피 자동 전환</text>
    <text x="16" y="204" fill="#fca5a5" font-size="8.3" font-weight="700">• 단일 고정 Threshold의 한계: 어두운 Lot은 전체 과검, 밝은 Lot은 Burr 미검 발생!</text>
    <text x="16" y="224" fill="#cbd5e1" font-size="8.3">• 해결: 배경 코팅 평균 밝기를 실시간 추정(55 기준 이원화)하여 절대 밝기가 아닌</text>
    <text x="16" y="242" fill="#6ee7b7" font-size="8.3" font-weight="700">  ‘배경 대비 상대적 음영 골짜기(Local Valley 낙차)’를 계산함으로써 Lot 편차 100% 제거</text>
    <text x="16" y="262" fill="#94a3b8" font-size="7.8">• 무거운 딥러닝 추론 대신 경량 행렬 연산으로 설계하여 장당 5ms(초당 200장) 속도 확보</text>
  </g>
  <!-- Panel B: 1x7 Bridge Kernel & 8-Connectivity -->
  <g transform="translate(490, 20)">
    <rect width="450" height="280" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12" font-weight="800">2. 1×7 수직 Bridge Kernel 모폴로지 연산 &amp; 8-연결성 치명 결함 판정</text>
    <rect x="16" y="42" width="418" height="140" rx="6" fill="#1e293b"/>
    <!-- Step 1: Broken zigzag dots -->
    <g transform="translate(35, 55)">
      <rect width="105" height="110" rx="4" fill="#0f172a" stroke="#475569"/>
      <text x="10" y="16" fill="#f87171" font-size="8" font-weight="700">① 원본 이진화 신호</text>
      <circle cx="52" cy="32" r="2.5" fill="#ef4444"/>
      <circle cx="55" cy="46" r="2.5" fill="#ef4444"/>
      <circle cx="50" cy="62" r="2.5" fill="#ef4444"/>
      <circle cx="54" cy="76" r="2.5" fill="#ef4444"/>
      <circle cx="20" cy="55" r="2" fill="#64748b"/>
      <circle cx="82" cy="70" r="2" fill="#64748b"/>
      <text x="8" y="98" fill="#fca5a5" font-size="7.2">점선 단절 ➔ 노이즈 오인!</text>
    </g>
    <!-- Step 2: 1x7 Vertical Kernel -->
    <g transform="translate(162, 55)">
      <rect width="110" height="110" rx="4" fill="#0f172a" stroke="#f59e0b"/>
      <text x="10" y="16" fill="#fde047" font-size="8" font-weight="700">② 1×7 Bridge Kernel</text>
      <rect x="47" y="25" width="14" height="56" fill="none" stroke="#fde047" stroke-width="1.5"/>
      <line x1="47" y1="33" x2="61" y2="33" stroke="#fde047" stroke-width="1"/>
      <line x1="47" y1="41" x2="61" y2="41" stroke="#fde047" stroke-width="1"/>
      <line x1="47" y1="49" x2="61" y2="49" stroke="#fde047" stroke-width="1"/>
      <line x1="47" y1="57" x2="61" y2="57" stroke="#fde047" stroke-width="1"/>
      <line x1="47" y1="65" x2="61" y2="65" stroke="#fde047" stroke-width="1"/>
      <line x1="47" y1="73" x2="61" y2="73" stroke="#fde047" stroke-width="1"/>
      <text x="8" y="96" fill="#fde68a" font-size="7.2">가로 노이즈 무시, 세로 연결</text>
    </g>
    <!-- Step 3: Connected Polygon (>=20px) -->
    <g transform="translate(294, 55)">
      <rect width="120" height="110" rx="4" fill="#0f172a" stroke="#10b981"/>
      <text x="10" y="16" fill="#34d399" font-size="8" font-weight="700">③ 8-연결성 (≥20px)</text>
      <path d="M 52 28 L 56 46 L 50 62 L 55 82" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
      <text x="10" y="98" fill="#6ee7b7" font-size="7.5" font-weight="800">★ 미검률 0% 완벽 포착!</text>
    </g>
    <text x="16" y="204" fill="#cbd5e1" font-size="8.3">• <tspan fill="#fde047" font-weight="700">도메인 지식 반영</tspan>: 실오라기 Burr는 세로 방향(MD)으로 길게 뻗지만 너무 얇아 픽셀이 끊김</text>
    <text x="16" y="224" fill="#cbd5e1" font-size="8.3">• <tspan fill="#34d399" font-weight="700">비대칭 커널 설계</tspan>: 1×7 수직 모폴로지 닫힘(Closing) 연산으로 7px 이내 단절 신호를 하나로 연결</text>
    <text x="16" y="244" fill="#6ee7b7" font-size="8.3" font-weight="700">• 8-연결성 성분분석(Connected Component)으로 대각선 지그재그까지 합산해 20px 이상 NG 판정</text>
    <text x="16" y="262" fill="#38bdf8" font-size="7.8">➔ 반도체 웨이퍼 마이크로 스크래치/크랙 ADC(자동 결함 분류) 알고리즘 원리와 완벽히 부합</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "기술 선택 이유 검증",
                "question": "요즘 비전 검사에는 CNN이나 YOLO 같은 딥러닝 모델을 많이 쓰는데, 왜 딥러닝 대신 '이원화 Valley + 1×7 Bridge Kernel' 같은 룰 기반 수학적 알고리즘을 직접 설계하셨나요?",
                "intent": "주어진 시간 제약(72시간, 100만 장)과 제조 출하 품질의 대전제(미검률 0%, 설명 가능성)에 맞춰 최적의 엔지니어링 의사결정을 내렸는지 확인하는 질문입니다.",
                "answer": (
                    "당시 상황의 세 가지 제약 조건 때문이었습니다.<br><br>"
                    "첫째, <strong>‘데이터 불균형과 학습 시간 부족’</strong>입니다. 100만 장 중 실제 Burr 불량은 0.5%에 불과했고, 72시간 내에 선별을 끝내야 하는 긴급 상황에서 수천 장의 라벨링과 딥러닝 학습·검증을 진행할 물리적 시간이 없었습니다.<br><br>"
                    "둘째, <strong>‘연산 속도(장당 5ms)’</strong>입니다. 사내 일반 PC 환경(고가 GPU 서버 부재)에서 72시간 내 100만 장을 처리하려면 장당 수 밀리초(ms) 단위의 초고속 연산이 필수였는데, 경량화된 행렬/모폴로지 연산이 압도적으로 유리했습니다.<br><br>"
                    "셋째, 가장 중요한 <strong>‘미검률 0% 보장과 고객 설명 가능성’</strong>입니다. 블랙박스인 딥러닝과 달리, 전극 경계면의 음영 낙차(Valley)와 세로 방향 결함 연속성($1\\times 7$ Bridge Kernel)을 수학적으로 명시화했기 때문에 미검률 0%를 확실히 통제하고 고객사에도 선별 기준의 타당성을 100% 논리적으로 설득할 수 있었습니다."
                )
            },
            {
                "tag": "알고리즘 난관 극복",
                "question": "이원화 Valley 알고리즘에서 '배경 스케일 55'를 기준으로 레시피를 2개로 나눴다고 하셨는데, 왜 단일 임계값(Threshold)으로는 안 됐고 어떻게 55라는 기준을 잡으셨나요?",
                "intent": "Lot 간 산포(조명 및 코팅 농도 편차)를 어떻게 상대적 음영 낙차로 극복했는지 구체적 과정을 검증하는 질문입니다.",
                "answer": (
                    "초기에 단일 고정 임계값(Threshold)을 적용했을 때 가장 큰 난관이 바로 <strong>‘Lot 간 코팅 표면 밝기 편차’</strong>였습니다. 슬러리 분산 상태나 조명 컨디션에 따라 어떤 Lot은 배경이 밝고 어떤 Lot은 어두웠는데, 고정 임계값을 쓰면 어두운 Lot에서는 정상 표면이 무더기로 과검되고, 밝은 Lot에서는 얕은 Burr 음영이 누락되는 미검이 발생했습니다.<br><br>"
                    "그래서 전체 Lot 샘플의 배경 그레이스케일 히스토그램 분포를 분석해 보니, 평균 밝기 <strong>‘55’</strong>를 기점으로 고휘도 그룹과 저휘도 그룹의 광학적 대비(Contrast) 특성이 나뉜다는 것을 확인했습니다. 이에 각 이미지가 들어올 때마다 배경 평균 밝기를 실시간 추정해 55 이상과 미만으로 이원화하고, <strong>절대 픽셀 밝기가 아니라 ‘배경 평균 대비 국소 음영이 얼마나 깊게 파였는가(상대적 Valley 낙차)’</strong>를 계산하도록 전면 수정하여 Lot 간 편차를 완벽히 상쇄했습니다."
                )
            },
            {
                "tag": "커널 설계 원리 검증",
                "question": "일반적인 정사각형 커널(예: 3×3, 5×5) 대신 왜 하필 '1×7 수직 비대칭 Bridge Kernel'과 '8-연결성 성분분석'을 조합하셨나요?",
                "intent": "컴퓨터 비전의 모폴로지(Morphology) 커널 형상 설계에 현장 도메인 지식이 어떻게 반영되었는지 묻는 핵심 질문입니다.",
                "answer": (
                    "실오라기 Burr는 두께가 극도로 얇아서 카메라로 촬영하면 하나의 실선이 아니라 <strong>중간중간 픽셀이 끊어진 세로 점선 형태</strong>로 찍힙니다. 만약これを 이어주려고 일반적인 $5\\times 5$나 $7\\times 7$ 정사각형 커널로 팽창/닫힘(Closing) 연산을 하면, 주변에 흩어져 있는 정상적인 가로 방향 코팅 입자 노이즈들까지 서로 뭉쳐져서 거대한 가짜 불량(과검)으로 둔갑하는 문제가 발생했습니다.<br><br>"
                    "여기서 저는 <strong>‘실오라기 Burr는 주행 방향(세로)으로만 길게 뻗는다’</strong>는 도메인 특성을 활용했습니다. 가로 폭은 $1\\text{px}$로 묶어 가로 노이즈 결합은 원천 차단하고, 세로로만 $7\\text{px}$ 탐색하는 <strong>$1\\times 7$ 수직 비대칭 Bridge Kernel</strong>을 설계해 세로로 끊어진 결함 점들 사이에만 다리(Bridge)를 놓아 실선으로 복원했습니다. 이후 결함이 미세하게 지그재그(대각선)로 꺾이는 특성을 고려해 상하좌우뿐 아니라 대각선 픽셀까지 하나의 객체로 묶어주는 <strong>8-연결성 성분분석(8-Connectivity)</strong>을 적용, 총 길이가 $20\\text{px}$ 이상인 치명 결함만 미검 0%로 정확히 포착해 냈습니다."
                )
            },
            {
                "tag": "미검률 0% 검증 방법",
                "question": "미검률 0%를 달성했다고 하셨는데, 100만 장을 다 눈으로 확인해 본 것도 아닐 텐데 미검률이 0%라는 걸 어떻게 검증하고 고객사를 설득하셨나요?",
                "intent": "엔지니어링 유효성 검증(Validation) 방법론과 고객 품질 대응 논리를 확인하는 날카로운 질문입니다.",
                "answer": (
                    "미검률 0%를 보장하기 위해 두 단계의 엄격한 검증 프로토콜을 적용했습니다.<br><br>"
                    "첫째, 개발 단계에서 작업자와 품질 엔지니어가 육안으로 교차 확인한 <strong>경계성 미세 Burr(가장 흐릿하고 끊어진 워스트 샘플 포함) 골든 샘플 셋(Golden Sample Set) 수천 장</strong>을 구축하여, 해당 샘플에서 미검(False Negative)이 단 1건도 발생하지 않도록 임계치 마진을 보수적으로(과검을 일부 감수하더라도 미검은 절대 없도록) 세팅했습니다.<br><br>"
                    "둘째, 100만 장 자동 선별 후 알고리즘이 <strong>NG(불량 의심)로 분류한 소수의 이미지들은 엔지니어가 2차 육안 검증해 과검을 걸러냈고, 양품(OK)으로 판정된 집단에서도 층화 랜덤 샘플링(Stratified Random Sampling) 검증</strong>을 수행해 누락된 결함이 0건임을 통계적으로 입증했습니다. 이 정량적 근거를 8D 리포트로 제시하여 고객사의 출하 승인을 지연 없이 받아냈습니다."
                )
            },
            {
                "tag": "장당 5ms 최적화 검증",
                "question": "파이썬으로 100만 장 이미지를 처리하면서 장당 평균 5ms라는 속도를 내려면 코드 최적화가 필요했을 텐데 어떻게 구현하셨나요?",
                "intent": "대용량 데이터 처리 시 파이썬 연산 병목(I/O 및 루프)을 어떻게 해결했는지 보는 실무 코딩 질문입니다.",
                "answer": (
                    "파이썬에서 이미지를 한 픽셀씩 이중 `for`문으로 돌리면 장당 수백 $\\text{ms}$가 걸려 72시간 내에 절대 끝낼 수 없습니다.<br><br>"
                    "저는 두 가지 최적화를 적용했습니다. 첫째, 결함이 발생할 수 있는 <strong>전극 에지 경계면 관심 영역(ROI, Region of Interest)만 크롭(Crop)</strong>하여 연산해야 할 픽셀 면적을 1/10 이하로 줄였습니다. "
                    "둘째, 모든 연산을 파이썬 루프가 아닌 C언어로 최적화된 <strong>NumPy 벡터화 행렬 연산과 OpenCV 내장 모폴로지/연결성 함수(`cv2.morphologyEx`, `cv2.connectedComponentsWithStats`)</strong>로만 파이프라인을 구성하고 멀티프로세싱을 병렬 적용하여 장당 평균 $5\\,\\text{ms}$라는 초고속 처리 속도를 달성했습니다."
                )
            }
        ]
    }
]
