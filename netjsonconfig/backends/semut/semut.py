from .converters.chilli import Chilli
from ..openwrt.openwrt import OpenWrt
from .schema import schema

class Semut(OpenWrt):
    """
    Custom Semut Configuration Backend
    """
    schema = schema

    def __init__(self, config=None, native=None, templates=None, context=None):
        super(Semut, self).__init__(config, native, templates, context);

        # Tambahkan converter Chilli
        self.converters.append(Chilli)
