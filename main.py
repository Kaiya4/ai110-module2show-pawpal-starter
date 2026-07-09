from pawpal_system import Owner, Pet, Task, Priority, Scheduler

# 1. Setup Owner, Pets, and Scheduler
owner = Owner(name="Alex", available_minutes=120)
biscuit = Pet(name="Biscuit", species="Golden Retriever")
luna = Pet(name="Luna", species="Cat")
owner.add_pet(biscuit)
owner.add_pet(luna)

scheduler = Scheduler(owner)

# 2. Add tasks scheduled at the exact same time
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

biscuit.add_task(t1)
luna.add_task(t2)

# 3. Detect and print conflicts
print("--- Checking for Schedule Conflicts ---")
conflicts = scheduler.check_conflicts()

if conflicts:
    for warning in conflicts:
        print(warning)
else:
    print("No conflicts detected. Schedule looks clear!")