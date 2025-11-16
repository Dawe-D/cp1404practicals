"""
CP1404 - Prac 7
Task - Project Management
Time
Estimate - 20 mins  Actual - 10 mins
"""

import datetime

class Project:

    def __init__(self, name="", start_date=datetime.date.today(), priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise project"""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, Start: {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, "
                f"Cost: ${self.cost_estimate: .2f}, Completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage >= 100
