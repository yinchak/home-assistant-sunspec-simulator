"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up SunSpec Simulator from a config entry."""
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "sensor"))
    return True
