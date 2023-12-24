class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []

        for address in self.data_map:
            if address is not None:
                for item in address:
                    all_keys.append(item[0])

        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()
my_hash_table.set("bolts", 1400)
my_hash_table.set("washers", 50)
my_hash_table.set("lumber", 70)
print(my_hash_table.keys())
# my_hash_table.print_table()
