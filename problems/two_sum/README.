# Two Sum

## Đề bài

Cho một mảng số nguyên `nums` và một số nguyên `target`, hãy tìm hai số trong mảng sao cho tổng của chúng bằng `target`. Trả về chỉ số của hai số đó.

**Ví dụ:**

- Input: `nums = [2, 7, 11, 15]`, `target = 9`
- Output: `[0, 1]`

## Lời giải

Duyệt từng phần tử, dùng một dictionary để lưu các số đã duyệt và vị trí của chúng. Với mỗi số, kiểm tra xem `target - num` đã gặp chưa. Nếu có, trả về chỉ số hai số đó.

### Code Python

```python
def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []
```

### Giải thích

- Sử dụng dictionary (`lookup`) để tra cứu số còn thiếu một cách nhanh chóng.
- Khi lặp qua từng số, nếu số còn thiếu đã xuất hiện, trả về chỉ số.
- Độ phức tạp thời gian: O(n).

---
