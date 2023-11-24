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

class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_history = CompletedTasksStack()

    def display_menu(self):
        print("\nTask Manager Menu:")
        print("1. Add a new task")
        print("2. Get a task by task id")
        print("3. Mark the highest priority task as completed")
        print("4. Display all tasks in order of priority")
        print("5. Display only tasks that are not completed")
        print("6. Display the last completed task")
        print("7. Exit")

    def add_new_task(self):
        description = input("Enter task description: ")
        priority = int(input("Enter task priority (integer value): "))
        new_task = Task(description, priority)
        self.task_queue.add_task(new_task)
        print("Task added successfully.")

    def get_task_by_id(self):
        task_id = int(input("Enter task id: "))
        # Assuming tasks are uniquely identified by their task_id
        for task in self.task_queue.tasks:
            if task.get_task_id() == task_id:
                print(f"Task found: {task.get_description()} (Priority: {task.get_priority()})")
                return
        print("Task not found.")

    def mark_highest_priority_task_completed(self):
        if not self.task_queue.is_empty():
            completed_task = self.task_queue.get_next_task()
            completed_task.set_completed(True)
            self.task_history.push_task(completed_task)
            print("Highest priority task marked as completed and moved to task history.")
        else:
            print("Task queue is empty.")

    def display_all_tasks(self):
        if not self.task_queue.is_empty():
            print("\nAll tasks in order of priority:")
            for task in self.task_queue.tasks:
                print(f"Task ID: {task.get_task_id()}, Description: {task.get_description()}, Priority: {task.get_priority()}, Completed: {task.is_completed()}")
        else:
            print("Task queue is empty.")

    def display_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.task_queue.tasks if not task.is_completed()]
        if incomplete_tasks:
            print("\nIncomplete tasks:")
            for task in incomplete_tasks:
                print(f"Task ID: {task.get_task_id()}, Description: {task.get_description()}, Priority: {task.get_priority()}, Completed: {task.is_completed()}")
        else:
            print("No incomplete tasks.")

    def display_last_completed_task(self):
        if not self.task_history.is_empty():
            last_completed_task = self.task_history.pop_task()
            print(f"Last completed task: {last_completed_task.get_description()} (Priority: {last_completed_task.get_priority()})")
        else:
            print("Task history is empty.")

    def run_task_manager(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                self.add_new_task()
            elif choice == '2':
                self.get_task_by_id()
            elif choice == '3':
                self.mark_highest_priority_task_completed()
            elif choice == '4':
                self.display_all_tasks()
            elif choice == '5':
                self.display_incomplete_tasks()
            elif choice == '6':
                self.display_last_completed_task()
            elif choice == '7':
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

# Example Usage:

task_manager = TaskManager()
task_manager.run_task_manager()