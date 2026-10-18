# -*- coding: utf-8 -*-
"""
sk_modules_part2.py
SK하이닉스 양산기술 맞춤형 심층 꼬리질문 & 방어 답변 (PART 05 ~ PART 08)
"""

SK_MODULES_PART2 = [
    {
        "badge": "프로젝트 4 · 스마트 팹 AX 자동화 · 월 40시간 절감",
        "nav_title": "[프로젝트 4] 인라인 IPQC 데이터 검토 자동화 (월 40시간 절감)",
        "title": "[프로젝트 4] 인라인 IPQC 데이터 검토 및 Lot 병합 판정 완전 자동화: 헌팅 노이즈 제거, HTML 대시보드 및 원클릭 GUI 배포",
        "context_summary": [
            "<strong>문제 상황 (Issue)</strong>: 신규 모델 생산 시 고객사가 모든 Lot에 대한 인라인 검사기 Data 송부를 요청. 사내 여러 IoT/품질 시스템에서 데이터를 수동 다운로드하고 설비 가감속/전환 구간의 <strong>헌팅(Hunting) 노이즈 데이터를 수작업으로 발라내느라 엔지니어가 매일 2시간씩 소모</strong>하는 심각한 비효율 발생.",
            "<strong>자동화 설계 및 구현 (Action)</strong>: ① 기존 수작업 프로세스를 표준 매뉴얼화하여 <strong>PRD(요구사항 정의서)</strong> 작성, ② 화면 좌표/이벤트 제어를 통해 사내 IoT 시스템에서 인라인 데이터를 자동 다운로드하는 파이프라인 구축, ③ <strong>룰 기반 헌팅 노이즈 자동 제거 로직</strong> 및 <strong>Lot 병합 가능 여부 자동 판정 로직</strong> 구현, ④ 공정능력($C_{pk}$) 그래프와 일일 품질 현황을 시각화한 <strong>HTML 대시보드</strong> 및 코딩을 모르는 팀원도 쓸 수 있는 <strong>원클릭 GUI 프로그램</strong> 배포.",
            "<strong>정량적 성과 (Result)</strong>: 매일 2시간씩 걸리던 단순 반복 업무를 <strong>월 40시간 이상(업무 공수 100%) 완전 자동화</strong>하여 엔지니어가 고부가가치 수율 개선에 집중할 수 있는 환경 구축."
        ],
        "base_speech": (
            "“신규 모델 양산 당시 모든 Lot의 인라인 검사 데이터를 고객사에 송부해야 했는데, 사내 여러 시스템에서 데이터를 받고 헌팅 노이즈를 발라내느라 엔지니어가 매일 2시간씩 단순 반복 수작업을 하는 문제가 있었습니다. "
            "저는 ‘고객향 데이터 검토 공수 100% 절감’을 목표로 AI 에이전트 워크플로우를 활용해 단독 자동화 개발에 착수했습니다. "
            "먼저 수작업 판단 기준을 명문화한 PRD를 작성한 뒤, IoT 시스템에서 데이터를 자동 수집하는 스크립트와 룰 기반 헌팅 노이즈 자동 제거 로직, 그리고 Lot 병합 가능 여부 판정 프로그램을 구현했습니다. "
            "나아가 공정능력($C_{pk}$) 현황을 한눈에 보는 HTML 대시보드와 함께, 파이썬을 모르는 동료도 클릭 한 번으로 실행할 수 있는 GUI 환경으로 패키징해 배포했습니다. "
            "그 결과 매일 2시간, 월 40시간의 반복 공수를 100% 자동화하여 팀의 AX 혁신을 이끌어냈습니다.”"
        ),
        "svg_title": "📊 [인라인 IPQC 데이터 검토 & Lot 병합 판정 100% 자동화 파이프라인] IoT 자동 수집 ➔ 헌팅 노이즈 필터링 ➔ Cpk HTML 대시보드 & 원클릭 GUI",
        "svg": """<svg viewBox="0 0 960 280" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Step 1 -->
  <g transform="translate(20, 25)">
    <rect width="215" height="230" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="14" y="26" fill="#38bdf8" font-size="11" font-weight="800">STEP 1. PRD 정의 &amp; 자동 수집</text>
    <rect x="14" y="42" width="187" height="170" rx="6" fill="#1e293b"/>
    <text x="24" y="66" fill="#fde047" font-size="9" font-weight="700">• 수작업 암묵지의 PRD 명문화</text>
    <text x="24" y="88" fill="#cbd5e1" font-size="8.2">• 사내 EioT / MES / QMS 연동</text>
    <text x="24" y="108" fill="#cbd5e1" font-size="8.2">• 마우스/화면 제어 자동화로</text>
    <text x="24" y="124" fill="#cbd5e1" font-size="8.2">  Lot별 Raw CSV 일괄 다운로드</text>
    <text x="24" y="155" fill="#94a3b8" font-size="7.8">➔ 폐쇄망 보안 규정 100% 준수</text>
    <text x="24" y="172" fill="#6ee7b7" font-size="8" font-weight="700">➔ 수동 다운로드 시간 0초화</text>
  </g>
  <polygon points="240,140 250,135 250,145" fill="#38bdf8"/>
  <!-- Step 2 -->
  <g transform="translate(255, 25)">
    <rect width="225" height="230" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11" font-weight="800">STEP 2. 헌팅 노이즈 정제 로직</text>
    <rect x="14" y="42" width="197" height="170" rx="6" fill="#1e293b"/>
    <text x="24" y="66" fill="#fde047" font-size="9" font-weight="700">• 룰 기반 Hunting 구간 제거</text>
    <text x="24" y="88" fill="#cbd5e1" font-size="8.2">• 코팅 시작/종료 과도 구간,</text>
    <text x="24" y="104" fill="#cbd5e1" font-size="8.2">  센서 스캔 전환 시점 스파이크를</text>
    <text x="24" y="120" fill="#cbd5e1" font-size="8.2">  규칙 기반으로 자동 트리밍</text>
    <text x="24" y="148" fill="#38bdf8" font-size="8.2" font-weight="700">• Lot 병합(Merge) 가능 여부 판정</text>
    <text x="24" y="166" fill="#94a3b8" font-size="7.8">  (평균/산포/규격 일치성 자동 검증)</text>
  </g>
  <polygon points="485,140 495,135 495,145" fill="#38bdf8"/>
  <!-- Step 3 -->
  <g transform="translate(500, 25)">
    <rect width="215" height="230" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="14" y="26" fill="#c4b5fd" font-size="11" font-weight="800">STEP 3. HTML 대시보드 &amp; GUI</text>
    <rect x="14" y="42" width="187" height="170" rx="6" fill="#1e293b"/>
    <text x="24" y="66" fill="#fde047" font-size="9" font-weight="700">• Cpk &amp; 트렌드 HTML 리포트</text>
    <text x="24" y="88" fill="#cbd5e1" font-size="8.2">• 이상치 유무 자동 하이라이트</text>
    <text x="24" y="108" fill="#cbd5e1" font-size="8.2">• 비개발자 팀원용 직관적 GUI</text>
    <text x="24" y="124" fill="#cbd5e1" font-size="8.2">  및 원클릭 실행 환경 배포</text>
    <text x="24" y="155" fill="#6ee7b7" font-size="8" font-weight="700">➔ 팀 내 표준 툴로 즉시 정착</text>
  </g>
  <polygon points="720,140 730,135 730,145" fill="#10b981"/>
  <!-- Step 4 -->
  <g transform="translate(735, 25)">
    <rect width="205" height="230" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="14" y="26" fill="#10b981" font-size="11" font-weight="800">STEP 4. AX 성과 &amp; FAB 확장</text>
    <rect x="14" y="42" width="177" height="170" rx="6" fill="#064e3b"/>
    <text x="20" y="70" fill="#fde047" font-size="10" font-weight="800">🏆 월 40시간 절감!</text>
    <text x="20" y="92" fill="#ffffff" font-size="8.5" font-weight="700">• 일 2시간 수작업 ➔ 공수 100% ↓</text>
    <text x="20" y="114" fill="#a7f3d0" font-size="8">• 휴먼 에러(데이터 누락/오판) 0건</text>
    <line x1="20" y1="130" x2="175" y2="130" stroke="#10b981" stroke-width="1"/>
    <text x="20" y="150" fill="#38bdf8" font-size="8.2" font-weight="700">[SK하이닉스 양산기술 적용]</text>
    <text x="20" y="168" fill="#e2e8f0" font-size="7.8">• 일일 웨이퍼 PCM/Inline 계측</text>
    <text x="20" y="184" fill="#e2e8f0" font-size="7.8">  리포트 및 설비 이상 요약 자동화</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "데이터 정제 검증",
                "question": "인라인 데이터에서 '헌팅(Hunting) Data'를 룰 기반으로 제거했다고 하셨는데, 헌팅 데이터가 왜 발생하며 실제 불량 데이터와 어떻게 구분해서 지우셨나요?",
                "intent": "정상적인 노이즈(센서 헌팅)를 지우다가 진짜 공정 불량까지 지워버리는 데이터 조작 위험을 어떻게 방어했는지 묻는 날카로운 질문입니다.",
                "answer": (
                    "인라인 웹게이지 데이터에서 발생하는 ‘헌팅(Hunting)’은 실제 전극 품질 불량이 아니라, <strong>① 코팅 시작·종료 시점(Start/End)의 가감속 구간, ② 무지부에서 유지부로 넘어가는 경계점 스캔 시 센서가 허공이나 테이프 구간을 읽을 때, ③ 센서 자체 영점 캘리브레이션 직후</strong>에 물리적으로 값이 순간 급등락하는 가짜 신호입니다.<br><br>"
                    "만약 단순히 ‘값이 크게 튄 것’을 무조건 지우면 진짜 불량까지 삭제될 위험이 있습니다. 그래서 저는 <strong>설비 운전 상태 신호(코팅 Run/Stop 플래그, 주행 속도, 스캔 프레임 인덱스)와 결합한 룰 기반 조건</strong>을 세웠습니다. 즉, 코팅 시작/종료 전후 $N$미터 과도 구간이나 센서 회귀 전환점 프레임에서 발생하는 비정상 스파이크만 정확히 마스킹해 제거하고, 정상 정속 주행 구간에서 발생한 이탈은 절대 지우지 않고 빨간색 경보로 대시보드에 띄우도록 설계해 데이터 무결성을 지켰습니다."
                )
            },
            {
                "tag": "Lot 병합 로직 검증",
                "question": "자동화 항목 중 'Lot 병합 가능 여부 검토 프로그램'이 있던데, 어떤 기준을 만족해야 서로 다른 Lot을 병합할 수 있는 건가요?",
                "intent": "생산운영 직무의 실질적 도메인 규칙(Lot Merge Criteria)을 알고 코딩했는지 확인하는 질문입니다.",
                "answer": (
                    "전극 공정에서 소량 잔여 롤이나 분할된 롤을 하나의 점보 롤로 병합(Merge)하여 후공정 효율을 높이려면 고객사와 합의된 까다로운 품질 동질성 기준을 통과해야 합니다.<br><br>"
                    "구체적으로 ① <strong>동일 슬러리 배치(Batch) 또는 허용된 선후 배치 여부</strong>, ② 두 Lot 간 <strong>평균 로딩량 및 두께 차이($\\Delta \\mu$)가 허용 편차 이내인지</strong>, ③ 병합 시 전체 구간의 <strong>합산 공정능력 지수($C_{pk}$)가 고객 출하 스펙(예: $1.33$ 이상)을 만족하는지</strong>, ④ <strong>스플라이싱(이음매) 횟수 제한</strong>을 넘지 않는지를 동시에 계산해야 했습니다. 기존에는 엔지니어가 엑셀로 일일이 대조하던 것을 파이썬 스크립트가 수 초 만에 시뮬레이션하여 ‘병합 가능 조합’과 ‘예상 합산 $C_{pk}$’를 자동 추천하도록 구현했습니다."
                )
            },
            {
                "tag": "폐쇄망 연동 검증",
                "question": "대기업 양산 라인은 보안상 외부 API나 DB 직접 접근 권한이 막혀 있는 경우가 많은데, IoT 시스템에서 데이터를 어떻게 자동 다운로드하셨나요?",
                "intent": "사내 보안 규정을 위반하지 않고 레거시 시스템의 데이터 수집 병목을 어떻게 풀었는지 확인하는 질문입니다.",
                "answer": (
                    "맞습니다. 사내 보안 정책상 일반 공정 엔지니어 계정에 DB 다이렉트 쿼리 권한이 열려 있지 않았고, 사내 표준 웹/클라이언트 UI를 통해서만 조회 및 엑셀/CSV 내보내기가 가능했습니다.<br><br>"
                    "그래서 보안 가드레일을 철저히 준수하는 범위 내에서, <strong>사내 승인된 파이썬 환경의 UI 제어(마우스 좌표·키보드 이벤트 및 창 핸들 제어)를 활용해 사람이 매일 아침 조건을 입력하고 ‘다운로드’ 버튼을 누르는 루틴을 그대로 에뮬레이션</strong>했습니다. 다운로드된 원천 CSV 파일은 자동으로 `Context` 폴더에 날짜별로 정리되고, 즉시 정제 스크립트가 돌아가 아침 출근과 동시에 HTML 대시보드가 생성되도록 구축했습니다."
                )
            },
            {
                "tag": "팀 확산 및 유지보수",
                "question": "본인이 만든 자동화 프로그램을 팀원들에게 배포했을 때, 파이썬이 안 깔려 있거나 에러가 나면 어떻게 대응하셨나요?",
                "intent": "혼자만 쓰는 스크립트인지, 조직 전체의 생산성을 높이는 엔지니어링 툴로 패키징했는지 평가하는 질문입니다.",
                "answer": (
                    "동료 엔지니어들이 검은색 콘솔 창이나 파이썬 환경 설정 때문에 거부감을 느끼지 않도록, <strong>직관적인 GUI 버튼과 원클릭 배치 파일(`run.bat`)을 함께 패키징</strong>해 배포했습니다.<br><br>"
                    "또한 사내 시스템 UI 위치가 바뀌거나 파일 컬럼 형식이 일부 누락되더라도 프로그램이 그냥 죽지 않도록, <strong>모든 함수 단위에 방어적 예외 처리(`try-except`)와 한글 에러 로그 안내창</strong>을 넣었습니다. 산출물 역시 별도 프로그램 설치 없이 크롬/엣지 브라우저만 있으면 어디서든 인터랙티브하게 열람할 수 있는 단일 **HTML 대시보드**로 생성되도록 만들어 팀 내 표준 업무 툴로 완벽히 정착시켰습니다."
                )
            }
        ]
    },
    {
        "badge": "특화 무기 · 나만의 AI 에이전트 워크플로우 · 본기함구",
        "nav_title": "[특화 무기] 나만의 AI 에이전트 워크플로우 (본·기·함·구)",
        "title": "[특화 무기] 환각(Hallucination)을 통제하고 100% 재현성을 확보하는 AI 에이전트 워크플로우: Context-Tool-Result 구조화와 '본·기·함·구' 빌드업",
        "context_summary": [
            "<strong>차별화 핵심</strong>: AI를 단순 웹 채팅창에 산발적으로 질의하는 챗봇으로 쓰지 않고, 데이터 오염과 환각(Hallucination)을 원천 통제하는 <strong>‘에이전트 워크플로우(Agentic Workflow)’</strong>를 직접 구축하여 실무 자동화 도구 개발.",
            "<strong>프로토콜 1 — 구조화 (Context - Tool - Result)</strong>: `rules.md`로 코딩 규칙과 보안 대전제를 가드레일로 고정하고, 원천 데이터인 <strong>`Context`(Read-Only & 데이터 사전 선행)</strong>, 실행 스크립트인 <strong>`Tool`(원클릭 `run.bat` 페어링)</strong>, 산출물인 <strong>`Result`(버전 관리 & Diff 벤치마크)</strong> 폴더를 엄격히 분리 통제.",
            "<strong>프로토콜 2 — 점진적 파이썬 빌드업 (본·기·함·구)</strong>: ① <strong>본(本)</strong>: 문제의 본질 파악, ② <strong>기(機)</strong>: 문장을 기능적 단위로 쪼개어 입출력 PRD 작성 및 사전 승인, ③ <strong>함(函)</strong>: 기능 단위 함수 모듈화 및 예외 처리, ④ <strong>구(構)</strong>: 아키텍처 리빌딩 vs 단순 추가 비교 검토 후 건물을 짓듯 완성."
        ],
        "base_speech": (
            "“네, 저는 AI를 단순 챗봇으로 쓰는 것을 넘어, 환각(Hallucination)을 제어하고 재현성을 확보하는 ‘에이전트 워크플로우(Agentic Workflow)’를 직접 구축하여 개발합니다. 웹 채팅창에 산발적으로 질의하면 데이터 오염과 환각이 발생해 실무에 적용할 수 없기 때문에 두 가지 프로토콜을 엄격히 사용합니다. "
            "첫째, ‘구조화’입니다. `rules.md`를 통해 코딩 규칙과 보안 대전제를 가드레일로 고정하고, 원천 데이터인 `Context`, 실행 스크립트인 `Tool`, 산출물인 `Result` 폴더를 엄격히 분리하여 AI가 신뢰할 수 있는 도메인 데이터 기반으로만 추론하도록 통제합니다. "
            "둘째, ‘본·기·함·구 점진적 파이썬 코딩 빌드업’입니다. 사용자·개발자·PM으로 역할을 분리해 문제의 본질을 먼저 파악하게 하고(본), 문장을 기능적 단위로 분리해 PRD를 작성합니다(기). 이를 통해 기능 단위로 함수화하고(함), 구조를 리빌딩할지 단순 덧붙일지 제시하게 하여(구) 건물을 짓듯이 코드를 완성합니다. "
            "이러한 AI 엔지니어링 체계를 바탕으로 입사 후에도 현장 도메인 지식에 AI 에이전트를 결합해 팀의 생산성을 극대화하겠습니다.”"
        ),
        "svg_title": "📊 [나만의 AI 에이전트 엔지니어링 2대 프로토콜] (A) Context-Tool-Result 폴더 격리 및 rules.md 가드레일 | (B) '본·기·함·구' 4단계 승인 게이트(Gate) 파이프라인",
        "svg": """<svg viewBox="0 0 960 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="300" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Left: Protocol 1 (Folder Architecture) -->
  <g transform="translate(20, 20)">
    <rect width="435" height="260" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">프로토콜 1. 구조화: rules.md 가드레일 &amp; 3단 폴더 완전 분리</text>
    <rect x="16" y="40" width="403" height="34" rx="5" fill="#1e1b4b" stroke="#818cf8"/>
    <text x="28" y="61" fill="#fde047" font-size="9" font-weight="800">🛡️ rules.md (상시 로드 가드레일): 보안 원칙 · 한글 문서화 · 임의 추측 금지</text>
    <!-- 3 Folders -->
    <rect x="16" y="84" width="126" height="158" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="26" y="106" fill="#38bdf8" font-size="9.5" font-weight="800">📁 1. Context/</text>
    <text x="24" y="126" fill="#cbd5e1" font-size="7.8">• 원천 데이터 Read-Only</text>
    <text x="24" y="144" fill="#cbd5e1" font-size="7.8">• 원본 훼손 원천 차단</text>
    <text x="24" y="162" fill="#fde047" font-size="7.8" font-weight="700">• data_dict.md 선행 필수</text>
    <text x="24" y="178" fill="#94a3b8" font-size="7.3">  (컬럼/단위/결측치 정의)</text>

    <rect x="154" y="84" width="126" height="158" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="164" y="106" fill="#fbbf24" font-size="9.5" font-weight="800">🛠️ 2. Tool/</text>
    <text x="162" y="126" fill="#cbd5e1" font-size="7.8">• 버전별 1:1 매칭 폴더</text>
    <text x="162" y="144" fill="#fde047" font-size="7.8" font-weight="700">• 원클릭 run.bat 동봉</text>
    <text x="162" y="162" fill="#cbd5e1" font-size="7.8">• 임시 코드는 scratch/</text>
    <text x="162" y="178" fill="#94a3b8" font-size="7.3">  격리로 코드 오염 방지</text>

    <rect x="292" y="84" width="127" height="158" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="302" y="106" fill="#34d399" font-size="9.5" font-weight="800">📊 3. Result/</text>
    <text x="300" y="126" fill="#cbd5e1" font-size="7.8">• PRD &amp; 최종 리포트(MD)</text>
    <text x="300" y="144" fill="#cbd5e1" font-size="7.8">• HTML 대시보드 / EXE</text>
    <text x="300" y="162" fill="#6ee7b7" font-size="7.8" font-weight="700">• 이전 버전 대비 Diff</text>
    <text x="300" y="178" fill="#94a3b8" font-size="7.3">  성능 벤치마크 기록</text>
  </g>
  <!-- Right: Protocol 2 (Bon-Gi-Ham-Gu) -->
  <g transform="translate(473, 20)">
    <rect width="467" height="260" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12" font-weight="800">프로토콜 2. 점진적 파이썬 빌드업: ‘본·기·함·구’ 4단계 게이트</text>
    <g transform="translate(16, 42)">
      <rect width="210" height="92" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="22" fill="#38bdf8" font-size="10" font-weight="800">① 본 (本 - 본질 파악)</text>
      <text x="12" y="42" fill="#cbd5e1" font-size="8">• 자연어 지시 이면의 진짜 엔지니어링</text>
      <text x="12" y="56" fill="#cbd5e1" font-size="8">  문제 정의 및 도메인 전제 조건 확인</text>
      <text x="12" y="74" fill="#fde047" font-size="7.8" font-weight="700">➔ 모호한 부분은 추측 대신 사전 질문!</text>
    </g>
    <g transform="translate(236, 42)">
      <rect width="215" height="92" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="22" fill="#fbbf24" font-size="10" font-weight="800">② 기 (機 - 기능 구분 &amp; PRD)</text>
      <text x="12" y="42" fill="#cbd5e1" font-size="8">• 사용자·개발자·PM 역할 분리</text>
      <text x="12" y="56" fill="#cbd5e1" font-size="8">• 기능적 단어로 쪼개어 입출력(I/O) 스펙을</text>
      <text x="12" y="74" fill="#fde047" font-size="7.8" font-weight="700">  담은 PRD.md 선행 작성 &amp; 승인 게이트</text>
    </g>
    <g transform="translate(16, 148)">
      <rect width="210" height="94" rx="6" fill="#1e293b" stroke="#8b5cf6"/>
      <text x="12" y="22" fill="#c4b5fd" font-size="10" font-weight="800">③ 함 (函 - 함수 단위 모듈화)</text>
      <text x="12" y="42" fill="#cbd5e1" font-size="8">• 통짜 스파게티 코드 생성 금지</text>
      <text x="12" y="56" fill="#cbd5e1" font-size="8">• 독립 테스트 가능한 함수 단위 모듈화</text>
      <text x="12" y="74" fill="#6ee7b7" font-size="7.8" font-weight="700">• 결측치/이상치 방어 Try-Except 로깅</text>
    </g>
    <g transform="translate(236, 148)">
      <rect width="215" height="94" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="22" fill="#34d399" font-size="10" font-weight="800">④ 구 (構 - 구조 검토 &amp; 패키징)</text>
      <text x="12" y="42" fill="#cbd5e1" font-size="8">• 기능 확장 시 전면 리빌딩(Rebuilding) vs</text>
      <text x="12" y="56" fill="#cbd5e1" font-size="8">  단순 추가(Append) 공학적 비교 제안</text>
      <text x="12" y="74" fill="#6ee7b7" font-size="7.8" font-weight="700">➔ run.bat &amp; 대시보드로 100% 재현 배포</text>
    </g>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "워크플로우 실전 검증",
                "question": "방금 말씀하신 '본·기·함·구' 프로토콜이 매우 인상적인데, 왜 그냥 AI에게 '이런 파이썬 코드 짜줘'라고 바로 시키지 않고 굳이 4단계로 쪼개서 시키시는 건가요?",
                "intent": "프롬프트 엔지니어링 수준을 넘어 소프트웨어 공학적 제어(환각 방지 및 유지보수성) 이유를 명확히 설명할 수 있는지 검증하는 질문입니다.",
                "answer": (
                    "AI에게 자연어로 ‘이 데이터 분석해서 이상치 잡는 코드 짜줘’라고 한 번에 시키면, AI가 도메인 단위(`mm`, `μm`, `ms`)나 예외 조건을 마음대로 추측해 <strong>그럴듯해 보이지만 통계적으로 완전히 틀린 코드(환각, Hallucination)</strong>를 내놓거나, 수백 줄짜리 통짜 스파게티 코드를 만들어 사후 수정이 불가능해지기 때문입니다.<br><br>"
                    "그래서 저는 <strong>‘본(本)’</strong> 단계에서 먼저 문제의 물리적 본질을 정의하게 하고, <strong>‘기(機)’</strong> 단계에서 코딩 전에 입출력 스펙을 담은 `PRD.md`와 데이터 사전(`data_dict.md`)을 먼저 작성하게 해 제가 검토·승인합니다. 설계도가 확정된 후에만 <strong>‘함(函)’</strong> 단계로 넘어가 기능별 독립 함수와 예외 처리를 구현하게 하고, 마지막 <strong>‘구(構)’</strong> 단계에서 기존 파이프라인에 단순 추가할지 구조를 리빌딩할지 판단해 통합합니다. 이렇게 건물을 짓듯 단계별 승인 게이트(Gate)를 두면 환각이 0%로 통제되고 코드 재사용성이 극대화됩니다."
                )
            },
            {
                "tag": "데이터 무결성 검증",
                "question": "Context, Tool, Result 폴더를 엄격히 분리한다고 하셨는데, 이렇게 분리했을 때 현업 데이터 분석에서 얻는 가장 큰 실익이 무엇인가요?",
                "intent": "폴더 구조화의 엔지니어링 실익(원본 보존, 재현성, 감사 추적성)을 확인하는 질문입니다.",
                "answer": (
                    "가장 큰 실익은 <strong>‘원천 데이터 무결성 보존’과 ‘누가 언제 실행해도 100% 동일한 재현성 확보’</strong>입니다.<br><br>"
                    "엔지니어가 AI와 협업해 전처리나 필터링 스크립트를 여러 번 돌리다 보면 실수로 원본 CSV나 로그 파일을 덮어써서 원천 데이터가 오염되는 사고가 흔히 발생합니다. 저는 `Context` 폴더를 <strong>절대 수정 불가(Read-Only) 영역</strong>으로 가드레일에 못 박고, 실험용 1회성 코드는 `Tool/scratch/`에 격리하며, 검증이 끝난 정식 코드만 `Tool/버전명/`에 원클릭 `run.bat`과 함께 보관합니다. 그리고 `Result/버전명/`에 산출물과 이전 버전 대비 성능 비교(`benchmark_vs_prev.md`)를 남기기 때문에, 수개월 뒤에 고객 감사(Audit)나 타 부서 검증 요청이 와도 `run.bat` 더블클릭 한 번으로 당시 결과를 100% 그대로 재현할 수 있습니다."
                )
            },
            {
                "tag": "사내 보안 규정 방어",
                "question": "SK하이닉스는 국가핵심기술을 다루는 반도체 기업이라 외부 상용 생성형 AI에 사내 데이터를 절대 올릴 수 없습니다. 이런 폐쇄망 환경에서도 본인의 AI 워크플로우를 쓸 수 있나요?",
                "intent": "보안 의식(Data Security)과 사내 LLM/로컬 파이썬 개발 환경 적용 방법을 확인하는 필수 질문입니다.",
                "answer": (
                    "네, 오히려 저의 `Context-Tool-Result` 분리 프로토콜이 <strong>폐쇄망 보안 환경에 가장 최적화된 방식</strong>입니다.<br><br>"
                    "저는 AI에게 실제 사내 원천 데이터(`Context` 내부의 실제 값)를 통째로 넘기지 않습니다. 대신 데이터의 구조와 단위, 가상 더미 스키마만 정의된 <strong>데이터 사전(`data_dict.md`)과 요구사항 정의서(`PRD.md`)만을 바탕으로 사내 승인된 생성형 AI(사내 구축형 LLM/코딩 어시스턴트)가 파이썬 분석 로직(`Tool`)을 설계</strong>하도록 합니다. 그리고 실제 데이터 연산은 외부 통신이 완전히 차단된 로컬 PC의 파이썬 엔진(`run.bat`) 내부에서만 돌아가도록 분리되어 있기 때문에, 사내 데이터 유출 위험이 원천적으로 0%입니다."
                )
            },
            {
                "tag": "구조 단계(구) 사례 검증",
                "question": "'구(構)' 단계에서 기존 구조를 리빌딩할지 단순 덧붙일지(Append) 검토한다고 하셨는데, 실제로 리빌딩을 선택했던 사례가 있나요?",
                "intent": "실제로 '본·기·함·구'를 써본 사람만 답할 수 있는 구체적 의사결정 경험을 묻는 질문입니다.",
                "answer": (
                    "앞서 말씀드린 100만 장 Burr 이미지 선별 엔진을 개발할 때가 대표적입니다. 초기 버전(v1.0)에서는 단일 임계값(Threshold) 함수 위에 노이즈 제거 조건문만 단순 추가(Append)하려 했습니다. 하지만 Lot 간 배경 밝기 편차 문제가 불거졌을 때, 기존 코드에 조건문만 계속 덧대면 임계치 파라미터가 꼬여 미검률 0%를 보장할 수 없다고 판단했습니다.<br><br>"
                    "그래서 <strong>‘구(構)’ 단계에서 단순 추가(Append) 대신 파이프라인 전면 리빌딩(Rebuilding, v2.0)을 결정</strong>하여, 아예 앞단에 ‘배경 평균 밝기 55 기준 이원화 분기 모듈’을 신설하고 뒷단에 ‘$1\\times 7$ 수직 Bridge Kernel 모듈’을 직렬 결합하는 구조로 재설계했습니다. 덕분에 코드가 훨씬 간결해지고 처리 속도도 장당 $5\\,\\text{ms}$로 단축할 수 있었습니다."
                )
            }
        ]
    },
    {
        "badge": "프로젝트 5 · 신규 폼팩터 양산 이관 · 8D & FACA 기술 대응",
        "nav_title": "[프로젝트 5] New-form factor 양산 셋업 & 8D 고객 대응",
        "title": "[프로젝트 5] New-form factor(21/46 Series) 전극 개발~양산 Full-Cycle 셋업 및 글로벌 고객사 8D Report 기술 대응",
        "context_summary": [
            "<strong>수행 역할 (Role)</strong>: 신규 원통형(18/21/46 Series) 및 스트라이프/간헐/2패턴/절연 코팅 등 <strong>New-form factor 전극 비즈니스에서 개발 단계 스펙 선정 ➔ 샘플 생산 ➔ 시운전 기획 ➔ 설비/검사기 셋업 ➔ 양산 안정화</strong>까지 전 주기(Full-Cycle) 수행.",
            "<strong>고객 기술 대응 & 품질 사고 관리</strong>: 글로벌 고객사(T사 등) 대상 <strong>FACA(Failure Analysis & Corrective Action) 및 8D Report 작성, Daily 기술 미팅 및 라인 투어/Audit 대응</strong>. QMS, MES, EioT, Spotfire를 활용한 불량 원인 분석, Risk Range(위험 구간) 산정, 개선 대책 수립 및 유효성 검증."
        ],
        "base_speech": (
            "“저는 정해진 매뉴얼만 돌리는 운영에 그치지 않고, 차세대 21·46 시리즈 원통형 등 New-form factor 전극 비즈니스에서 개발 단계의 스펙 선정부터 샘플 시운전 기획, 설비·검사기 제어부 셋업, 그리고 양산 수율 안정화까지 전 주기를 바닥부터 수행했습니다. "
            "특히 까다로운 글로벌 고객사를 대상으로 매일 Daily 기술 미팅을 진행하며, 인라인 데이터 특이점이나 품질 이슈 발생 시 물리적 메커니즘에 기반한 원인 분석부터 Risk Range 확정, 재발 방지 대책 및 유효성 검증까지 담긴 FACA와 8D Report를 직접 작성해 출하 승인을 이끌어냈습니다. "
            "이러한 신제품 양산 이관(Ramp-up)과 데이터 기반 8D 문제 해결 역량은 SK하이닉스의 차세대 선단 공정 양산 안정화에도 즉시 기여할 수 있는 저의 핵심 자산입니다.”"
        ),
        "svg_title": "📊 [신규 제품 개발~양산 이관(Ramp-up) & 8D Report 품질 방어 프로세스]",
        "svg": """<svg viewBox="0 0 960 260" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="260" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <g transform="translate(20, 20)">
    <rect width="450" height="220" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="11.5" font-weight="800">1. New-form factor 개발 ➔ 양산 안정화 Full-Cycle</text>
    <rect x="16" y="42" width="418" height="162" rx="6" fill="#1e293b"/>
    <text x="28" y="66" fill="#fde047" font-size="9" font-weight="700">① 개발 스펙(Spec) 선정 &amp; 시운전 기획</text>
    <text x="36" y="82" fill="#cbd5e1" font-size="8">• 18/21/46 Series, 간헐·스트라이프·2패턴·절연 코팅 공정 능력 검토</text>
    <text x="28" y="106" fill="#38bdf8" font-size="9" font-weight="700">② 설비/검사기 셋업 &amp; 제어부 개조</text>
    <text x="36" y="122" fill="#cbd5e1" font-size="8">• Shim 전동화(LVDT) 및 웹게이지 미세라인 감지 로직 탑재</text>
    <text x="28" y="146" fill="#34d399" font-size="9" font-weight="700">③ SOP 정립 · 작업자 교육(PLM) · 양산 Cpk 안정화</text>
    <text x="36" y="162" fill="#6ee7b7" font-size="8">• 작업자 숙련도 편차 제거 및 초기 양산 수율 조기 안정화 달성</text>
    <text x="36" y="186" fill="#94a3b8" font-size="7.8">➔ SK하이닉스 R&amp;D ➔ 양산 FAB 이관(Ramp-up) 프로세스와 100% 상통</text>
  </g>
  <g transform="translate(490, 20)">
    <rect width="450" height="220" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="11.5" font-weight="800">2. 품질 사고 대책 관리 (FACA / 8D Report) 4단계</text>
    <rect x="16" y="42" width="418" height="162" rx="6" fill="#1e293b"/>
    <text x="28" y="66" fill="#f87171" font-size="9" font-weight="700">Step 1. Risk Range(위험 영향 범위) 즉각 확정 (QMS/MES/EioT)</text>
    <text x="36" y="82" fill="#cbd5e1" font-size="8">• 이상 발생 전후 Lot 및 설비 이력 추적으로 의심 구간 완벽 격리(Hold)</text>
    <text x="28" y="106" fill="#fde047" font-size="9" font-weight="700">Step 2. 물리적·데이터 기반 근본 원인 분석 (Spotfire / Python)</text>
    <text x="36" y="122" fill="#cbd5e1" font-size="8">• 발생 원인(Occurrence)과 유출 원인(Escape) 2축으로 4M1E 분석</text>
    <text x="28" y="146" fill="#34d399" font-size="9" font-weight="700">Step 3 &amp; 4. 시스템적 재발 방지 대책 수립 &amp; 유효성 검증</text>
    <text x="36" y="162" fill="#6ee7b7" font-size="8">• 작업자 주의 교육이 아닌 ‘설비 인터록·알고리즘 개조’로 원천 봉쇄 증명</text>
    <text x="36" y="186" fill="#94a3b8" font-size="7.8">➔ 글로벌 고객사 Daily 기술 미팅 및 Audit 무결점 통과</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "8D 리포트 실무 검증",
                "question": "고객 기술 대응으로 FACA와 8D Report를 많이 작성하셨다고 했는데, 8D 리포트를 쓸 때 고객사가 가장 집요하게 파고드는 항목이 무엇이며 본인은 어떻게 방어하셨나요?",
                "intent": "8D Report의 핵심인 '발생 원인(Occurrence) vs 유출 원인(Escape)' 구분과 '시스템적 재발 방지 대책'을 실제로 해봤는지 검증하는 질문입니다.",
                "answer": (
                    "글로벌 고객사가 8D 리포트에서 가장 집요하게 검증하는 두 가지는 <strong>① ‘왜 불량이 발생했는가(Occurrence Cause)’ 못지않게 ‘왜 기존 검사기가 이를 잡지 못하고 흘렸는가(Escape Cause)’</strong>, 그리고 <strong>② 재발 방지 대책이 단순 ‘작업자 재교육’인지 아니면 ‘설비·시스템적 Fool-proof 개조’인지</strong>입니다.<br><br>"
                    "또한 불량이 터졌을 때 어디서부터 어디까지가 오염 구간인지 특정하는 <strong>Risk Range(위험 범위) 산정 근거</strong>를 가장 엄격하게 봅니다. 저는 MES, EioT 설비 로그, Spotfire 데이터를 교차 분석해 설비 파라미터가 흔들린 정확한 시점(Timestamp)으로 Risk Range를 완벽히 구획해 보여줬고, 유출 원인에 대해서도 웹게이지 동적 임계치 로직이나 비전 Bridge Kernel처럼 <strong>검사 알고리즘 자체를 업그레이드한 정량적 유효성 검증 데이터</strong>를 제시해 고객사의 신뢰와 출하 승인을 이끌어냈습니다."
                )
            },
            {
                "tag": "개발-양산 스펙 조율",
                "question": "New-form factor 개발 단계에서 스펙(Spec) 선정부터 참여하셨다고 했는데, 개발 부서가 요구하는 타이트한 스펙과 실제 양산 설비 능력(Cpk)이 충돌할 때는 어떻게 해결하셨나요?",
                "intent": "SK하이닉스 양산기술의 핵심 업무인 'R&D 소자/공정 개발팀 ↔ FAB 양산 라인 간의 스펙 및 마진 조율' 역량을 평가하는 질문입니다.",
                "answer": (
                    "개발 부서는 제품 성능 극대화를 위해 공차를 최대한 타이트하게 잡으려 하고, 양산 라인은 기존 설비의 산포 한계 때문에 그대로 받으면 수율이 급락하는 딜레마가 항상 존재합니다.<br><br>"
                    "이때 저는 두 가지 트랙으로 접근했습니다. 첫째, <strong>설비 개조로 양산 능력을 끌어올릴 수 있는 영역</strong>(예: 수동 Shim 조정 산포를 LVDT 전동화로 제거)은 제가 직접 하드웨어와 제어 로직을 개선해 타이트한 스펙을 맞춰냈습니다. "
                    "둘째, 물리적 한계로 인해 불필요하게 과도한 스펙이 걸린 항목에 대해서는 시운전 샘플의 계측 데이터와 후공정·셀 성능 간의 상관관계 데이터를 분석하여, <strong>‘실제 품질에 영향이 없는 실질 관리 한계선’을 역제안해 스펙을 합리적으로 조정(Spec-in 협의)</strong>함으로써 초기 양산 수율과 품질을 동시에 잡았습니다."
                )
            },
            {
                "tag": "현장 작업자 설득 및 SOP",
                "question": "신규 기술이나 자동화 로직을 현장에 도입할 때 베테랑 오퍼레이터(작업자)들이 기존 방식을 고수하며 저항하는 경우는 없었나요?",
                "intent": "양산기술 엔지니어로서 현장 오퍼레이터 소통 능력과 SOP 정착 리더십을 확인하는 질문입니다.",
                "answer": (
                    "초기에는 분명 있었습니다. 예를 들어 수십 년간 손감각으로 다이얼게이지를 돌려 Shim을 맞추던 베테랑 작업자분들은 처음 전동화 장치를 도입할 때 ‘기계가 사람 손보다 못 맞춘다’며 불신하셨습니다.<br><br>"
                    "저는 말로만 지시하지 않고 현장에 밀착해 함께 야간 시운전을 뛰면서, <strong>수동 조작 시 발생하는 전후 편차 데이터와 LVDT 전동화 적용 시 단 한 번에 타겟에 안착해 작업자분들의 재조정 수고(조건조정 Loss)가 18%나 줄어든다는 결과</strong>를 눈앞에서 직접 보여드렸습니다. ‘작업자분들을 감시하려는 게 아니라 가장 힘들고 반복적인 셋업 스트레스를 덜어드리는 도구’라는 점을 체감하게 해드리자 오히려 현장에서 먼저 적극 활용하게 되었고, 이를 직관적인 사진 위주의 SOP로 표준화해 전 교대조에 성공적으로 안착시켰습니다."
                )
            },
            {
                "tag": "자주적 문제 해결",
                "question": "경력 기술서에 '사수가 퇴사하면서 내가 하고자 하는 대로 자주적으로 라인을 운영하며 풀어가는 과정이 재밌었다'고 하셨는데, 가장 막막했던 순간과 이를 독학으로 돌파한 경험은 무엇인가요?",
                "intent": "가르쳐주는 사람 없는 낯선 기술/트러블 상황에서 스스로 파고드는 자생력(Self-starter)을 확인하는 질문입니다.",
                "answer": (
                    "사수 부재 상황에서 신규 폼팩터 라인의 설비 제어부 개조와 비전/웹게이지 로직 변경을 혼자 맡았을 때가 가장 큰 도전이었습니다. 저는 기계공학 전공도, 컴퓨터비전 전공도 아니었기 때문에 기어의 백래시나 이미지 모폴로지 연산 같은 개념을 처음에는 전혀 몰랐습니다.<br><br>"
                    "하지만 누군가의 지시를 기다리는 대신, <strong>현장에서 직접 렌치를 들고 슬롯 다이와 기구부를 분해·조립하며 체결 토크와 유격의 물리적 원리를 몸으로 익혔고, 퇴근 후에는 AI 에이전트 워크플로우를 구축해 신호처리와 비전 알고리즘 수식을 바닥부터 파고들어 내 것으로 만들었습니다.</strong> 모르는 영역이라도 현장의 물리 현상과 데이터를 연결해 끝까지 해답을 찾아내는 이 자생력이야말로, 나노 반도체 공정에서도 제가 가장 빠르게 성장할 수 있는 원동력입니다."
                )
            }
        ]
    },
    {
        "badge": "도메인 물리 · 바인더 마이그레이션 · 체결 토크 정밀도",
        "nav_title": "[도메인 & 하이브리드] 건조 물리·체결 토크·전극 공정 원리",
        "title": "[도메인 & 하이브리드 역량] 바인더 마이그레이션(모세관 대류) 제어, 기계적 체결 토크 정밀도 및 반도체 공정 물리와의 연결",
        "context_summary": [
            "<strong>코터 공정의 중요성 이해</strong>: 코터는 배터리 품질과 원가의 80% 이상을 결정짓는 핵심 공정. 후공정(롤프레스·슬리팅)과 달리 코터에서 발생한 <strong>로딩량 편차, 코팅폭 불균일, 건조 크랙, 바인더 마이그레이션은 절대 되돌릴 수 없으며</strong> 셀의 N/P Ratio 불균형 및 급속충전 시 리튬 덴드라이트 석출로 직결됨.",
            "<strong>바인더 마이그레이션 5단계 메커니즘 & 해결책</strong>: ① Wet 슬러리 균일 분포 ➔ ② 건조 오븐 열풍에 의한 최외곽 표면 용매 증발 ➔ ③ <strong>모세관 압력(Capillary Force)에 의한 내부 용매의 표면 상승 대류(Convective Flux)</strong> ➔ ④ 용매에 휩쓸린 바인더 고분자의 표면 동반 상승 ➔ ⑤ 고화 임계점(Consolidation Point)에서 표면 바인더 편석 및 하부(Foil 계면) 바인더 고갈로 접착력 저하·미세크랙 발생. (<strong>해결: 항률 건조 구간 온도 하향 완속 건조 유도 및 슬러리 고형분 상향</strong>).",
            "<strong>슬러리 5대 물성 및 기계 체결 정밀도</strong>: 고형분, 점도(내부마찰저항), 분산도, <strong>그라인드게이지(Grind Gauge, 몇 $\\mu\\text{m}$ 깊이에서 입자 스크래치가 나는지 측정)</strong>, <strong>입도($D_{50}$ 평균 입경, $D_{max}$ 최대 응집 입경)</strong> 관리 및 <strong>토크렌치 기반 슬롯 다이 균일 체결</strong>."
        ],
        "base_speech": (
            "“저는 사무실에서 데이터만 본 것이 아니라, 현장에서 슬러리 유변학 물성과 열풍 건조의 이동현상(Transport Phenomena), 그리고 기계적 체결 정밀도까지 모든 물리적 변수를 통합적으로 다뤄왔습니다. "
            "예를 들어 건조 공정에서 바인더가 표면으로 쏠려 접착력을 떨어뜨리는 ‘바인더 마이그레이션’을 막기 위해, 모세관 상승 대류 속도보다 확산 속도가 지배하도록 항률 건조 구간(Constant-rate period)의 온도를 낮춰 완속 건조를 유도하고 고형분 조건을 최적화했습니다. "
            "또한 슬롯 다이 볼트를 조일 때도 작업자의 감이 아니라 토크렌치로 균일한 토크를 인가해 미세 뒤틀림에 의한 주름과 단차를 잡았습니다. "
            "이러한 열·물질 전달 물리와 기계적 정밀도 제어 감각은 반도체 박막 증착/베이크 공정의 열 예산(Thermal Budget) 및 박막 응력(Stress) 제어와도 물리적 본질이 정확히 맞닿아 있습니다.”"
        ),
        "svg_title": "📊 [바인더 마이그레이션(Binder Migration) 모세관 물리 & 기계적 체결 토크 정밀도 메커니즘]",
        "svg": """<svg viewBox="0 0 960 280" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
  <!-- Left: Binder Migration Physics -->
  <g transform="translate(20, 20)">
    <rect width="465" height="240" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">1. 바인더 마이그레이션 5단계 메커니즘 &amp; 페클레 수(Pe) 제어</text>
    <rect x="16" y="42" width="433" height="182" rx="6" fill="#1e293b"/>
    <text x="28" y="64" fill="#fca5a5" font-size="9" font-weight="700">❌ 급속 과열 건조 시 (표면 증발 속도 E &gt;&gt; 내부 확산 속도 D)</text>
    <text x="28" y="82" fill="#cbd5e1" font-size="8">• 표면 용매 급증발 ➔ 모세관력(Capillary Force)에 의해 하부 용매가 표면으로 급상승</text>
    <text x="28" y="98" fill="#cbd5e1" font-size="8">• 바인더(PVDF / SBR·CMC)가 용매 대류에 휩쓸려 상부 표면에만 편석(Segregation)</text>
    <text x="28" y="114" fill="#fca5a5" font-size="8" font-weight="700">➔ Foil-합제 계면 접착력 급락(박리) + 표면 급수축 미세크랙 + 셀 내부저항 폭증!</text>
    <line x1="28" y1="128" x2="430" y2="128" stroke="#475569" stroke-width="1"/>
    <text x="28" y="148" fill="#34d399" font-size="9" font-weight="700">✔ 해결 솔루션 (항률 건조 구간 제어 &amp; 고형분 상향)</text>
    <text x="28" y="166" fill="#6ee7b7" font-size="8">1) <tspan fill="#ffffff" font-weight="700">항률 구간(Zone 1~2) 온도 하향</tspan>: 표면 증발 속도를 늦춰 완속 건조 유도</text>
    <text x="28" y="184" fill="#6ee7b7" font-size="8">2) <tspan fill="#ffffff" font-weight="700">슬러리 고형분(Solid Content) 상향</tspan>: 날려야 할 용매 절대량 축소로 대류 억제</text>
    <text x="28" y="206" fill="#38bdf8" font-size="7.8">🔗 반도체 PR Soft Bake / SOD 큐어링 시 용매 급증발 보이드·크랙 제어와 동일 물리!</text>
  </g>
  <!-- Right: Slurry Metrology & Mechanical Torque -->
  <g transform="translate(503, 20)">
    <rect width="437" height="240" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="11.5" font-weight="800">2. 슬러리 입도(D50/Dmax)·그라인드게이지 &amp; 기계적 체결 토크</text>
    <rect x="16" y="42" width="405" height="86" rx="6" fill="#1e293b"/>
    <text x="28" y="62" fill="#fde047" font-size="9" font-weight="700">■ 슬러리 분산도 및 입도 관리 (라인 스크래치 원천 예방)</text>
    <text x="28" y="80" fill="#cbd5e1" font-size="8">• <tspan fill="#38bdf8" font-weight="700">그라인드게이지(Grind Gauge)</tspan>: 몇 μm 깊이에서 응집 입자가 긁혀 줄무늬가 나는지 측정</text>
    <text x="28" y="96" fill="#cbd5e1" font-size="8">• <tspan fill="#38bdf8" font-weight="700">입도 분포(D50 vs Dmax)</tspan>: 평균 입경(D50)이 정상이어도 최대 덩어리(Dmax)가</text>
    <text x="36" y="112" fill="#fca5a5" font-size="7.8">코팅 갭(Gap)보다 크면 다이 립에 걸려 치명적 라인 결함 유발 (필터 차압 관리 필수)</text>
    <rect x="16" y="138" width="405" height="86" rx="6" fill="#1e293b"/>
    <text x="28" y="158" fill="#34d399" font-size="9" font-weight="700">■ 기계적 정밀도의 핵심: 체결 토크(Torque)와 미세 유격</text>
    <text x="28" y="176" fill="#cbd5e1" font-size="8">• 슬롯 다이 바디 볼트 체결 시 작업자 감으로 조이면 미세 뒤틀림 ➔ 폭 방향 단차 및 주름</text>
    <text x="28" y="192" fill="#6ee7b7" font-size="8">• 토크렌치 정량 체결 표준화 ➔ 반도체 진공 챔버 조립·PM 정밀도 사상과 100% 일치</text>
  </g>
