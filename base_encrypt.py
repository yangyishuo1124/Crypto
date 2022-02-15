import time

import base_main_function


def jiami(aa):
    return base_main_function.bin_hex(base_main_function.ascii_bin(base_main_function.str_ascii(str(aa))))


def files(aa):
    write = open('jiami.rpc', 'w')
    write.write(aa)
    write.close()


if __name__ == '__main__':
    a = input('请输入需要加密的文字:')
    print('\n结果为:\n')
    a = jiami(a)
    files(a)
    print(a)
    time.sleep(100000)
