import pytest
from main import get_folder

FIXTURES = [('test', 201), ('test', 409)]

@pytest.mark.parametrize('a, etalon', FIXTURES)
def test_get_folder(a, etalon):
    result = get_folder(a)
    assert result == etalon