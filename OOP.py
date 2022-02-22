class student:
    def __init__(self, first, last, fees):
        self.first = first
        self.last = last
        self.fees = fees
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

stu_1 = student('Krishay', 'Bhardwaj', 5000)
stu_2 = student('Aaryaveer', 'Katoch', 10000)

print(stu_1.fullname())