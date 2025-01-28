

Arr = [4,3,4,1,2,2]

def solution(A):
    size = 0
    candidate = None

    for i in A:
        if size == 0:
            candidate = i
            size+=1
        elif i == candidate:
            size+=1
        else:
            size-=1
    
    count = A.count(candidate)

    leader = candidate

    equi_leader = 0
    left_count = 0
    total_count = count
    n = len(A)

    for i in range(n):
        if A[i] == leader:
            left_count+=1
        right_count = total_count - left_count

        if (left_count > (i + 1) //2) and (right_count > (n - i - 1)//2):
            equi_leader+=1
        
    return equi_leader

print(solution(Arr))