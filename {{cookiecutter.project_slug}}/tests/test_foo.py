from {{cookiecutter.project_slug.replace('-', '_')}}.foo import bar


def test_bar():
    # Test the return type
    assert isinstance(bar(), str)
