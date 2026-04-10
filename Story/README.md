# 라프라시아 야구 세계관 시뮬레이션

> **Lafprasia Baseball World Simulation**
> 
> 마법과 과학이 공존하는 라프라시아 대륙에서 펼쳐지는 야구 이야기

---

## 📖 프로젝트 개요

이 프로젝트는 **AI 기반 세계관 시뮬레이션**으로, 라프라시아 대륙이라는 가상 세계에서 펼쳐지는 야구 이야기를 다룹니다.

### 핵심 특징

- 🌍 **동적 세계 상태 관리**: 시간, 날씨, 이벤트가 실시간으로 변화
- 👥 **NPC 관계 시스템**: 호감도, 신뢰도, 관계 유형 추적
- 📊 **훈련 시뮬레이션**: 데이터 기반 선수 성장 시스템
- 📝 **이벤트 로깅**: 모든 상호작용 기록 및 추적
- 🏆 **프로 스카우트 시스템**: 선수들의 프로 진출 관리

---

## 🗺️ 세계관 설정

### 라프라시아 대륙 (Lafprasia)

마법과 과학이 공존하는 판타지 대륙. 야구는 전 대륙의 주요 스포츠이며, 다양한 종족들이 함께 경기합니다.

### 주요 종족

| 종족 | 특징 | 야구 강점 |
|------|------|----------|
| **휴먼 (Human)** | 균형 잡힌 능력 | 전략, 리더십 |
| **엘프 (Elf)** | 정밀함, 장수 | 컨트롤, 정확도 |
| **드워프 (Dwarf)** | 힘, 끈기 | 파워, 수비 |
| **하플링 (Halfling)** | 민첩함, 행운 | 스피드, 타격 |
| **오크 (Orc)** | 힘, 공격성 | 파워 투구 |

### 주요 국가

- **하플랜드 왕국 (Hafland)**: 야구의 본고장
- **아스테르 왕국 (Astell)**: 전통 강호
- **아이언 포지 왕국 (Iron Forge)**: 드워프 중심
- **실바니아 연방 (Sylvania)**: 엘프 중심

---

## 👤 주요 등장인물

### 카일 윈저 (Kyle Winzer)

- **나이**: 8세
- **종족**: 휴먼
- **직업**: 하플랜드 로얄 야구 아카데미 코치과 입학생
- **특기**: 현대 야구 전략, 데이터 분석, 세이버메트릭스
- **목표**: 프로팀 전략 코치

**능력치**:
```json
{
  "str": 5,
  "dex": 6,
  "int": 15,
  "cha": 8,
  "baseball_knowledge": 108
}
```

### 에릴 (Elil)

- **나이**: 62세 (엘프 기준, 외형 8세)
- **종족**: 엘프
- **직업**: 야구부 선수 (투수)
- **특기**: 정교한 커브, 엘프족 활쏘기 기술
- **목표**: 프로 야구 선수

**투구 스탯**:
```json
{
  "era": 2.78,
  "strikeouts": 145,
  "pitch_speed": 89,
  "pitch_control": 94,
  "curve_accuracy": 96
}
```

### 토비 (Toby)

- **나이**: 9세
- **종족**: 하플링
- **직업**: 코치과 입학생
- **특기**: 세이버메트릭스, 통계 분석
- **목표**: 데이터 분석 코치

---

## 🏢 라프라시아 야구 연구회

**창설일**: 라프라시아 780년 3월 15일

### 멤버

| 이름 | 역할 | 특기 |
|------|------|------|
| **카일** | 회장 (코치 지망생) | 데이터 분석, 현대 야구 전략 |
| **토비** | 데이터 분석가 | 세이버메트릭스, 통계학 |
| **에릴** | 기술 고문 (선수) | 엘프족 커브, 투구 기술 |

### 목표

코치와 선수의 협력을 통한 야구 발전

---

## 📁 폴더 구조

```
novel/
├── world_state.json              # 세계 상태 (메인 데이터)
├── chapters/                     # 에피소드
│   ├── episode_01.md            # 입학
│   ├── episode_02.md            # 첫 수업
│   └── episode_03.md            # 전략 과제
├── characters/                   # 캐릭터 설정
│   └── protagonist.md
├── research/                     # 세계관 설정
│   ├── world_overview.md
│   ├── continent_lafprasia.md
│   ├── races.md
│   ├── countries.md
│   ├── baseball_culture.md
│   └── magic_science.md
├── simulation_log/              # 시뮬레이션 로그
│   ├── 780-03-15_log.json
│   ├── 780-03-15_complete.json
│   ├── 780-03-15_training.json
│   ├── 780-03-15_eril_player.json
│   ├── 780-03-15_eril_training.json
│   └── 780-03-16_log.json
└── training_journal/            # 훈련 일지
    └── kyle_journal_780-03-15.json
```

---

## 🎮 시뮬레이션 기능

### 1. 세계 상태 관리

- 시간 흐름 (년/월/일/시간)
- 날씨 변화
- 이벤트 발생 및 추적
- NPC 위치 및 활동 관리

### 2. 관계 시스템

- 호감도 변화
- 관계 유형 (친구, 멘토, 전문가 등)
- 대화 기록
- 협력 이벤트

