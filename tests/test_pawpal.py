from datetime import date
from pawpal_system import Task, Pet


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