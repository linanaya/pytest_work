import pytest,yaml

def add_function(a,b):
        return a+b
def get_data():
    with open("./test_data.yml") as f:
        datas = yaml.safe_load(f)
        x = datas["data_param"]
        y = datas["data_ids"]
        return [x,y]
class Test_first():
    #参数化+别名
    # @pytest.mark.parametrize("a,b,expect_out",
    #                         yaml.safe_load(open("./test_data.yml"))["data_param"],
    #                         ids=yaml.safe_load(open("./test_data.yml"))["data_ids"])
    @pytest.mark.parametrize("a,b,expect_out",
                            get_data()[0],
                            ids=get_data()[1])
    def test_add(self,a,b,expect_out):
        assert add_function(a,b) == expect_out
        print("参数化测试成功!")