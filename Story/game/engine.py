"""
라프라시아 야구 시뮬레이션 RPG 엔진
"Diamond & Magic"

Author: World Simulator Agent
Version: 0.2.0
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum


class ChoiceEffect:
    """선택지의 효과"""
    def __init__(self, 
                 affinity_changes: Optional[Dict[str, int]] = None,
                 stat_changes: Optional[Dict[str, int]] = None,
                 time_hours: int = 1,
                 stamina_cost: int = 5,
                 mood_change: int = 0,
                 items_added: Optional[List[str]] = None,
                 items_removed: Optional[List[str]] = None,
                 events_completed: Optional[List[str]] = None,
                 events_added: Optional[List[str]] = None,
                 next_scene: Optional[str] = None):
        self.next_scene = next_scene
        self.affinity_changes = affinity_changes or {}
        self.stat_changes = stat_changes or {}
        self.time_hours = time_hours
        self.stamina_cost = stamina_cost
        self.mood_change = mood_change
        self.items_added = items_added or []
        self.items_removed = items_removed or []
        self.events_completed = events_completed or []
        self.events_added = events_added or []


class Choice:
    """플레이어 선택지"""
    def __init__(self, 
                 id: str, 
                 text: str, 
                 effect: ChoiceEffect,
                 required_condition: Optional[str] = None):
        self.id = id
        self.text = text
        self.effect = effect
        self.required_condition = required_condition


class Scene:
    """게임 장면"""
    def __init__(self,
                 id: str,
                 title: str,
                 description: str,
                 choices: List[Choice],
                 location: Optional[str] = None,
                 time_of_day: Optional[str] = None):
        self.id = id
        self.title = title
        self.description = description
        self.choices = choices
        self.location = location
        self.time_of_day = time_of_day


class GameState:
    """게임 상태 관리"""
    def __init__(self, world_state_path: str = "../novel/world_state.json"):
        self.world_state_path = world_state_path
        self.world_state = self.load_world_state()
        self.current_scene_id = "intro_001"
        self.play_log = []
        self.game_flags: Dict[str, bool] = {}
        
    def load_world_state(self) -> Dict:
        """월드 상태 로드"""
        try:
            with open(self.world_state_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"경고: {self.world_state_path} 파일을 찾을 수 없습니다.")
            return self.create_default_state()
    
    def create_default_state(self) -> Dict:
        """기본 상태 생성"""
        return {
            "world_info": {
                "current_date": "780-03-17",
                "current_time": "08:00",
                "weather": "sunny"
            },
            "player": {
                "name": "카일 윈저",
                "stats": {"str": 5, "dex": 6, "int": 15, "cha": 8, "baseball_knowledge": 108},
                "condition": {"stamina": 100, "mood": 100},
                "relationships": {
                    "에릴": {"type": "friend", "affinity": 100},
                    "토비": {"type": "friend", "affinity": 72},
                    "레이몬드": {"type": "professional", "affinity": 25}
                },
                "inventory": ["야구 전략 노트", "아카데미 입학증", "가족 사진"]
            },
            "events": {
                "completed_events": [],
                "active_events": [],
                "upcoming_events": [
                    {"id": "ev_006", "name": "인턴십 시작", "date": "780-04-01"},
                    {"id": "ev_007", "name": "아마추어 리그 개막", "date": "780-04-15"}
                ]
            }
        }
    
    def save_world_state(self):
        """월드 상태 저장"""
        os.makedirs(os.path.dirname(self.world_state_path), exist_ok=True)
        with open(self.world_state_path, 'w', encoding='utf-8') as f:
            json.dump(self.world_state, f, ensure_ascii=False, indent=2)
    
    def save_game(self, slot: int = 1):
        """게임 세이브"""
        save_data = {
            "world_state": self.world_state,
            "current_scene_id": self.current_scene_id,
            "play_log": self.play_log,
            "game_flags": self.game_flags,
            "timestamp": datetime.now().isoformat()
        }
        
        save_dir = "saves"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, f"save_{slot:03d}.json")
        
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
        
        return save_path
    
    def load_game(self, slot: int = 1) -> bool:
        """게임 로드"""
        save_path = os.path.join("saves", f"save_{slot:03d}.json")
        
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            
            self.world_state = save_data["world_state"]
            self.current_scene_id = save_data["current_scene_id"]
            self.play_log = save_data.get("play_log", [])
            self.game_flags = save_data.get("game_flags", {})
            
            return True
        except FileNotFoundError:
            return False
    
    def apply_effect(self, effect: ChoiceEffect):
        """선택지 효과 적용"""
        player = self.world_state["player"]
        
        # 호감도 변경
        for npc, change in effect.affinity_changes.items():
            if npc in player["relationships"]:
                player["relationships"][npc]["affinity"] += change
            else:
                player["relationships"][npc] = {"affinity": 50 + change, "type": "acquaintance"}
        
        # 스탯 변경
        for stat, change in effect.stat_changes.items():
            if stat in player["stats"]:
                player["stats"][stat] += change
        
        # 시간 경과
        self.advance_time(effect.time_hours)
        
        # 체력 변경
        player["condition"]["stamina"] = max(0, min(100, 
            player["condition"]["stamina"] - effect.stamina_cost))
        
        # 기분 변경
        player["condition"]["mood"] = max(0, min(200,
            player["condition"]["mood"] + effect.mood_change))
        
        # 아이템 추가/제거
        for item in effect.items_added:
            if item not in player["inventory"]:
                player["inventory"].append(item)
        for item in effect.items_removed:
            if item in player["inventory"]:
                player["inventory"].remove(item)
        
        # 이벤트 처리
        self._process_events(effect)
    
    def advance_time(self, hours: int):
        """시간 경과"""
        current_time = self.world_state["world_info"]["current_time"]
        current_date = self.world_state["world_info"]["current_date"]
        
        hour, minute = map(int, current_time.split(':'))
        hour += hours
        
        # 날짜 넘어감 처리
        days_passed = hour // 24
        hour = hour % 24
        
        if days_passed > 0:
            year, month, day = map(int, current_date.split('-'))
            day += days_passed
            if day > 30:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            self.world_state["world_info"]["current_date"] = f"{year}-{month:02d}-{day:02d}"
        
        self.world_state["world_info"]["current_time"] = f"{hour:02d}:{minute:02d}"
    
    def _process_events(self, effect: ChoiceEffect):
        """이벤트 처리"""
        events = self.world_state["events"]
        
        for event_id in effect.events_completed:
            for event in events["active_events"]:
                if event["id"] == event_id:
                    events["completed_events"].append(event)
                    events["active_events"].remove(event)
                    break
    
    def log_action(self, scene_id: str, choice_id: str, result: str):
        """행동 로그 기록"""
        self.play_log.append({
            "timestamp": f"{self.world_state['world_info']['current_date']} {self.world_state['world_info']['current_time']}",
            "scene": scene_id,
            "choice": choice_id,
            "result": result
        })
    
    def get_relationship_text(self, affinity: int) -> str:
        """호감도 텍스트 반환"""
        if affinity >= 100:
            return "특별한 관계"
        elif affinity >= 80:
            return "친구"
        elif affinity >= 60:
            return "우호"
        elif affinity >= 40:
            return "보통"
        elif affinity >= 20:
            return "낯섦"
        else:
            return "적대"


class GameEngine:
    """게임 엔진"""
    def __init__(self):
        self.state = GameState()
        self.scenes: Dict[str, Scene] = {}
        self.load_scenes()
    
    def load_scenes(self):
        """장면 데이터 로드 (JSON + 하드코딩)"""
        # JSON 에서 장면 로드 시도
        json_path = os.path.join(os.path.dirname(__file__), "scenes.json")
        
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                for scene_data in data.get("scenes", {}).values():
                    choices = []
                    for choice_data in scene_data.get("choices", []):
                        effect = ChoiceEffect(
                            affinity_changes=choice_data.get("effect", {}).get("affinity_changes"),
                            stat_changes=choice_data.get("effect", {}).get("stat_changes"),
                            time_hours=choice_data.get("effect", {}).get("time_hours", 1),
                            stamina_cost=choice_data.get("effect", {}).get("stamina_cost", 5),
                            mood_change=choice_data.get("effect", {}).get("mood_change", 0),
                            items_added=choice_data.get("effect", {}).get("items_added"),
                            next_scene=choice_data.get("effect", {}).get("next_scene")
                        )
                        choices.append(Choice(
                            id=choice_data["id"],
                            text=choice_data["text"],
                            effect=effect
                        ))
                    
                    self.scenes[scene_data["id"]] = Scene(
                        id=scene_data["id"],
                        title=scene_data["title"],
                        description=scene_data["description"],
                        choices=choices,
                        location=scene_data.get("location"),
                        time_of_day=scene_data.get("time_of_day")
                    )
                print(f"✓ {len(self.scenes)}개의 장면을 로드했습니다.")
            except Exception as e:
                print(f"⚠ JSON 장면 로드 실패: {e}")
                self._load_hardcoded_scenes()
        else:
            print("⚠ scenes.json 을 찾을 수 없습니다. 하드코딩 장면을 사용합니다.")
            self._load_hardcoded_scenes()
    
    def _load_hardcoded_scenes(self):
        """하드코딩 장면 로드 (폴백)"""
        self.scenes = {
            "intro_001": Scene(
                id="intro_001",
                title="새로운 아침",
                description=self._get_intro_description(),
                choices=[
                    Choice(id="c1", text="아카데미 도서관으로 가서 에릴과 토비를 만난다",
                          effect=ChoiceEffect(affinity_changes={"에릴": 5, "토비": 5}, time_hours=1, stamina_cost=5, mood_change=10, next_scene="library_meeting_001")),
                    Choice(id="c2", text="스피드스터즈 구장으로 가서 레이몬드 감독을 만난다",
                          effect=ChoiceEffect(affinity_changes={"레이몬드": 10}, time_hours=2, stamina_cost=10, mood_change=5, next_scene="speedsters_visit_001")),
                    Choice(id="c3", text="아카데미 훈련장에서 개인 훈련을 한다",
                          effect=ChoiceEffect(stat_changes={"baseball_knowledge": 2}, time_hours=3, stamina_cost=20, mood_change=-5, next_scene="training_001")),
                    Choice(id="c4", text="퀵 홈 시티 중심가를 산책한다",
                          effect=ChoiceEffect(time_hours=2, stamina_cost=10, mood_change=15, next_scene="city_walk_001"))
                ],
                location="아카데미 기숙사",
                time_of_day="morning"
            )
        }
    
    def _get_intro_description(self) -> str:
        """도입부 설명"""
        ws = self.state.world_state
        date = ws["world_info"]["current_date"]
        time = ws["world_info"]["current_time"]
        weather = ws["world_info"]["weather"]
        
        return f"""
