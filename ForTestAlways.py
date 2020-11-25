def subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    i = 0
    j = 0

    while i<m and j<n:
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return j == m


print("Yes, its a subsequence ") if subsequence("gksrek","gksrekjdkakl") else print("NO, Not a subsequence")