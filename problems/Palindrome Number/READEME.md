# 9. Palindrome Number

## Đề bài

Kiểm tra một số nguyên `x` có phải là số Palindrome không (nghĩa là đọc xuôi hay ngược đều giống nhau).

**Ví dụ:**
- Input: `121` → Output: `True`
- Input: `-121` → Output: `False`
- Input: `10` → Output: `False`

## Lời giải

- Số âm **không** phải là Palindrome.
- Số có số 0 ở cuối (trừ số 0) cũng **không** phải.
- Đảo ngược một nửa số nguyên và so sánh với nửa còn lại.
- Nếu số lượng chữ số là lẻ, bỏ qua chữ số giữa.

### Code Python

```python
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    return x == reverted or x == reverted // 10
```

### Giải thích

- Đảo ngược nửa sau của số (ví dụ với 1221 sẽ thành 12 và 12).
- Nếu số có lẻ chữ số (ví dụ 12321), bỏ qua chữ số giữa so sánh `x == reverted // 10`.
- Độ phức tạp thời gian: **O(log₁₀ n)** vì chỉ xét một nửa số chữ số.

---
