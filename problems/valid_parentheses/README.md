# Valid Parentheses

## Đề bài

Cho một chuỗi chỉ gồm các ký tự `'('`, `')'`, `'{'`, `'}'`, `'['`, và `']'`.  
Hãy xác định xem chuỗi đó có phải là một chuỗi ngoặc hợp lệ hay không.

**Một chuỗi ngoặc hợp lệ cần thỏa mãn:**
1. Các ngoặc đóng phải đúng loại với ngoặc mở tương ứng.
2. Các ngoặc đóng phải được đóng theo đúng thứ tự mở.

- Chuỗi rỗng được xem là hợp lệ.

## Ví dụ

| Input      | Output  |
|------------|---------|
| "()"       | True    |
| "()[]{}"   | True    |
| "(]"       | False   |
| "([)]"     | False   |
| "{[]}"     | True    |

---

## Ý tưởng giải

- Sử dụng **stack** để lưu các dấu ngoặc mở.
- Khi gặp dấu ngoặc đóng, kiểm tra xem dấu mở trên cùng của stack có khớp loại không. Nếu không khớp hoặc stack rỗng thì trả về False.
- Duyệt xong, nếu stack rỗng thì hợp lệ, ngược lại thì không hợp lệ.

## Code Python

```python
def isValid(s: str) -> bool:
    stack = []
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
    return not stack
```

## Hướng dẫn sử dụng

- Lưu code vào file `valid_parentheses.py`
- Gọi hàm `isValid(s)` với `s` là chuỗi cần kiểm tra

**Ví dụ:**
```python
print(isValid("()[]{}"))    # True
print(isValid("([)]"))      # False
```
