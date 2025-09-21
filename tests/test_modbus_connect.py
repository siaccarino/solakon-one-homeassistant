from os import environ
import pytest
from custom_components.solakon_one import SolakonModbusHub
from unittest.mock import MagicMock
import asyncio


@pytest.fixture
def hass():
    return MagicMock(name="HomeAssistant")


def test_modbus_connection(hass):
    client = SolakonModbusHub(
        hass,
        environ["SOLAKON_ONE_HOST"],
        int(environ["SOLAKON_ONE_PORT"]),
        int(environ["SOLAKON_ONE_MODBUS_SLAVE_ID"]),
        10,
    )

    result = asyncio.run(client.async_test_connection())

    assert result
