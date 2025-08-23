class Mission:
    def __init__(self, title, description, mission_id):
        self.title = title
        self.description = description
        self.mission_id = mission_id
        self.status = 'inactive'  # Possible values: 'inactive', 'active', 'completed'

    def activate(self):
        self.status = 'active'

    def complete(self):
        self.status = 'completed'

    def __repr__(self):
        return f"<Mission(title={self.title}, status={self.status})>"