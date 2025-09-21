from os import environ
import pytest
from custom_components.solakon_one import SolakonModbusHub
from custom_components.solakon_one.const import DEFAULT_PORT, DEFAULT_SLAVE_ID, DEFAULT_SCAN_INTERVAL
from unittest.mock import MagicMock
import asyncio


@pytest.fixture
def hass():
    return MagicMock(name="HomeAssistant")


def test_modbus_connection(hass):
    client = SolakonModbusHub(
        hass,
        environ["SOLAKON_ONE_HOST"],
        int(environ.get("SOLAKON_ONE_PORT", DEFAULT_PORT)),
        int(environ.get("SOLAKON_ONE_MODBUS_SLAVE_ID", DEFAULT_SLAVE_ID)),
        DEFAULT_SCAN_INTERVAL,
    )

    result = asyncio.run(client.async_test_connection())

    assert result

def test_get_device_info(hass):
    client = SolakonModbusHub(
        hass,
        environ["SOLAKON_ONE_HOST"],
        int(environ.get("SOLAKON_ONE_PORT", DEFAULT_PORT)),
        int(environ.get("SOLAKON_ONE_MODBUS_SLAVE_ID", DEFAULT_SLAVE_ID)),
        DEFAULT_SCAN_INTERVAL,
    )

    result = asyncio.run(client.async_get_device_info())

    assert result is not None
    assert "manufacturer" in result

def test_read_registers(hass):
    client = SolakonModbusHub(
        hass,
        environ["SOLAKON_ONE_HOST"],
        int(environ.get("SOLAKON_ONE_PORT", DEFAULT_PORT)),
        int(environ.get("SOLAKON_ONE_MODBUS_SLAVE_ID", DEFAULT_SLAVE_ID)),
        DEFAULT_SCAN_INTERVAL,
    )

    result = asyncio.run(client.async_read_registers())

    assert result is not None
    assert "model_name" in result
