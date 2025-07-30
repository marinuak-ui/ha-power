from .sensor import HelloWorldSensor

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([HelloWorldSensor()])
    return True