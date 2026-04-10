# OpenSpec 실제 사용 예시 분석
## ClickerGameCaterpillars 프로젝트 참조

---

## 📊 분석 결과

### 1. 프로젝트 개요
- **프로젝트명**: ClickerGameCaterpillars (Unity 애벌레 클릭 게임)
- **장르**: 클릭커 게임
- **상태**: Phase 1-3 완료 (100%)
- **OpenSpec 적용**: 실제 운영 중

---

## 📁 실제 OpenSpec 구조

### 생성된 Change 예시
```
openspec/changes/fix-phase3-prefab-references/
├── proposal.md          # 왜 필요한지, 무엇을 변경하는지
├── design.md            # 어떻게 구현하는지 (의사결정 포함)
├── tasks.md             # 구현 체크리스트
└── specs/
    ├── touch-function-list-item-ui/
    │   └── spec.md      # UI 명세
    └── touch-function-list-view/
        └── spec.md      # 뷰 명세
```

---

## 📝 실제 명세 파일 분석

### 1. proposal.md (33 줄)
```markdown
## Why
TouchFunctionListItem 프리팹의 UI 참조가 모두 null 로 설정되어 있어, 
게임 실행 시 터치 강화 목록 UI 가 정상 작동하지 않습니다.

## What Changes
- TouchFunctionListItem 프리팹의 UI 요소 이름을 코드와 일치시킴
- 누락된 CostText, PointsText UI 요소 추가
- 모든 UI 참조를 SerializedObject 로 자동 연결

## Capabilities
### New Capabilities
- `touch-function-list-item-ui`: 터치 강화 리스트 아이템 UI 컴포넌트

### Modified Capabilities
- `touch-function-list-view`: 리스트 뷰가 올바르게 연결된 프리팹 인스턴스화

## Impact
**Affected Files:**
- `Assets/Prefabs/TouchFunctionListItem.prefab` (재생성)
- `Assets/Editor/Phase3Setup.cs` (UI 요소 이름 수정)

**Breaking Changes:**
- 기존 Scene 에 배치된 UpgradeListItem 오브젝트는 더 이상 작동하지 않음
```

**✅ 배운 점:**
- **Why 섹션**: 문제 상황을 명확히 설명
- **Capabilities**: 새로운/수정된 기능 명시
- **Impact**: 영향받는 파일과 Breaking Changes 명시

---

### 2. design.md (107 줄)
```markdown
## Context
**Background:**
TouchFunctionListItem 프리팹은 Phase 3 터치 강화 시스템의 핵심 UI 컴포넌트입니다.

**Current State:**
```
Prefab Structure (현재):
├── FunctionName (Text)      ← 코드는 NameText 찾음
├── Description (Text)       ← 코드는 DescriptionText 찾음
└── [CostText 없음]         ← 코드는 CostText 찾음
```

## Goals / Non-Goals
**Goals:**
- TouchFunctionListItem 프리팹의 모든 UI 참조가 정상 연결됨
- CostText, PointsText UI 요소가 프리팹에 포함됨

**Non-Goals:**
- UI 디자인/레이아웃 변경 (위치, 크기, 색상 등)
- TouchFunctionListItem.cs 의 로직 변경

## Decisions
### Decision 1: 프리팹 재생성 방식 선택
**Decision:** 기존 프리팹 삭제 후 Phase3Setup.CreatePrefab() 으로 재생성

**Rationale:**
- 자동화된 코드로 생성하는 것이 일관성 보장
- SerializedObject 를 사용하면 private 필드도 자동 설정 가능

**Alternatives Considered:**
1. ❌ 수동으로 프리팹 편집
   - 일관성 보장 어려움
   - 재현 불가능

2. ❌ 프리팹 Variant 사용
   - 복잡도 증가

## Risks / Trade-offs
### Risk 1: 기존 Scene 의 UpgradeListItem 오브젝트 무효화
**Risk:** Scene 에 수동으로 배치한 UpgradeListItem 이 새 프리팹과 호환되지 않음

**Mitigation:** Phase3Setup.ConnectSceneUI() 에서 자동으로 삭제하고 교체
```

**✅ 배운 점:**
- **Context**: 현재 상태와 배경 설명
- **Goals/Non-Goals**: 범위 명확히 설정 (무엇을 **안** 하는지 포함)
- **Decisions**: 결정과 대안, 그리고 그 이유 (Rationale)
- **Risks**: 위험 요소와 완화 방안

---

