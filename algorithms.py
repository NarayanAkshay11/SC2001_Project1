import random
import time
import matplotlib.pyplot as plt

def mergesort(arr):
    comparisons = [0]
    
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, comparisons[0]

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr, comparisons

def hybrid_sort(arr, threshold):
    comparisons = [0]
    
    def insertion_sort(arr, start, end):
        for i in range(start + 1, end + 1):
            key = arr[i]
            j = i - 1
            while j >= start and arr[j] > key:
                comparisons[0] += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(arr, start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i, j, k = 0, 0, start
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def sort(arr, start, end):
        if end - start + 1 <= threshold:
            insertion_sort(arr, start, end)
        else:
            mid = (start + end) // 2
            sort(arr, start, mid)
            sort(arr, mid + 1, end)
            merge(arr, start, mid, end)

    sort(arr, 0, len(arr) - 1)
    return arr, comparisons[0]

def generate_data(size):
    return [random.randint(1, size) for _ in range(size)]

def run_experiment(sizes, threshold):
    mergesort_comparisons = []
    insertion_sort_comparisons = []
    hybrid_sort_comparisons = []
    time_taken_mergesort = []
    time_taken_insertion = []
    time_taken_hybrid = []

    for size in sizes:
        data = generate_data(size)
        
        start_time = time.time()
        _, m_comparisons = mergesort(data.copy())
        time_taken_mergesort.append(time.time() - start_time)
        mergesort_comparisons.append(m_comparisons)
        
        start_time = time.time()
        _, i_comparisons = insertion_sort(data.copy())
        time_taken_insertion.append(time.time() - start_time)
        insertion_sort_comparisons.append(i_comparisons)
        
        start_time = time.time()
        _, h_comparisons = hybrid_sort(data.copy(), threshold)
        time_taken_hybrid.append(time.time() - start_time)
        hybrid_sort_comparisons.append(h_comparisons)

    return (mergesort_comparisons, insertion_sort_comparisons, hybrid_sort_comparisons,
            time_taken_mergesort, time_taken_insertion, time_taken_hybrid)

def plot_results(sizes, time_taken_mergesort, time_taken_insertion, time_taken_hybrid,
                 mergesort_comparisons, insertion_sort_comparisons, hybrid_sort_comparisons, max_size):
    
    # Plot time taken
    plt.figure(figsize=(12, 7))
    plt.plot(sizes, time_taken_mergesort, label='Mergesort Time', color='#6366f1')
    plt.plot(sizes, time_taken_insertion, label='Insertion Sort Time', color='#ef4444')
    plt.plot(sizes, time_taken_hybrid, label='Hybrid Sort Time', color='#10b981')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Time Comparison')
    plt.legend()
    plt.grid(True)
    plt.xlim(1000, max_size + 500)
    plt.tight_layout()
    plt.savefig('sorting_time_comparison.png')
    plt.show()

    # Plot number of comparisons
    plt.figure(figsize=(12, 7))
    plt.plot(sizes, mergesort_comparisons, label='Mergesort Comparisons', color='#6366f1')
    plt.plot(sizes, insertion_sort_comparisons, label='Insertion Sort Comparisons', color='#ef4444')
    plt.plot(sizes, hybrid_sort_comparisons, label='Hybrid Sort Comparisons', color='#10b981')
    plt.xlabel('Array Size')
    plt.ylabel('Number of Comparisons')
    plt.title('Sorting Algorithm Comparisons')
    plt.legend()
    plt.grid(True)
    plt.xlim(1000, max_size + 500)
    plt.tight_layout()
    plt.savefig('sorting_comparisons.png')
    plt.show()

def analyze_threshold(max_size):
    thresholds = range(10, 71)  # Thresholds from 10 to 70
    time_taken_hybrid = []

    for threshold in thresholds:
        data = generate_data(max_size)
        start_time = time.time()
        hybrid_sort(data.copy(), threshold)
        time_taken_hybrid.append(time.time() - start_time)

    plt.figure(figsize=(12, 7))
    plt.plot(thresholds, time_taken_hybrid, marker='o', color='#10b981')
    plt.xlabel('Threshold Value')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity vs Threshold Value')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('time_complexity_vs_threshold.png')
    plt.show()

if __name__ == "__main__":
    while True:
        max_size = int(input("Enter the maximum array size (1,000 to 10,000,000): "))
        if 1000 <= max_size <= 10000000:
            break
        print("Invalid input. Please enter a number between 1,000 and 10,000,000.")

    sizes = [i for i in range(1000, max_size + 1, 1000)]  # Increment by 1000
    threshold = 16  # You can experiment with different threshold values

    mergesort_comparisons, insertion_sort_comparisons, hybrid_sort_comparisons, \
    time_taken_mergesort, time_taken_insertion, time_taken_hybrid = run_experiment(sizes, threshold)
    
    plot_results(sizes, time_taken_mergesort, time_taken_insertion, time_taken_hybrid,
                 mergesort_comparisons, insertion_sort_comparisons, hybrid_sort_comparisons, max_size)

    # Analyze time complexity vs threshold
    analyze_threshold(max_size)
