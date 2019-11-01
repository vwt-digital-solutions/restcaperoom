# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.door_panel import DoorPanel
from openapi_server import util

from openapi_server.models.door_panel import DoorPanel  # noqa: E501

class Door(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, panel=None):  # noqa: E501
        """Door - a model defined in OpenAPI

        :param panel: The panel of this Door.  # noqa: E501
        :type panel: List[DoorPanel]
        """
        self.openapi_types = {
            'panel': List[DoorPanel]
        }

        self.attribute_map = {
            'panel': 'panel'
        }

        self._panel = panel

    @classmethod
    def from_dict(cls, dikt) -> 'Door':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The door of this Door.  # noqa: E501
        :rtype: Door
        """
        return util.deserialize_model(dikt, cls)

    @property
    def panel(self):
        """Gets the panel of this Door.


        :return: The panel of this Door.
        :rtype: List[DoorPanel]
        """
        return self._panel

    @panel.setter
    def panel(self, panel):
        """Sets the panel of this Door.


        :param panel: The panel of this Door.
        :type panel: List[DoorPanel]
        """

        self._panel = panel