from ...countries import countries

"""
Koloni specific JSON-Schema definition
"""
schema = {
    "properties": {
        #"general": {
        #    "required": ["hostname"]
        #},
        "chilli": {
            "type": "object",
            "title": "Hotspot Settings",
            "additionalProperties": True,
            "required": [
                "domain",
                "tundev", "dhcpif", "net",
                "uamlisten", "uamserver", "uamhompage",
                "uamsecret", "uamallowed",
                "radiusserver1", "radiusserver2", "radiussecret",
                "radiusnasid", "locationname",
                
            ],
            "properties": {
                "disabled": {
                    "type": "boolean",
                    "title": "Disable Hotspot",
                    "default": False,
                    "format": "checkbox",
                    "propertyOrder": 0,
                },
                "domain": {
                    "type": "string",
                    "title": "Domain name",
                    "description": "Domain to use for DNS lookups",
                    "minLength": 3,
                    "maxLength": 64,
                    "default": "kolonisemut.com",
                    "propertyOrder": 1,
                },
                "tundev": {
                    "type": "string",
                    "title": "TUN Device",
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "tun0",
                    "propertyOrder": 2,
                },
                "dhcpif": {
                    "type": "string",
                    "title": "DHCP Interface",
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "wlan0",
                    "propertyOrder": 3,
                },
                "net": {
                    "type": "string",
                    "title": "Netmask",
                    "minLength": 7,
                    "maxLength": 31,
                    "default": "",
                    "propertyOrder": 4,
                },
                "uamlisten": {
                    "type": "string",
                    "title": "UAM Listen IP",
                    "minLength": 7,
                    "maxLength": 31,
                    "default": "",
                    "propertyOrder": 5,
                },
                "uamport": {
                    "type": "integer",
                    "title": "UAM Listen Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 3990,
                    "propertyOrder": 6,
                },
                "coaport": {
                    "type": "integer",
                    "title": "CoA Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 3799,
                    "propertyOrder": 7,
                },
                "uamhompage": {
                    "type": "string",
                    "title": "UAM Homepage URL",
                    "minLength": 10,
                    "maxLength": 255,
                    "default": "http://www.kolonisemut.com/splash",
                    "propertyOrder": 8,
                },
                "uamserver": {
                    "type": "string",
                    "title": "UAM Server URL",
                    "minLength": 10,
                    "maxLength": 255,
                    "default": "http://www.kolonisemut.com",
                    "propertyOrder": 9,
                },
                "uamsecret": {
                    "type": "string",
                    "title": "UAM Secret Key",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 10,
                },
                "uamallowed": {
                    "type": "string",
                    "title": "UAM Dommain Allowed without Authenticating",
                    "minLength": 10,
                    "maxLength": 1024,
                    "default": "www.kolonisemut.com,kolonisemut.com,bit.kolonisemut.com",
                    "propertyOrder": 11,
                },
                "radiusserver1": {
                    "type": "string",
                    "title": "Radius Server #1",
                    "minLength": 7,
                    "maxLength": 64,
                    "default": "voucher.kolonisemut.com",
                    "propertyOrder": 12,
                },
                "radiusserver2": {
                    "type": "string",
                    "title": "Radius Server #2",
                    "minLength": 7,
                    "maxLength": 64,
                    "default": "5.170.0.2",
                    "propertyOrder": 13,
                },
                "radiusauthport": {
                    "type": "integer",
                    "title": "Radius Auth Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 1812,
                    "propertyOrder": 14,
                },
                "radiusacctport": {
                    "type": "integer",
                    "title": "Radius Acct Port",
                    "minimum": 1,
                    "maximum": 9999,
                    "default": 1813,
                    "propertyOrder": 15,
                },
                "radiussecret": {
                    "type": "string",
                    "title": "Radius Secret Key",
                    "minLength": 10,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 16,
                },
                "radiusnasid": {
                    "type": "string",
                    "title": "Radius NAS-Identifier",
                    "minLength": 7,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 17,
                },
                "locationname": {
                    "type": "string",
                    "title": "NAS Location Name",
                    "minLength": 7,
                    "maxLength": 64,
                    "default": "",
                    "propertyOrder": 19,
                },
                "radiuslocationid": {
                    "type": "string",
                    "title": "NAS Location ID",
                    "minLength": 7,
                    "maxLength": 255,
                    "default": "isocc=ID,cc=62,ac=031,network=KoloniSemut",
                    "propertyOrder": 20,
                },
                "location": {
                    "type": "object",
                    "title": "Location Attributes",
                    "propertyOrder": 20,
                    "required": [
                        "locname", "locisocc",
                        "loccc", "locac"
                    ],
                    "properties": {
                        "locname": {
                            "type": "string",
                            "title": "NAS Name",
                            "minLength": 2,
                            "maxLength": 64,
                            "default": "",
                            "propertyOrder": 19,
                        },
                        "locisocc": {
                            "type": "string",
                            "title": "Country",
                            "maxLength": 2,
                            "default": "62",
                            "enum": list(countries.values()),
                            "options": {"enum_titles": list(countries.keys())},
                            "propertyOrder": 7,
                        },
                        "loccc": {
                            "type": "string",
                            "title": "Phone Prefix",
                            "minLength": 2,
                            "maxLength": 4,
                            "default": "62",
                            "propertyOrder": 19,
                        },
                        "locac": {
                            "type": "string",
                            "title": "Phone Area Code",
                            "minLength": 2,
                            "maxLength": 6,
                            "default": "031",
                            "propertyOrder": 19,
                        },
                        
                    }
                },
                

                "uamanydns": {
                    "type": "boolean",
                    "title": "Allow any DNS",
                    "default": True,
                    "format": "checkbox",
                    "propertyOrder": 21,
                },
                "dns1": {
                    "type": "string",
                    "title": "DNS #1",
                    "minLength": 7,
                    "maxLength": 15,
                    "default": "8.8.8.8",
                    "propertyOrder": 22,
                },
                "dns2": {
                    "type": "string",
                    "title": "DNS #2",
                    "minLength": 7,
                    "maxLength": 15,
                    "default": "8.8.4.4",
                    "propertyOrder": 23,
                },
                "nasip": {
                    "type": "string",
                    "title": "Radius NAS-IP-Address Attribute",
                    "minLength": 0,
                    "maxLength": 15,
                    "default": "",
                    "propertyOrder": 24,
                },

                # OPSIONAL
                "network": {
                    "type": "string",
                    "title": "Network Interface",
                    "minLength": 3,
                    "maxLength": 10,
                    "default": "lan",
                    "propertyOrder": 25,
                },
                "interval": {
                    "type": "integer",
                    "title": "Interval Re-read Configuration",
                    "minimum": 120,
                    "maximum": 86400,
                    "default": 3600,
                    "propertyOrder": 26,
                },
                "statedir": {
                    "type": "string",
                    "title": "State Directory",
                    "minLength": 1,
                    "maxLength": 100,
                    "default": "./",
                    "propertyOrder": 27,
                },
                
                "fg": {
                    "type": "boolean",
                    "title": "Foreground Process",
                    "default": False,
                    "format": "checkbox",
                    "propertyOrder": 28,
                },
                "debug": {
                    "type": "integer",
                    "title": "Debug Level",
                    "minimum": 1,
                    "maximum": 9,
                    "default": 9,
                    "propertyOrder": 29,
                },
            }        
        }
    }
}