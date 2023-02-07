def countStrings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    def backtrack(n, curr_str):
        nonlocal count
        if len(curr_str) == n:
            count += 1
            return
        for vowel in vowels:
            if not curr_str or vowel >= curr_str[-1]:
                backtrack(n, curr_str + vowel)
                
    backtrack(n, '')
    return count

print(countStrings(1))
print(countStrings(2))
print(countStrings(3))