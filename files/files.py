FILES_ONE = 'files/1.txt'
FILES_TWO = 'files/2.txt'
FILES_THREE = 'files/3.txt'
FILES_WORK = 'files/work.txt'

files_one = {}
files_two = {}
files_three = {}

def  files_worker_one(FILES_ONE, mode: str = 'r'):
    with open(FILES_ONE, mode, encoding='UTF-8') as files:
        len = 0
        f = []
        for file in files.read().split('\n'):
            f.append(file)
            len += 1

        files_one[len] = f
    return files_one

def  files_worker_two(FILES_TWO, mode: str = 'r'):
    with open(FILES_TWO, mode, encoding='UTF-8') as files:
        len = 0
        f = []
        for file in files.read().split('\n'):
            f.append(file)
            len += 1

        files_two[len] = f
    return files_two

def  files_worker_three(FILES_THREE, mode: str = 'r'):
    with open(FILES_THREE, mode, encoding='UTF-8') as files:
        len = 0
        f = []
        for file in files.read().split('\n'):
            f.append(file)
            len += 1

        files_three[len] = f
    return files_three

def files_worker(file_name, mode: str = 'r'):
    files_worker_one(FILES_ONE)
    files_worker_two(FILES_TWO)
    files_worker_three(FILES_THREE)
    for number_one in files_one.keys():
        break

    for number_two in files_two.keys():
        break

    for number_three in files_three.keys():
        break

    with open(file_name, mode, encoding='UTF-8') as files:
        if number_three >= number_two and number_three >= number_one:
            if number_one >= number_two:
                string_one = 0
                string_two = 0
                string_three = 0
                for three in files_three.values():
                    for item_three in three:
                        string_three += 1
                        files.write(f'{"Строка номер", string_three, "файла номер 3: ", item_three}\n')
                    break
                for one in files_one.values():
                    for item_one in one:
                        string_one += 1
                        files.write(f'{"Строка номер", string_one, "файла номер 1: ", item_one}\n')
                    break
                for two in files_two.values():
                    for item_two in two:
                        string_two += 1
                        files.write(f'{"Строка номер", string_two, "файла номер 2: ", item_two}\n')
                    break

        else:
            print('Ошибка')

files_worker(FILES_WORK, 'a')
