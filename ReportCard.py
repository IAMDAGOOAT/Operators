print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
indonesian = int(input("indonesian :"))
sum = math+english+science+indonesian
print("sum of math, english, science, and indonesian")

perc = (sum/400)*100

print(end='Percentage Mark = ')
print(perc)