"""
Koloni specific JSON-Schema definition
(extends OpenWrt JSON-Schema)
"""
from ...utils import merge_config
from ..openwrt.schema import schema as openwrt_schema
from .chillischema import schema as chilli_schema

schema = merge_config(openwrt_schema, chilli_schema)
