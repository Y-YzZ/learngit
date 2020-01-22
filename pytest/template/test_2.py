# test_2.py
# -*- coding: utf-8 -*-
import pytest


def test_fix3():
    print("test_fix3 in test_2.py：不需要登陆再执行操作")


def test_fix4(login):
    print("test_fix4 in test_2.py：需要登陆再执行操作")


if __name__ == "__main__":
    pytest.main(['-s', 'test_2.py'])