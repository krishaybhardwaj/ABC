class employee:
    user_input = 1.04
    number_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        employee.number_of_emps+=1
 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.user_input)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') 
        return cls(first, last, pay)

emp_1 = employee('Krishay', 'Bhardwaj', 50000 )
emp_2 = employee('Cary', 'Maguire', 60000)
emp_3 = employee('Tin', 'Schaufer', 20000)


emp_str_1 = 'Krishay-Bhardwaj-50000'
emp_str_2 = 'Vishakha-Bhardwaj-70000'
emp_str_3 = 'Vedika-Bhardwaj-100000'
emp_str_4 = 'Rajeev-Bhardwaj-90000'

new_emp_1 = employee.from_string(emp_str_1)

print(new_emp_1.pay)
