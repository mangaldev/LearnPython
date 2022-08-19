digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lower_chars = [c for c in "abcdefghijklmnopqrstuvwxyz"]
upper_chars = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

# Converting an integer to character chr(a_number)
def rotate(s, r):
    updated_str = ''
    for ch in s:
        if 0 <= ord(ch) - ord('A') < 26:
            updated_str = updated_str + chr((ord(ch) - ord('A') + r % 26) + ord('A'))
        elif 0 <= ord(ch) - ord('a') < 26:
            updated_str = updated_str + chr((ord(ch) - ord('a') + r % 26) + ord('a'))
        elif 0 <= ord(ch) - ord('0') < 10:
            updated_str += str((r + int(ch)) % 10)
        else:
            updated_str = updated_str + ch
    return updated_str


print(rotate("A-b!c", 2))
print(rotate("39ZA", 4))
