"""SunSpec Simulator Sensors."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
import datetime
import random

DOMAIN = "sunspec_simulator"

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
):
    """Set up the SunSpec simulator sensors."""
    sensors = [
        SunSpecPowerSensor(),
        SunSpecVoltageSensor(),
        SunSpecStatusSensor()
    ]
    
    async_add_entities(sensors, update_before_add=True)

    # 每30秒更新數據
    async_track_time_interval(hass, lambda now: update_sensors(sensors), datetime.timedelta(seconds=30))

def update_sensors(sensors):
    """更新所有 Sensor 狀態"""
    for sensor in sensors:
        sensor.async_schedule_update_ha_state(True)

class SunSpecPowerSensor(SensorEntity):
    """SunSpec Power Sensor."""
    def __init__(self):
        self._state = None
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

    async def async_update(self):
        """模擬功率數據"""
        self._state = random.uniform(50, 500)  
        self.async_write_ha_state()

class SunSpecVoltageSensor(SensorEntity):
    """SunSpec Voltage Sensor."""
    def __init__(self):
        self._state = None
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

    async def async_update(self):
        """模擬電壓數據"""
        self._state = random.uniform(220, 240)  
        self.async_write_ha_state()

class SunSpecStatusSensor(SensorEntity):
    """SunSpec Status Sensor."""
    def __init__(self):
        self._state = None
        self._attr_unique_id = "sunspec_simulator_status"

    @property
    def name(self):
        return "SunSpec Simulated Status"

    @property
    def state(self):
        return "ON" if self._state else "OFF"

    async def async_update(self):
        """模擬狀態數據"""
        self._state = random.choice([True, False])  
        self.async_write_ha_state()
