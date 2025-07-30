from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

class HaPowerSensor(SensorEntity):
    _attr_name = "HA Power Sensor"
    _attr_unique_id = "ha_power_sensor"
    _attr_icon = "mdi:flash"

    @property
    def state(self):
        return "Hello, Power World!"