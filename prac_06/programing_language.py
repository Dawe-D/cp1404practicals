"""
CP1404 Prac 6
Programming Languages class
Time
Estimate = 30 mins
Actual   = 40 mins
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=""):
        """
        name: string, name of program language
        typing: string, typing style
        reflection: string, if it has reflection
        year: int, year of creation
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection = {self.reflection}, First appeared in {self.year}"