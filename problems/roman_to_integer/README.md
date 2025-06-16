# 13. Roman to Integer

## Đề bài

Chuyển đổi một số La Mã (chuỗi) thành số nguyên.

**Ví dụ:**
- Input: `"III"` → Output: `3`
- Input: `"IV"` → Output: `4`
- Input: `"IX"` → Output: `9`
- Input: `"LVIII"` → Output: `58`
- Input: `"MCMXCIV"` → Output: `1994`

## Lời giải

- Mỗi ký tự trong số La Mã có giá trị riêng.
- Nếu một ký tự nhỏ hơn ký tự bên trái nó, thì giá trị đó bị trừ đi (ví dụ: `IV = 5 - 1 = 4`).
- Duyệt chuỗi từ phải sang trái, cộng hoặc trừ giá trị từng ký tự dựa trên giá trị ký tự trước đó.

### Code Python

```python
def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev = 0
    for c in reversed(s):
        value = roman[c]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total
```

### Giải thích

- Tạo một dictionary ánh xạ ký tự La Mã sang số nguyên.
- Duyệt chuỗi từ phải sang trái.
- Nếu giá trị hiện tại nhỏ hơn giá trị trước đó (`prev`), thì trừ, ngược lại thì cộng.
- Độ phức tạp: **O(n)** với n là độ dài chuỗi.

---