</svg>""",
        "qas": [
            {
                "tag": "열·물질 전달 물리 검증",
                "question": "건조 오븐에서 발생하는 '바인더 마이그레이션'이 무엇이며, 생산성을 높이려고 오븐 온도를 무조건 올리면 왜 불량이 나는지 물리적 메커니즘을 설명해 보세요.",
                "intent": "현상만 아는 오퍼레이터인지, 모세관 현상(Capillary Force)과 대류-확산 평형(Peclet Number) 원리를 이해하는 엔지니어인지 확인하는 질문입니다.",
                "answer": (
                    "바인더 마이그레이션은 건조 과정에서 집전체(Foil)와 활물질을 붙여줘야 할 바인더 고분자(양극 PVDF, 음극 SBR/CMC)가 전극 표면 쪽으로 몰려 올라가는 편석(Segregation) 현상입니다.<br><br>"
                    "라인 속도를 높이겠다고 초기 오븐 온도를 급격히 올리면, 전극 최외곽 표면의 용매가 먼저 맹렬하게 증발합니다. 이때 표면의 빈 공간을 채우기 위해 하부(Foil 쪽)에 있던 액체 용매가 <strong>모세관 압력(Capillary Force)에 의해 표면으로 강하게 빨려 올라가는 대류 현상(Convective Flux)</strong>이 일어납니다. 용매 안에 녹아 있거나 분산된 가벼운 바인더 입자들이 이 급격한 상승 물살에 휩쓸려 표면으로 동반 상승하고 그대로 굳어버립니다. "
                    "그 결과 <strong>정작 Foil과 맞닿는 바닥면에는 바인더가 텅 비어 전극이 벗겨지는 접착력 불량(Delamination)이 나고, 표면은 바인더 과밀집으로 급격히 수축해 미세 크랙</strong>이 발생하며 리튬이온 통로까지 막히게 됩니다.<br><br>"
                    "이를 막기 위해 저는 용매 증발이 가장 활발한 <strong>초기 항률 건조 구간(Constant-rate zone)에서는 온도를 낮춰 표면 증발 속도를 늦추는 완속 건조 프로파일</strong>을 적용하고, 선행 공정과 협의해 슬러리 고형분(Solid Content)을 높여 증발시켜야 할 용매의 절대량을 줄임으로써 해결했습니다."
                )
            },
            {
                "tag": "입도 & 계측 원리 검증",
                "question": "슬러리 품질 지표 중 $D_{50}$과 $D_{max}$, 그리고 그라인드게이지(Grind Gauge)가 각각 무엇이고 코터 공정에서 왜 중요한가요?",
                "intent": "선행 공정(믹싱)에서 넘어오는 원소재/슬러리 물성 지표를 정확히 해석할 줄 아는지 묻는 질문입니다.",
                "answer": (
                    "입도 분포에서 <strong>$D_{50}$은 입자들을 크기순으로 줄 세웠을 때 정중앙(50%)에 위치하는 평균 입자 크기</strong>이고, <strong>$D_{max}$는 완전히 풀리지 않고 남아 있는 가장 큰 응집체(덩어리)의 최대 크기</strong>입니다.<br><br>"
                    "코터 엔지니어에게 특히 $D_{max}$와 <strong>그라인드게이지(Grind Gauge)</strong>가 중요한 이유는 ‘라인 결함(Scratch / Line Defect)’과 직결되기 때문입니다. 그라인드게이지는 경사진 홈이 파인 금속 블록에 슬러리를 밀어 긁어보면서 <strong>몇 $\\mu\\text{m}$ 깊이에서 입자가 걸려 줄무늬 스크래치가 시작되는지 육안 판독하는 분산도 측정기</strong>입니다. 평균 입경($D_{50}$)이 정상이어도 $D_{max}$나 그라인드게이지 수치가 슬롯 다이의 코팅 갭($50 \\sim 150\\,\\mu\\text{m}$)이나 심(Shim) 간격에 근접하면 다이 립에 덩어리가 걸려 앞서 말씀드린 미세라인 불량을 유발합니다. 이는 반도체 CMP 슬러리에서 거대 응집 입자(Large Particle Tail)가 웨이퍼 마이크로 스크래치를 유발하는 원리와 정확히 같습니다."
                )
            },
            {
                "tag": "왜 코터만 했는가 방어",
                "question": "이력서를 보면 5년간 전극 코터(Coater) 공정만 담당하셨는데, 시야가 특정 설비에만 좁혀져 있는 건 아닌지 우려됩니다. 어떻게 생각하시나요?",
                "intent": "`context` 문서의 '왜 코터만 했어요?' 항목을 기반으로 한 경력 편중 압박 질문입니다.",
                "answer": (
                    "코터가 배터리 전체 품질과 원가의 80% 이상을 결정짓고, 전·후방 공정의 모든 물리적 변수가 교차하는 핵심 허브 공정이기 때문에 깊이 있게 파고들었습니다.<br><br>"
                    "후공정인 롤프레스나 슬리팅에서 발생하는 치수 문제는 공정 조건으로 일부 보정이 가능하지만, <strong>코터에서 발생한 로딩량 산포, Fat Edge/Sliding, 건조 크랙, 바인더 마이그레이션은 후공정에서 절대 되돌릴 수 없으며 곧바로 셀의 N/P Ratio 불균형과 리튬 덴드라이트 석출</strong>로 이어집니다. "
                    "특히 코터 문제를 해결하려면 앞단 믹싱의 슬러리 유변학($D_{50}/D_{max}$, 점도, 고형분)을 알아야 하고, 뒷단 롤프레스의 압연율·연신 특성과 슬리팅/노칭의 Burr 및 무지부 규격을 동시에 고려해 역설계해야 했습니다. 즉, 코터를 완벽히 통제하기 위해 전후 공정과의 상관관계를 5년간 치열하게 협업해 왔기 때문에 어떤 단위 공정에 배치되더라도 전후 공정 맥락을 아우르며 빠르게 적응할 자신이 있습니다."
                )
            },
            {
                "tag": "하이브리드 강점 종합",
                "question": "마지막으로, SK하이닉스 양산기술 지원자 중에는 반도체 전공자나 반도체 설비 경력자도 있습니다. 그들과 비교했을 때 본인을 반드시 뽑아야 하는 단 한 가지 결정적 강점은 무엇인가요?",
                "intent": "면접을 마무리하는 최종 킬러 질문입니다. HW(렌치/기구 개조) + SW(신호처리/비전/AI 프로토콜)를 모두 실전에서 증명한 유일무이한 실행력을 각인시켜야 합니다.",
                "answer": (
                    "저의 결정적 강점은 <strong>‘현장에서 직접 렌치를 들고 기구와 센서를 개조하는 하드웨어 실행력’과 ‘시계열 신호처리·컴퓨터 비전·AI 에이전트 워크플로우를 단독 코딩해 양산에 적용하는 소프트웨어 실행력’을 한 몸에 갖춘 하이브리드 엔지니어</strong>라는 점입니다.<br><br>"
                    "보통 설비를 잘 아는 엔지니어는 데이터 코딩을 어려워하고, 데이터 분석을 잘하는 엔지니어는 현장의 기구적 유격(Backlash)이나 체결 토크 같은 물리 현상을 모릅니다. 저는 실제로 <strong>100:1 웜기어와 LVDT 센서로 장비를 개조해 수율을 0.2% 올렸고, EMA 동적 임계치와 $1\\times 7$ Bridge Kernel 비전 엔진을 직접 코딩해 100만 장 선별(미검 0%)과 월 40시간 자동화를 이뤄낸 검증된 실행 기록</strong>이 있습니다. 입사 즉시 현장에 밀착해 공정 산포 제어와 스마트 팹 AX 혁신을 동시에 결과로 증명하겠습니다."
                )
            }
        ]
    }
]
