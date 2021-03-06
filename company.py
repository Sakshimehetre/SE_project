class CompanyDatabaseError(Exception):
    '''
    Create a custom error inheriting from Exception class
    '''
    
    pass

global retired_age,min_distance
retired_age=65
min_distance=3

class Employee:

    '''
    Class that creates employee instances based on personal details (first, last name etc).
    Includes method for outputing employee's email address, apply pay rise and promotion.
    '''

    raise_amount = 1.5

    def __init__(self, first, last, pay, years_in_company,mob_no=None,age=None,distance=None):
        self.first = first
        self.last = last
        self.pay = pay
        self.years_in_company = years_in_company
        self.mobile_no=mob_no
        self.age=age
        self.distance=distance
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.last}{self.first[0].upper()}@company.uk"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    def can_be_promoted(self):
        if self.years_in_company > 2:
            return True
        else:
            return False
    
    def is_correct_mobno(self):
        if len(self.mobile_no)==10:
            return True
        else:
            return False
    
    def check_retired(self):
        if(self.age>retired_age):
            return True
        else:
            return False
        
    def can_get_transportallowance(self):
        if self.distance > min_distance:
            return True
        else:
            return False

class Manager(Employee):
  '''
  Inherits from Employee class and adds a few methods specific to this class
  '''
  raise_amount = 1.8

  def __init__(self, first, last, pay, years_in_company, employees = None):
    super().__init__(first, last, pay, years_in_company)
    if employees is None:
        self.employees = []
    else:
        self.employees = [employees]

  def add_employee(self, employee_name):
    if type(employee_name) in [int, float, None] or employee_name == "":
      raise TypeError("Please make sure employee name is a valid string")
    else:
      if employee_name in self.employees:
        raise CompanyDatabaseError(f"Employee '{employee_name}' already in the company's database")
      else:
        self.employees.append(employee_name)

  def remove_employee(self, employee_name):
    if self.employees == []:
        raise CompanyDatabaseError("No employees have been added yet")
    else:
        if employee_name in self.employees:
            self.employees.remove(employee_name)
        else:
          raise CompanyDatabaseError(f"Employee '{employee_name}' not found in the company's database")

  def list_employees(self):
    if len(self.employees) == 0:
        raise CompanyDatabaseError("No employees have been added so far")
    else:
        for employee in self.employees:
            print(employee)
