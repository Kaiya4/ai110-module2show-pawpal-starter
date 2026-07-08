from dataclasses import dataclass, field
from typing import List
from enum import IntEnum

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
    frequency: str = "daily"
    completed: bool = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.completed = True

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