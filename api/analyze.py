from flask import Flask, request, jsonify
import random

app = Flask(__name__)

class InsertionSort:
    def insertion_sort(self, arr):
        comparisons = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                comparisons += 1
            arr[j + 1] = key
            comparisons += 1  # For the last comparison where the while condition fails
        return comparisons

class MergeSort:
    def merge_sort(self, arr):
        comparisons = 0
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            comparisons += self.merge_sort(left_half)
            comparisons += self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
                comparisons += 1  # Count the comparison

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return comparisons

class HybridSort(MergeSort):
    def __init__(self, threshold):
        self.threshold = threshold

    def hybrid_sort(self, arr):
        if len(arr) <= self.threshold:
            insertion_sort = InsertionSort()
            return insertion_sort.insertion_sort(arr)
        else:
            return self.merge_sort(arr)

@app.route('/api/analyze', methods=['GET'])
def analyze():
    size = int(request.args.get('size'))
    arr = [random.randint(0, 10000) for _ in range(size)]

    insertion_sort = InsertionSort()
    merge_sort = MergeSort()
    hybrid_sort = HybridSort(threshold=10)  # Example threshold for hybrid sort

    insertion_comparisons = insertion_sort.insertion_sort(arr.copy())
    merge_comparisons = merge_sort.merge_sort(arr.copy())
    hybrid_comparisons = hybrid_sort.hybrid_sort(arr.copy())

    return jsonify({
        'sizes': [size],
        'insertion': [insertion_comparisons],
        'merge': [merge_comparisons],
        'hybrid': [hybrid_comparisons],
    })

if __name__ == '__main__':
    app.run(debug=True)
