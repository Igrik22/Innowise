import requests
import pytest
from rest_framework.test import APIRequestFactory


class Setup:
    factory = APIRequestFactory()


class Tests(Setup):

    @staticmethod
    def _prepare_body(task_text: str) -> dict:
        """
        Prepare body with admin abd password

        :param task_text: requested task_text
        :return: dict
        """
        payload = {
            "task_text": task_text
        }
        return payload

    @pytest.mark.parametrize("task_text, status",
                             [("hello world", 201),
                              ("Middle English taske", 201)])
    def test_post_user_info(self, task_text, status) -> None:
        """
        Returns ticket information

        :return: None
        """
        response_jwt = requests.post(url="http://127.0.0.1:8000/token/", json={
            "username": "admin",
            "password": "123"
        })
        jwt_token = response_jwt.json().get('access')
        base_url = "http://127.0.0.1:8000/api/v1/support/create/"
        response = requests.post(
            headers={'Authorization': 'Bearer {}'.format(jwt_token)},
            url=base_url,
            json=self._prepare_body(task_text=task_text))
        assert response.status_code == status
