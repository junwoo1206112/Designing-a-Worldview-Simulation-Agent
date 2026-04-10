# OpenSpec 설정 - 라프라시아 야구 시뮬레이션 RPG

## 프로젝트 개요

**프로젝트명**: Diamond & Magic - 라프라시아 야구 시뮬레이션 RPG  
**유형**: 텍스트 기반 시뮬레이션 게임  
**주요 기술**: Python, JSON, Markdown  
**AI 어시스턴트**: Qwen3.5-Plus (World Simulator)

---

## 📁 OpenSpec 디렉토리 구조

```
openspec/
├── changes/                    # 변경 사항 관리
│   ├── active/                 # 진행 중인 변경
│   │   ├── add-battle-system/
│   │   ├── expand-npc-relationships/
│   │   └── implement-gacha-system/
│   └── archive/                # 완료된 변경 (아카이브)
│       └── 2026-04-07-initial-game-engine/
├── specs/                      # 명세 문서
│   ├── game-system-spec.md
│   ├── world-state-spec.md
│   └── npc-relationship-spec.md
└── proposals/                  # 제안서
    ├── new-feature-proposals/
    └── accepted-proposals/
```

---

## 🎯 OpenSpec 워크플로우 적용 예시

### 1. 새 기능 추가 (예: 배틀 시스템)

```bash
# 1. 제안 생성
/opsx:propose "배틀 시스템 추가 - 야구 경기 중 특수 능력 배틀"

# 생성되는 파일:
openspec/changes/add-battle-system/
├── proposal.md          # 왜 추가하는지, 어떤 변경이 있는지
├── specs/
│   ├── requirements.md  # 요구사항
│   └── scenarios.md     # 시나리오
├── design.md            # 기술적 접근
└── tasks.md             # 구현 체크리스트

# 2. 명세 검토 후 적용
/opsx:apply

# 3. 구현 완료 후 아카이브
/opsx:archive
```

### 2. NPC 관계 시스템 확장

```bash
/opsx:propose "NPC 관계 시스템 확장 - 호감도 단계 세분화 및 이벤트 추가"
```

### 3. 새 에피소드 추가

```bash
/opsx:propose "에피소드 4 추가 - 인턴십 첫 날"
```

---

## 📝 명세 템플릿

### `proposal.md` 템플릿

```markdown
# 제안: [기능명]

## 배경
[왜 이 기능이 필요한가?]

## 목표
- [ ] 목표 1
- [ ] 목표 2

## 범위
### 포함
- 기능 A
- 기능 B

### 제외
- 기능 C (나중으로 연기)

## 영향 분석
### 변경되는 파일
- `game/engine.py`
- `novel/world_state.json`
- `game/scenes.json`

### 영향받는 시스템
- 상태 관리 시스템
- 관계 시스템

## 성공 기준
- [ ] 기준 1
- [ ] 기준 2
```

### `design.md` 템플릿

```markdown
# 기술 설계: [기능명]

## 아키텍처
[시스템 다이어그램 또는 설명]

## 데이터 구조
```json
{
  "new_field": "type"
}
```

## 구현 계획
1. 단계 1
2. 단계 2
3. 단계 3

## 테스트 계획
- [ ] 단위 테스트
- [ ] 통합 테스트
- [ ] 플레이 테스트
```

---

## 🔄 GitHub Actions 와 연동

### OpenSpec 변경 감지 워크플로우

```yaml
# .github/workflows/openspec-validate.yml
name: OpenSpec Validation

on:
  push:
    paths:
      - 'openspec/**'

jobs:
  validate-proposal:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Validate Proposal Structure
        run: |
          # openspec/changes/active/ 폴더 검증
          python3 scripts/validate-openspec.py
      
      - name: Check Spec Completeness
        run: |
          # 명세서 완결성 확인
          python3 scripts/check-specs.py
```

---

## 🎮 라프라시아 프로젝트 적용 사례

### 사례 1: 게임 엔진 확장

```bash
/opsx:propose "경기 시뮬레이션 시스템 추가"
```

**생성되는 명세:**
- `openspec/changes/add-game-simulation/proposal.md`
- `openspec/changes/add-game-simulation/specs/requirements.md`
- `openspec/changes/add-game-simulation/design.md`
- `openspec/changes/add-game-simulation/tasks.md`

### 사례 2: 월드스테이트 스키마 변경

```bash
/opsx:propose "월드스테이트 스키마 v2.0 - 종족 관계 시스템 추가"
```

### 사례 3: 새 지역 추가

```bash
/opsx:propose "새 지역 추가 - 실바니아 연방 (엘프 왕국)"
```

---

## 📊 OpenSpec 사용 이점

| 이점 | 설명 |
|------|------|
| **명확한 요구사항** | AI 와 인간이 명세로 소통 |
| **조직화된 변경** | 각 기능이 별도 폴더로 관리 |
| **추적 가능성** | 변경 이력이 명확히 기록 |
| **재사용성** | 명세를 템플릿으로 활용 |
| **협업 용이** | 여러 기여자가 명세 기반 작업 |

---

## 🚀 빠른 시작

### 1. OpenSpec 설치

```bash
npm install -g @fission-ai/openspec@latest
```

### 2. 프로젝트 초기화

```bash
cd C:\Story
openspec init
```

### 3. 프로필 설정

```bash
openspec config profile
# → "spec-driven" 선택
```

### 4. 첫 제안 시작

```bash
/opsx:propose "게임 밸런스 조정 - 체력 시스템 개선"
```

---

## 📁 권장 파일 구조

```
C:\Story/
├── .openspec/                    # OpenSpec 설정
│   ├── config.json
│   └── profiles/
│       └── spec-driven.json
├── openspec/
│   ├── changes/
│   │   ├── active/
│   │   └── archive/
│   ├── specs/
│   └── proposals/
├── game/
├── novel/
└── .github/
    └── workflows/
        ├── openspec-validate.yml
        └── game-test.yml
```

---

## 🎯 다음 단계

1. **OpenSpec 설치**: `npm install -g @fission-ai/openspec`
2. **프로젝트 초기화**: `openspec init`
3. **첫 명세 작성**: `/opsx:propose` 사용
4. **GitHub Actions 연동**: 워크플로우 추가

---

> **OpenSpec 철학**:
> - 엄격하지 않고 유연하게
> - 워터폴이 아닌 반복적으로
> - 복잡하지 않고 쉽게
> - 그린필드뿐만 아니라 브라운필드도
> - 개인 프로젝트부터 기업까지 확장 가능
