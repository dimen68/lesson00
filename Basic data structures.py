# Средний балл
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_abc = sorted(students_list)
average_grades = list(map(lambda x:sum(x)/len(x),grades))
average_score = dict(zip(students_abc,average_grades))
print('Средний балл студентов: \n',average_score)