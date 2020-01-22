# test_1.py
# -*- coding: utf-8 -*-
import pytest


def test_fix1(login):
    print("test_fix1 in test_1.py：需要登陆再执行操作")


def test_fix2():
    print("test_fix2 in test_1.py：不需要登陆再执行操作")


def test_fix3(login):
    print("test_fix3 in test_1.py：需要登陆再执行操作")


if __name__ == "__main__":
    pytest.main(['-s', 'test_1.py'])