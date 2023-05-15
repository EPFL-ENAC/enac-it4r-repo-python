from project_name.hello import get_python_version


def test_get_python_version():
    # Test the return type
    assert isinstance(get_python_version(), str)
