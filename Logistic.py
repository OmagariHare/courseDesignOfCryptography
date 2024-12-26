import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Logistic混沌序列生成函数
def logistic_map(r, x0, n):
    """生成n个Logistic混沌序列"""
    sequence = np.zeros(n)
    sequence[0] = x0
    for i in range(1, n):
        sequence[i] = r * sequence[i-1] * (1 - sequence[i-1])
    return sequence

# 图像加密函数
def encrypt_image(image_path, r=3.99, x0=0.5):
    # 读取图像
    img = Image.open(image_path)
    img_data = np.array(img)
    
    # 获取图像的像素总数
    height, width, channels = img_data.shape
    total_pixels = height * width * channels
    
    # 生成混沌序列
    chaos_sequence = logistic_map(r, x0, total_pixels)
    
    # 将混沌序列映射到0-255范围
    chaos_sequence = np.uint8(chaos_sequence * 255)
    
    # 加密过程：将图像数据与混沌序列异或
    encrypted_data = img_data ^ chaos_sequence.reshape(height, width, channels)
    
    # 转换为加密后的图像
    encrypted_img = Image.fromarray(encrypted_data)
    
    # 显示加密后的图像
    plt.imshow(encrypted_img)
    plt.show()
    
    return encrypted_img

# 解密函数
def decrypt_image(encrypted_img, r=3.99, x0=0.5):
    encrypted_data = np.array(encrypted_img)
    height, width, channels = encrypted_data.shape
    total_pixels = height * width * channels
    
    # 生成混沌序列
    chaos_sequence = logistic_map(r, x0, total_pixels)
    chaos_sequence = np.uint8(chaos_sequence * 255)
    
    # 解密过程：将加密图像数据与混沌序列异或
    decrypted_data = encrypted_data ^ chaos_sequence.reshape(height, width, channels)
    
    # 转换为解密后的图像
    decrypted_img = Image.fromarray(decrypted_data)
    
    # 显示解密后的图像
    plt.imshow(decrypted_img)
    plt.show()
    
    return decrypted_img

# 使用示例
image_path = "pic.jpg"  # 请替换为实际图像路径
encrypted_img = encrypt_image(image_path)
decrypted_img = decrypt_image(encrypted_img)
