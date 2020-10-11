x = [1,6,8,1,2,1,5,6]
a = int(input("Enter a number: "))
count = len([i for i in x if i == a])
print(f'{a} appears {count} times in list')