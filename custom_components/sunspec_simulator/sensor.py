"""SunSpec Simulator Sensors."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
import datetime
import random

DOMAIN = "sunspec_simulator"

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities: AddEntitiesCallback, discovery_info=None):
    """Set up SunSpec simulator sensors."""
    sensors = [
        SunSpecSensor("Power", "W", 50, 500),
        SunSpecSensor("Voltage", "V", 220, 240),
        SunSpecSensor("Status", None, 0, 1, status=True)
    ]

    async_add_entities(sensors, update_before_add=True)

    # 每 30 秒更新數據
    async_track_time_interval(hass, lambda now: update_sensors(sensors), datetime.timedelta(seconds=30))

def update_sensors(sensors):
    """更新所有 Sensor 狀態"""
    for sensor in sensors:
        sensor.async_schedule_update_ha_state(True)

class SunSpecSensor(SensorEntity):
    """通用 SunSpec Sensor"""
    def __init__(self, name, unit, min_value, max_value, status=False):
        self._state = None
        self._name = f"SunSpec Simulated {name}"
        self._unit = unit
        self._min = min_value
        self._max = max_value
        self._status = status
        self._attr_unique_id = f"sunspec_simulator_{name.lower()}"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    async def async_update(self):
        """生成模擬數據"""
        if self._status:
            self._state = "ON" if random.choice([True, False]) else "OFF"
        else:
            self._state = random.uniform(self._min, self._max)
        self.async_write_ha_state()
