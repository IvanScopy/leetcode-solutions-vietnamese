def romanToInt(s):
    """
    Chuyển đổi một chuỗi số La Mã (s) thành số nguyên.
    """
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
    for c in reversed(s):  # Duyệt ngược chuỗi
        value = roman[c]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

# Ví dụ sử dụng:
if __name__ == "__main__":
    print(romanToInt("III"))     # 3
    print(romanToInt("IV"))      # 4
    print(romanToInt("IX"))      # 9
    print(romanToInt("LVIII"))   # 58
    print(romanToInt("MCMXCIV")) # 1994
