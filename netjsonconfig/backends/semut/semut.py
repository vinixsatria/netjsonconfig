from . import converters
from ..openwrt.openwrt import OpenWrt
from .schema import schemaß

class Semut(OpenWrt):
    """
    Custom Semut Configuration Backend
    """
    schema = schema

    def __init__(self, config=None, native=None, templates=None, context=None):
        super(Semut, self).__init__(config, native, templates, context);

        # Tambahkan converter Chilli
        self.converters.append(converters.Chilli)
