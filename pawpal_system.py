from dataclasses import dataclass, field
from typing import List
from enum import IntEnum
from datetime import date, timedelta

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class Task:
    name: str
    description: str
    duration: int
    priority: Priority
    pet_name: str
    time: str = "00:00" 
    frequency: str = "daily"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> 'Task':
        """Marks the task as completed and returns a new instance if recurring."""
        self.completed = True
        
        if self.frequency.lower() == "daily":
            new_date = self.due_date + timedelta(days=1)
        elif self.frequency.lower() == "weekly":
            new_date = self.due_date + timedelta(days=7)
        else:
            return None
            
        return Task(
            name=self.name,
            description=self.description,
            duration=self.duration,
            priority=self.priority,
            pet_name=self.pet_name,
            time=self.time,
            frequency=self.frequency,
            completed=False,
            due_date=new_date
        )

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Appends a new task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Removes an existing task from the pet's task list if present."""
        if task in self.tasks:
            self.tasks.remove(task)

class Owner:
    def __init__(self, name: str, available_minutes: int = 0):
        self.name = name
        self.available_minutes = available_minutes
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Adds a new pet profile to the owner's account."""
        self.pets.append(pet)

    def set_available_time(self, minutes: int) -> None:
        """Updates the owner's total daily available minutes for pet care."""
        self.available_minutes = minutes

    def get_all_tasks(self) -> List[Task]:
        """Returns a flat list of all tasks combined across all of the owner's pets."""
        return [task for pet in self.pets for task in pet.tasks]

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.daily_plan: List[Task] = []
    
    def check_conflicts(self) -> List[str]:
        """Lightweight conflict detection that returns a list of warning messages."""
        warnings = []
        seen_times = {}
        
        for task in self.owner.get_all_tasks():
            if task.completed:
                continue
                
            if task.time in seen_times:
                conflict_task = seen_times[task.time]
                warnings.append(
                    f"WARNING: Time conflict at {task.time} between '{conflict_task.name}' ({conflict_task.pet_name}) and '{task.name}' ({task.pet_name})."
                )
            else:
                seen_times[task.time] = task
                
        return warnings

    def complete_task(self, task: Task, pet: Pet) -> None:
        """Completes a task and schedules the next occurrence if applicable."""
        next_task = task.mark_complete()
        if next_task:
            pet.add_task(next_task)

    def edit_task(self, task: Task, new_duration: int, new_priority: Priority) -> bool:
        """Updates an existing task's duration and priority level."""
        task.duration = new_duration
        task.priority = new_priority
        return True

    def generate_plan(self, current_day: str) -> None:
        """Builds a daily plan bounded by available time and sorted by highest priority."""
        all_tasks = self.owner.get_all_tasks()
        
        all_tasks.sort(key=lambda t: t.priority, reverse=True)
        
        self.daily_plan = []
        time_used = 0
        
        for task in all_tasks:
            is_due = (task.frequency.lower() == "daily" or 
                      task.frequency.lower() == current_day.lower())
            
            if not task.completed and is_due and (time_used + task.duration) <= self.owner.available_minutes:
                self.daily_plan.append(task)
                time_used += task.duration

    def explain_plan(self) -> str:
        """Generates a brief summary string explaining the scheduled tasks."""
        return f"Scheduled {len(self.daily_plan)} tasks taking {sum(t.duration for t in self.daily_plan)} minutes. Prioritized high-priority, incomplete tasks due today."