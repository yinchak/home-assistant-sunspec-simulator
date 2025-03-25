"""SunSpec Simulator Custom Component."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .sensor import SunSpecPowerSensor, SunSpecVoltageSensor, SunSpecStatusSensor

DOMAIN = "sunspec_simulator"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SunSpec Simulator component."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            hass.config_entries.async_entries(DOMAIN)[0], "sensor"
        )
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            hass.config_entries.async_entries(DOMAIN)[0], "binary_sensor"
        )
    )
    return True

async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities: AddEntitiesCallback):
    """Set up SunSpec Simulator sensors."""
    sensors = [
        SunSpecPowerSensor(hass),
        SunSpecVoltageSensor(hass),
        SunSpecStatusSensor(hass)
    ]
    async_add_entities(sensors)
