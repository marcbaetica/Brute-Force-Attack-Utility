import requests as req


def get_url(url):
    res = req.get(url)
    print(f'GET to {url} resulted in {res.status_code}')


def post_with_credentials(url, username, password):
    headers = {'username': username, 'password': password}
    res = req.post(url, headers)
    print(f'POST to {url} resulted in {res.status_code}. User [{username}], pass [{password}].')


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/login'
    get_url(url)
    post_with_credentials(url, 'masteradmin', 'masteradmin')
    post_with_credentials(url, 'masteradmin', 'dsaljfhjasf')
    post_with_credentials(url, 'masteradmin', 'masteradmin')
    post_with_credentials(url, 'dsaljfhjasf', 'masteradmin')
    post_with_credentials(url, 'dsaljfhjasf', '')
    post_with_credentials(url, '', 'dsaljfhjasf')
    post_with_credentials(url, '', '')
    post_with_credentials(url, 'masteradmin', 'masteradmin')
