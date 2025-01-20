import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#################### HARDER WITHOUT with for

# password = ""
#  jeste zjednodusim viz 2
# for char in range(1, nr_letters + 1 ):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1 ):
#     password += random.choice(letters)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(letters)

#####################################2
password_list = []

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)




########## EASY VERSIOn WITH RANDOM FUNCTION
# fin_num_lett = random.sample(letters, nr_letters)
# fin_num_num = random.sample(numbers, nr_numbers)
# fin_num_sym = random.sample(symbols, nr_symbols)
#
# in_order = fin_num_lett + fin_num_num + fin_num_sym
# ran_order = random.sample(in_order,len(in_order))
#
# print(in_order)
# print(ran_order)
#
# # print(fin_num_lett + fin_num_sym + nr_symbols)







