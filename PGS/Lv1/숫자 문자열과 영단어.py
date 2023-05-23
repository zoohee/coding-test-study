def solution(s):
    alphabets = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(10):
        s = s.replace(alphabets[i], str(i))
        
    return int(s)