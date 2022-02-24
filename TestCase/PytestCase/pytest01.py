__author__ = 'Admin'

import pytest


class TestCase01:
    def test_01(self):
        print("test01")

    def test_02(self):
        print("test02")
        print("test03")


if __name__ == '__main__':
    pytest.main(['-s'])
