import pytest

class Test_fix():
    def test_1(self):
        print("执行test_1")
    def test_2(self,myfixture):
        print("执行test_2")
    def test_3(self):
        print("执行test_3")