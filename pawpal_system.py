from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    name: str
    duration: int
    priority: str

    def edit_task(self, duration: int, priority: str) -> None:
        """Updates the task's duration and priority."""
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a new task to the pet's task list."""
        pass

    def remove_task(self, task: Task) -> None:
        """Removes a task from the pet's task list."""
        pass

class Owner:
    def __init__(self, name: str, available_minutes: int = 0):
        self.name = name
        self.available_minutes = available_minutes
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner's pet list."""
        pass

    def set_available_time(self, minutes: int) -> None:
        """Sets the owner's total available minutes for pet care."""
        pass

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.daily_plan: List[Task] = []

    def generate_plan(self) -> None:
        """Sorts tasks by priority and filters by available time."""
        pass

    def explain_plan(self) -> str:
        """Returns the reasoning behind the generated daily plan."""
        pass