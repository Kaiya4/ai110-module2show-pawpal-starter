# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
#--- Today's Schedule ---
#[HIGH]    Biscuit    | Morning Walk    (30 min)
#[HIGH]    Luna       | Give Meds       (5 min)
#[MEDIUM]  Luna       | Laser Pointer   (15 min)

#--- Summary ---
#Scheduled 3 tasks taking 50 minutes. Prioritized high-priority, incomplete tasks due today.
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
pytest --cov

#What these tests cover:
#Task Management: Verifies that tasks can be correctly added to a pet's list and successfully marked as complete.  #Sorting Correctness: Verifies that the scheduler properly sorts tasks by highest priority first.  
#Recurrence Logic: Confirms that marking a "daily" task as complete successfully generates a new task instance scheduled for the next day.  
#Conflict Detection: Verifies that the system correctly generates a warning when multiple tasks are assigned the exact same time.  
```

Sample test output:

```
# Paste your pytest output here
========================================================= test session starts =========================================================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/kdeng/Documents/CodePath/ai110-module2show-pawpal-starter
plugins: anyio-4.14.1
collected 5 items                                                                                                                     

tests/test_pawpal.py .....                                                                                                      [100%]

========================================================== 5 passed in 0.02s ==========================================================

My confidence level in the system's reliability would be a 5/5 since the test results all pass and I understand what the test purpose are for. 
```


## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.generate_plan()` | Sorts tasks using `lambda t: t.priority` to ensure high-priority tasks are scheduled first before time runs out. |
| Filtering | `Scheduler.generate_plan()` | Filters tasks by checking their completion status (`task.completed`) and whether their frequency matches the `current_day`. |
| Conflict handling | `Scheduler.check_conflicts()` | Uses a lightweight dictionary to track start times and returns warning messages if multiple tasks share the same time slot. |
| Recurring tasks | `Task.mark_complete()` & `Scheduler.complete_task()` | Calculates the next occurrence using Python's `timedelta` and automatically generates a new task instance when marked complete. |

## ✨ Features

1. **Priority-Based Sorting:** The scheduler organizes tasks by highest priority first.
2. **Constraint Filtering:** Tasks are only scheduled if they match the current day and fit within the available time limit.
3. **Conflict Detection:** The system warns you if multiple tasks share the exact same time slot.
4. **Task Recurrence:** Marking a task as complete automatically generates a new instance for the next due date

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. **Initialize Profile:** Enter the owner's name and add a pet's name and species
2. **Add Tasks:** Input the task's title, duration, priority level, and time
3. **Detect Overlaps:** The app will display a visual warning if you schedule multiple tasks at the exact same time
4. **Generate Schedule:** Click to produce a clean table showing your daily plan, prioritized by importance and bounded by your available time

**Sample CLI Output (`main.py`)**:
```text
--- Checking for Schedule Conflicts ---
WARNING: Time conflict at 08:00 between 'Morning Walk' (Biscuit) and 'Give Meds' (Luna).

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
