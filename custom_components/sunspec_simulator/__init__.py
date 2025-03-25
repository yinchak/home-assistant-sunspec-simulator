"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from .sensor import SunSpecPowerSensor, SunSpecVoltageSensor, SunSpecStatusSensor

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    # 直接喺呢度設實體
    sensors = [
        SunSpecPowerSensor(hass),
        SunSpecVoltageSensor(hass),
        SunSpecStatusSensor(hass)
    ]

    # 註冊實體
    platform = hass.helpers.entity_platform.async_get_current_platform()
    platform.async_add_entities(sensors)

    return True
