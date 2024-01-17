import copy
subjects = ["a", ["b", "c"], "d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)
subjects[1][1] = "x"
print(subjects, a, b, c, d, e)

# 문자열 immutable, 리스트는 mutable하니까

# number_list = []
# for number in range(1, 6):
#     number_list.append(number)
# print(number_list)
#
# number_list2 = [number for number in range(1, 6)]
# print (number_list2)
#
# squares = list()
# for i in range(1, 6, 1):
#     squares.append(i*i)
# print(squares)

