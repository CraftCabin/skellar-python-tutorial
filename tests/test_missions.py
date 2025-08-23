import unittest
from src.missions.mission_registry import MissionRegistry

class TestMissions(unittest.TestCase):

    def setUp(self):
        self.registry = MissionRegistry()

    def test_mission_registration(self):
        # Assuming mission_01_hello_world is registered
        self.registry.register_mission('mission_01_hello_world')
        self.assertIn('mission_01_hello_world', self.registry.get_registered_missions())

    def test_mission_execution(self):
        # Assuming mission_01_hello_world can be executed
        mission = self.registry.get_mission('mission_01_hello_world')
        result = mission.execute()
        self.assertTrue(result['success'])

if __name__ == '__main__':
    unittest.main()