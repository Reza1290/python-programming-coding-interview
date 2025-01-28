

arr = [3,2,-6,4,0]

def solution(A):
    max_ending = 0
    max_slice = A[0]

    for a in A:
        print(max_ending)
        print(max_slice)
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice,max_ending)

    return max_slice


print(solution(arr))