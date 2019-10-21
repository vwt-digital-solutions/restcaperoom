
from flask import make_response
from flask import jsonify
from flask import send_file

import os
import hashlib
import base64
import string
import random

homeurl = os.environ.get("BASE_URL", "http://localhost:8080")


def randomString(stringLength=18):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


doorids = ["0000", randomString(), randomString(), randomString()]
roomids = [randomString() for i in range(3)]
itemids = [randomString() for i in range(5)]


def get_doorlink(door_nr):
    return f"{homeurl}/doors/{doorids[door_nr]}"


def get_roomlink(room_nr):
    return f"{homeurl}/rooms/{roomids[room_nr]}"


def get_itemlink(item_nr):
    return f"{homeurl}/items/{itemids[item_nr]}"


doorkeys = {
    doorids[0]: "KA1Eqx6febXM4t1PWPX+kfD7rNrJ90R9/8MYzrefLQI=",
    doorids[1]: "iIsZpDsVFoPIeJX2IR2fhkD5e9yO8y8D2+BXyPXlbTI=",
    doorids[2]: "AITDR3lrYUBoT7JOYiFjlOu7ofX0XxhlgdbEC08AKDc=",
    doorids[3]: "P3qqX8YI6ogxbC5IlKfU0RG1+IzcrXch6UjbFjm4UcI="
}


doors = {
    doorids[0]: {
        "i_am_a": "door",
        "self_link": get_doorlink(0),
        "panel": [
            {
                "color": "green"
            }
        ],
        "enters": {
            "type": "room",
            "link": get_roomlink(0)
        }
    },
    doorids[1]: {
        "i_am_a": "door",
        "self_link": get_doorlink(1),
        "panel": [
            {
                "color": "green"
            }
        ],
        "enters": {
            "type": "room",
            "link": get_roomlink(1)
        }
    },
    doorids[2]: {
        "i_am_a": "door",
        "self_link": get_doorlink(2),
        "panel": [
            {
                "color": "green"
            }
        ],
        "enters": {
            "type": "room",
            "link": get_roomlink(2)
        }
    },
    doorids[3]: {
        "i_am_a": "door",
        "self_link": get_doorlink(3),
        "panel": [
            {
                "color": "green"
            }
        ],
        "enters": {
            "type": "outside",
            "link": "https://www.google.com/maps/place/Modemweg+33,+3821+BS+Amersfoort/"
                    "@52.1716506,5.4212663,3a,75y,300.07h,80.63t/data=!3m6!1e1!3m4!1sXcHvpBUvMrC0XbboOt8bPA!2e0!7i13312!"
                    "8i6656!4m5!3m4!1s0x47c64660ee050499:0x9f8028d7c90725d8!8m2!3d52.1714425!4d5.4214408"
        }
    }
}


rooms = {
    roomids[0]: {
        "i_am_a": "room",
        "self_link": get_roomlink(0),
        "items": [
            {
                "i_am_a": "door",
                "link": get_doorlink(1)
            },
            {
                "i_am_a": "key",
                "value": "0001"
            }
        ]
    },
    roomids[1]: {
        "i_am_a": "room",
        "self_link": get_roomlink(1),
        "items": [
            {
                "i_am_a": "door",
                "link": get_doorlink(2)
            },
            {
                "i_am_a": "painting",
                "image": get_itemlink(1)
            }
        ]
    },
    roomids[2]: {
        "i_am_a": "room",
        "self_link": get_roomlink(2),
        "items": [
            {
                "i_am_a": "door",
                "link": get_doorlink(3)
            },
            {
                "i_am_a": "painting",
                "image": get_itemlink(2)
            },
            {
                "i_am_a": "painting",
                "image": get_itemlink(3)
            },
            {
                "i_am_a": "painting",
                "image": get_itemlink(4)
            },
            {
                "i_am_a": "disc",
                "items": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                          'u', 'v', 'w', 'y', 'z']
            },
            {
                "i_am_a": "disc",
                "items": ['03b1', '03b2', '03b3', '03b4', '03b5', '03b6', '03b7', '03b8', '03b9', '03ba', '03bb', '03bc',
                          '03bd', '03be', '03bf', '03c0', '03c1', '03c3', '03c4', '03c5', '03c6', '03c7', '03c8', '03c9']
            },
            {
                "i_am_a": "text_on_floor",
                "text": ['03b6', '03c8', '03c1', '03b3', '03bd', '03c8', '03c0']
            }
        ]
    }
}


items = {
    itemids[0]: {
        "i_am_a": "table",
        "self_link": get_itemlink(0),
        "color": "brown"
    },
    itemids[1]: {
        "i_am_a": "file",
        "self_link": get_itemlink(1),
        "filename": "assets/painting1.jpg"
    },
    itemids[2]: {
        "i_am_a": "file",
        "self_link": get_itemlink(2),
        "filename": "assets/painting2.jpg"
    },
    itemids[3]: {
        "i_am_a": "file",
        "self_link": get_itemlink(3),
        "filename": "assets/painting3.jpg"
    },
    itemids[4]: {
        "i_am_a": "file",
        "self_link": get_itemlink(4),
        "filename": "assets/painting4.png"
    }
}


def getentrance():  # noqa: E501
    return doors["0000"]


def getdoor(door_id, key):  # noqa: E501
    """Get a door

    Gets the details of a single instance of a &#x60;door&#x60;. # noqa: E501

    :param door_id: A unique identifier for a &#x60;door&#x60;.
    :type door_id: str

    :rtype: Door
    """
    if door_id in doors:
        encoded_key = base64.b64encode(hashlib.sha256(key.encode()).digest()).decode()
        if encoded_key == doorkeys[door_id]:
            return doors[door_id]
        else:
            return make_response(jsonify('Wrong key'), 401)
    else:
        return make_response(jsonify('Not found'), 404)


def getdoors():  # noqa: E501
    """List All doors

    Gets a list of all &#x60;door&#x60; entities. # noqa: E501


    :rtype: List[Door]
    """
    return [doors["0000"]]


def getitem(item_id):  # noqa: E501
    """Get a item

    Gets the details of a single instance of a &#x60;item&#x60;. # noqa: E501

    :param item_id: A unique identifier for a &#x60;item&#x60;.
    :type item_id: str

    :rtype: Item
    """
    if item_id in items:
        if items[item_id]['i_am_a'] == "file":
            return send_file(items[item_id]['filename'])
        else:
            return items[item_id]
    else:
        return make_response(jsonify('Not found'), 404)


def getitems():  # noqa: E501
    """List All items

    Gets a list of all &#x60;item&#x60; entities. # noqa: E501


    :rtype: List[Item]
    """
    return [items[itemids[0]]]


def getroom(room_id):  # noqa: E501
    """Get a room

    Gets the details of a single instance of a &#x60;room&#x60;. # noqa: E501

    :param room_id: A unique identifier for a &#x60;room&#x60;.
    :type room_id: str

    :rtype: Room
    """
    if room_id in rooms:
        return rooms[room_id]
    else:
        return make_response(jsonify('Not found'), 404)


def getrooms():  # noqa: E501
    """List All rooms

    Gets a list of all &#x60;room&#x60; entities. # noqa: E501


    :rtype: List[Room]
    """
    return 'do some magic!'
