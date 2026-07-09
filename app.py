import streamlit as st
from pawpal_system import Owner, Pet, Task, Priority, Scheduler
import datetime

# Initialize the owner in session state
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_minutes=120)

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.
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

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value="Jordan")
st.session_state.owner.name = owner_name

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks to feed into your scheduler.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    task_time = st.time_input("Time")

if st.button("Add task"):
    priority_map = {"low": Priority.LOW, "medium": Priority.MEDIUM, "high": Priority.HIGH}
    
    pet = next((p for p in st.session_state.owner.pets if p.name == pet_name), None)
    if not pet:
        pet = Pet(name=pet_name, species=species)
        st.session_state.owner.add_pet(pet)
        
    # Create task with formatted time string
    new_task = Task(
        name=task_title, 
        description="", 
        duration=int(duration), 
        priority=priority_map[priority], 
        pet_name=pet_name,
        time=task_time.strftime("%H:%M") 
    )
    pet.add_task(new_task)
    st.success(f"Added {task_title} for {pet_name} at {new_task.time}!")

# Display current tasks directly from the backend logic
all_tasks = st.session_state.owner.get_all_tasks()
if all_tasks:
    st.write("Current tasks:")
    for t in all_tasks:
        st.write(f"- **{t.pet_name}**: {t.name} ({t.duration}m) [{t.priority.name}]")
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    
    # 1. Check and display conflicts
    conflicts = scheduler.check_conflicts()
    if conflicts:
        for warning in conflicts:
            st.warning(warning)
            
    # 2. Generate plan
    scheduler.generate_plan(current_day="Wednesday") 
    
    st.write("### Today's Plan")
    if scheduler.daily_plan:
        # 3. Format as a professional table
        plan_data = [
            {
                "Priority": task.priority.name, 
                "Pet": task.pet_name, 
                "Task": task.name, 
                "Duration (m)": task.duration
            } 
            for task in scheduler.daily_plan
        ]
        st.table(plan_data)
            
        st.success(scheduler.explain_plan())
    else:
        st.info("No tasks scheduled. Check your available time or ensure tasks are added.")