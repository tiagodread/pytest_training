import pytest, requests, json


@pytest.fixture
def base_url():
    return 'https://reqres.in'


@pytest.mark.parametrize('email, password, status_code, message',
                         [('foo@bar.com.br', '12345', 400, 'user not found'),
                          ('eve.holt@reqres.in', 'cityslicka', 200, 'QpwL5tke4Pnpja7X4')])
def test_login(base_url, email, password, status_code, message):
    url = base_url + '/api/login'
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)
    response_json = json.loads(response.text)

    assert response.status_code == status_code
    for key, value in response_json.items():
        assert value == message
