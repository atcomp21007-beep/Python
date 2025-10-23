marks = (60, 70, 80, 90, 100, 110)
print(marks)
print(marks[3])
print(marks[-2])

n = (10,20,30,40,50,60,70,80,90)
print(n[2:5])
print(n[::-2])

colors = ("red", "green", "blue")
colorl = list(colors)
colorl[1] = "yellow"
colors = tuple(colorl)
print(colors)  

t1 =(1,2,3)
t2 =(4,5,6)
t3 =(t1 + t2)
print(f"T1:{t1},\nT2:{t2},\nT3:{t3}")

print(t1 * int(input("Enter a number:")))