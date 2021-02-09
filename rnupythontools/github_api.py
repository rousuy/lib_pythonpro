import requests


def search_avatar(user):
    """
    Busca o avatar de um usuário no GitHub.
    :param user: str com o nome do usuário no GitHub.
    :return: str com o link do avatar.
    """
    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(search_avatar('rousuy'))
