from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# 从文件中读取加密内容
def jiemi(data_name='encrypted_data.bin'):
    # 从私钥文件中读取私钥
    private_key = RSA.import_key(open("private_key.pem", "rb").read())
    # 实例化加密套件
    cipher = PKCS1_OAEP.new(private_key)
    encrypted_data = open(data_name, "rb").read()
    # 解密，如无意外data值为最先加密的b"123456"
    data = cipher.decrypt(encrypted_data)
    #('解密后文字为:\n' + data.decode('utf8'))
    return data.decode('utf8')

#print(jiemi())