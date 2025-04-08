def vowelsCounter(s: str) -> int:
    # if s is an empty string, return 0, because is not possible to count any vowel
    if not s:
        return 0
    # if the first chat of the string s is a vowel, we count a vowel, so add 1 and call vowelCOunter to check the next char of the string s recursevely
    if s[0].lower() in["a", "e", "i", "o", "u"]:
    
        return 1 + vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])
    
print(vowelsCounter("ciao"))
