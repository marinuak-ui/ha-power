from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN, PLATFORM
from .sensor import HelloWorldSensor

async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities: AddEntitiesCallback):
    async_add_entities([HelloWorldSensor()])
    return True