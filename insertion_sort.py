def insertion_sort_joey(my_list):
    for i in range(len(my_list)-1):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j] and j > -1:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
                j = j - 1
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


def main():

    list1 = [89, 4, 76, 12, 54, 903]
    print(insertion_sort_joey(list1))


if __name__ == '__main__':
    main()