┌─────────────────────────────────────────────────────────┐
│  라프라시아 780 년 {date} {time} | {weather.upper()}        
└─────────────────────────────────────────────────────────┘

아침 햇살이 기숙사 창문을 통해 들어옵니다.
어제는 라프라시아 야구 연구회 제 1 회 미팅이 있었습니다.

오늘은 무엇을 할까요?
"""
    
    def get_current_scene(self) -> Optional[Scene]:
        """현재 장면 반환"""
        return self.scenes.get(self.state.current_scene_id)
    
    def make_choice(self, choice_id: str) -> str:
        """선택 처리"""
        scene = self.get_current_scene()
        if not scene:
            return "오류: 현재 장면을 찾을 수 없습니다."
        
        choice = None
        for c in scene.choices:
            if c.id == choice_id:
                choice = c
                break
        
        if not choice:
            return f"오류: 선택지 {choice_id} 를 찾을 수 없습니다."
        
        # 효과 적용
        self.state.apply_effect(choice.effect)
        
        # 로그 기록
        self.state.log_action(scene.id, choice.id, choice.text)
        
        # 다음 장면으로 이동
        if choice.effect.next_scene:
            self.state.current_scene_id = choice.effect.next_scene
        
        # 결과 메시지
        result = self._generate_result_message(choice)
        
        # 상태 저장
        self.state.save_world_state()
        
        return result
    
    def _generate_result_message(self, choice: Choice) -> str:
        """결과 메시지 생성"""
        effect = choice.effect
        messages = []
        
        if effect.affinity_changes:
            for npc, change in effect.affinity_changes.items():
                sign = "+" if change > 0 else ""
                messages.append(f"{npc} 호감도 {sign}{change}")
        
        if effect.stat_changes:
            for stat, change in effect.stat_changes.items():
                sign = "+" if change > 0 else ""
                messages.append(f"{stat} {sign}{change}")
        
        if effect.mood_change != 0:
            sign = "+" if effect.mood_change > 0 else ""
            messages.append(f"기분 {sign}{effect.mood_change}")
        
        if effect.items_added:
            messages.append(f"아이템 획득: {', '.join(effect.items_added)}")
        
        return "결과: " + ", ".join(messages) if messages else "행동이 완료되었습니다."
    
    def display_status(self):
        """상태 표시"""
        ws = self.state.world_state
        print("\n" + "═"*50)
        print(f"📅 {ws['world_info']['current_date']} {ws['world_info']['current_time']}")
        print(f"🌤️  날씨: {ws['world_info']['weather']}")
        print("═"*50)
        print(f"❤️  체력: {ws['player']['condition']['stamina']}/100")
        print(f"😊 기분: {ws['player']['condition']['mood']}/200")
        print(f"📚 야구 지식: {ws['player']['stats']['baseball_knowledge']}")
        print("═"*50)
        print("👥 관계:")
        for npc, data in ws['player']['relationships'].items():
            affinity = data.get('affinity', 0)
            rel_text = self.state.get_relationship_text(affinity)
            print(f"   {npc}: {affinity} ({rel_text})")
        print("═"*50)
    
    def display_scene(self, scene: Scene):
        """장면 표시"""
        print("\n" + "█"*60)
        print(f"  {scene.title}")
        if scene.location:
            print(f"  📍 {scene.location}")
        print("█"*60)
        print(scene.description)
        print("\n[선택지]")
        for i, choice in enumerate(scene.choices, 1):
            print(f"  {i}. {choice.text}")
        print()
    
    def show_help(self):
        """도움말 표시"""
        print("""
