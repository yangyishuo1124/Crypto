import time

import base_main_function as main


def jiemi(aa):
    return main.ascii_str(main.bin_dec(main.hex_bin(aa)))


def files():
    read = open('jiami.rpc', 'r')
    read_rpc = read.read()
    read.close()
    return read_rpc


if __name__ == '__main__':
    print('1:本地录入\n2:文件读取\n3:云端读取')
    aa = input('请选择模式：')
    if aa == '1':
        a = input('请输入需要破译的文字：')
        a = main.ascii_str(main.bin_dec(main.hex_bin(a)))
        print('\n结果为:\n' + a)
    if aa == '2':
        a = main.ascii_str(main.bin_dec(main.hex_bin(files())))
        print('\n结果为:\n'+a)
    if aa == '3':
        print('本功能正在开发')
    # time.sleep(100000)
