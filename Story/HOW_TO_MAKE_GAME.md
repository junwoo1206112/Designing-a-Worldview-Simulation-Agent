# 라프라시아 야구 시뮬레이션 RPG - 게임 제작 가이드

## 🎮 현재 상태

```
✅ 세계관 설정 완료 (novel/research/)
✅ 게임 엔진 작성 (game/engine.py)
✅ 장면 데이터 20 개 (game/scenes.json)
✅ OpenSpec 명세 시스템
✅ GitHub Actions 자동화
❌ 그래픽/사운드 에셋
❌ 실행 파일 (.exe)
❌ 모바일 버전
```

---

## 🚀 게임 제작 5 단계

```
1 단계: 텍스트 게임 (현재)     [██████████] 100%
2 단계: 게임 확장              [████░░░░░░] 40%
3 단계: 그래픽 추가            [░░░░░░░░░░] 0%
4 단계: 사운드/음악            [░░░░░░░░░░] 0%
5 단계: 배포 패키지            [░░░░░░░░░░] 0%
```

---

## 1 단계: 텍스트 게임 (현재) ✅

### 바로 플레이 가능!

```bash
# Windows
cd C:\Story\game
python engine.py

# 또는
start.bat
```

### 게임 화면 예시
```
══════════════════════════════════════
📅 780-03-17 08:00
🌤️  날씨: sunny
══════════════════════════════════════
❤️  체력: 100/100
😊 기분: 100/200
📚 야구 지식: 108
══════════════════════════════════════

████████████████████████████████████████
  새로운 아침
  📍 아카데미 기숙사
████████████████████████████████████████

아침 햇살이 기숙사 창문을 통해 들어옵니다...

[선택지]
  1. 아카데미 도서관으로 가서 에릴과 토비를 만난다
  2. 스피드스터즈 구장으로 가서 레이몬드 감독을 만난다
  3. 아카데미 훈련장에서 개인 훈련을 한다
  4. 퀵 홈 시티 중심가를 산책한다

선택하세요: _
```

### 현재 콘텐츠
- **장면**: 20 개
- **선택지**: 60 개 이상
- **엔딩**: 4 개
- **플레이 시간**: 2-3 시간

---

## 2 단계: 게임 확장 (진행 중)

### 2-1. 장면 추가

#### OpenSpec 으로 명세 작성
```bash
/opsx:propose "에피소드 5 추가 - 인턴십 첫 날"
```

#### 생성되는 명세
```
openspec/changes/add-episode-5/
├── proposal.md
├── design.md
└── tasks.md
```

#### scenes.json 에 추가
```json
"episode_5_internship_001": {
  "id": "episode_5_internship_001",
  "title": "인턴십 첫 날",
  "location": "스피드스터즈 구장",
  "description": "드디어 인턴십 첫 날입니다...",
  "choices": [
    {
      "id": "c1",
      "text": "레이몬드 감독에게 인사한다",
      "effect": {
        "affinity_changes": {"레이몬드": 10},
        "time_hours": 1
      },
      "next_scene": "internship_meeting_001"
    }
  ]
}
```

### 2-2. 시스템 확장

#### 새 시스템 추가 예시
```python
# game/systems/relationship.py
class RelationshipSystem:
    """관계 시스템"""
    
    def __init__(self):
        self.relationships = {}
    
    def update_affinity(self, npc: str, change: int):
        """호감도 업데이트"""
        if npc in self.relationships:
            self.relationships[npc] += change
        else:
            self.relationships[npc] = 50 + change
    
    def get_relationship_level(self, affinity: int) -> str:
        """호감도 레벨 반환"""
        if affinity >= 100:
            return "특별한 관계"
        elif affinity >= 80:
            return "친구"
        elif affinity >= 60:
            return "우호"
        else:
            return "보통"
```

### 2-3. 경기 시뮬레이션 추가

