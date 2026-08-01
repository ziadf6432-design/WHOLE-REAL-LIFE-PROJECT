import json
from datetime import datetime
import os


class Task:
    def __init__(self, task_name, description, status, priority, category, deadline):
        self.task_name = task_name
        self.description = description
        self.status = status
        self.priority = priority
        self.category = category
        self.deadline = deadline  

    def to_dict(self):
        return {
            "task_name": self.task_name,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "category": self.category,
            "deadline": self.deadline
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_name"],
            data["description"],
            data["status"],
            data["priority"],
            data["category"],
            data["deadline"]
        )


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def mark_task_complete(self, name):
        for task in self.tasks:
            if task.task_name == name:
                task.status = "Complete"
                print(" Task marked as complete!")
                return
        print(" Task not found!")

    def save_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "w") as file:
                data = [task.to_dict() for task in self.tasks]
                json.dump(data, file, indent=4)
            print(" Tasks saved successfully!")
        except Exception as e:
            print(" Error saving tasks:", e)

    def load_tasks(self, filename="tasks.json"):
        if not os.path.exists(filename):
            return

        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(t) for t in data]
            print(" Tasks loaded successfully!")
        except Exception as e:
            print(" Error loading tasks:", e)

    def backup_tasks(self, filename="tasks_backup.json"):
        try:
            with open(filename, "w") as file:
                data = [task.to_dict() for task in self.tasks]
                json.dump(data, file, indent=4)
            print(" Backup created!")
        except:
            print(" Failed to create backup!")