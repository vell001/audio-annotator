#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2018/5/10
import os
import re


def list_files(root_dir, suffix, recursion=True):
    ret = list()
    for filename in os.listdir(root_dir):
        path = os.path.join(root_dir, filename)
        if recursion and os.path.isdir(path):
            ret.extend(list_files(path, suffix))
        if os.path.isfile(path) and filename.endswith(suffix):
            ret.append(path)

    return ret


def find_child_path_by_re(path, re_pattern_str, is_file=None):
    '''
    查找指定后缀的文件
    :param path:
    :param postfix:
    :param is_file: None则返回所有，True则只返回文件，False只返回文件夹
    :return:
    '''
    pattern = re.compile(re_pattern_str)
    ret = list()
    f_list = os.listdir(path)
    for f in f_list:
        f_path = os.path.join(path, f)
        if is_file is not None and os.path.isfile(f_path) != is_file:
            continue
        if pattern.fullmatch(f):
            ret.append(f_path)
    return ret


def read_tags_from_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        tags = f.readlines()
        tags = [tag.strip() for tag in tags]
        return tags


def count_file_lines(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
        return len(lines)


def all_equal(elements):
    first_element = elements[0]
    for other_element in elements[1:]:
        if other_element != first_element:
            return False
    return True


def common_prefix(*sequences):
    if not sequences:
        return [], []
    common = []
    for elements in zip(*sequences):
        if not all_equal(elements):
            break
        common.append(elements[0])
    return common, [sequence[len(common):] for sequence in sequences]


def get_relative_path(parent_path, target_path, sep=os.path.sep, pardir=os.path.pardir):
    if parent_path.endswith(sep):
        # 去除以“/”结尾的情况
        parent_path = parent_path[:len(parent_path) - len(sep)]
    common, (u1, u2) = common_prefix(parent_path.split(sep), target_path.split(sep))
    if not common:
        return target_path
    return sep.join([pardir] * len(u1) + u2)


if __name__ == "__main__":
    print(get_relative_path("test/test11/", "test/test11/test21"))
    print(find_child_path_by_re("../dataset", r".*dev\.txt_xy.*\.h5"))
