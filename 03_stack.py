from functools import wraps

def print_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{args[0]}: {'Симетрично' if result else 'Несиметрично'}"
    return wrapper

@print_result
def is_symmetric(s: str) -> bool:
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    print(is_symmetric("( ) { [ ] ( ) ( ) { } } }"))
    print(is_symmetric("( 23 ( 2 - 3);"))
    print(is_symmetric("( 11 }"))
