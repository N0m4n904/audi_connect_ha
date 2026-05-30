"""Support for Audi Connect buttons."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.const import CONF_USERNAME

from .audi_entity import AudiEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Old way."""


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Audi buttons from a config entry."""
    buttons = []
    account = config_entry.data.get(CONF_USERNAME)
    audiData = hass.data[DOMAIN][account]

    for config_vehicle in audiData.config_vehicles:
        for button in config_vehicle.buttons:
            buttons.append(AudiButton(config_vehicle, button))

    async_add_entities(buttons)


class AudiButton(AudiEntity, ButtonEntity):
    """Representation of an Audi button."""

    async def async_press(self) -> None:
        """Press the button."""
        await self._instrument.press()
