from pawpal_system import Pet, Task, Priority

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