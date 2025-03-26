"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .sensor import SunSpecPowerSensor, SunSpecVoltageSensor, SunSpecStatusSensor

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    # 喺呢度直接註冊實體
    sensors = [
        SunSpecPowerSensor(hass),
        SunSpecVoltageSensor(hass),
        SunSpecStatusSensor(hass)
    ]

    # 直接用 platform 註冊實體
    platform = hass.helpers.entity_platform.current_platform()
    platform.async_add_entities(sensors)

    return True
