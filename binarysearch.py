def locate_number(list1,querry):
    first_index = 0
    last_index = len(list1)-1
    while first_index <= last_index:
        mid_index = (first_index +last_index) //2
        mid_number = list1[mid_index]
        print('low: ', first_index, 'high: ', last_index, 'mid:', mid_index, 'mid_number: ', mid_number)
        if mid_number == querry:
           return mid_index
        elif mid_number < querry:
            last_index = mid_index -1
        elif mid_number > querry:
            first_index = mid_index +1

    return 'number not in the list'



list1=[10,9,7,6,5,4,3,2,1]
querry = 3
querry_index= locate_number(list1,querry)
print(f'index of number {querry} in the list is {querry_index} ')

#tests
test1 = {'input':{'list1':list1,'querry': 7},'output':2}
querry_index1 =locate_number(test1['input']['list1'],test1['input']['querry'])
if querry_index1 == test1['output']:
    print('TEST1 PASSED')
else:
    print('TEST1 FAILED')

test2 = {'input':{'list1':list1,'querry': 2},'output':7}
querry_index2=locate_number(test2['input']['list1'],test2['input']['querry'])
if querry_index2 == test2['output']:
    print('TEST2 PASSED')
else:
    print('TEST2 FAILED')
