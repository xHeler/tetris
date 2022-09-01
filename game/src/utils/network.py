# -*- coding: utf-8 -*-
"""Network tools

Networking between server and client, catching errors.
"""
import ast
import requests

from src.utils.settings import LOGIN_URL, CONN_URL


class Network:
    """Network class

    Attribiutes:
        errors: str, Response text message.
        key: str, User login token.
        username: str, Player username.
    """

    def __init__(self):
        """Constructor

        Attribiutes:
            errors: str, Response text message.
            key: str, User login token.
            username: str, Player username.
        """
        self.errors = None
        self.key = None
        self.username = None

    def is_connected_to_server(self, email, password):
        """Login and connect to server

        Send post method to authentication API and wait for response.

        Return:
            bool: True, If connection successful and False when something.
                its wrong.
        """
        json = Network.make_json(
            username=email, email=email, password=password)
        response = requests.post(LOGIN_URL, json=json, timeout=10)

        response_json = ast.literal_eval(response.text)

        if "key" in response_json:
            self.key = str(response_json['key'])
            self.username = email
            return True
        self.errors = response_json
        return False

    def send_score_to_server(self, points):
        """ Updates points at server

        Send new player score into server.
        """
        if not self.key:
            return False
        json = Network.make_json(author=self.username, points=points)
        headers = Network.make_json(Authorization='Token ' + self.key)

        response = requests.post(
            CONN_URL, json=json, headers=headers, timeout=10)
        self.errors = ast.literal_eval(response.text)
        return True

    @staticmethod
    def make_json(**kwargs):
        """Make json

        Making json from kwargs.

        Example:
            print(make_json(test=1, hello="abcd"))
            # return
            { "test": 1, "hello": "abcd"}
        """
        json = {}
        for key, value in kwargs.items():
            json[str(key)] = value
        return json
