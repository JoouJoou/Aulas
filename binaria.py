def search(main_list, number, count = 0):
    if len(main_list) == 1:
        count += 1
        return count
    elif len(main_list)%2 == 0:
        list_size = len(main_list)
        middle_slice = int(list_size/2)
        list_left = main_list[:middle_slice]
        list_right = main_list[middle_slice:]
        middle_number = list_left[-1]
        if middle_number == number:
            count += 1
            return count
        elif middle_number < number:
            count += 1
            return search(list_right, number, count)
        else:
            count += 1
            return search(list_left, number, count)
    else:
        list_size = len(main_list)
        middle_slice = int(list_size/2)
        list_left = main_list[:middle_slice]
        list_right = main_list[middle_slice+1:]
        middle_number = main_list[middle_slice]
        if middle_number == number:
            count += 1
            return count
        elif middle_number < number:
            count += 1
            return search(list_right, number, count)
        else:
            count += 1
            return search(list_left, number, count)

search_input = [int(i) for i in input("").split()]
range_list = search_input.pop(0)
main_list = [search_input.pop(0) for e in range(range_list)]
for test in search_input:
    print(search(main_list, test), end=' ')