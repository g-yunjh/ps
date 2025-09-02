def solution(num_list, n):
    answer = []
    
    # solution
    answer = num_list[n:] + num_list[0:n]

    return answer