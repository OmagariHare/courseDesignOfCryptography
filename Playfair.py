# 密钥表生成函数
def create_playfair_table(key):
    key = key.lower().replace(" ", "").replace("z", "x")
    table = []
    used = set()
    for char in key:
        if char not in used:
            table.append(char)
            used.add(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in used and char != "z":  # 去掉字母z
            table.append(char)
            used.add(char)
    return [table[i:i + 5] for i in range(0, 25, 5)]


# 查找字母位置
def find_position(table, char):
    for row_idx, row in enumerate(table):
        if char in row:
            return row_idx, row.index(char)
    return None


# 加密一对字母
def encrypt_pair(table, pair):
    row1, col1 = find_position(table, pair[0])
    row2, col2 = find_position(table, pair[1])
    if row1 == row2:  # 同一行
        return table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
    elif col1 == col2:  # 同一列
        return table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
    else:  # 矩形替换
        return table[row1][col2] + table[row2][col1]


# 解密一对字母
def decrypt_pair(table, pair):
    row1, col1 = find_position(table, pair[0])
    row2, col2 = find_position(table, pair[1])
    if row1 == row2:  # 同一行
        return table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
    elif col1 == col2:  # 同一列
        return table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
    else:  # 矩形替换
        return table[row1][col2] + table[row2][col1]

# 格式化密文输出（每两个字母为一组，用空格分隔）
def format_ciphertext(ciphertext):
    return " ".join([ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)])


# 整理明文或密文（同时记录大小写）
def prepare_text_with_case(text, encrypt=True):
    text = text.replace(" ", "").replace("z", "x")
    result = []
    case_info = []  # 记录大小写信息

    i = 0
    while i < len(text):
        char1 = text[i]
        case_info.append(char1.isupper())  # 记录第一个字符大小写
        char1 = char1.lower()

        if i + 1 < len(text):
            char2 = text[i + 1]
            if encrypt and char1 == char2:  # 插入'x'防止重复
                result.append(char1 + 'x')
                case_info.append(False)  # 插入的'x'是小写
                i += 1
            else:
                case_info.append(char2.isupper())  # 记录第二个字符大小写
                char2 = char2.lower()
                result.append(char1 + char2)
                i += 2
        else:  # 最后一个字符单独补'x'
            if encrypt:
                result.append(char1 + 'x')
                case_info.append(False)  # 插入的'x'是小写
            else:
                result.append(char1)
            i += 1

    return result, case_info


# 根据大小写信息还原
def restore_case(text, case_info):
    restored_text = ""
    for i, char in enumerate(text):
        if case_info[i]:
            restored_text += char.upper()
        else:
            restored_text += char.lower()
    return restored_text


# 加密函数
def playfair_encrypt(plaintext, table):
    """
    对明文进行Playfair加密，同时保留大小写信息
    """
    pairs, case_info = prepare_text_with_case(plaintext)  # 整理明文并记录大小写
    ciphertext = []
    for pair in pairs:
        ciphertext.append(encrypt_pair(table, pair))
    # 合并密文并还原大小写
    return restore_case("".join(ciphertext), case_info)


# 解密函数
def playfair_decrypt(ciphertext, table):
    """
    对密文进行Playfair解密，同时保留大小写信息
    """
    pairs, case_info = prepare_text_with_case(ciphertext.replace(" ", ""), encrypt=False)  # 整理密文并记录大小写
    plaintext = ""
    for pair in pairs:
        if len(pair) == 1:
            pair += 'x'  # 如果最后一个字符单独存在，补x
        plaintext += decrypt_pair(table, pair)
    # 还原大小写
    return restore_case(plaintext, case_info)


if __name__ == "__main__":
    key = input("请输入密钥：")
    plaintext = input("请输入明文：")
    table = create_playfair_table(key)
    print("生成的密码表：")
    for row in table:
        print(" ".join(row))

    ciphertext = playfair_encrypt(plaintext, table)
    formatted_ciphertext = format_ciphertext(ciphertext)  # 调用格式化函数
    print("加密后的密文：", formatted_ciphertext)

    decrypted_text = playfair_decrypt(ciphertext, table)
    print("解密后的明文：", decrypted_text)
