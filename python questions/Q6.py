lst= []
num=int(input('No of elements: '))
for n in range(num):
    numbers= int(input('Enter numbers') )
    lst.append(numbers)
    set_res= set(lst)
    list_res= (list(set_res))
    for item in list_res:
        print(item)
