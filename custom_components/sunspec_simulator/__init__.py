"""SunSpec Simulator Custom Component."""
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from .sensor import SunSpecPowerSensor, SunSpecVoltageSensor, SunSpecStatusSensor

_LOGGER = logging.getLogger(__name__)
DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    _LOGGER.info("Setting up SunSpec Simulator component")

    # 喺呢度直接註冊實體
    sensors = [
        SunSpecPowerSensor(hass),
        SunSpecVoltageSensor(hass),
        SunSpecStatusSensor(hass)
    ]

    # 直接用 hass.async_add_entities 註冊實體
    hass.async_create_task(
        hass.helpers.entity_component.async_add_entities(sensors)
    )

    _LOGGER.info("SunSpec Simulator component setup completed")
    return True
