from dataclasses import dataclass, field
from datetime import date
from typing import List


# -------------------- Task --------------------
@dataclass
class Task:
    title: str
    duration: int
    priority: int
    due_date: date
    completed: bool = False

    def mark_complete(self):
        pass

    def is_due_today(self):
        pass

# -------------------- Pet --------------------
@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass

    def get_tasks(self):
        pass


# -------------------- Owner --------------------
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def get_pets(self):
        pass

# -------------------- Scheduler --------------------
class Scheduler:
    def generate_daily_plan(self, pets: List[Pet]):
        pass

    def get_tasks_for_today(self, pets: List[Pet]):
        pass

    def sort_by_priority(self, tasks: List[Task]):
        pass

    def filter_by_time(self, tasks: List[Task], available_time: int):
        pass