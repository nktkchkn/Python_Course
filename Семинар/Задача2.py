# Вводятся строки, пока не будет введена пустая строка. Если длина очередного введеного слова равна 5, то
# нужно вывести сообщение "YES" и прекратить возможность ввода для пользователя, если таких слов нет, то
# вывести 'NO' один раз в конце


flag = True 
while True:
    some_str = input()
    # if some_str == '':
    #     break
    if not some_str:
        break
    if len(some_str) == 5:
        print('YES')
        flag = False
        break
if flag == True:
    print ('NO')