# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
It will have pets, owner, tasks, and scheduler. With one owner being with multiple dogs with multiple tasks. 
Some core actions will be registering pets, creating a task, and generating a schedule.
- What classes did you include, and what responsibilities did you assign to each?
I included a owner, pet, task, and scheduler class. The owner will have available minutes, their name, and the pets. The pet will have species, name, and task. The task will have a title, duration, and priority. The scheduler will have owner and list of schedule tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Yes, the design changed during implementation because the priority sorting was wrong since it would go alphabetically and instead of how important it is. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler considers the owner's available time, the task priority, the task frequency, and if the task is completed or not.
- How did you decide which constraints mattered most?
Priority mattered the most with available time as a boundary because this helps prioritize the needs of the pets before the owner's availability runs out.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff it makes is that it goes based off of priority rather than perfectly packing the schedule with the maximum number of smaller tasks. 
- Why is that tradeoff reasonable for this scenario?
This is reasonable because not every task has equal weight just like how needs and wants are. A pet will NEED foot or medication, but it will not NEED brushing or playing time. It's better to not let the pet die. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI with the initial brainstorming design and iterated to a simple architecture skeleton rather than a feature-rich complex app. I also had AI help me with debugging when I had trouble with terminal not running the tests. Refactoring was a major use in making the code more align and bug free. 
- What kinds of prompts or questions were most helpful?
The prompts where I asked it to review the current code for edge cases or potential bugs was most helpful as this helped prevent bigger debugging later. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
 When implementing a time picker, the AI suggested to use a hardcoded time but I decided to go with current time instead. 
- How did you evaluate or verify what the AI suggested?
From the user experience, I decided that using a local time as default would make the task entry more intuitive for a pet owner.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested task management, priority-based sorting, daily recurrence logic, and time conflict detection.
- Why were these tests important?
These tests ensure the core logic actually works, especially the high-priority tasks get scheduled before time runs out and that overlapping times are caught.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am very confident that the scheduler works correctly.
- What edge cases would you test next if you had more time?
I would test what happens if a single task's duration is larger than the owner's total available_minutes, or how the system handles an unrecognized frequency string like "monthly"

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
Building the logic to creating a working app and the smart algorithms to make it smarter.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I think the UI is still kinda ugly so I would improve it.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
AI is a very useful tool for full-stack and can even identify errors it makes itself. But the one making the design choices and the architecture ultimately falls into our hands since we decide what our needs and constraints are for the app. AI is a very good tool to brainstorm and implement our ideas.
