from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


print("=== PawPal+ Demo ===\n")

# Create owner
owner = Owner("Saad")

# Create pets
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 2)

owner.add_pet(dog)
owner.add_pet(cat)

print("Pets:")
for pet in owner.get_pets():
    print(f"- {pet.name} ({pet.species})")


# Create tasks (more variety)
task1 = Task("Morning Walk", 30, 1, date.today(), time="08:00", frequency="daily")
task2 = Task("Feed Dog", 10, 2, date.today(), time="08:00")  # conflict
task3 = Task("Clean Litter", 15, 1, date.today(), time="09:00")
task4 = Task("Play Time", 20, 3, date.today(), time="10:00")

# Add tasks
dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)
dog.add_task(task4)

print("\nAll Tasks:")
for task in owner.get_all_tasks():
    print(f"- {task.title} at {task.time} (priority {task.priority})")


# Scheduler
scheduler = Scheduler()

print("\n=== Generated Schedule ===")
plan = scheduler.generate_daily_plan(owner.get_pets(), available_time=40)

for task in plan:
    print(f"🕒 {task.time} - {task.title} ({task.duration} mins, priority {task.priority})")


# Conflict detection
conflicts = scheduler.detect_conflicts(owner.get_all_tasks())

if conflicts:
    print("\n⚠️ Conflicts detected:")
    for t1, t2 in conflicts:
        print(f"- {t1.title} conflicts with {t2.title} at {t1.time}")


# Recurrence demo
print("\n=== Recurrence Test ===")

new_task = task1.mark_complete()

if new_task:
    print(f"New recurring task created: {new_task.title} on {new_task.due_date}")