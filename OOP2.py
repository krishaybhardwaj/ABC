
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
        
print(employee.number_of_emps)   
emp_1 = employee('Krishay', 'Bhardwaj', 50000 )
emp_2 = employee('Cary', 'Maguire', 60000)
emp_3 = employee('Tin', 'Schaufer', 20000)

print(employee.number_of_emps)