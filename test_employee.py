import unittest
from company import Employee, CompanyDatabaseError

# Test Employee class
class TestEmployeeCreation(unittest.TestCase):
    
  def setUp(self):
    '''
    Creates re-usable cases for tests that follow
    '''
    self.emp_1 = Employee("Suresh", "Patil", 30000, 4,'9975403171',66)
    self.emp_2 = Employee("Neha", "Joshi", 20000, 2,'908834897',35)   
        
  def test_employee_fullname(self):
    '''
    Fullname method should combine employee's first and last name
    '''
    emp_1_fullname = self.emp_1.fullname
    self.assertEqual(emp_1_fullname, "Suresh Patil")
    
    emp_2_fullname = self.emp_2.fullname
    self.assertEqual(self.emp_2.fullname, "Neha Joshi")
      
  def test_employee_email(self):
    '''
    Email method should combine lastname and uppercase of
    first name's first letter with @company.uk
    '''
    email1 = self.emp_1.email
    self.assertEqual(email1, "PatilS@company.uk")

    email2 = self.emp_2.email
    self.assertEqual(email2, "JoshiN@company.uk")

  def test_employee_email_regex(self):
    '''
    Testing email structure against regex
    '''
    email1 = self.emp_1.email
    self.assertRegex(email1, r"[\w]+[\w]@company\.uk")

    email2 = self.emp_2.email
    self.assertRegex(email2, r"[\w]+[\w]@company\.uk")

  def test_employee_apply_raise(self):
    '''
    Apply raise should multiply pay with raise amount
    '''
    raise_emp_1 = self.emp_1.apply_raise()
    self.assertEqual(raise_emp_1, 45000)

    raise_emp_2 = self.emp_2.apply_raise()
    self.assertEqual(raise_emp_2, 30000)

  def test_employee_can_be_promoted(self):
    '''
    If employee years in the company > 2
    then this should return True
    '''
    promotion_1 = self.emp_1.can_be_promoted()
    self.assertTrue(promotion_1)

    promotion_2 = self.emp_2.can_be_promoted()
    self.assertFalse(promotion_2)
  def test_is_correct_mobno(self):
    mob_1 = self.emp_1.is_correct_mobno()
    self.assertTrue(mob_1)

    mob_2 = self.emp_2.is_correct_mobno()
    self.assertFalse(mob_2)

  def test_check_retired(self):
    age1=self.emp_1.check_retired()
    self.assertTrue(age1)
    age2=self.emp_2.check_retired()
    self.assertFalse(age2)
    
  def test_can_get_transportallowance(self):
    TA1=self.emp_1.can_get_transportallowance()
    self.assertTrue(TA1)
    TA2=self.emp_2.can_get_transportallowance()
    self.assertFalse(TA2)


if __name__ == "__main__":
  unittest.main()
