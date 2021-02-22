from unittest.mock import Mock
import pytest
from rnupythontools import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/76751870?v=4'
    resp_mock.json.return_value = {'login': 'rousuy', 'id': 76751870, 'avatar_url': url, }
    get_mock = mocker.patch('rnupythontools.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.search_avatar('rousuy')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.search_avatar('rousuy')
    assert 'https://avatars.githubusercontent.com/u/76751870?v=4' == url
