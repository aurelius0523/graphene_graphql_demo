# dummy test case for pytest. pytest throws Exit Code 5 when no test case is found
# TODO setup proper test case. Maybe using Django

def func(x):
    return x


def test_func():
    assert func(3) == 3