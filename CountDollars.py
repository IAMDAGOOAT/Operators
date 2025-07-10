Amount = int(input("Please Enter the Amount For Windrawl in Dollars: $"))

note_100 = Amount // 100
note_50 = (Amount % 100) // 50
note_10 = ((Amount % 100)% 50) // 10

print("number of $100 bills:", note_100)
print("number of $50 bills:", note_50)
print("number of $10 bills:", note_10)
