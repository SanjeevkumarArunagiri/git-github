def twosum(input_user1, input_target):
    required = {}
    for i in range(len(input_user1)):
        if input_target - input_user1[i] in required:
            return  [required[input_target - input_user1[i]],i]
        else:
            required[input_user1[i]] = i


list = [12,21,3,4,5]
print(twosum(list, 9))
