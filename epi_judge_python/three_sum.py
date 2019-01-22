from test_framework import generic_test


def has_three_sum(A, t):
    # TODO - you fill in here.
    A.sort()
    for i in range(len(A)):
        j, k = i, len(A) - 1
        while j <= k:
            sum2 = A[j] + A[k]
            if sum2 == t - A[i]:
                return True
            elif sum2 > t - A[i]:
                k -= 1
            else:
                j += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
