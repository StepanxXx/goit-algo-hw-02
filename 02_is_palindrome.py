from collections import deque

def is_palindrome(s: str) -> bool:
    queue = deque(s.lower().strip().replace(" ", ""))
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True 

if __name__ == "__main__":
    print(is_palindrome("racecar")) # True
    print(is_palindrome("hello")) # False
    print(is_palindrome("madam")) # True 
    print(is_palindrome("step on no pets")) # True
    print(is_palindrome(" Was  it a car rac  a tI saw")) # True
    
