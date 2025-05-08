class SortingAlgos:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(self.arr)

    def bubble_sort(self):
        for i in range(0, self.n):
            for j in range(i, self.n):
                if self.arr[j] < self.arr[i]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def optimized_bubble_sort(self):
        for i in range(self.n):
            swapped = False
            for j in range(i, self.n):
                if self.arr[j] < self.arr[i]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    swapped = True

            if not swapped:
                break

    def selection_sort(self):
        for i in range(0, self.n):
            minimum = i
            temp = self.arr[i]
            for j in range(i+1, self.n):
                if self.arr[j] < self.arr[minimum]:
                    minimum = j

            self.arr[i] = self.arr[minimum]
            self.arr[minimum] = temp

    def insertion_sort(self):
        for i in range(1, self.n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def merge_sort(self, arr):
        self.arr = arr
        self.n = len(self.arr)

        if self.n == 0 or self.n == 1:
            return self.arr

        mid = self.n // 2
        left = [self.arr[i] for i in range(0, mid)]
        right = [self.arr[i] for i in range(mid, self.n)]
        #print(f"left: {left}")
        #print(f"right: {right}")

        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def merge(self, left, right):

        i = 0
        j = 0
        k = [] # merge array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                k.append(left[i])
                i += 1
            else:
                k.append(right[j])
                j += 1

        #print(left, right)
        k = k + left[i:] + right[j:]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = right
            partition_index = self.partition(pivot, left, right)

            self.quick_sort(left, partition_index-1)
            self.quick_sort(partition_index+1, right)


    def partition(self, pivot, left, right):
        pivot_value = self.arr[pivot]
        partition_index = left

        for i in range(left, right):
            if self.arr[i] < pivot_value:
                self.swap(i, partition_index)
                partition_index += 1

        self.swap(right, partition_index)
        return partition_index

    def swap(self, first_index, second_index):
        temp = self.arr[first_index]
        self.arr[first_index] = self.arr[second_index]
        self.arr[second_index] = temp


arr = [12, 11, 13, 5, 6, 7]
algo = SortingAlgos(arr)
## for merge sort only
# print(algo.arr)
# result = algo.merge_sort(arr)
# print(result)
print(algo.arr)
algo.quick_sort(0, algo.n - 1)
print(algo.arr)