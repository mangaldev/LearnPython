import datetime
import json


class DepartmentEmployee:

    def __init__(self, department: str = '', department_division: str = '', position_title: str = '',
                 hire_date: str = '', salary: str = "0"):
        self.department = department
        self.department_division = department_division
        self.position_title = position_title
        self.hire_date = hire_date
        self.salary = salary

    def filter(self):
        from datetime import datetime
        return self.department in ['ECC', 'CIT', 'EMS'] and datetime.strptime(self.hire_date,
                                                                              '%d-%b-%Y') > self.from_date()

    def from_date(self):
        return datetime.datetime(2010, 1, 1, 0, 0)

    @staticmethod
    def from_csv_line(line):
        return DepartmentEmployee(line[0], line[1], line[3], line[5], line[7])

    def to_json(self):
        return json.dumps(self.__dict__)
