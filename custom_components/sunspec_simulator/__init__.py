"""SunSpec Simulator Custom Component."""
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import async_get_current_platform
from .sensor import SunSpecPowerSensor, SunSpecVoltageSensor, SunSpecStatusSensor

_LOGGER = logging.getLogger(__name__)
DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    _LOGGER.info("Setting up SunSpec Simulator component")

    # 喺呢度直接註冊實體
    platform = async_get_current_platform()
    if platform is None:
        _LOGGER.error("Unable to get current platform for SunSpec Simulator")
        return False

    sensors = [
        SunSpecPowerSensor(hass),
        SunSpecVoltageSensor(hass),
        SunSpecStatusSensor(hass)
    ]

    platform.async_add_entities(sensors)
    _LOGGER.info("SunSpec Simulator component setup completed")
    return True
