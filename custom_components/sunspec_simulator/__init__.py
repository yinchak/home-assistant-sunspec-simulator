"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .sensor import async_setup_entry

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up SunSpec Simulator from a config entry."""
    await async_setup_entry(hass, entry)
    return True
