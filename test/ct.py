def solution(nums):

    
    i = 0
    answer = 0

    for num in nums:
        if answer < 4:
            i = i + num
            answer = answer + 1
        else:
            return answer

    print(answer)

nums = [1, 2, 7, 6, 4]
solution(nums)