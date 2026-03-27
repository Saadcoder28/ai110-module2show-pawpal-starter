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
task1 = Task("Morning Walk", 30, 1, date.today(), time="08:00", frequency="daily")
task2 = Task("Feed Dog", 10, 2, date.today(), time="08:00")  # SAME TIME
task3 = Task("Clean Litter", 15, 1, date.today(), time="09:00")

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
    
conflicts = scheduler.detect_conflicts(owner.get_all_tasks())

if conflicts:
    print("\n⚠️ Conflicts detected:")
    for t1, t2 in conflicts:
        print(f"- {t1.title} conflicts with {t2.title} at {t1.time}")
        
print("\nTesting recurrence:")

new_task = task1.mark_complete()

if new_task:
    print(f"New recurring task created: {new_task.title} on {new_task.due_date}")