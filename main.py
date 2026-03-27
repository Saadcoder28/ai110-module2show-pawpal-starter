from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner
owner = Owner("Saad")

# Create pets
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 2)

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks (all due today)
task1 = Task("Morning Walk", duration=30, priority=1, due_date=date.today())
task2 = Task("Feed Dog", duration=10, priority=2, due_date=date.today())
task3 = Task("Clean Litter", duration=15, priority=1, due_date=date.today())

# Add tasks to pets
dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

# Create scheduler
scheduler = Scheduler()

# Generate plan (e.g., 40 minutes available)
plan = scheduler.generate_daily_plan(owner.get_pets(), available_time=40)

# Print schedule
print("Today's Schedule:\n")

for task in plan:
    print(f"- {task.title} ({task.duration} mins, priority {task.priority})")