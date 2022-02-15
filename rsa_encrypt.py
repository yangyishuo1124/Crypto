from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def jiami(d: str):
    public_key = RSA.import_key(open("public_key.pem").read())
    # 实例化加密套件
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(bytes(d, encoding="utf8"))
    file_out = open("encrypted_data.bin", "wb")
    file_out.write(encrypted_data)
    file_out.close()
    return '加密完成'

jiami('''.......................................................................................................................................................................................................................''')
