def bubble_sort_joey(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def main():
    my_list = [5, 3, 6, 7, 5, 3, 1, 9]
    list2 = [2, 7, 5, 9, 2, 3, 6, 45, 4, -2, 8, 0, -6, 1, 2, 859]
    print(bubble_sort_joey(list2))
    print(bubble_sort(list2))

if __name__ == '__main__':
    main()
