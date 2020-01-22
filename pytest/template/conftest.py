# conftest.py
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="function")
def login():
    print("请先输入账号和密码，然后登陆")

    yield
    print("退出登陆")