import datetime

class Person():

    def __init__(self, name_, age_, bday_, hair_color_):
        self.name = name_
        self.age = age_
        self.birthday = bday_
        self.hair_color = hair_color_

    def set_name(self, name_):
        self.name = name_
    def set_age(self, age_):
        self.age = age_
    def set_bday(self, bday_):
        self.birthday = bday_

    def current_age(self):
        now = datetime.datetime.now()
        now_seconds = now.timestamp()
        bday = datetime.datetime.strptime(self.birthday, '%m/%d/%y')
        bday_seconds = bday.timestamp()
        
        age_seconds = now_seconds - bday_seconds
        age_minutes = (age_seconds // 60)
        age_hours = age_minutes / 60
        age_days = age_hours / 24
        age_years = age_days // 365
        
        if bday.day < now.day:
            age_years -= 1
        # age_years = ((age_seconds // 60) / 60 / 24) // 365
        print(age_years)
        return age_years

Danny = ["Danny", 10, "01/22/16", "Coral"]
print(Danny[0], end=" ")
print(Danny[3], end=" ")
print(Danny[2], end=" ")

Johnny = ["J man", 10, "01/22/16", "Pink"]


peoples = []
peoples.append(Danny)
peoples.append(Johnny)
print(peoples)
# print(Danny[1])
print(peoples[0][1])

# Danny.set_name("Danny")
# Danny.set_age(10)
# Danny.set_bday("1/20/16")

# Johnny = Person()
# Johnny.set_name("J boi")

# print(Danny.birthday)
# print(Johnny.birthday)
# Danny.current_age()