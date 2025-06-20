def isValid(s: str) -> bool:
    stack = []
    # Ánh xạ dấu đóng với dấu mở tương ứng
    mapping = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if mapping[c] != top:
                return False
    # Nếu stack rỗng sau khi duyệt hết, chuỗi hợp lệ
    return not stack
