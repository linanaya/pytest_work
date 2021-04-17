import pytest

def setup_module():
    print("每个模块文件执行时会执行--start")

def setup_function():
    print("每个不在类中的函数会执行--start")
def test_func():
    print("不在类中的函数")
def teardown_function():
    print("每个不在类中的函数会执行--end")

class Test_first():
    def setup_class():
        print("每个模块中的类执行时会执行--start")

    def setup_method(self):
        print("每个模块中的类执行时其中的方法会执行--start")
    def test(self):
        print("类中的方法")
    def teardown_method(self):
        print("每个模块中的类执行时其中的方法会执行--end")
    
    def teardown_class():
        print("每个模块中的类执行时会执行--end")

def teardown_module():
    print("每个模块文件执行时会执行--end")