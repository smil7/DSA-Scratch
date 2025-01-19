class Arrays:
    def __init__(self):
        self.length = 0
        self.array = {}

    def append(self, element):
        self.array[self.length] = element
        self.length += 1
        print("Array: ", self.array)

    def pop(self):
        if self.length <= 0:
            raise IndexError("The Array is empty")
        last_item = self.array[self.length-1]
        del self.array[self.length-1]
        self.length -= 1
        return last_item

    def lookup(self, index):
        if index >= self.length:
            raise IndexError("Array index out of range")
        return self.array[index]

    def get_length(self):
        return self.length

    def insert(self, element, index):
        if self.length > 0:
            for i in range(self.length, index, -1):
                self.array[i] = self.array[i-1]
        if self.length <= 0 < index:
            index = 0
        self.array[index] = element
        self.length += 1
        print("Array: ", self.array)

    def remove(self, element):
        if self.length <= 0:
            return "The Array is empty!!!"
        index = self.get_index_of(element)
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        del self.array[self.length-1]
        self.length -= 1
        print("Array: ", self.array)

    def get_index_of(self, element):
        index = -1
        for i in range(self.length - 1):
            if self.array[i] == element:
                index = i
                break
        if index == -1:
            raise ValueError("Value not found")
        return index

#### Testing
# arr1 = Arrays()
# print("Length of the array: ", arr1.get_length())
# arr1.push(1)
# arr1.push(2)
# arr1.push(3)
# print(arr1.lookup(1))
# print("Length of the array: ", arr1.get_length())
# arr1.insert(4, 1)
# print("Length of the array: ", arr1.get_length())
# arr1.remove(1)
# print("Length of the array: ", arr1.get_length())

##### Simple questions
# def reverse_str(var):
#     if type(var) is not 'str' or len(var) < 2:
#         return "Check the variable!"
#
#     length = len(var)
#     reversed_str = ""
#     for i in range(len(var)-1, -1, -1):
#         reversed_str += var[i]
#     return reversed_str
# print(reverse_str("osamaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

# def merge_sorted_array(arr1, arr2):
#     merged_array = []
#     i = 0
#     j = 0
#     n1 = len(arr1)
#     n2 = len(arr2)
#
#     while i < n1 and j < n2:
#
#         if arr1[i] < arr2[j]:
#             merged_array.append(arr1[i])
#             i += 1
#         else:
#             merged_array.append(arr2[j])
#             j += 1
#
#     while i < n1:
#         merged_array.append(arr1[i])
#         i += 1
#
#     while j < n2:
#         merged_array.append(arr2[j])
#         j += 1
#
#     return merged_array
#
# merged_array = merge_sorted_array([0, 3, 4, 31], [4, 6, 30])
# print(merged_array)
