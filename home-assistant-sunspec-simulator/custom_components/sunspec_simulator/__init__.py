"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from .sensor import setup_sunspec_sensors

DOMAIN = "sunspec_simulator"

def setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    hass.data[DOMAIN] = {}
    setup_sunspec_sensors(hass)
    return True