t1 = (5)
print(type(t1))
t2 = 5,
print(type(t2))
t3 = (5, )
print(type(t3))
t6 = "python", 'kim'  # packing
print(type(t6), t6[1])
subject, prof = t6  # unpacking
# a, b, c = t6  # ValueError: not enough to unpack
print(prof)
print(subject)
t7 = ()
t8 = tuple()
print(type(t7), type(t8), type(9,), type((9,)))

t9 = 1, 2, 3
t10 = 1, 2, 3, 1
print(t9 == t10)
print(t9 <= t10)