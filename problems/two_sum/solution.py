def twoSum(nums, target):
    """
    Hàm tìm hai số trong mảng `nums` sao cho tổng bằng `target`.
    Trả về chỉ số của hai số đó.
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

# Ví dụ sử dụng:
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # Kết quả: [0, 1]
