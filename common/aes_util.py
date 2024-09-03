from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64


def encrypt_aes_parameter(plaintext, key, iv):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    # 填充明文
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # 加密
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext


# 明文、密钥和初始向量
plaintext = "rank_type=1&bring_type=2&page=&size=10000&sort_column=volume&order_by=&cmm_cid=0&cmm_cid_snd=0&cmm_cid_third=0&is_new_product=false&price_min=&price_max=&ratio_min=&ratio_max="
key = b'9rDal3705V6xVMLL'  # 128位密钥
iv = b'9rDal3705V6xVMLL'  # 128位初始向量

# 加密明文
# ciphertext = encrypt_aes_parameter(plaintext, key, iv)
# print(type(ciphertext), ciphertext)
# print("加密后的密文:", base64.b64encode(ciphertext).decode())


def decryptor_aes_parameter(plaintext, key, iv):
    # 待解密的密文（经过base64编码）
    ciphertext = base64.b64decode(plaintext)
    print(ciphertext)
    # 创建 Cipher 对象
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # 创建解密器
    decryptor = cipher.decryptor()

    # 解密操作
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    # 去除填充
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()

    return decrypted_text

plaintext = 'cOdUgIdOchTDeID7JVl4uFB07WrF9cOP5LJaTtnT8wZrMHDqzEsDKGeQBjc5rY/L13myh7L/YKPVEIPh+fDfyloGWou+JEkn8hPXxdji5QfdLWrQNxCYAsb6YusK9Q85//wPc9ZS3QCaDpaW39xPo1uXgE3SZsij9pYgZjEMvuHaNI2/bpHm3fwV0AA0rE3gwdPRCguiBtRmthrBddRQLoprsw2qjVEC/GzPUnqEZiw='
text = decryptor_aes_parameter(plaintext, key, iv)
text = text.decode('utf-8')
print(type(text), text)
