from datetime import datetime


class TaskViewer:

    def show_all_tasks(self, tasks):
        print("\n ALL TASKS:")
        for t in tasks:
            self.print_task(t)

    def show_incomplete_tasks(self, tasks):
        print("\nINCOMPLETE TASKS:")
        for t in tasks:
            if t.status == "Incomplete":
                self.print_task(t)

    def show_tasks_by_priority(self, tasks, priority):
        print(f"\n TASKS WITH PRIORITY: {priority}")
        for t in tasks:
            if t.priority == priority:
                self.print_task(t)

    def show_tasks_by_category(self, tasks, category):
        print(f"\n TASKS IN CATEGORY: {category}")
        for t in tasks:
            if t.category == category:
                self.print_task(t)

    def show_overdue_tasks(self, tasks):
        print("\n OVERDUE TASKS:")
        today = datetime.today().date()
        for t in tasks:
            if datetime.strptime(t.deadline, "%Y-%m-%d").date() < today:
                self.print_task(t)

    def show_today_tasks(self, tasks):
        print("\n TODAY TASKS:")
        today = datetime.today().date()
        for t in tasks:
            if datetime.strptime(t.deadline, "%Y-%m-%d").date() == today:
                self.print_task(t)

    def print_task(self, t):
        print(f"""
------------------------------
Task: {t.task_name}
Desc: {t.description}
Status: {t.status}
Priority: {t.priority}
Category: {t.category}
Deadline: {t.deadline}
------------------------------
""")