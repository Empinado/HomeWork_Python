"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной"""

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии для изменения данных\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Сохранить справочник в текстовом формате\n"
        "6. Закончить работу")
    choice = int(input())
    return choice

def show_menu_2() -> int:
    print("\nВыберите необходимое действие:\n"
        "1. Удалить абонента\n"
        "2. Изменить фамилию\n"
        "3. Изменить Имя\n"
        "4. Изменить Номер телефона\n"
        "5. Изменить Описание\n"
        "6. Выйти в главное меню")
    choice = int(input())
    return choice

def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data     


def read_csv(filename: str):
	data = []
	fields = ["Фамилия","Имя","Телефон","Описание"]
	with open(filename, 'r', encoding = 'utf-8') as fin:
		for line in fin:
			record = dict(zip(fields, line.strip().split(',')))
			data.append(record)
	return data

def print_result(data: list):
	for el in data:
		for k, v in el.items():
			print(f'{k}: {v}')
		print()
	input("Для продолжения нажмите клавишу Enter")

def find_abonent_family(data):
	family = input("Введите фамилию абонента: ")
	count = 0
	index = 0
	find_abonent = []
	for el in data:
		if family in el['Фамилия']: #Ищет полное или частичное совпадение
			count += 1
			find_abonent.append(el)
			print(count, "найденный абонент:")
			for k, v in el.items():
				print(f'{k}: {v}')
			print()
	if count > 1:
		index = int(input("Найдено несколько абонентов\n"
						"Если не хотите ничего делать нажмите 0\n "
						"Если хотите изменить абонента, напишите номер найденного: "))
		if index > 0:
			count = 1
			index = index - 1
			print()
	if count == 1:
		choise = 0
		while choise != 6:
			choise = show_menu_2()
			if choise == 1:
				data.remove(find_abonent[index])
				print("Абонент удален\n")
			if choise == 2:
				find_abonent[index]['Фамилия'] = input('Введите новую Фамилию: ')
				print("Изменения приняты\n")
			if choise == 3:
				find_abonent[index]['Имя'] = input('Введите новое Имя: ')
				print("Изменения приняты\n")
			if choise == 4:
				find_abonent[index]['Телефон'] = input('Введите новый Номер телефона: ')
				print("Изменения приняты\n")
			if choise == 5:
				find_abonent[index]['Описание'] = input('Введите новое Описание: ')
				print("Изменения приняты\n")
	if count == 0:
		print('Указанная фамилия не найдена')
		print()
		input('Для продолжения нажмите клавишу Enter')

def find_abonent_number(data):
	"""number = input("Введите телефон абонента: ")
	count = 0
	for el in data:
		if el['Телефон'] == number: 
			count += 1
			for k, v in el.items():
				print(f'{k}: {v}')
			print()"""
	number = input("Введите номер абонента: ")
	count = 0
	find_abonent = []
	for el in data:
		if number in el['Телефон']: #Ищет полное или частичное совпадение
			count += 1
			find_abonent.append(el)
			print("Найденный абонент:")
			for k, v in el.items():
				print(f'{k}: {v}')
			print()		
	if count == 0:
		print('Указанный номер не найден')
		print()
	input('Для продолжения нажмите клавишу Enter')

def add_abonent(data):
	list1 = []
	fields = ["Фамилия","Имя","Телефон","Описание"]
	list1.append(input("Введите Фамилию абонента: "))
	list1.append(input("Введите Имя абонента: "))
	list1.append(input("Введите Телефон абонента: "))
	list1.append(input("Введите Описание абонента: "))
	new_abonent = dict(zip(fields, list1))
	data.append(new_abonent)
	print()
	print("Новый абонент добавлен в список")
	for k, v in new_abonent.items():
		print(f'{k}: {v}')
	print()
	input('Для продолжения нажмите клавишу Enter')

def save_spravochnik(data):
	with open(input("Введите имя файла: "), 'w', encoding = 'utf - 8') as new_file:
		for i in data:
			str_i = ""
			for v in i.values():
				str_i += v + ","
			str_i = str_i[:-1]
			new_file.write(str_i + "\n")
	print("Справочник сохранен")
	input('Для продолжения нажмите клавишу Enter')

spravochnik = read_csv('phonebook.csv')

choise = 0
while choise != 6:
	choise = show_menu()
	if choise == 1:
		print_result(spravochnik)
	if choise == 2:
		find_abonent_family(spravochnik)
	if choise == 3:
		find_abonent_number (spravochnik)
	if choise == 4:
		add_abonent (spravochnik)
	if choise == 5:
		save_spravochnik(spravochnik)