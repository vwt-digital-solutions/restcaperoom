# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.door import Door  # noqa: E501
from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.room import Room  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_getdoor(self):
        """Test case for getdoor

        Get a door
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/doors/{door_id}'.format(door_id='door_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getdoors(self):
        """Test case for getdoors

        List All doors
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/doors',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getitem(self):
        """Test case for getitem

        Get a item
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/items/{item_id}'.format(item_id='item_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getitems(self):
        """Test case for getitems

        List All items
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/items',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getroom(self):
        """Test case for getroom

        Get a room
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rooms/{room_id}'.format(room_id='room_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getrooms(self):
        """Test case for getrooms

        List All rooms
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rooms',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
