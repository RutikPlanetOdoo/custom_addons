def list_compare(l1,l2):
    for num1 in l1:
        if num1 in l2:
            return True
        else:
            return False


first = input('Enter the 1st string: ')
second = input('Enter the 2nd string: ')

split_first_list = first.split(' ')
split_second_list = second.split(' ')

if list_compare(split_first_list,split_second_list):
    for i in split_first_list:
        split_second_list.remove(i)
    print(split_second_list)
else:
    print('There is no simpilar words')

# print(type(split_first_list),type(split_second_list))

