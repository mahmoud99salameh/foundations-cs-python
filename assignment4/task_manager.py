class Task:
    task_counter = 0

    def __init__(self, description, priority):
        self.task_id = Task.task_counter
        Task.task_counter += 1
        self.description = description
        self.priority = priority
        self.completed = False

    def get_task_id(self):
        return self.task_id

    def get_description(self):
        return self.description

    def get_priority(self):
        return self.priority

    def is_completed(self):
        return self.completed

    def set_completed(self, completed):
        self.completed = completed


class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.get_priority(), reverse=True)

    def get_next_task(self):
        if self.tasks:
            return self.tasks.pop()

    def is_empty(self):
        return not bool(self.tasks)


class CompletedTasksStack:
    def __init__(self):
        self.stack = []

    def push_task(self, task):
        self.stack.append(task)

    def pop_task(self):
        if self.stack:
            return self.stack.pop()

    def is_empty(self):
        return not bool(self.stack)


# Example Usage:

# Create tasks
task1 = Task("Complete project", 2)
task2 = Task("Study for exam", 1)
task3 = Task("Exercise", 3)

# Create priority queue
priority_queue = PriorityQueue()

# Add tasks to the priority queue
priority_queue.add_task(task1)
priority_queue.add_task(task2)
priority_queue.add_task(task3)

# Mark tasks as completed and push them onto the stack
completed_tasks_stack = CompletedTasksStack()

completed_task = priority_queue.get_next_task()
completed_task.set_completed(True)
completed_tasks_stack.push_task(completed_task)

completed_task = priority_queue.get_next_task()
completed_task.set_completed(True)
completed_tasks_stack.push_task(completed_task)

# View completed tasks
while not completed_tasks_stack.is_empty():
    completed_task = completed_tasks_stack.pop_task()
    print(f"Completed Task: {completed_task.get_description()} (Priority: {completed_task.get_priority()})")


    
        