```python
# game/systems/baseball_game.py
class BaseballGameSimulator:
    """야구 경기 시뮬레이션"""
    
    def __init__(self, home_team: dict, away_team: dict):
        self.home_team = home_team
        self.away_team = away_team
        self.score = {"home": 0, "away": 0}
        self.inning = 1
    
    def play_inning(self):
        """한 이닝 진행"""
        # 타석 시뮬레이션
        # 투구 시뮬레이션
        # 득점 계산
        pass
    
    def play_game(self) -> dict:
        """경기 전체 진행"""
        for i in range(9):
            self.play_inning()
        
        return {
            "home_score": self.score["home"],
            "away_score": self.score["away"],
            "winner": "home" if self.score["home"] > self.score["away"] else "away"
        }
```

---

## 3 단계: 그래픽 추가

### 3-1. Ren'Py 엔진 사용 (추천)

#### Ren'Py란?
- **장르**: 비주얼 노벨/어드벤처 게임 엔진
- **특징**: Python 기반, 2D 그래픽 지원, 크로스플랫폼
- **웹사이트**: https://www.renpy.org/

#### 설치
```bash
# 1. Ren'Py SDK 다운로드
https://www.renpy.org/latest.html

# 2. 프로젝트 생성
renpy-launcher → Create New Project → "LafprasiaBaseball"
```

#### 프로젝트 구조
```
LafprasiaBaseball/
├── game/
│   ├── script.rpy          # 메인 시나리오
│   ├── screens.rpy         # UI 화면
│   ├── options.rpy         # 게임 설정
│   ├── images/             # 그래픽 에셋
│   │   ├── bg/             # 배경
│   │   ├── characters/     # 캐릭터
│   │   └── ui/             # UI 요소
│   └── audio/              # 사운드
└── renpy/                  # Ren'Py 엔진
```

#### script.rpy 예시
```renpy
# 캐릭터 정의
define k = Character("카일", color="#c8ffff")
define e = Character("에릴", color="#c8ffc8")

# 배경 정의
image bg academy_dorm = "images/bg/academy_dorm.jpg"
image bg library = "images/bg/library.jpg"

# 캐릭터 스프라이트
image eriel normal = "images/characters/eriel_normal.png"
image eriel smile = "images/characters/eriel_smile.png"

# 레이블 (장면)
label start:
    scene bg academy_dorm
    show eriel normal at center
    
    k "아침이다. 오늘은 무엇을 할까?"
    
    menu:
        "도서관으로 간다":
            jump library_scene
        "구장으로 간다":
            jump stadium_scene

label library_scene:
    scene bg library
    show eriel smile
    
    e "왔어, 카일! 오늘 어떤 연구를 할까?"
    
    return
```

#### Python 연동
```renpy
# game/script.rpy
init python:
    # 라프라시아 게임 엔진 임포트
    import sys
    sys.path.append('../game')
    from engine import GameState
    
    game_state = GameState()

# 게임 내 사용
label check_status:
    python:
        stamina = game_state.world_state['player']['condition']['stamina']
    
    "현재 체력: [stamina]"
    
    return
```

### 3-2. Unity 엔진 사용 (고급)

#### Unity란?
- **장르**: 종합 게임 엔진
- **특징**: 3D/2D 모두 지원, 강력한 기능, 학습 곡선 높음
- **웹사이트**: https://unity.com/

#### 필요한 에셋
| 에셋 | 용도 | 가격 |
|------|------|------|
| TextMeshPro | 텍스트 표시 | 무료 |
| Dialogue System | 대화 시스템 | $75 |
| PlayMaker | 비주얼 스크립팅 | $65 |

#### 기본 구조
```
Assets/
├── Scripts/
│   ├── GameManager.cs
│   ├── StoryManager.cs
│   └── UI/
├── Scenes/
│   ├── MainMenu.unity
│   ├── GameScene.unity
│   └── Ending.unity
├── Prefabs/
│   ├── Character/
│   └── UI/
└── Resources/
    ├── Data/ (JSON)
    └── Audio/
```

### 3-3. 웹 브라우저 게임 (간단)

