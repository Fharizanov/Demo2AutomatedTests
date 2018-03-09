'''
my_list = [1,5,10]
my_list.reverse()

my_list1 = my_list[:]
my_list.append(11)

print(my_list1)
print(my_list)

odd_list = []
even_list = []
a = 1
while True:
    a = int(input())
    if a == 0:
        break
    elif a % 2 == 1:
        odd_list.append(a)
    elif a % 2 == 0:
        even_list.append(a)
print("Odd: " + str(odd_list))
print("Even: " + str(even_list))

print("Odd sum: " + str(sum(odd_list)))
print("Even sum : " + str(sum(even_list)))
'''