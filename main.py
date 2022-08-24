import module1

answer = 0
while True:
    answer = int(input('\nВыберите меню:\n'
          '1 - Считать имена и фамилии\n'
          '2 - Считать все емайлы\n'
          '3 - Считать названия файлов\n'
          '4 - Считать цвета\n'
          '5 - Выход\n'
          'Выберать №: '))

    if answer == 1:
        module1.read_names()

    if answer == 2:
          module1.read_emails()

    if answer == 3:
          module1.read_names_of_files()

    if answer == 4:
        module1.read_codes_of_colors()

    if answer == 5:
           print(f'bye...')
           break