#### HTML + JavaScript
```html
<!DOCTYPE html>
<html>
<head>
    <title>라프라시아 야구 RPG</title>
    <style>
        .game-container {
            width: 800px;
            margin: 0 auto;
            font-family: 'Malgun Gothic', sans-serif;
        }
        .status-bar {
            background: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
        }
        .choice-button {
            display: block;
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <div class="status-bar">
            <span>📅 780-03-17</span>
            <span>❤️ 체력: 100</span>
            <span>📚 지식: 108</span>
        </div>
        
        <div id="story-text">
            아침 햇살이 기숙사 창문을 통해 들어옵니다...
        </div>
        
        <div id="choices">
            <button class="choice-button" onclick="choose(1)">
                도서관으로 간다
            </button>
            <button class="choice-button" onclick="choose(2)">
                구장으로 간다
            </button>
        </div>
    </div>
    
    <script>
        // JSON 데이터 로드
        fetch('scenes.json')
            .then(response => response.json())
            .then(data => loadScene(data['intro_001']));
        
        function loadScene(scene) {
            document.getElementById('story-text').innerText = scene.description;
            // 선택지 생성...
        }
        
        function choose(choiceNum) {
            // 선택 처리...
        }
    </script>
</body>
</html>
```

---

## 4 단계: 사운드/음악 추가

### 4-1. 무료 음원 사이트

| 사이트 | 라이선스 | 링크 |
|--------|----------|------|
| **유튜브 오디오 라이브러리** | 무료 | https://www.youtube.com/audiolibrary |
| **Freesound** | CC0/CC-BY | https://freesound.org/ |
| **Otowa no Souko** | 무료 | https://otowanosouko.com/ |
| **H/MIX GALLERY** | 무료 | http://www.hmix.net/ |

### 4-2. BGM 카테고리

```
audio/
├── bgm/
│   ├── title_theme.mp3      # 타이틀 화면
│   ├── field_day.mp3        # 필드 (낮)
│   ├── field_night.mp3      # 필드 (밤)
│   ├── battle.mp3           # 경기 중
│   ├── sad.mp3              # 슬픈 장면
│   └── happy.mp3            # 즐거운 장면
├── sfx/
│   ├── click.mp3            # 클릭음
│   ├── decision.mp3         # 결정음
│   ├── levelup.mp3          # 레벨업
│   └── notification.mp3     # 알림
└── voice/ (선택사항)
    ├── kyle_greeting.mp3
    └── eriel_greeting.mp3
```

### 4-3. Ren'Py 에 사운드 추가

```renpy
# options.rpy
define config.sound = True

# script.rpy
# BGM 설정
define config.default_music = "audio/bgm/title_theme.mp3"

# 장면별 BGM
label start:
    scene bg academy_dorm
    play music "audio/bgm/field_day.mp3" fadein 2.0
    
    k "아침이다."
    
    # 효과음
    play sound "audio/sfx/click.mp3"
    
    menu:
        "도서관으로 간다":
            play sound "audio/sfx/decision.mp3"
            jump library_scene
```

---

## 5 단계: 배포 패키지

### 5-1. Ren'Py 배포

#### 빌드 방법
```
1. Ren'Py 런처 실행
2. 프로젝트 선택 → "Build Distributions"
3. 플랫폼 선택:
   ☑ Windows
   ☑ Mac
   ☑ Linux
   ☑ Android (선택)
4. "Build" 클릭
```

#### 생성되는 파일
```
dist/
├── LafprasiaBaseball-1.0-pc/
│   ├── LafprasiaBaseball.exe    # Windows 실행 파일
│   ├── game/
│   └── renpy/
├── LafprasiaBaseball-1.0-mac/
│   └── LafprasiaBaseball.app    # Mac 앱
└── LafprasiaBaseball-1.0-linux/
    └── LafprasiaBaseball.sh     # Linux 실행 파일
```

### 5-2. Steam 배포

#### 필요한 것
1. **Steam Direct fee**: $100 (게임당)
2. **앱 ID**: Steam 에서 발급
3. **상점 페이지**: 캡처이미지, 설명, 트레일러
4. **빌드**: Windows/Mac/Linux

#### 제출 체크리스트
- [ ] 게임 완성
- [ ] 캡처이미지 (최소 5 장)
- [ ] 트레일러 영상 (선택)
- [ ] 상점 설명
- [ ] 연령 등급
- [ ] $100 결제

