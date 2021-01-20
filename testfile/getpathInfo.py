# 获取项目绝对路径

import os


def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path

def get_root_path():
    root_path = os.path.split(os.path.realpath(__file__))[0].split('\\testfile')[0]
    return root_path
    # print(str(root_path))

if __name__ == "__main__":
    print("测试路径是否OK，路径为： ", get_Path())
