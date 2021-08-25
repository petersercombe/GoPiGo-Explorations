import random

studentList = ['Anisson',
               'Arran',
               'Noah',
               'Ahmed',
               'Tali',
               'Katrina',
               'Josh',
               'Keilan',
               'Grace',
               'Charlia',
               'Luca',
               'Loki',
               'Solomon',
               'Brodey',
               'Damon',
               'Pheonix',
               'Ben',
               'Ava',
               'Kai',
               'Tully']

while len(studentList) > 3:
    group = []
    for person in range(3):
        select = random.randint(0,len(studentList)-1)
        group.append(studentList[select])
        studentList.pop(select)
    print(group)
print(studentList)