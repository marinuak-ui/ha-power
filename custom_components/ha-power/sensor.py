from homeassistant.components.sensor import SensorEntity

class HelloWorldSensor(SensorEntity):
    def __init__(self):
        self._state = "Hello, World!"

    @property
    def name(self):
        return "Hello World Sensor"

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return "mdi:hand-wave"