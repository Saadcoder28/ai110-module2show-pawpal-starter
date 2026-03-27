from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class Task:
    title: str
    duration: int
    priority: int
    due_date: date
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def is_due_today(self):
        """Check if the task is due today."""
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
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self):
        return self.pets

    def get_all_tasks(self):
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
        """Generate a daily plan of tasks for the given pets within available time."""
        tasks = self.get_tasks_for_today(pets)
        tasks = self.sort_by_priority(tasks)
        plan = self.filter_by_time(tasks, available_time)
        return plan