import random
import time

class InsertionSort:
    def __init__(self):
        self.comp = 0  # Comparison counter

    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                self.comp += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.comp += 1  # For the last comparison

    def reset(self):
        self.comp = 0

class MergeSort:
    def __init__(self):
        self.comp = 0  # Comparison counter

    def sort(self, arr):
        self._merge_sort(arr, 0, len(arr) - 1)

    def _merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        left_sub = arr[left:mid + 1]
        right_sub = arr[mid + 1:right + 1]
        i, j, k = 0, 0, left
        
        while i < len(left_sub) and j < len(right_sub):
            self.comp += 1
            if left_sub[i] <= right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            k += 1

        while i < len(left_sub):
            arr[k] = left_sub[i]
            i += 1
            k += 1

        while j < len(right_sub):
            arr[k] = right_sub[j]
            j += 1
            k += 1

    def reset(self):
        self.comp = 0

class HybridSort(MergeSort):
    def __init__(self, threshold):
        super().__init__()
        self.threshold = threshold

    def _merge_sort(self, arr, left, right):
        if right - left + 1 <= self.threshold:
            insertion_sort = InsertionSort()
            insertion_sort.sort(arr[left:right + 1])
            self.comp += insertion_sort.comp
        else:
            super()._merge_sort(arr, left, right)

def generate_data(size):
    return [random.randint(1, 10000) for _ in range(size)]

def analyze_algorithms(size, threshold):
    insertion_sort = InsertionSort()
    merge_sort = MergeSort()
    hybrid_sort = HybridSort(threshold)

    data = generate_data(size)

    # Analyze Insertion Sort
    insertion_sort.reset()
    start_time = time.time()
    insertion_sort.sort(data.copy())
    insertion_time = time.time() - start_time
    insertion_comparisons = insertion_sort.comp

    # Analyze Merge Sort
    merge_sort.reset()
    start_time = time.time()
    merge_sort.sort(data.copy())
    merge_time = time.time() - start_time
    merge_comparisons = merge_sort.comp

    # Analyze Hybrid Sort
    hybrid_sort.reset()
    start_time = time.time()
    hybrid_sort.sort(data.copy())
    hybrid_time = time.time() - start_time
    hybrid_comparisons = hybrid_sort.comp

    return {
        "insertion": (insertion_comparisons, insertion_time),
        "merge": (merge_comparisons, merge_time),
        "hybrid": (hybrid_comparisons, hybrid_time)
    }
