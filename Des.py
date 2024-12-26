from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


def des_encrypt(plaintext, key):
    """
    使用 DES 对明文进行加密
    :param plaintext: 明文字符串
    :param key: 8 字节的密钥
    :return: 加密后的密文（以十六进制表示）
    """
    # 创建 DES 加密对象
    cipher = DES.new(key, DES.MODE_ECB)
    # 明文填充到 64 位（8 字节）的倍数
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    # 加密
    encrypted = cipher.encrypt(padded_text)
    # 返回加密后的密文（以十六进制表示）
    return binascii.hexlify(encrypted).decode('utf-8')


def des_decrypt(ciphertext, key):
    """
    使用 DES 对密文进行解密
    :param ciphertext: 密文字符串（十六进制表示）
    :param key: 8 字节的密钥
    :return: 解密后的明文
    """
    # 创建 DES 解密对象
    cipher = DES.new(key, DES.MODE_ECB)
    # 将十六进制密文转换为二进制
    encrypted_bytes = binascii.unhexlify(ciphertext)
    # 解密并去掉填充
    decrypted = unpad(cipher.decrypt(encrypted_bytes), DES.block_size)
    # 返回解密后的明文
    return decrypted.decode('utf-8')


if __name__ == "__main__":
    # 用户输入明文和密钥
    plaintext = input("请输入明文：")
    key = input("请输入密钥（8 字节）：").encode('utf-8')

    # 检查密钥长度是否为 8 字节
    if len(key) != 8:
        print("密钥必须为 8 字节！")
    else:
        # 加密
        ciphertext = des_encrypt(plaintext, key)
        print(f"加密后的密文：{ciphertext}")

        # 解密
        decrypted_text = des_decrypt(ciphertext, key)
        print(f"解密后的明文：{decrypted_text}")
