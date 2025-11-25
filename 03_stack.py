from functools import wraps


def format_symmetric_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{args[0]}: {'Симетрично' if result else 'Несиметрично'}"
    return wrapper


@format_symmetric_result
def is_symmetric(s: str) -> bool:
    stack = []
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    opening_brackets = set(bracket_map.values())
    closing_brackets = set(bracket_map.keys())

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    print(is_symmetric("( ) { [ ] ( ) ( ) { } }")) # Симетрично
    print(is_symmetric("( 23 ( 2 - 3);")) # Несиметрично
    print(is_symmetric("( 11 }")) # Несиметрично
    print(is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}")) # Симетрично
    print(is_symmetric("( 23 ( 2 - 3);")) # Несиметрично
    print(is_symmetric("( 11 }")) # Несиметрично
