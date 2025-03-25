"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.discovery import async_load_platform

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up SunSpec Simulator."""
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up SunSpec Simulator from a config entry."""
    hass.async_create_task(async_load_platform(hass, "sensor", DOMAIN, {}, entry))
    return True
