import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("User")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

st.subheader("Add a Pet")

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Age", min_value=0, step=1, value=1)

if st.button("Add Pet"):
    new_pet = Pet(pet_name, species, int(pet_age))
    owner.add_pet(new_pet)
    st.success(f"{pet_name} added!")
    
st.subheader("Current Pets")

pets = owner.get_pets()

if pets:
    for pet in pets:
        st.write(f"- {pet.name} ({pet.species}, age {pet.age})")
else:
    st.info("No pets yet.")

st.divider()

st.subheader("Add Task")

if pets:
    pet_names = [pet.name for pet in pets]
    selected_pet = st.selectbox("Select Pet", pet_names)

    task_title = st.text_input("Task title", value="Morning walk")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add Task"):
        priority_map = {"high": 1, "medium": 2, "low": 3}

        new_task = Task(
            task_title,
            int(duration),
            priority_map[priority],
            date.today()
        )

        for pet in pets:
            if pet.name == selected_pet:
                pet.add_task(new_task)
                st.success(f"Task added to {pet.name}")
                break
else:
    st.warning("Add a pet first!")

st.subheader("Current Tasks")

all_tasks = owner.get_all_tasks()

if all_tasks:
    for task in all_tasks:
        st.write(f"- {task.title} ({task.duration} mins, priority {task.priority})")
else:
    st.info("No tasks yet.")

st.divider()

st.subheader("Today's Schedule")

available_time = st.number_input("Available Time (minutes)", min_value=1, value=60)

if st.button("Generate Schedule"):
    plan = scheduler.generate_daily_plan(owner.get_pets(), available_time)

    if plan:
        st.success("Today's Plan:")
        total = 0
        for task in plan:
            st.write(f"- {task.title} ({task.duration} mins, priority {task.priority})")
            total += task.duration
        st.write(f"Total Time Used: {total} mins")
    else:
        st.warning("No tasks fit today's schedule.")