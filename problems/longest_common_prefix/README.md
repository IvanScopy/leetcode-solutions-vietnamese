# 14. Longest Common Prefix

## Đề bài

Viết hàm tìm tiền tố chung dài nhất giữa các chuỗi trong mảng `strs`.

Nếu không có tiền tố chung, trả về chuỗi rỗng `""`.

### Ví dụ

- **Input:** `["flower","flow","flight"]`
- **Output:** `"fl"`

- **Input:** `["dog","racecar","car"]`
- **Output:** `""`
- **Giải thích:** Không có tiền tố chung nào giữa 3 chuỗi.

## Lời giải

- Chọn chuỗi đầu tiên làm tiền tố chung tạm thời (`prefix`).
- So sánh lần lượt với từng chuỗi còn lại:
  - Nếu chuỗi hiện tại không bắt đầu bằng `prefix`, cắt bớt ký tự cuối của `prefix` cho đến khi phù hợp hoặc rỗng.
- Nếu cắt hết mà vẫn không khớp, trả về chuỗi rỗng.

### Code Python

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

### Giải thích

- Sử dụng hàm `startswith` để kiểm tra một chuỗi có bắt đầu bằng tiền tố không.
- Độ phức tạp thời gian: **O(S)** với S là tổng số ký tự trong tất cả các chuỗi.

---
