import datetime
# print()

class Person:
    def __init__(self) -> None:
        pass
    
    def person_info(self,person_name, person_country, DOB):
        self.name = person_name
        self.country = person_country
        self.DOB = datetime.datetime.strptime(DOB,'%Y-%m-%d').date()
    
    def calculate_age(self):
        today_date = datetime.date.today()
        return  today_date.year - self.DOB.year - ((today_date.month,today_date.day)<(self.DOB.month,self.DOB.day))
    

person = Person()
person.person_info('Pawan Shah',person_country='Nepal',DOB='2001-09-02')
print(f'The age of {person.name} is {person.calculate_age()}')