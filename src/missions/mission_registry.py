from typing import List, Dict

class Mission:
    def __init__(self, title: str, description: str, module_name: str):
        self.title = title
        self.description = description
        self.module_name = module_name

class MissionRegistry:
    def __init__(self):
        self.missions: List[Mission] = []

    def register_mission(self, title: str, description: str, module_name: str):
        mission = Mission(title, description, module_name)
        self.missions.append(mission)

    def get_missions(self) -> List[Dict[str, str]]:
        return [{"title": mission.title, "description": mission.description, "module_name": mission.module_name} for mission in self.missions]

# Initialize the mission registry and register the first mission
mission_registry = MissionRegistry()
mission_registry.register_mission(
    title="Hello World",
    description="Create a simple program that prints 'Hello, World!' to the console.",
    module_name="mission_01_hello_world"
)