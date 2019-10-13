from _pytest.capture import CaptureFixture
from pytest import mark

from {{ cookiecutter.project_slug }} import greet


@mark.integration
@mark.parametrize('name', (
    'Alice',
    'Bob',
))
def test_greet(name, capsys: CaptureFixture):
    assert greet(name) is None

    out, err = capsys.readouterr()
    assert 'Hello' in out
    assert name in out
    assert not err
