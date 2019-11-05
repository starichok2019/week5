import os
import sys
import shutil
from os import listdir
from os.path import isfile, join



while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. посмотреть информацию об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10 мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_folder = input ("Введите название папки: ")
        os.mkdir(name_folder)
    elif choice == '2':
        remove_folder = input("Введите название удаляемой файла/папки: ")
        shutil.rmtree(remove_folder)
        os.unlink(remove_folder)

    elif choice == '3':
        path = os.getcwd()
        folder_name = input("Введите имя копируемой папки:")
        copy_folder_name = input("Введите название новой папки: ")
        if os.path.isdir(folder_name): # копирует только если это папка (вместе с содержимым)
            shutil.copytree(join(path, folder_name), join(path,copy_folder_name))
        else:
            shutil.copy(folder_name, copy_folder_name)

    elif choice == '4':
        path = input("Введите путь для проверки содержимого дитектории( если текущей, то введите ""this"": ")
        if path == 'this' :
            path = os.getcwd()
        print(os.listdir(path))

    elif choice == '5':
        path = input("Введите путь для поиска папок:")
        d = '.'
        folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
        print(folders)


    elif choice == '6':
        path = input("Введите путь для поиска файлов:")
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        print(*onlyfiles)

    elif choice == '7':
        print (sys.platform)

    elif choice == '8':
        print("Создатель программы: Борис Шустров")

    elif choice == '9':
         get_random_famous_person()

    elif choice == '10':
         use_funnctions()

    elif choice == '11':
          path = input("Введите директорию:")
          s.chdir(path)
    elif choice == '12':
          break

    else:
        print('Неверный пункт меню! ')