╔════════════════════════════════════════════════════════╗
║                    📖 도움말                           ║
╠════════════════════════════════════════════════════════╣
║  1-9       선택지 선택                                 ║
║  s         상태 상세 확인                              ║
║  i         인벤토리 확인                               ║
║  save      게임 저장                                   ║
║  load      게임 로드                                   ║
║  q         게임 저장 및 종료                           ║
║  h         도움말                                      ║
╚════════════════════════════════════════════════════════╝
""")
    
    def show_inventory(self):
        """인벤토리 표시"""
        inv = self.state.world_state["player"]["inventory"]
        print("\n🎒 인벤토리:")
        if inv:
            for item in inv:
                print(f"   • {item}")
        else:
            print("   빈 가방")
        print()
    
    def run(self):
        """게임 실행"""
        print("\n" + "█"*60)
        print("  라프라시아 야구 시뮬레이션 RPG")
        print("  'Diamond & Magic'")
        print("█"*60)
        print("\n게임을 시작합니다...\n")
        print("도움말은 'h' 를 입력하세요.\n")
        
        while True:
            scene = self.get_current_scene()
            if not scene:
                print("오류: 장면을 찾을 수 없습니다.")
                break
            
            self.display_status()
            self.display_scene(scene)
            
            # 사용자 입력
            try:
                user_input = input("선택하세요: ").strip().lower()
                
                if user_input == 'q':
                    self.state.save_game(1)
                    print("게임을 저장하고 종료합니다.")
                    break
                elif user_input == 'h':
                    self.show_help()
                    continue
                elif user_input == 's':
                    self.display_status()
                    input("계속하려면 엔터를 누르세요...")
                    continue
                elif user_input == 'i':
                    self.show_inventory()
                    input("계속하려면 엔터를 누르세요...")
                    continue
                elif user_input == 'save':
                    slot = input("세이브 슬롯 (1-3): ").strip()
                    if slot.isdigit():
                        path = self.state.save_game(int(slot))
                        print(f"게임을 저장했습니다: {path}")
                    continue
                elif user_input == 'load':
                    slot = input("로드할 슬롯 (1-3): ").strip()
                    if slot.isdigit():
                        if self.state.load_game(int(slot)):
                            print("게임을 로드했습니다.")
                        else:
                            print("세이브 파일을 찾을 수 없습니다.")
                    continue
                
                choice_num = int(user_input)
                if 1 <= choice_num <= len(scene.choices):
                    choice = scene.choices[choice_num - 1]
                    result = self.make_choice(choice.id)
                    print("\n" + result)
                    input("계속하려면 엔터를 누르세요...")
                else:
                    print("잘못된 선택입니다.")
            except ValueError:
                print("숫자 또는 명령어를 입력해주세요.")
            except KeyboardInterrupt:
                print("\n게임을 저장하고 종료합니다.")
                self.state.save_game(1)
                break


if __name__ == "__main__":
    engine = GameEngine()
    engine.run()
