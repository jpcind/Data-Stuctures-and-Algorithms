class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_items(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys





def item_in_common_forloop(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common_dict(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


def main():
    # list1 = [1, 3, 5]
    # list2 = [2, 4, 5]
    # print("Using a dictionary: {}".format(item_in_common_dict(list1, list2)))
    # print("Using a nested forloop: {}".format(item_in_common_forloop(list1, list2)))

    food = {"eggs": 3.99, "chicken": 11.99}
    print(food["eggs"])


    food = HashTable()
    food.set_items("eggs", 3.99)
    food.set_items("chicken", 11.99)
    print(food.get_item("eggs"))


    # food.set_items("milk", 4.99)
    # food.set_items("bread", 4.99)
    # food.set_items("cereal", 4.50)
    #
    # # food.print_table()



if __name__ == '__main__':
    main()
