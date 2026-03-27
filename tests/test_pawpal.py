from datetime import date, timedelta
from pawpal_system import Task, Pet, Scheduler


# Test 1: Task Completion
def test_task_completion():
    task = Task("Feed", 10, 1, date.today())
    assert task.completed == False

    task.mark_complete()

    assert task.completed == True


# Test 2: Task Addition to Pet
def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)

    task = Task("Walk", 30, 1, date.today())

    initial_count = len(pet.get_tasks())

    pet.add_task(task)

    assert len(pet.get_tasks()) == initial_count + 1

# Test 3: Sorting by Time
def test_sort_by_time():
    scheduler = Scheduler()

    t1 = Task("Task1", 10, 1, date.today(), time="09:00")
    t2 = Task("Task2", 10, 1, date.today(), time="07:00")
    t3 = Task("Task3", 10, 1, date.today(), time="08:00")

    tasks = [t1, t2, t3]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].time == "07:00"
    assert sorted_tasks[1].time == "08:00"
    assert sorted_tasks[2].time == "09:00"


# Test 4: Recurrence Logic
def test_daily_recurrence():
    task = Task("Walk", 30, 1, date.today(), frequency="daily")

    new_task = task.mark_complete()

    assert task.completed == True
    assert new_task is not None
    assert new_task.due_date == date.today() + timedelta(days=1)


# Test 5: Conflict Detection
def test_conflict_detection():
    scheduler = Scheduler()

    t1 = Task("Walk", 30, 1, date.today(), time="08:00")
    t2 = Task("Feed", 10, 2, date.today(), time="08:00")

    conflicts = scheduler.detect_conflicts([t1, t2])

    assert len(conflicts) == 1


# Test 6: Edge Case - No Tasks
def test_empty_tasks():
    scheduler = Scheduler()

    plan = scheduler.generate_daily_plan([], available_time=60)

    assert plan == []