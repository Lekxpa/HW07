import Actions

def select_an_action():
    data = int(input('\nВыберите действие: \
        \n1. Добавить данные в справочник\
        \n2. Просмотр телефонной книги\
        \n3. Поиск данных\
        \n \
        \nУкажите цифру, соответствующую выбранному действию: \
            \n'))
    if data == 1:
        Actions.Actions.add()
    elif data == 2:
        Actions.Actions.show()
    elif data == 3:
        Actions.Actions.search()
    else:
        print('Неверно выбрано действие. Попробуйте еще раз!')