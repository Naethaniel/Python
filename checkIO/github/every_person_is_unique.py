from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def age(self):
        curr_time = '01.01.2018'

        curr_time = datetime.strptime(curr_time, '%d.%m.%Y')
        age = datetime.strptime(self.birth_date, '%d.%m.%Y')

        years = curr_time.year - age.year

        if curr_time.month < age.month or (curr_time.month == age.month and curr_time.day < age.day):
            years -= 1

        return years

    def work(self):
        if self.gender == 'male':
            return 'He is a {}'.format(self.job)
        elif self.gender == 'female':
            return 'She is a {}'.format(self.job)
        elif self.gender == 'unknown':
            return 'Is a {}'.format(self.job)

    def money(self):
        months = self.working_years * 12
        salary = str(self.salary * months)
        output = ''
        helper = 0
        for i in range(len(salary)-1, 0, -1):
            if helper == 2:
                output = ' ' + salary[i] + output
                helper = 0
            else:
                output = salary[i] + output
                helper += 1
        output = salary[0] + output
        return output

    def home(self):
        return 'Lives in {}, {}'.format(self.city, self.country)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    # p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    # p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    # p1.money()
    # assert p1.name() == "John Smith", "Name"
    # assert p1.age() == 38, "Age"
    # assert p2.work() == "Is a designer", "Job"
    # assert p1.money() == "648 000", "Money"
    # assert p2.home() == "Lives in Vienna, Austria", "Home"
    # # print("Coding complete? Let's try tests!")
    print(Person('Adam', 'Greene', '24.12.1961', 'director', 36, 11000, 'England', 'London', 'male').money())