### 5-3. itch.io 배포 (무료)

#### 업로드 방법
```
1. https://itch.io/ 회원가입
2. "Create New Project" 클릭
3. 프로젝트 정보 입력:
   - 제목: 라프라시아 야구 RPG
   - 장르: 시뮬레이션/RPG
   - 가격: 무료/유료 (선택)
4. 게임 파일 업로드 (.zip)
5. 페이지 꾸미기
6. Publish!
```

### 5-4. 모바일 배포

#### Android (APK)
```bash
# Ren'Py 에서
Build Distributions → Android

# 생성된 APK:
dist/LafprasiaBaseball-1.0-android.apk
```

#### iOS (App Store)
```
필요한 것:
- Mac 컴퓨터
- Xcode
- Apple Developer 계정 ($99/년)
- IPA 파일
```

---

## 📋 추천 개발 로드맵

### 초보자용 (Ren'Py)
```
1 주: Ren'Py 기초 학습
2 주: 텍스트 게임 이식
3 주: 그래픽 에셋 준비
4 주: 사운드 추가
5 주: 테스트 및 디버깅
6 주: 배포 패키지 빌드
7 주: itch.io 업로드
```

### 중급자용 (Unity)
```
1 개월: Unity 기초 학습
2 개월: 게임 시스템 구현
3 개월: 그래픽/애니메이션
4 개월: 사운드/UI
5 개월: 최적화
6 개월: 배포
```

### 웹용 (HTML/JS)
```
1 주: HTML/CSS 기초
2 주: JavaScript 게임 로직
3 주: JSON 데이터 연동
4 주: 반응형 UI
5 주: 배포 (GitHub Pages)
```

---

## 🎯 지금 바로 할 수 있는 일

### 1. 텍스트 게임 테스트
```bash
cd C:\Story\game
python engine.py
```

### 2. 장면 추가
```bash
/opsx:propose "새 에피소드 추가"
```

### 3. Ren'Py 시작
```
1. https://www.renpy.org/latest.html 다운로드
2. Ren'Py 런처 실행
3. Create New Project → "LafprasiaBaseball"
4. game/script.rpy 편집 시작
```

### 4. 그래픽 에셋 찾기
- **배경**: https://opengameart.org/
- **캐릭터**: https://itch.io/game-assets
- **아이콘**: https://www.flaticon.com/

---

## 📊 개발 도구 비교

| 도구 | 난이도 | 비용 | 플랫폼 | 추천 |
|------|--------|------|--------|------|
| **텍스트 (현재)** | ⭐ | 무료 | PC | ✅ 시작용 |
| **Ren'Py** | ⭐⭐ | 무료 | PC/Mac/Linux/Android | ✅ 입문용 |
| **Unity** | ⭐⭐⭐⭐ | 무료 (수익 $100k 까지) | 모든 플랫폼 | 고급 |
| **HTML/JS** | ⭐⭐ | 무료 | 웹 브라우저 | 웹용 |
| **Unreal** | ⭐⭐⭐⭐⭐ | 로열티 5% | 모든 플랫폼 | 3D 전용 |

---

## 💡 추천

### 지금 당장:
1. **텍스트 게임 완성** (장면 50 개 목표)
2. **OpenSpec 으로 명세 관리**
3. **GitHub 에 공개**

### 다음 단계:
1. **Ren'Py 학습** (2 주)
2. **텍스트 게임 이식** (2 주)
3. **그래픽 추가** (4 주)
4. **itch.io 배포** (1 주)

### 최종 목표:
1. **Steam 출시** (6 개월)
2. **모바일 이식** (추가 3 개월)

---

> **시작은 텍스트로, 확장은 Ren'Py 로!**
> 
> 현재 텍스트 게임 엔진이 이미 완성되어 있습니다.
> 이제 장면을 추가하고 스토리를 확장하세요.
> 그래픽은 나중에 추가해도 됩니다!

**첫 번째 단계: `python game/engine.py` 실행해보기!** 🎮⚾🪄
