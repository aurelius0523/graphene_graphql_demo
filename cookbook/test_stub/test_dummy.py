"""stub test method"""

def stub_method():
    """this test is the stub as exit code 5 returned by pytest when no test case is found will cause Travis CI build to fail"""
    return 5


def test_answer():
    """test case"""
    assert stub_method() == 5
