
Arr = [3,4,3,2,3,-1,3,3]

def solution(A):

    size = 0
    value = None

    for element in A:
        if size == 0:
            size+=1
            value = element
        elif value == element:
            size+=1
        else:
            size-=1
    
    candidate = -1 if size == 0 else value
    candidate_index = -1
    count = 0

    for index, value in enumerate(A):
        if value == candidate:
            count+=1
            if candidate_index == -1:
                candidate_index = index
            # candidate_index = index
    
    if count > len(A) // 2:
        return candidate_index
    else:
        return -1
    
print(solution(Arr))