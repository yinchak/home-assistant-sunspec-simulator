"""SunSpec Simulator Sensors."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_interval
import datetime
import random

DOMAIN = "sunspec_simulator"

async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    """Set up the SunSpec simulator sensors."""
    sensors = [
        SunSpecPowerSensor(hass),
        SunSpecVoltageSensor(hass),
        SunSpecStatusSensor(hass)
    ]
    
    # 註冊實體
    async_add_entities(sensors)

    # 每30秒更新一次數據
    async_track_time_interval(hass, lambda now: update_sensors(sensors), datetime.timedelta(seconds=30))

def update_sensors(sensors):
    """Update all sensors."""
    for sensor in sensors:
        sensor.async_schedule_update_ha_state(True)

class SunSpecPowerSensor(SensorEntity):
    """SunSpec Power Sensor."""
    def __init__(self, hass):
        self._state = None
        self._hass = hass
        self._attr_unique_id = "sunspec_simulator_power"
        self._attr_device_class = "power"

    @property
    def name(self):
        return "SunSpec Simulated Power"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return "W"

    @property
    def extra_state_attributes(self):
        return {"friendly_name": "模擬太陽能功率"}

    async def async_update(self):
        """Simulate power data."""
        self._state = random.uniform(50, 500)  # 假功率50-500W

class SunSpecVoltageSensor(SensorEntity):
    """SunSpec Voltage Sensor."""
    def __init__(self, hass):
        self._state = None
        self._hass = hass
        self._attr_unique_id = "sunspec_simulator_voltage"
        self._attr_device_class = "voltage"

    @property
    def name(self):
        return "SunSpec Simulated Voltage"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return "V"

    @property
    def extra_state_attributes(self):
        return {"friendly_name": "模擬太陽能電壓"}

    async def async_update(self):
        """Simulate voltage data."""
        self._state = random.uniform(220, 240)  # 假電壓220-240V

class SunSpecStatusSensor(BinarySensorEntity):
    """SunSpec Status Sensor."""
    def __init__(self, hass):
        self._state = None
        self._hass = hass
        self._attr_unique_id = "sunspec_simulator_status"

    @property
    def name(self):
        return "SunSpec Simulated Status"

    @property
    def is_on(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {"friendly_name": "模擬太陽能狀態"}

    async def async_update(self):
        """Simulate status data."""
        self._state = random.choice([True, False])  # 假狀態：運行或關閉
