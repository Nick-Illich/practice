from pprint import pprint


class GetInfoMixin:
    def get_info(self):
        return self.__dict__


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person, GetInfoMixin):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


e = Employee(
    name="John",
    skills=["python programming", "project management"],
    dependents={"wife": "Jane", "children": ["Alice", "Bob"]}
)

profile = e.get_info()
print(type(profile))

