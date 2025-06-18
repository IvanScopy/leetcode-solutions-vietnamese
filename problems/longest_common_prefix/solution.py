def longestCommonPrefix(strs):
    """
    Tìm tiền tố chung dài nhất trong một mảng các chuỗi.
    Nếu không có tiền tố chung, trả về chuỗi rỗng "".
    """
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Ví dụ sử dụng:
if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"
    print(longestCommonPrefix(["dog","racecar","car"]))     # ""
