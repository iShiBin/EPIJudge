from test_framework import generic_test


def search_first_of_k(A, k):
    # TODO - you fill in here.
    low, high, index = 0, len(A) -1, -1
    while low <= high:
        mid = low + (high-low) // 2
        if A[mid] == k:
            index = mid
            high = mid - 1
        elif A[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
        
    return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
