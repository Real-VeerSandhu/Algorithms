def bubble_sort(x):
    """Bubble Sort"""

    n = len(x)

    for i in range(n-1):
        for j in range (0, n - i - 1):
            if (x[j] > x[j + 1]):
                x[j], x[j + 1] = x[j + 1], x[j]
    
    return x



