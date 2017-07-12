from . import converters
from .renderer import *
from ..base.backend import BaseBackend
from .schema import schema


class Raspbian(BaseBackend):
    """
    Raspbian Backend
    """
    schema = schema
    env_path = 'netjsonconfig.backends.raspbian'
    converters = [
        converters.General,
        converters.Interfaces,
        converters.Wireless,
        converters.DnsServers,
        converters.DnsSearch,
        converters.Ntp
    ]
    renderers = [
        Hostname,
        Hostapd,
        Interfaces,
        Resolv,
        Ntp
    ]

    def render(self, files=True):
        self.validate()
        if self.intermediate_data is None:
            self.to_intermediate()
        output = ''
        for renderer_class in self.renderers:
            renderer = renderer_class(self)
            output += renderer.render()
            del renderer
        return output
