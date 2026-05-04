def reverseString(s:str):
    rev = ""
    for i in s:
        rev = i + rev
    return rev
print(reverseString("Lokesh"))

def palindrome(s:str):
    s = "".join(char.lower() for char in s if char.isalnum())
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
print(palindrome("Lokesh"))
print(palindrome("Madam"))

def isAnagram(s: str, t: str) -> bool:
    s = s.replace(" ", "").strip()
    t = t.replace(" ", "").strip()
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True
print(isAnagram("silent","listen"))
print(isAnagram("lokesh","mahesh"))

def vowelConsonantCount(s):
    vowels = "aeiou"
    v_count , c_count = 0 , 0
    s = "".join(char.lower() for char in s if char.isalpha())
    for i in s:
        if i in vowels:
            v_count +=1
        else:
            c_count +=1
    return v_count , c_count
print(vowelConsonantCount("Lokesh"))

def characterFrequency(s):
    s = s.lower()
    count_dict = {char:s.count(char) for char in s}
    return count_dict
print(characterFrequency("Programming"))