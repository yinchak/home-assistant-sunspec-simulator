"""SunSpec Simulator Sensors."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.const import UnitOfPower, UnitOfElectricPotential
from homeassistant.core import HomeAssistant
import random

DOMAIN = "sunspec_simulator"

class SunSpecPowerSensor(SensorEntity):
    """SunSpec Power Sensor."""
    def __init__(self, hass: HomeAssistant):
        self._hass = hass
        self._attr_unique_id = "sunspec_simulator_power"
        self._attr_device_class = "power"
        self._attr_unit_of_measurement = UnitOfPower.WATT
        self._attr_name = "SunSpec Simulated Power"
        self._state = None

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {"friendly_name": "模擬太陽能功率"}

    async def async_update(self):
        """Simulate power data."""
        self._state = random.uniform(50, 500)  # 假功率50-500W

class SunSpecVoltageSensor(SensorEntity):
    """SunSpec Voltage Sensor."""
    def __init__(self, hass: HomeAssistant):
        self._hass = hass
        self._attr_unique_id = "sunspec_simulator_voltage"
        self._attr_device_class = "voltage"
        self._attr_unit_of_measurement = UnitOfElectricPotential.VOLT
        self._attr_name = "SunSpec Simulated Voltage"
        self._state = None

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {"friendly_name": "模擬太陽能電壓"}

    async def async_update(self):
        """Simulate voltage data."""
        self._state = random.uniform(220, 240)  # 假電壓220-240V

class SunSpecStatusSensor(BinarySensorEntity):
    """SunSpec Status Sensor."""
    def __init__(self, hass: HomeAssistant):
        self._hass = hass
        self._attr_unique_id = "sunspec_simulator_status"
        self._attr_name = "SunSpec Simulated Status"
        self._state = None

    @property
    def is_on(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {"friendly_name": "模擬太陽能狀態"}

    async def async_update(self):
        """Simulate status data."""
        self._state = random.choice([True, False])  # 假狀態：運行或關閉
