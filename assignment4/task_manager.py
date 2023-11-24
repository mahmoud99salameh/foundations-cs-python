class Task:
    def __init__(self,description,priority):
        self.task_id=None
        self.description=description
        self.priority=priority
        self.completed=False
    @property
    def task_id(self):
        return self._task_id
    
    @task_id.setter
    def task_id(self,task_id):
        self.task_id=task_id
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self,description):
        self.description=description
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self,priorety):
        self.priority=priorety
    @property
    def completed(self):
        return self._completed
    @completed.setter
    def completed(self,completed):
        self.completed=completed
    
        