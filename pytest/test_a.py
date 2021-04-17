import pytest

def add_function(a,b):
        return a+b

class Test_first():
    @pytest.mark.demo1  #mark 标签
    def test_1(self):
        a = 3;
        b = 3;
        assert a == b #断言
        print("my first test file.py")
    
    #参数化+别名
    @pytest.mark.parametrize("a,b,expect_out",
                            [(1,2,3),(-1,1,0),(-1,-2,-3),(100000,100000,200000)],ids=['test1','test2','test3','test4'])
    def test_add(self,a,b,expect_out):
        assert add_function(a,b) == expect_out
        print("参数化测试成功!")