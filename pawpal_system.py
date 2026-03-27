from dataclasses import dataclass, field
from datetime import date
from typing import List


from datetime import timedelta

@dataclass
class Task:
    title: str
    duration: int
    priority: int
    due_date: date
    completed: bool = False
    time: str = "09:00"
    frequency: str = "none"

    def mark_complete(self):
        self.completed = True

        # 🔥 Handle recurrence
        if self.frequency == "daily":
            return Task(
                self.title,
                self.duration,
                self.priority,
                self.due_date + timedelta(days=1),
                False,
                self.time,
                self.frequency
            )

        elif self.frequency == "weekly":
            return Task(
                self.title,
                self.duration,
                self.priority,
                self.due_date + timedelta(days=7),
                False,
                self.time,
                self.frequency
            )

        return None
    
    def is_due_today(self):
        return self.due_date == date.today()

@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from the pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        """Get the list of tasks for the pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str):
        """Initialize an Owner with a name."""
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from the owner's pet list."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self):
        """Get the list of pets owned by the owner."""
        return self.pets

    def get_all_tasks(self):
        """Get all tasks from all pets owned by the owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def get_tasks_for_today(self, pets: List[Pet]):
        """Get all tasks due today from the given pets."""
        today_tasks = []
        for pet in pets:
            for task in pet.get_tasks():
                if task.is_due_today() and not task.completed:
                    today_tasks.append(task)
        return today_tasks

    def sort_by_priority(self, tasks: List[Task]):
        """Sort tasks by priority."""
        return sorted(tasks, key=lambda task: task.priority)

    def filter_by_time(self, tasks: List[Task], available_time: int):
        """Filter tasks that fit within the available time."""
        selected_tasks = []
        time_used = 0
        for task in tasks:
            if time_used + task.duration <= available_time:
                selected_tasks.append(task)
                time_used += task.duration
        return selected_tasks

    def generate_daily_plan(self, pets: List[Pet], available_time: int):
        tasks = self.get_tasks_for_today(pets)
        tasks = self.filter_completed(tasks)
        tasks = self.sort_by_priority(tasks)
        tasks = self.sort_by_time(tasks)
        plan = self.filter_by_time(tasks, available_time)
        return plan
    
    def sort_by_time(self, tasks: List[Task]):
        """Sort tasks by time (HH:MM)."""
        return sorted(tasks, key=lambda task: task.time)
    
    def filter_completed(self, tasks: List[Task]):
        """Return only incomplete tasks."""
        return [task for task in tasks if not task.completed]


    def filter_by_pet(self, pets: List[Pet], pet_name: str):
        """Return tasks for a specific pet."""
        for pet in pets:
            if pet.name == pet_name:
                return pet.get_tasks()
        return []
    
    def detect_conflicts(self, tasks: List[Task]):
        """Detect tasks scheduled at the same time."""
        time_map = {}
        conflicts = []

        for task in tasks:
            if task.time in time_map:
                conflicts.append((task, time_map[task.time]))
            else:
                time_map[task.time] = task

        return conflicts