
arr = [23171, 21011, 21123, 21366, 21013, 21367]

def solution(A):

    buy = 200000 # maks value in index
    profit = 0

    for i in A:
        print(buy)
        print(profit)
        buy = min(i, buy)
        profit = max(profit, i - buy)
    
    return profit

print(solution(arr))