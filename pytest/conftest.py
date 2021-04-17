import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    print("执行了我的fixture文件,参数：{}".format(request.param))