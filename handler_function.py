# !/usr/bin/python
# -*- coding:UTF-8 -*-
# -----------------------------------------------------------------------#
# File Name: handler_function
# Author: Junyi Li
# Mail: 4ljy@163.com
# Created Time: 2021-05-03
# Description:
# -----------------------------------------------------------------------#
from amazon_api.tranlate import translate_helper
from calorie_helper.calorie_flow import main


def helper(input_sentence):
    """
    对输入的所有string sentence进行处理

    :param input_sentence: string
    :return: string
    """
    zh_res = main(input_sentence)
    if zh_res:
        en_res = translate_helper(zh_res)
    else:
        en_res = ""
    res = f"中文结果: {zh_res}\n" \
          f"English result is: {en_res}"
    return res


if __name__ == '__main__':
    res = helper("鸡蛋的热量是多少")
    print(res)
    res = helper("水电费水电费")
    print(res)
