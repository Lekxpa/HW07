
contatc = []

class Actions:

    def add():
        Name = input('Введите ФИО:')
        contatc.append(Name)
        Phone = input('Введите номер телефона: ')
        contatc.append(Phone)
        City = input('Введите название населенного пункта: ')
        contatc.append(City)
        with open('Phonebook.txt', 'a', encoding = 'utf-8') as file:
            file.write(f'\n{Name};{Phone};{City};')
        file.close()

    def show():
        f = open('Phonebook.txt','r', encoding='utf-8')
        ls = f.read()
        print(f'{ls}\n')

    def search():
        f = open('Phonebook.txt','r', encoding='utf-8')
        lst = f.read()
        ls = lst.split(';')
        t = input('Введите значение, которое необходимо найти: \n')
        for i in range(0, len(ls)-1, 3):
            line = ls[i] + '  ' + ls[i+1] + '  ' + ls[i+2]
            if t in line:
                print('\nНайдена запись в телефонной книге: \n ' + line + '\n')
                break
        else:
            print('\nУказанного значения в телефонной книге нет. \n'
            + 'Попробуйте еще раз! \n')