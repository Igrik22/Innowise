import requests
import pytest
from rest_framework.test import APIRequestFactory


class Setup:
    factory = APIRequestFactory()


class Tests(Setup):

    @staticmethod
    def _prepare_body(username: str, password: str) -> dict:
        """
        Prepare body with admin abd password

        :param username: requested username
        :param password: password for the username
        :return: dict
        """
        payload = {
            "username": username,
            "password": password
        }
        return payload

    @pytest.mark.parametrize("username, password, status",
                             [("admin", "123", 200),
                              ("Rik", "igor12345", 401)])
    def test_post_token_info(self, username, password, status) -> None:
        """
        Returns token information

        :return: None
        """
        base_url = "http://127.0.0.1:8000/token/"
        response = requests.post(
            url=base_url,
            json=self._prepare_body(username=username, password=password))
        assert response.status_code == status

