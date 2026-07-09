from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Priority, Scheduler

def test_task_completion():
    # Setup
    task = Task(name="Walk", description="Park", duration=30, priority=Priority.HIGH, pet_name="Biscuit")
    
    # Action
    task.mark_complete()
    
    # Assert
    assert task.completed is True

def test_task_addition():
    # Setup
    biscuit = Pet(name="Biscuit", species="Golden Retriever")
    task = Task(name="Walk", description="Park", duration=30, priority=Priority.HIGH, pet_name="Biscuit")
    
    # Action
    biscuit.add_task(task)
    
    # Assert
    assert len(biscuit.tasks) == 1
    assert task in biscuit.tasks

def test_priority_sorting():
    owner = Owner(name="Jordan", available_minutes=120)
    pet = Pet(name="Mochi", species="Dog")
    owner.add_pet(pet)
    
    # Add a low priority and high priority task
    pet.add_task(Task(name="Low Priority", description="", duration=30, priority=Priority.LOW, pet_name="Mochi"))
    pet.add_task(Task(name="High Priority", description="", duration=30, priority=Priority.HIGH, pet_name="Mochi"))
    
    scheduler = Scheduler(owner)
    scheduler.generate_plan(current_day="daily")
    
    # Assert the high priority task was scheduled first
    assert len(scheduler.daily_plan) == 2
    assert scheduler.daily_plan[0].name == "High Priority"

def test_recurrence_logic():
    task = Task(name="Walk", description="", duration=30, priority=Priority.HIGH, pet_name="Mochi", frequency="daily")
    
    # Complete the task
    new_task = task.mark_complete()
    
    # Assert original is complete and new task is scheduled for tomorrow
    assert task.completed is True
    assert new_task is not None
    assert new_task.due_date == date.today() + timedelta(days=1)

def test_conflict_detection():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="Dog")
    owner.add_pet(pet)
    
    # Add two tasks at the exact same time
    pet.add_task(Task(name="Task 1", description="", duration=15, priority=Priority.MEDIUM, pet_name="Mochi", time="08:00"))
    pet.add_task(Task(name="Task 2", description="", duration=15, priority=Priority.MEDIUM, pet_name="Mochi", time="08:00"))
    
    scheduler = Scheduler(owner)
    conflicts = scheduler.check_conflicts()
    
    # Assert a conflict warning was generated
    assert len(conflicts) == 1
    assert "WARNING: Time conflict at 08:00" in conflicts[0]