import rsa


def saver(len):
    (publicKey, privateKey) = rsa.newkeys(len)
    pub = open('public_key.pem', 'wb+')
    pub.write(publicKey.save_pkcs1())
    pub.close()
    pri = open('private_key.pem', 'wb+')
    pri.write(privateKey.save_pkcs1())
    pri.close()
    return
