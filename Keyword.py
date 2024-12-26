def generate_cipher_table(keyword):
    """
    根据输入的密钥生成替换表。
    """
    # 去掉重复字符和空格，保持顺序
    keyword = "".join(dict.fromkeys(keyword.replace(" ", "").upper()))
    # 补全剩余的字母
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remaining_letters = "".join(letter for letter in alphabet if letter not in keyword)
    cipher_table = keyword + remaining_letters
    return cipher_table


def encrypt(plaintext, cipher_table):
    """
    根据密码表对明文进行加密。
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    ciphertext = "".join(cipher_table[alphabet.index(char)] if char in alphabet else char for char in plaintext)
    return ciphertext


def decrypt(ciphertext, cipher_table):
    """
    根据密码表对密文进行解密。
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    reverse_table = {cipher_table[i]: alphabet[i] for i in range(len(cipher_table))}
    plaintext = "".join(reverse_table[char] if char in reverse_table else char for char in ciphertext)
    return plaintext


if __name__ == "__main__":
    # 用户输入密钥
    keyword = input("请输入密钥（如HAPPY NEW YEAR）：")
    cipher_table = generate_cipher_table(keyword)
    print(f"生成的密码表: {cipher_table}")

    # 用户输入明文并加密
    plaintext = input("请输入明文（如LOVE）：")
    ciphertext = encrypt(plaintext, cipher_table)
    print(f"加密后的密文: {ciphertext}")

    # 用户输入密文并解密
    ciphertext_input = input("请输入要解密的密文：")
    decrypted_text = decrypt(ciphertext_input, cipher_table)
    print(f"解密后的明文: {decrypted_text}")
