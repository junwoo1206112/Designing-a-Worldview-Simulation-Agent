# OpenSpec 전체 도구 설정 완료

## ✅ 생성된 설정 파일

### 1. OpenCode (`.opencode/`)
```
.opencode/
└── skills/
    └── openspec-core/
        └── SKILL.md              ✅ OpenCode 코어 스킬
└── commands/
    ├── opsx-propose.md           ✅ 명세 제안
    ├── opsx-apply.md             ✅ 명세 적용
    └── opsx-archive.md           ✅ 아카이브
```

### 2. GitHub Copilot (`.github/`)
```
.github/
├── skills/
│   └── openspec-core/
│       └── SKILL.md              ✅ Copilot 코어 스킬
└── prompts/
    ├── opsx-propose.prompt.md    ✅ 제안 프롬프트
    ├── opsx-apply.prompt.md      ✅ 적용 프롬프트
    └── opsx-archive.prompt.md    ✅ 아카이브 프롬프트
```

### 3. Qwen Code (`.qwen/`)
```
.qwen/
├── skills/
│   └── openspec-core/
│       └── SKILL.md              ✅ Qwen 코어 스킬
└── commands/
    ├── opsx-propose.toml         ✅ 제안 명령 (TOML)
    ├── opsx-apply.toml           ✅ 적용 명령 (TOML)
    └── opsx-archive.toml         ✅ 아카이브 명령 (TOML)
```

### 4. Cursor (`.cursor/`)
```
.cursor/
├── skills/
│   └── openspec-core/
│       └── SKILL.md              ✅ Cursor 코어 스킬
└── commands/
    └── opsx-propose.md           ✅ 제안 명령
```

### 5. Claude Code (`.claude/`)
```
.claude/
├── skills/
│   └── openspec-core/
│       └── SKILL.md              ✅ Claude 코어 스킬
└── commands/
    └── opsx/
        └── propose.md            ✅ 제안 명령
```

---

## 📊 지원 도구 목록 (OpenSpec 공식 27 개 중 5 개 설정 완료)

| 도구 | 설정 완료 | 파일 위치 |
|------|----------|-----------|
| **OpenCode** | ✅ | `.opencode/skills/`, `.opencode/commands/` |
| **GitHub Copilot** | ✅ | `.github/skills/`, `.github/prompts/` |
| **Qwen Code** | ✅ | `.qwen/skills/`, `.qwen/commands/` |
| **Cursor** | ✅ | `.cursor/skills/`, `.cursor/commands/` |
| **Claude Code** | ✅ | `.claude/skills/`, `.claude/commands/` |
| Amazon Q | 📋 | `.amazonq/` (필요시 생성) |
| Cline | 📋 | `.cline/` (필요시 생성) |
| Continue | 📋 | `.continue/` (필요시 생성) |
| Windsurf | 📋 | `.windsurf/` (필요시 생성) |
| 기타 17 개 | 📋 | 필요시 생성 가능 |

---

## 🚀 도구별 사용법

### OpenCode
```bash
# 터미널에서
/opsx:propose 배틀 시스템 추가
/opsx:apply
/opsx:archive
```

### GitHub Copilot (VS Code)
```
# 명령 팔레트
Cmd+Shift+P → GitHub Copilot → OpenSpec: Propose

# 또는 채팅에서
@workspace /opsx:propose 새 기능
```

### Qwen Code
```bash
# 터미널에서
/opsx:propose 에피소드 4 작성
/opsx:apply
/opsx:archive
```

### Cursor
```
# 채팅에서
Cmd+L → /opsx:propose 배틀 시스템

# 편집기에서
선택 → Cmd+K → "OpenSpec 명세로 변환"
```

### Claude Code
```bash
# 터미널에서
claude "/opsx:propose 새 NPC 추가"

# 또는 대화에서
/opsx:propose 새 NPC 추가
```

---

## 📁 전체 프로젝트 구조

