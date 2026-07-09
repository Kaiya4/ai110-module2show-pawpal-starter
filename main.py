from pawpal_system import Owner, Pet, Task, Priority, Scheduler

# 1. Setup Owner, Pets, and Scheduler
owner = Owner(name="Alex", available_minutes=120)
biscuit = Pet(name="Biscuit", species="Golden Retriever")
luna = Pet(name="Luna", species="Cat")
owner.add_pet(biscuit)
owner.add_pet(luna)

scheduler = Scheduler(owner)

# 2. Add tasks scheduled for the pets
t1 = Task(
    name="Morning Walk", 
    description="Park walk", 
    duration=30, 
    priority=Priority.HIGH, 
    pet_name=biscuit.name,
    time="08:00"
)

t2 = Task(
    name="Give Meds", 
    description="Heartworm pill", 
    duration=5, 
    priority=Priority.HIGH, 
    pet_name=luna.name,
    time="08:00"
)

t3 = Task(
    name="Playtime", 
    description="Laser pointer", 
    duration=15, 
    priority=Priority.MEDIUM, 
    pet_name=luna.name,
    time="14:00"
)

t4 = Task(
    name="Dinner Feeding", 
    description="Kibble and wet food", 
    duration=10, 
    priority=Priority.HIGH, 
    pet_name=biscuit.name,
    time="18:00"
)

t5 = Task(
    name="Grooming", 
    description="Brush coat", 
    duration=20, 
    priority=Priority.LOW, 
    pet_name=biscuit.name,
    time="19:00"
)

biscuit.add_task(t1)
luna.add_task(t2)
luna.add_task(t3)
biscuit.add_task(t4)
biscuit.add_task(t5)

# 3. Detect and print conflicts
print("--- Checking for Schedule Conflicts ---")
conflicts = scheduler.check_conflicts()

if conflicts:
    for warning in conflicts:
        print(warning)
else:
    print("No conflicts detected. Schedule looks clear!")

# 4. Generate and display the plan
print("\n--- Generating Today's Plan ---")
scheduler.generate_plan(current_day="daily")
if scheduler.daily_plan:
    for task in scheduler.daily_plan:
        print(f"[{task.priority.name}] {task.pet_name} | {task.name} ({task.duration} min)")
    print(f"\nSummary: {scheduler.explain_plan()}")