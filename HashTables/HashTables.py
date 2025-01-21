from operator import index


class HashTables:
    def __init__(self, size):
        self.data = [0] * size

    def hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)

        return hash

    def set(self, key, value):
        address = self.hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        hash_table_index = self.hash(key)
        current_bucket = self.data[hash_table_index]
        if current_bucket:      # if a bucket exists, retrieve its value
            for i in range(0, len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]

        return None

    def retrieve_keys(self):
        keysArray = []
        for i in range(0, len(self.data)): # iterate through the hash tables
            if self.data[i]:
                array_of_buckets = len(self.data[i])
                if array_of_buckets > 1:                    # check if the length of array in this index more than 1
                    for j in range(0, array_of_buckets):        # iterate through this array and get the key of bucket
                        keysArray.append(self.data[i][j][0])
                else:                                       # if single bucket in an array just get its key
                    keysArray.append(self.data[i][0][0])
        return keysArray

#### Testing
# ht = HashTables(2)
# ht.set("grapes", 10000)
# ht.set("apples", 123132)
# # ht.set("apples", 12300)
# print(ht.data)
# print(ht.retrieve_keys())

#### Simple questions
# def first_recurring_character(arr):
#     hash_table = []
#     for i in range(0, len(arr)):
#         if arr[i] in hash_table:
#             return arr[i]
#         hash_table.append(arr[i])
#     return None
#
# print(first_recurring_character([2, 3, 4, 5]))
