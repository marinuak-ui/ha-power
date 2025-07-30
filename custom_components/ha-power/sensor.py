from homeassistant.components.sensor import SensorEntity

class HelloWorldSensor(SensorEntity):
    _attr_name = "Hello World Sensor"
    _attr_unique_id = "hello_world_sensor"
    _attr_icon = "mdi:hand-wave"

    @property
    def state(self):
        return "Hello, World!"