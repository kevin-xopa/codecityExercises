"""
    Task description
    An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

    Your goal is to find that missing element.

    Write a function:

    def solution(A)

    that, given an array A, returns the value of the missing element.

    For example, given array A such that:

    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5
    the function should return 4, as it is the missing element.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [0..100,000];
    the elements of A are all distinct;
    each element of array A is an integer within the range [1..(N + 1)].
"""


def solution(A):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                intercambio = True

    lost = 0
    n = A[0]
    for i in A:
        if n != i:
            lost = n
            break
        n += 1
    return lost


if __name__ == "__main__":
    lista = [1, 8, 4, 5, 6, 7, 3, 10]
    print(str(solution(lista)))
