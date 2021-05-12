# -*- coding: UTF-8 -*-
def search(value, list, bigger, smaller = 0, count = 0):
    middle = (bigger+smaller)//2
    
    if middle%2 == 0:
        
        if bigger-smaller <= 1:
            count+= 1
            return count
        
        elif value == list[middle]:
            count+= 1
            return count
        
        elif value < list[middle]:
            count+= 1
            return search(value, list, middle, smaller, count)
        
        else:
            count+= 1
            smaller = middle + 1
            return search(value, list, bigger, smaller, count)
    
    else:
    
        if bigger-smaller <= 1:
            count+= 1
            return count
    
        elif value == list[middle]:
            count+= 1
            return count
    
        elif value < list[middle]:
            count+= 1
            limit = middle - 1
            return search(value, list, limit, smaller, count)
    
        else:
            count+= 1
            smaller = middle + 1
            return search(value, list, bigger, smaller, count)

search_input = [int(i) for i in input("").split()]
range_list = search_input.pop(0)
main_list = [search_input.pop(0) for e in range(range_list)]
bigger = len(main_list)-1
for test in search_input:
    print(search(test, main_list, bigger), end=' ')