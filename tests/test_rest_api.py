import pytest
import requests

@pytest.mark.reqres
@pytest.mark.rest_api
def test_get_users():

    # Arrange
    url = "https://reqres.in/api/users?page=2"
    names=[]

    # Act
    response = requests.get(url)
    body = response.json()

    for i in range(len(body)):
        name = body['data'][i]['first_name']
        names.append(name)

    # Assert
    assert response.status_code == 200
    assert 'Byron' in names