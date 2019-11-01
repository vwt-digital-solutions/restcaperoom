# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DoorPanel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, color=None):  # noqa: E501
        """DoorPanel - a model defined in OpenAPI

        :param color: The color of this DoorPanel.  # noqa: E501
        :type color: str
        """
        self.openapi_types = {
            'color': str
        }

        self.attribute_map = {
            'color': 'color'
        }

        self._color = color

    @classmethod
    def from_dict(cls, dikt) -> 'DoorPanel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The door_panel of this DoorPanel.  # noqa: E501
        :rtype: DoorPanel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color(self):
        """Gets the color of this DoorPanel.


        :return: The color of this DoorPanel.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this DoorPanel.


        :param color: The color of this DoorPanel.
        :type color: str
        """

        self._color = color
