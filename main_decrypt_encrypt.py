from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import base_encrypt
import base_decrypt
import rsa_decrypt
import rsa_encrypt
import rsa_builder
import re


def encrypt(data_encrypt):
    base_data: str = base_encrypt.jiami(data_encrypt)
    rsa_data: str = rsa_encrypt.jiami(base_data)
    return rsa_data


def decrypt(data_decrypt_name='encrypted_data.bin'):
    rsa_data = rsa_decrypt.jiemi(data_decrypt_name)
    base_data = base_decrypt.jiemi(rsa_data.encode('utf8'))
    return base_data


def builder(builder_len):
    rsa_builder.saver(builder_len)
    return


if __name__ == '__main__':
    print('1:加密\n2:解密\n3:生成rsa密钥')
    a = input('请选择需要的模式:')
    if a == '1':
        print('1:手动输入\n2:文件读取')
        a = input('请选择加密源文件出处:')
        if a == '1':
            data = input('请输入需要加密的文字:')
            encrypt(data)
        if a == '2':
            data_read_name = input('请输入读取文件的名称(后缀为txt)')
            try:
                data_read = open(data_read_name, 'r')
            except FileNotFoundError:
                print('输入的文件名称有误')
            else:
                data = data_read.read()
                data_read.close()
                encrypt(data)
    if a == '2':
        data_name = input('请输入需要解密的文件名称(留空默认为‘encrypted_data.bin’):')
        if data_name == '':
            data_name = 'encrypted_data.bin'
        try:
            print('解密的结果为:'+decrypt(data_name))
        except FileNotFoundError:
            print('输入的文件名称有误')
        else:
            print('解密完成')
    if a == '3':
        len = input('请输入rsa密钥生成长度:')
        builder(int(len))
