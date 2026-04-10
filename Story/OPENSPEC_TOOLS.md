# OpenSpec 지원 도구 - 라프라시아 프로젝트

## 📋 지원 도구 목록 (27 개)

OpenSpec 은 다음과 같은 AI 코딩 어시스턴트를 지원합니다:

### 🔧 현재 프로젝트에서 사용 중인 도구

| 도구 | 상태 | 설정 경로 |
|------|------|----------|
| **Qwen Code** | ✅ 사용 중 | `.qwen/` |
| **GitHub Copilot** | ✅ 사용 중 | `.github/` |
| **OpenCode** | ✅ 사용 중 | `.opencode/` |

---

## 🎯 권장 도구 설정

### 라프라시아 프로젝트 추천 조합

```bash
# Qwen Code + GitHub Copilot + OpenCode
openspec init --tools qwen,github-copilot,opencode --profile core
```

### 도구별 특징

| 도구 | 추천 사용 사례 | 설정 난이도 |
|------|---------------|------------|
| **Qwen Code** | 세계관 시뮬레이션, 데이터 관리 | ⭐⭐⭐ |
| **GitHub Copilot** | 코드 작성, 게임 엔진 개발 | ⭐⭐ |
| **OpenCode** | 에이전트 기반 작업 | ⭐⭐ |
| **Claude Code** | 명세 작성, 문서화 | ⭐⭐ |
| **Cursor** | 통합 개발 환경 | ⭐ |

---

## 📁 도구별 설치 경로

### Qwen Code (`.qwen/`)
```
.qwen/
├── skills/
│   └── openspec-*/
│       ├── openspec-propose.md
│       ├── openspec-apply.md
│       └── openspec-archive.md
└── commands/
    └── opsx-<id>.toml
```

### GitHub Copilot (`.github/`)
```
.github/
├── skills/
│   └── openspec-*/
│       └── SKILL.md
└── prompts/
    └── opsx-<id>.prompt.md
```

### OpenCode (`.opencode/`)
```
.opencode/
├── skills/
│   └── openspec-*/
│       └── SKILL.md
└── commands/
    └── opsx-<id>.md
```

---

## 🚀 초기화 명령어

### Windows (Batch)
```batch
REM scripts/init_openspec.bat 실행
scripts\init_openspec.bat
```

### 수동 설정
```bash
# 1. OpenSpec 설치
npm install -g @fission-ai/openspec@latest

# 2. 프로젝트 초기화 (Qwen + Copilot + OpenCode)
cd C:\Story
openspec init --tools qwen,github-copilot,opencode

# 3. 프로필 설정 (core 또는 expanded)
openspec config profile

# 4. 설정 적용
openspec update
```

---

## 🎮 라프라시아 프로젝트 도구 활용 가이드

### Qwen Code 활용
```toml
# .qwen/commands/opsx-propose.toml
[command]
name = "opsx:propose"
description = "새 기능 제안"

[prompt]
system = "당신은 라프라시아 세계관 마스터입니다."
user = "다음 기능을 제안합니다: {{feature}}"
```

**사용 예시:**
```
/opsx:propose "에릴의 프로 스카우트 이벤트 추가"
```

### GitHub Copilot 활용
```markdown
<!-- .github/prompts/opsx-apply.prompt.md -->
# OpenSpec 적용 명령

라프라시아 야구 시뮬레이션 RPG 프로젝트에 명세를 적용합니다.

## 현재 명세
{{spec_content}}

## 구현할 작업
{{tasks}}
```

### OpenCode 활용
```markdown
<!-- .opencode/commands/opsx-archive.md -->
# OpenSpec 아카이브 명령

완료된 변경 사항을 아카이브합니다.

## 아카이브 위치
openspec/changes/archive/{{date}}-{{feature_name}}/
```

---

## 📊 워크플로우 비교

### Core 프로필 (기본)
| 워크플로우 | 설명 |
|------------|------|
| `propose` | 명세 제안 |
| `explore` | 현황 분석 |
| `apply` | 명세 적용 |
| `archive` | 아카이브 |

### Expanded 프로필 (선택)
| 워크플로우 | 설명 |
|------------|------|
| `new` | 새 변경 시작 |
| `continue` | 진행 중 변경 계속 |
| `ff` | 빠른 포워딩 |
| `verify` | 명세 검증 |
| `sync` | 명세 동기화 |
| `bulk-archive` | 일괄 아카이브 |
| `onboard` | 새 기여자 온보딩 |

---

## 🔍 도구별 명령어 예시

### Qwen Code
```bash
# 명세 제안
/opsx:propose "새 NPC 추가 - 올리비아 (엘프 상인)"

# 명세 적용
/opsx:apply

# 아카이브
/opsx:archive
```

### GitHub Copilot
```bash
# VS Code 에서
Cmd+Shift+P → GitHub Copilot → OpenSpec: Propose

# 또는 .github/prompts/opsx-*.prompt.md 파일 사용
```

### Cursor
```bash
# Cursor IDE 에서
Cmd+K → /opsx:propose "배틀 시스템 추가"
```

---

## 📝 설정 파일 예시

### `.openspec/config.json`
```json
{
  "version": "1.0",
  "project": "라프라시아 야구 시뮬레이션 RPG",
  "profile": "core",
  "tools": ["qwen", "github-copilot", "opencode"],
  "created_at": "2026-04-10",
  "world_state": {
    "current_date": "780-03-17",
    "version": "1.0"
  }
}
```

### `.qwen/settings.json`
```json
{
  "model": "qwen3.5-plus",
  "temperature": 0.2,
  "max_tokens": 4096,
  "system_prompt": "당신은 라프라시아 세계관 마스터입니다."
}
```

---

## 🎯 추천 워크플로우

### 1. 새 기능 개발
```bash
# 1. 명세 제안
/opsx:propose "가챠 시스템 구현"

# 2. 명세 검토 (수동)
# openspec/changes/add-gacha-system/ 폴더 확인

# 3. 명세 적용
/opsx:apply

# 4. 검증
/opsx:verify

# 5. 아카이브
/opsx:archive
```

### 2. 에피소드 작성
```bash
# 1. 명세 제안
/opsx:propose "에피소드 4 작성 - 인턴십 첫 날"

# 2. 작성 (AI 자동)
# openspec/changes/write-episode-4/ 에서 진행

# 3. 적용
/opsx:apply

# 4. 아카이브
/opsx:archive
```

### 3. 월드스테이트 업데이트
```bash
# 1. 명세 제안
/opsx:propose "월드스테이트 v2.0 - 종족 관계 시스템"

# 2. 스키마 정의
# openspec/specs/world-state-v2.md

# 3. 적용
/opsx:apply

# 4. 검증 (GitHub Actions)
# 자동 실행
```

---

## 🐛 문제 해결

### 도구가 인식되지 않음
```bash
# 도구 재설정
openspec update --tools qwen,github-copilot,opencode
```

### 명령어가 작동하지 않음
```bash
# 스킬 재생성
openspec update
```

### 프로필 변경
```bash
# 프로필 설정
openspec config profile
# → core 또는 expanded 선택

# 적용
openspec update
```

---

## 📚 추가 리소스

| 문서 | 링크 |
|------|------|
| OpenSpec 메인 문서 | https://github.com/Fission-AI/OpenSpec |
| 지원 도구 목록 | https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md |
| 명령어 참조 | https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md |
| CLI 참조 | https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md |
| 워크플로우 | https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md |

---

> **팁**: 라프라시아 프로젝트는 **Qwen Code**를 주력으로 사용하고, **GitHub Copilot**과 **OpenCode**를 보조적으로 활용하는 것을 권장합니다.