### 3. tasks.md (56 줄)
```markdown
## 1. Prefab Recreation
- [x] 1.1 Delete existing TouchFunctionListItem.prefab
- [x] 1.2 Create TouchFunctionListItem Prefab via code
- [x] 1.3 Verify prefab has all 7 UI elements
- [x] 1.4 Verify all UI references are connected

## 2. Scene UI Connection
- [x] 2.1 Auto-connect Scene UI via code
- [x] 2.2 Verify TouchFunctionListView.itemPrefab references new prefab
- [x] 2.3 Verify TouchFunctionListView.contentParent references Content

## 3. Testing
- [ ] 3.1 Run game and verify TouchFunctionPanel displays function list
- [ ] 3.2 Click character 50 times to earn 50 points
- [ ] 3.3 Click Add button (+) on a function and verify it activates
- [ ] 3.4 Click Remove button (-) on active function and verify it deactivates

## 4. Cleanup
- [x] 4.1 Remove UpgradeListItem objects from scene (automated)
- [x] 4.2 Remove GameObject empty objects from scene (automated)
- [x] 4.3 Fixed: Removed infinite debug logging

---

## Implementation Notes
**Completed via code:**
- Task 1.1-1.4: Prefab 생성 및 UI 연결 ✓
- Task 2.1-2.4: Scene UI 자동 연결 ✓
- Task 4.1-4.2: 정리 작업 자동화 ✓

**Requires Unity Editor (Manual Testing):**
- Task 3.1-3.5: 게임 실행 및 기능 테스트

**Bug Fixes:**
- Removed infinite Update() loop in TouchFunctionListItem
- Removed excessive Debug.Log calls
```

**✅ 배운 점:**
- **체크박스**: `[x]` 완료, `[ ]` 미완료 시각적 표시
- **그룹화**: 관련 작업을 섹션으로 묶음
- **Implementation Notes**: 완료된 작업과 수동 테스트 필요 항목 구분
- **Bug Fixes**: 수정된 버그 명시

---

## 🔧 .opencode 설정 분석

### 스킬 구조
```
.opencode/
├── skills/
│   ├── openspec-propose/
│   │   └── SKILL.md          # 명세 제안 스킬
│   ├── openspec-apply-change/
│   │   └── SKILL.md          # 명세 적용 스킬
│   ├── openspec-archive-change/
│   │   └── SKILL.md          # 아카이브 스킬
│   └── openspec-explore/
│       └── SKILL.md          # 탐색 스킬
└── command/
    ├── opsx-propose.md       # 제안 명령
    ├── opsx-apply.md         # 적용 명령
    ├── opsx-archive.md       # 아카이브 명령
    └── opsx-explore.md       # 탐색 명령
```

### SKILL.md 특징 (110 줄)
```markdown
---
name: openspec-propose
description: Propose a new change with all artifacts generated in one step
license: MIT
compatibility: Requires openspec CLI
metadata:
  author: openspec
  version: "1.0"
---

Propose a new change - create the change and generate all artifacts in one step.

I'll create a change with artifacts:
- proposal.md (what & why)
- design.md (how)
- tasks.md (implementation steps)

When ready to implement, run /opsx-apply

---

**Input**: The user's request should include a change name...

**Steps**

1. **If no clear input provided, ask what they want to build**
   Use the **AskUserQuestion tool**...

2. **Create the change directory**
   ```bash
   openspec new change "<name>"
   ```

3. **Get the artifact build order**
   ```bash
   openspec status --change "<name>" --json
   ```

4. **Create artifacts in sequence until apply-ready**
   Loop through artifacts in dependency order...

5. **Show final status**
   ```bash
   openspec status --change "<name>"
   ```

**Guardrails**
- Create ALL artifacts needed for implementation
- Always read dependency artifacts before creating a new one
- If context is critically unclear, ask the user
```

**✅ 배운 점:**
- **메타데이터**: name, description, license, version 명시
- **입력 정의**: 사용자가 무엇을 입력해야 하는지 명확히
- **단계적 절차**: 1-5 단계까지 구체적인 순서
- **Guardrails**: 안전 장치와 가이드라인

---

## 🎯 라프라시아 프로젝트에 적용할 점

### 1. 명세 파일 구조 개선
```markdown
# 현재 라프라시아 명세
- proposal.md (배경, 목표, 범위)
- design.md (기술 설계)
- tasks.md (작업 목록)

# 개선할 점
✅ Why 섹션 강화 (문제 상황 명확히)
✅ Capabilities 섹션 추가 (새로운/수정된 기능)
✅ Goals/Non-Goals 명시 (무엇을 안 하는지)
✅ Decisions with Rationale (결정과 이유)
✅ Risks/Mitigation (위험과 완화 방안)
✅ Implementation Notes (완료/수동 테스트 구분)
```

### 2. tasks.md 체크박스 활용
```markdown
## 1. 기능 구현
- [x] 1.1 작업 설명
- [ ] 1.2 작업 설명

## 2. 테스트
- [ ] 2.1 게임 실행 테스트

## Implementation Notes
**Completed:**
- Task 1.1-1.2 ✓

**Requires Manual Testing:**
- Task 2.1
```