```
C:\Story/
├── .github/
│   ├── skills/openspec-core/SKILL.md
│   ├── prompts/opsx-*.prompt.md
│   └── workflows/
│       ├── openspec-validate.yml
│       ├── game-test.yml
│       └── content-index.yml
├── .qwen/
│   ├── skills/openspec-core/SKILL.md
│   └── commands/opsx-*.toml
├── .opencode/
│   ├── skills/openspec-core/SKILL.md
│   └── commands/opsx-*.md
├── .cursor/
│   ├── skills/openspec-core/SKILL.md
│   └── commands/opsx-*.md
├── .claude/
│   ├── skills/openspec-core/SKILL.md
│   └── commands/opsx/propose.md
├── openspec/
│   ├── changes/
│   │   ├── active/
│   │   └── archive/
│   ├── specs/
│   └── proposals/
├── game/
│   ├── engine.py
│   ├── scenes.json
│   └── README.md
├── novel/
│   ├── world_state.json
│   ├── chapters/
│   └── research/
├── scripts/
│   ├── validate_openspec.py
│   └── init_openspec.bat
├── README.md
├── OPENSPEC_GUIDE.md
├── OPENSPEC_TOOLS.md
├── OPENSPEC_SETUP_SUMMARY.md
└── OPENSPEC_ALL_TOOLS_SETUP.md  # 이 파일
```

---

## 🎯 초기화 명령어

### 전체 초기화
```bash
# 1. OpenSpec 설치
npm install -g @fission-ai/openspec@latest

# 2. 프로젝트 초기화 (5 개 도구)
openspec init --tools opencode,github-copilot,qwen,cursor,claude

# 3. 프로필 설정
openspec config profile  # core 또는 expanded 선택

# 4. 설정 적용
openspec update
```

### Windows 배치 스크립트
```batch
scripts\init_openspec.bat
```

---

## 📝 워크플로우 예시

### 1. 새 기능 개발
```bash
# 1. 명세 제안 (어떤 도구에서든)
/opsx:propose 배틀 시스템 추가

# 2. 명세 확인
# openspec/changes/add-battle-system/ 폴더 확인

# 3. 명세 적용
/opsx:apply

# 4. 검증
/opsx:verify

# 5. 아카이브
/opsx:archive
```

### 2. GitHub Actions 연동
```bash
# Git 커밋
git add .
git commit -m "Add OpenSpec integration for 5 tools"
git push origin main

# GitHub Actions 에서 자동 검증 실행
# .github/workflows/openspec-validate.yml
```

---

## 🔍 검색 및 인덱싱

### GitHub Code Search
```
# OpenCode 명령어 검색
path:.opencode/commands "opsx"

# GitHub Copilot 프롬프트 검색
path:.github/prompts "opsx"

# Qwen 명령어 검색
path:.qwen/commands "opsx"

# Cursor 명령어 검색
path:.cursor/commands "opsx"

# Claude 명령어 검색
path:.claude/commands "opsx"
```

### 로컬 검색
```bash
# 검증 스크립트 실행
python scripts/validate_openspec.py

# 보고서 확인
cat .github/openspec-reports/validation-report.json
```

---

## 🐛 문제 해결

### 도구가 인식되지 않음
```bash
# 도구 재설정
openspec update --tools opencode,github-copilot,qwen,cursor,claude
```

### 명령어가 작동하지 않음
```bash
# 스킬 재생성
openspec update
```

### 폴더가 없음
```bash
# 수동 생성
mkdir -p .opencode/skills/openspec-core
mkdir -p .github/skills/openspec-core
mkdir -p .qwen/skills/openspec-core
mkdir -p .cursor/skills/openspec-core
mkdir -p .claude/skills/openspec-core
```

---

## 📚 참조 문서

| 문서 | 설명 |
|------|------|
| [OpenSpec 공식](https://github.com/Fission-AI/OpenSpec) | 메인 저장소 |
| [지원 도구](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md) | 27 개 도구 목록 |
| [명령어 참조](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md) | Slash commands |
| [CLI 참조](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md) | 터미널 명령어 |
| `OPENSPEC_GUIDE.md` | 라프라시아 통합 가이드 |
| `OPENSPEC_TOOLS.md` | 도구별 설정 가이드 |
| `OPENSPEC_ALL_TOOLS_SETUP.md` | 이 파일 |

---

## ✨ 완료!

**5 개 AI 도구에 대한 OpenSpec 설정이 완료되었습니다!**

이제 다음 도구에서 명세 기반 개발을 사용할 수 있습니다:
- ✅ OpenCode
- ✅ GitHub Copilot
- ✅ Qwen Code
- ✅ Cursor
- ✅ Claude Code

**나머지 22 개 도구도 필요시 언제든지 추가 가능!**

```bash
# 추가 도구 설치
openspec init --tools amazon-q,cline,continue,windsurf
openspec update
```

---

> **OpenSpec 철학**:
> - fluid not rigid
> - iterative not waterfall
> - easy not complex
> - built for brownfield not just greenfield
> - scalable from personal projects to enterprises

**명세 기반 개발로 라프라시아 프로젝트를 조직적으로 관리하세요!** 🚀⚾🪄
