"""SunSpec Simulator Sensors."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
import datetime
import random

DOMAIN = "sunspec_simulator"

async def async_setup_platform(
    hass: HomeAssistant, config, async_add_entities: AddEntitiesCallback, discovery_info=None
):
    """Set up SunSpec simulator sensors."""
    sensors = [
        SunSpecSensor("Power", "W", 50, 500, "power"),
        SunSpecSensor("Voltage", "V", 220, 240, "voltage"),
        SunSpecSensor("Status", None, 0, 1, "status", status=True),
    ]

    async_add_entities(sensors, update_before_add=True)  # **✅ 確保正確使用 async_add_entities()**

    # 每 30 秒更新數據
    async_track_time_interval(hass, lambda now: update_sensors(sensors), datetime.timedelta(seconds=30))

def update_sensors(sensors):
    """更新所有 Sensor 狀態"""
    for sensor in sensors:
        sensor.async_schedule_update_ha_state(True)

class SunSpecSensor(SensorEntity):
    """通用 SunSpec Sensor"""
    def __init__(self, name, unit, min_value, max_value, sensor_type, status=False):
        self._state = None
        self._name = f"SunSpec Simulated {name}"
        self._unit = unit
        self._min = min_value
        self._max = max_value
        self._status = status
        self._sensor_type = sensor_type
        self._attr_unique_id = f"sunspec_simulator_{sensor_type}"
        self._attr_device_class = "power" if sensor_type == "power" else "voltage" if sensor_type == "voltage" else None
        self._attr_state_class = "measurement" if sensor_type in ["power", "voltage"] else None
        self._attr_entity_id = f"sensor.sunspec_simulator_{sensor_type}"  # **✅ 正確設定 entity_id**
    
    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def unique_id(self):
        """提供 `entity_id`，避免 `NoEntitySpecifiedError`"""
        return self._attr_unique_id
    
    @property
    def entity_id(self):
        """確保 Home Assistant 能夠識別 `entity_id`"""
        return self._attr_entity_id

    async def async_update(self):
        """生成模擬數據"""
        if self._status:
            self._state = "ON" if random.choice([True, False]) else "OFF"
        else:
            self._state = random.uniform(self._min, self._max)
        self.async_write_ha_state()
