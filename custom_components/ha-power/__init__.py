from homeassistant.core import HomeAssistant
from .config_flow import HaPowerConfigFlow
from .sensor import HaPowerSensor

async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    async_add_entities([HaPowerSensor()])
    return True