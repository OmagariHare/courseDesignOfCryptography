def caesar_cipher(text, shift, mode='encrypt'):
    """
    实现凯撒密码加密和解密的函数。
    
    :param text: 输入的明文或密文
    :param shift: 密钥（移动的位数）
    :param mode: 模式，'encrypt'表示加密，'decrypt'表示解密
    :return: 加密后的密文或解密后的明文
    """
    result = []
    if mode == 'decrypt':
        shift = -shift  # 解密时移动方向相反

    for char in text:
        if char.isalpha():  # 只处理字母字符
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # 非字母字符不变
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":
    # 用户输入密钥
    shift = int(input("请输入密钥（一个小于26的正整数）："))
    while shift < 0 or shift >= 26:
        print("密钥无效，请输入一个小于26的正整数。")
        shift = int(input("请输入密钥（一个小于26的正整数）："))
    
    # 用户选择操作模式
    mode = input("请选择模式（encrypt 加密 / decrypt 解密）：").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("无效模式，默认设置为加密模式：encrypt")
        mode = 'encrypt'
    
    # 用户输入明文或密文
    text = input("请输入明文（加密模式）或密文（解密模式）：")
    
    # 生成结果
    result = caesar_cipher(text, shift, mode)
    print(f"结果：{result}")
