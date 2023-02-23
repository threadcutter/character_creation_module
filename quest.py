# Импортируйте datetime. 
import datetime as dt
# Импортируйте time.
from datetime import time


class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        # Допишите два свойства класса.
        self.start_time = None
        self.end_time = None
    
    # Напишите методы приема и сдачи квеста.
    
    def accept_quest(self):
        start_time = dt.now()
        if end_time != None:
            print('С этим испытанием вы уже справились.')
        return f'Начало {self.name} положено.'
        
    def pass_quest(self):
        start_time = None
        if start_time == None:
            return print('Нельзя завершить то, что не имеет начала!')
        

quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())