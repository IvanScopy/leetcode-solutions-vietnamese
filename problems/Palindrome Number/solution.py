def isPalindrome(x):
    """
    Kiểm tra số nguyên x có phải là số Palindrome (đọc xuôi hay ngược đều như nhau) không.
    Trả về True nếu là Palindrome, ngược lại trả về False.
    """
    # Số âm không phải là Palindrome, số có số 0 ở cuối (trừ 0) cũng không phải
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    # Nếu số lượng chữ số lẻ, bỏ qua chữ số ở giữa bằng reverted//10
    return x == reverted or x == reverted // 10

# Ví dụ sử dụng:
if __name__ == "__main__":
    print(isPalindrome(121))   # True
    print(isPalindrome(-121))  # False
    print(isPalindrome(10))    # False
