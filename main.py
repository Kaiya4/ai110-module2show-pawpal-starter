from pawpal_system import Owner, Pet, Task, Priority, Scheduler

# 1. Create an Owner
owner = Owner(name="Alex", available_minutes=60)

# 2. Create at least two Pets
biscuit = Pet(name="Biscuit", species="Golden Retriever")
luna = Pet(name="Luna", species="Cat")

owner.add_pet(biscuit)
owner.add_pet(luna)

# 3. Add at least three Tasks with different times/priorities
t1 = Task(name="Morning Walk", description="Park walk", duration=30, priority=Priority.HIGH, pet_name=biscuit.name)
t2 = Task(name="Brush Fur", description="Weekly grooming", duration=20, priority=Priority.LOW, pet_name=biscuit.name, frequency="Wednesday")
t3 = Task(name="Laser Pointer", description="Play session", duration=15, priority=Priority.MEDIUM, pet_name=luna.name)
t4 = Task(name="Give Meds", description="Heartworm pill", duration=5, priority=Priority.HIGH, pet_name=luna.name)

biscuit.add_task(t1)
biscuit.add_task(t2)
luna.add_task(t3)
luna.add_task(t4)

# 4. Generate and print "Today's Schedule"
scheduler = Scheduler(owner)
scheduler.generate_plan(current_day="Wednesday")

print("--- Today's Schedule ---")
for task in scheduler.daily_plan:
    priority_label = f"[{task.priority.name}]"
    # :<9 aligns text to the left with a fixed width of 9 characters
    print(f"{priority_label:<9} {task.pet_name:<10} | {task.name:<15} ({task.duration} min)")

print("\n--- Summary ---")
print(scheduler.explain_plan())