"""
Koloni specific JSON-Schema definition
(extends OpenWrt JSON-Schema)
"""
from ...utils import merge_config
from ..openwrt.schema import schema as openwrt_schema

schema = merge_config(openwrt_schema, {
    "properties": {
        "chilli": {
            "type": "object",
            "title": "CoovaChilli Settings",
            "additionalProperties": True,
            "required": [
                "tundev", "dhcpif", "net",
                "uamlisten", "uamsecret",
                "uamserver", "uamhompage",
                "uamsecret", "uamallowed",
                "radiusserver1", "radiusserver2", "radiussecret",
                "radiusnasid", "locationname", "radiuslocationid",
                
            ],
            "properties": {
                "disabled": {
                    "type": "boolean",
                    "title": "Disable CoovaChilli",
                    "default": False,
                    "format": "checkbox",
                    "propertyOrder": 1,
                },
                "domain": {
                    "type": "string",
                    "title": "Domain name",
                    "description": "Domain to use for DNS lookups. If empty default='coova.org'"
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "kolonisemut.com",
                    "propertyOrder": 2,
                },
                "tundev": {
                    "type": "string",
                    "title": "TUN Device",
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "tun0",
                    "propertyOrder": 3,
                },
                "dhcpif": {
                    "type": "string",
                    "title": "DHCP Interface",
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "wlan0",
                    "propertyOrder": 4,
                },
                "net": {
                    "type": "string",
                    "title": "Network Interface",
                    "minLength": 10,
                    "maxLength": 31,
                    "default": "",
                    "propertyOrder": 5,
                },
                "uamlisten": {
                    "type": "string",
                    "title": "UAM Listen IP",
                    "minLength": 10,
                    "maxLength": 31,
                    "default": "",
                    "propertyOrder": 6,
                },
                "uamport": {
                    "type": "integer",
                    "title": "UAM Listen Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 3990,
                },
                "coaport": {
                    "type": "integer",
                    "title": "CoovaChilli CoA Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 3799,
                },
                "uamhompage": {
                    "type": "string",
                    "title": "UAM Homepage URL",
                    "minLength": 10,
                    "maxLength": 255,
                    "default": "http://www.kolonisemut.com/splash",
                    "propertyOrder": 7,
                },
                "uamserver": {
                    "type": "string",
                    "title": "UAM Server URL",
                    "minLength": 10,
                    "maxLength": 255,
                    "default": "http://www.kolonisemut.com",
                    "propertyOrder": 8,
                },
                "uamsecret": {
                    "type": "string",
                    "title": "UAM Secret Key",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 9,
                },
                "uamallowed": {
                    "type": "string",
                    "title": "UAM Dommain Allowed without Authenticating",
                    "minLength": 10,
                    "maxLength": 1024,
                    "default": "www.kolonisemut.com,kolonisemut.com,bit.kolonisemut.com",
                    "propertyOrder": 10,
                },
                "radiusserver1": {
                    "type": "string",
                    "title": "Radius Server #1",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "voucher.kolonisemut.com",
                    "propertyOrder": 11,
                },
                "radiusserver2": {
                    "type": "string",
                    "title": "Radius Server #2",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "5.170.0.2",
                    "propertyOrder": 12,
                },
                "radiusauthport": {
                    "type": "integer",
                    "title": "UAM Listen Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 1812,
                },
                "radiusacctport": {
                    "type": "integer",
                    "title": "UAM Listen Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 1813,
                },
                "radiussecret": {
                    "type": "string",
                    "title": "Radius Secret Key",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 13,
                },
                "radiusnasid": {
                    "type": "string",
                    "title": "Radius NAS-Identifier",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 14,
                },
                "locationname": {
                    "type": "string",
                    "title": "NAS Location Name",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 15,
                },
                "radiuslocationid": {
                    "type": "string",
                    "title": "NAS Location ID",
                    "minLength": 10,
                    "maxLength": 255,
                    "default": "isocc=ID,cc=62,ac=031,network=KoloniSemut",
                    "propertyOrder": 16,
                },
                

                "uamanydns": {
                    "type": "boolean",
                    "title": "Foreground Process",
                    "default": True,
                    "format": "checkbox",
                },
                "dns1": {
                    "type": "string",
                    "title": "Network Interface",
                    "minLength": 7,
                    "maxLength": 15,
                    "default": "8.8.8.8",
                },
                "dns2": {
                    "type": "string",
                    "title": "Network Interface",
                    "minLength": 7,
                    "maxLength": 15,
                    "default": "8.8.4.4",
                },
                "nasip": {
                    "type": "string",
                    "title": "Radius NAS-IP-Address Attribute",
                    "minLength": 7,
                    "maxLength": 15,
                    "default": "",
                },

                # OPSIONAL
                "network": {
                    "type": "string",
                    "title": "Network Interface",
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "lan",
                },
                "interval": {
                    "type": "integer",
                    "title": "Interval Re-read Configuration",
                    "minimum": 120,
                    "maximum": 86400,
                    "default": 3600,
                },
                "statedir": {
                    "type": "string",
                    "title": "State Directory",
                    "minLength": 5,
                    "maxLength": 100,
                    "default": "./",
                },
                
                "fg": {
                    "type": "boolean",
                    "title": "Foreground Process",
                    "default": False,
                    "format": "checkbox",
                },
                "debug": {
                    "type": "integer",
                    "title": "Debug Level",
                    "minimum": 1,
                    "maximum": 9,
                    "default": 9,
                },
            }        
        }
    }
})
