even = [number for number in range(10) if number % 2 == 0]
print(even)
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get"),
    ("fope", "turn"),
    ("fa", "get"),
    ("fudge", "call"),
    ("fat", "pet"),
    ("fog", "walk"),
    ("fun", "say"),
]
start2 = "Someone better"

start1_caps = " ".join([word.capitalize() + "!" for word in start1])
for fisrt, second in rhymes:
    print(f"{start1_caps} {fisrt.capitalize()}!")
    print(f"{start2} {second}.")

print(start1_caps)