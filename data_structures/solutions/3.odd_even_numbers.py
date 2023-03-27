# max = int(input("Please enter your max number :"))

# odd_numbers = []

# for i in range(max):
#     if i %2 ==1:
#         odd_numbers.append(i)
# print("odd_numbers", odd_numbers)

def odd_even():
    max = int(input("Please enter your max number :"))

    odd_numbers = []

    for i in range(max):
        if i %2 ==1:
            odd_numbers.append(i)
    print("odd_numbers", odd_numbers)

odd_even()