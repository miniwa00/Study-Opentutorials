persons = [
    {'name':'jongmin','address':'seoul','interest':'soccer'},
    {'name':'mom','address':'daegu','interest':'book'},
    {'name':'dad','address':'busan','interest':'cycle'}
]

for person in persons:
    for key in person:
        print(key,':',person[key])
    print('------------------------')    