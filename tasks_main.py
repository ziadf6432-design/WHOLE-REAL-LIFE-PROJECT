from task_manger import Task, TaskManager
from task_riview import TaskViewer
from datetime import datetime

manager = TaskManager()
viewer = TaskViewer()

print("\n Welcome to Task Organizer System!\n")

manager.load_tasks()

while True:
    print("""
========= MENU =========
1) Add new task
2) Mark task as complete
3) View all tasks
4) View incomplete tasks
5) View tasks by priority
6) View tasks by category
7) View overdue tasks
8) View today's tasks
9) Save and Exit
========================
""")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print(" Invalid input!")
        continue

    if choice == 1:
        name = input("Task name: ")
        desc = input("Description: ")
        status = "Incomplete"
        priority = input("Priority (High/Medium/Low): ")
        category = input("Category (Study/Assignment/Project/Exam/Personal): ")
        deadline = input("Deadline (YYYY-MM-DD): ")

        task = Task(name, desc, status, priority, category, deadline)
        manager.add_task(task)

    elif choice == 2:
        name = input("Enter task name to mark complete: ")
        manager.mark_task_complete(name)

    elif choice == 3:
        viewer.show_all_tasks(manager.tasks)

    elif choice == 4:
        viewer.show_incomplete_tasks(manager.tasks)

    elif choice == 5:
        p = input("Enter priority: ")
        viewer.show_tasks_by_priority(manager.tasks, p)

    elif choice == 6:
        c = input("Enter category: ")
        viewer.show_tasks_by_category(manager.tasks, c)

    elif choice == 7:
        viewer.show_overdue_tasks(manager.tasks)

    elif choice == 8:
        viewer.show_today_tasks(manager.tasks)

    elif choice == 9:
        manager.save_tasks()
        manager.backup_tasks()
        print(" Exiting...")
        break

    else:
        print("Invalid menu choice!")