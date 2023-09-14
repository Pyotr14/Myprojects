class Human:
    
    def __init__(self,gender, name, age, high, color_of_eyes, color_of_skin, color_of_hair, education, country):
        self.gender = gender
        self.name = name
        self.age = age
        self.high = high
        self.color_of_eyes = color_of_eyes
        self.color_of_skin = color_of_skin
        self.color_of_hair = color_of_hair
        self.education = education
        self.country = country
    
    def character(self):
        return f'Gender: {self.gender}\nName: {self.name}\nAge: {self.age}\nHigh: {self.high}\nColor of eyes: {self.color_of_eyes}\nColor of skin: {self.color_of_skin}\nEducation: {self.education}\nCountry: {self.country}'
Number = 1
while True:
    Que1 = input('What is your gender? ')
    Que2 = input('What is your name? ')
    Que3 = input('What is your age? ')
    Que4 = input('What is your high? ')
    Que5 = input('What is your color of eyes? ')
    Que6 = input('What is your color of skin? ')
    Que7 = input('What is your color of hair? ')
    Que8 = input('What is your education? ')
    Que9 = input('What is your country? ')

    Charakter1 = Human(Que1,Que2,Que3,Que4,Que5,Que6,Que7,Que8,Que9)

    print('*' * 40)
    if Number < 10:
        print(' ' * 14, f'CHARACTER{Number}')
    if Number >= 10:
        print(' ' * 13, f'CHARACTER{Number}')
    if Number >= 100:
        print(' ' * 12, f'CHARACTER{Number}')
    print('*' * 40)
    print(Charakter1.character())
    print('*' * 40)
    print()

    while True:
        Question = input('''If you want to create new character type "NEXT", but if you want to leave type "STOP": ''')
        Ch1 = ['NEXT','Next','next']
        Ch2 = ['STOP','Stop','stop']
        Ch3 = Ch1 + Ch2
        Ch4 = Question in Ch1
        Ch5 = Question in Ch2
        Ch6 = Question in Ch3
        if Ch4 is True:
            Number += 1
            break
        if Ch5 is True:
            break
        if Ch6 is True:
            continue
    if Ch5 is True:
        break

end = input()