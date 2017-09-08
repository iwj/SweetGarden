# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2017-09-07
# Author: juzi
# E-mail: jentlewoo@gmail.com


import sys

def convert(
        number = 999,
        ):
    '''
    convert number to chinese words
    only support 100 ~ 999 :(
    '''
    yuan = '圆'
    ten = '拾'
    hundred = '佰'
    words_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    number_list = list(str(number))
    if(int(number_list[0]) > 0):
        result = words_list[int(number_list[0])] + hundred
    else:
        result = ''
    if(int(number_list[1]) > 0):
        result += words_list[int(number_list[1])] + ten
        if(int(number_list[2]) > 0):
            result += words_list[int(number_list[2])] + yuan
        else:
            result = result + yuan
    else:
        result += words_list[0]
        if(int(number_list[2]) > 0):
            result += words_list[int(number_list[2])] + yuan
        else:
            result = result[:-1] + yuan
    return result

if __name__ == '__main__':
    arg = sys.argv[1]
    print(convert(arg))