### 3. .opencode 스킬 메타데이터 추가
```markdown
---
name: openspec-propose
description: Propose a new feature for Lafprasia RPG
license: MIT
author: World Simulator Agent
version: "1.0"
---
```

### 4. Change 이름 규칙
```
# 좋은 예
fix-phase3-prefab-references      ✅ 구체적
add-battle-system                 ✅ 기능 명확
write-episode-4-internship        ✅ 내용 포함

# 나쁜 예
fix-bug                           ❌ 너무 일반적
update                            ❌ 내용 불명확
new-feature                       ❌ 구체성 부족
```

---

## 📋 라프라시아 프로젝트에 바로 적용할 템플릿

### proposal.md 템플릿 (개선됨)
```markdown
# 제안: {{feature}}

## Why
[왜 필요한가? 현재 문제점은? 구체적인 상황 설명]

## What Changes
- 변경 사항 1
- 변경 사항 2

## Capabilities
### New Capabilities
- `capability-id`: 새로운 기능 설명

### Modified Capabilities
- `modified-capability`: 수정된 기능 설명

## Impact
**Affected Files:**
- `경로/파일명` (변경 내용)

**Dependencies:**
- 의존성 설명

**Breaking Changes:**
- 하위 호환성 깨지는 변경사항
```

### design.md 템플릿 (개선됨)
```markdown
## Context
**Background:**
[배경 설명]

**Current State:**
```
현재 구조:
├── 요소 A      ← 문제점
└── 요소 B      ← 문제점
```

## Goals / Non-Goals
**Goals:**
- 달성할 목표 1
- 달성할 목표 2

**Non-Goals:**
- 하지 않을 작업 1
- 하지 않을 작업 2

## Decisions
### Decision 1: {{decision_name}}
**Decision:** 선택한 방안

**Rationale:**
- 선택 이유 1
- 선택 이유 2

**Alternatives Considered:**
1. ❌ 대안 1
   - 채택하지 않은 이유

2. ❌ 대안 2
   - 채택하지 않은 이유

## Risks / Trade-offs
### Risk 1: {{risk_name}}
**Risk:** 위험 설명

**Mitigation:** 완화 방안
```

### tasks.md 템플릿 (개선됨)
```markdown
## 1. {{group_name}}
- [ ] 1.1 작업 설명
- [ ] 1.2 작업 설명

## 2. {{group_name}}
- [ ] 2.1 작업 설명

---

## Implementation Notes
**Completed:**
- Task 1.1-1.2: 작업 내용 ✓

**Requires Manual Testing:**
- Task 2.1: 테스트 내용

**Bug Fixes:**
- 수정된 버그 설명
```

---

## 🚀 다음 단계

### 1. 라프라시아 프로젝트에 적용
```bash
# 첫 번째 개선된 명세 작성
/opsx:propose "add-eril-pro-scout-event"
```

### 2. 기존 명세 업데이트
```
openspec/changes/
├── add-initial-game-engine/
│   ├── proposal.md          # 개선된 템플릿으로 업데이트
│   ├── design.md
│   └── tasks.md
```

### 3. .opencode 스킬 메타데이터 추가
```markdown
---
name: openspec-propose
description: Propose a new feature for Lafprasia Baseball RPG
license: MIT
author: World Simulator Agent
version: "1.0"
---
```

---

## 📊 비교 요약

| 항목 | ClickerGameCaterpillars | 라프라시아 (현재) | 개선 방향 |
|------|------------------------|------------------|----------|
| **proposal.md** | Why, Capabilities, Impact 명시 | 배경, 목표, 범위 | ✅ Why 강화, Capabilities 추가 |
| **design.md** | Goals/Non-Goals, Decisions, Risks | 기술 설계 | ✅ Non-Goals, Risks 추가 |
| **tasks.md** | 체크박스, Implementation Notes | 작업 목록 | ✅ 체크박스, Notes 추가 |
| **SKILL.md** | 메타데이터, 단계적 절차 | 기본 설명 | ✅ 메타데이터, Guardrails 추가 |

---

> **핵심 교훈**:
> 1. **명확한 Why**: 문제 상황을 구체적으로 설명
> 2. **범위 설정**: 무엇을 **안** 하는지 명시 (Non-Goals)
> 3. **결정과 이유**: 왜 이 방식을 선택했는지 (Rationale)
> 4. **위험 관리**: 예상 위험과 완화 방안
> 5. **시각적 표시**: 체크박스로 진행 상황 표시
> 6. **메타데이터**: 스킬에 버전, 저자, 라이선스 명시

**이제 라프라시아 프로젝트의 OpenSpec 명세를 더 구체적이고 실용적으로 개선할 수 있습니다!** 🚀⚾🪄
