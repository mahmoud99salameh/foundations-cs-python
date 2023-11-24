class Task:
    def __init__(self,description,priority):
        self.task_id=None
        self.description=description
        self.priority=priority
        self.completed=False
    @property
    def task_id(self):
        return self.task_id
    @task_id.setter
    def task_id(self,task_id):
        self.task_id=task_id
    
        