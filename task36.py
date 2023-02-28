# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Создание пустой таблицы N*Nsource .venv/bin/activate
# N=int(input("Введите число строк "))
# M=int(input("Введите число столюцов "))
# table = [ [0]*M for i in range(N)]
# # Заполнение таблицы рандомными значениями 0 или 1 
# def new_table (table):
#     for i in range(0, len(table)):
#         for i2 in range(0, len(table[i])):
#             table[i][i2]=random.randint(0,1)
#     return 0
# # Вывод таблицы на экран 
# def printed(table):
#     for i in range(0, len(table)):
#         for i2 in range(0, len(table[i])):
#             print(table[i][i2], end=' ')
#         print()
#     return 0 
# # Позиция человека идущего по площадке 
def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [ [0]*num_rows for i in range(num_columns)]
    for i in range(0, len(table)):
        for i2 in range(0, len(table[i])):
            table[i][i2]=(operation(i+1,i2+1))
            print(table[i][i2], end=' ')
        print()
print_operation_table(lambda x,y:x*y)