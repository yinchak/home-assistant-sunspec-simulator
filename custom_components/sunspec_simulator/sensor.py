"""SunSpec Simulator Sensors."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
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

    async_add_entities(sensors, update_before_add=True)  # **✅ 正確使用 async_add_entities()**

    # 每 30 秒更新數據
    async_track_time_interval(hass, lambda now: update_sensors(sensors), datetime.timedelta(seconds=30))

def update_sensors(sensors):
    """更新所有 Sensor 狀態"""
    for sensor in sensors:
        sensor.async_schedule_update_ha_state(True)
