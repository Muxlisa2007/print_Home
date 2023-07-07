a = int(input("Kiriting: "))
b = int(input("Kiriting: "))
c = int(input("Kiriting: "))

if a>b and c>a or a<b and c<a :
    print("Natija = ",a)
elif b<a and c<b or b>a and c>b:
    print("natija = ",b)
else:
    print("Natija = ",c)
