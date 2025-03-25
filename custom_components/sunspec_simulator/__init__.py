"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    # 喺呢度直接設實體
    from .sensor import async_setup_sensors
    await async_setup_sensors(hass, config)
    return True
