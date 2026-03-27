# PawPal+ Project Reflection

## 1. System Design

Three core actions user should perform:
1) Enter pet information  
2) Do tasks like feeding pet  
3) Get a daily schedule  

### a. Initial design

My design includes four classes: Owner, Pet, Task, and Scheduler. Owner manages pets, Pet manages tasks, Task stores task details, and Scheduler generates a daily plan.

I used Copilot to refine relationships and ensure clean separation of responsibilities between classes.

### b. Design changes

Yes, my design evolved during implementation. I added attributes like `time` and `frequency` to Task and introduced methods like conflict detection and time-based sorting to improve functionality.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler considers time availability, task priority, due date, and completion status. Priority was most important because it ensures critical tasks are handled first.

### b. Tradeoffs

My scheduler uses a simple greedy approach to select tasks within available time. This may not always be optimal, but it is efficient and easy to understand for this use case.

---

## 3. AI Collaboration

### a. How you used AI

I used Copilot for generating methods, debugging errors, and refining logic such as sorting, filtering, and recurrence handling. Short, focused prompts worked best.

### b. Judgment and verification

At one point, Copilot suggested overly complex logic for scheduling, which I simplified to keep the system readable. I verified correctness by testing and manually tracing outputs.

### c. AI Strategy Reflection

Inline suggestions and chat-based explanations in Copilot were most helpful for building and refining the scheduler.  

I rejected one suggestion that overcomplicated recurrence logic and instead implemented a simpler version using `timedelta`.  

Using separate chat sessions helped me focus on one phase at a time (design, logic, testing), which kept my work organized.  

I learned that as the "lead architect," I must guide AI tools, verify outputs, and prioritize clarity over unnecessary complexity.

---

## 4. Testing and Verification

### a. What you tested

I tested task completion, task addition, sorting by time, recurrence logic, conflict detection, and edge cases like empty task lists.

### b. Confidence

I am highly confident (5/5) since all tests pass and key behaviors work correctly. With more time, I would test overlapping time ranges and more complex scheduling scenarios.

---

## 5. Reflection

### a. What went well

I am most satisfied with integrating backend logic with the Streamlit UI and making the scheduler both functional and user-friendly.

### b. What you would improve

I would improve the scheduling algorithm to handle overlapping durations and optimize task selection beyond a greedy approach.

### c. Key takeaway

I learned how to design structured systems, break problems into components, and effectively collaborate with AI while maintaining control over design decisions.