### 3. 훈련 시스템

- 선수별 맞춤 훈련 프로그램
- 스탯 성장 추적
- 데이터 기반 피드백
- 훈련 일지 작성

### 4. 이벤트 시스템

- 완료된 이벤트 기록
- 진행 중인 이벤트 추적
- 예정된 이벤트 관리

---

## 📅 주요 이벤트 타임라인

### 780년 3월 15일

- ✅ 아카데미 입학
- ✅ 첫 수업
- ✅ 에릴 만남
- ✅ 라프라시아 야구 연구회 창설
- ✅ 레이몬드 감독 면담
- ✅ 스피드스터즈 선수 코칭
- ✅ 에릴 선수 전향
- ✅ 에릴 전용 훈련 프로그램 개발

### 780년 3월 16일

- ✅ 라프라시아 야구 연구회 제 1회 미팅
- ✅ 향후 훈련 계획 수립
- ✅ 프로 스카우트 대비 전략

### 예정된 이벤트

- 🗓️ **780년 4월 1일**: 인턴십 시작 (스피드스터즈)
- 🗓️ **780년 4월 15일**: 아마추어 리그 개막

---

## 🛠️ 기술 스택

- **데이터 형식**: JSON
- **문서 형식**: Markdown
- **버전 관리**: Git
- **시뮬레이션**: AI 기반 대화형
- **자동화**: GitHub Actions
- **명세 관리**: [OpenSpec](https://github.com/Fission-AI/OpenSpec)

---

## 📘 OpenSpec 명세 기반 개발

이 프로젝트는 **OpenSpec**을 사용하여 명세 기반 개발 (SDD) 을 수행합니다.

### 빠른 시작

```bash
# Windows
scripts\init_openspec.bat

# macOS/Linux
chmod +x scripts/init_openspec.sh
./scripts/init_openspec.sh
```

### 지원 도구 (OpenSpec 공식 27 개 중 5 개 설정 완료)

| 도구 | 설정 파일 | 상태 |
|------|----------|------|
| **OpenCode** | `.opencode/skills/`, `.opencode/commands/` | ✅ 설정 완료 |
| **GitHub Copilot** | `.github/skills/`, `.github/prompts/` | ✅ 설정 완료 |
| **Qwen Code** | `.qwen/skills/`, `.qwen/commands/` | ✅ 설정 완료 |
| **Cursor** | `.cursor/skills/`, `.cursor/commands/` | ✅ 설정 완료 |
| **Claude Code** | `.claude/skills/`, `.claude/commands/` | ✅ 설정 완료 |

자세한 도구 목록은 [OPENSPEC_ALL_TOOLS_SETUP.md](OPENSPEC_ALL_TOOLS_SETUP.md) 를 참조하세요.

### 주요 명령어

| 명령어 | 설명 |
|--------|------|
| `/opsx:propose "기능명"` | 새 기능 제안 |
| `/opsx:apply` | 명세 적용 |
| `/opsx:archive` | 완료된 기능 아카이브 |

### 예시

```bash
# Qwen Code 에서
/opsx:propose "배틀 시스템 추가"
/opsx:propose "새 NPC 추가 - 올리비아"
/opsx:propose "에피소드 4 작성 - 인턴십 첫 날"

# 명세 적용
/opsx:apply

# 아카이브
/opsx:archive
```

자세한 내용은 [OPENSPEC_GUIDE.md](OPENSPEC_GUIDE.md) 와 [OPENSPEC_TOOLS.md](OPENSPEC_TOOLS.md) 를 참조하세요.

---

## ⚙️ GitHub Actions 워크플로우

이 프로젝트는 GitHub Actions 를 통해 자동화된 테스트와 콘텐츠 인덱싱을 수행합니다.

| 워크플로우 | 설명 | 상태 |
|------------|------|------|
| [Game Test](.github/workflows/game-test.yml) | Python/JSON 유효성 검사, 장면 검증 | ![Game Test](https://github.com/kimjunwoo1206112-oss/Designing-a-Worldview-Simulation-Agent/actions/workflows/game-test.yml/badge.svg) |
| [Content Index](.github/workflows/content-index.yml) | 콘텐츠 검색 인덱스 생성 | ![Content Index](https://github.com/kimjunwoo1206112-oss/Designing-a-Worldview-Simulation-Agent/actions/workflows/content-index.yml/badge.svg) |

### 검색 인덱스

`.github/search-index/` 폴더에 자동 생성되는 인덱스 파일:
- `content-index.json` - 전체 콘텐츠 검색 인덱스
- `project-summary.json` - 프로젝트 요약 정보

GitHub Code Search 를 통해 인덱스를 검색할 수 있습니다.

---

## 📝 라이선스

이 프로젝트는 교육 및 연구 목적으로 작성되었습니다.

---

## 🤝 기여자

- **세계관 설계**: AI Assistant (Qwen3.5-Plus)
- **스토리 진행**: 사용자 참여형
- **캐릭터 개발**: 협업

---

> *"마법과 과학이 공존하는 라프라시아에서, 야구는 단순한 스포츠가 아닌 예술이다."*
