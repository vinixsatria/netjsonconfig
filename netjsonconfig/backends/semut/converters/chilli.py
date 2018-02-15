from ...openwrt.converters.base import OpenWrtConverter

class Chilli(OpenWrtConverter):
    netjson_key = 'chilli'
    intermediate_key = 'chilli'
    _uci_types = ['chilli']

    def to_intermediate_loop(self, block, result, index=None):
        chilli = self.__intermediate_chilli(block)
        if chilli:
            result.setdefault('chilli', [])
            result['chilli'] = chilli
        return result

    def __intermediate_chilli(self, chilli):
        if not chilli:
            return

        chilli.update({
            '.type': 'chilli',
            '.name': chilli.pop('name', 'chilli'),
        })

        chilli['acctupdate'] = True
        chilli['macauth'] = True
        if 'disabled' in chilli and not chilli['disabled']:
            del chilli['disabled']
        if 'fg' in chilli and not chilli['fg']:
            del chilli['fg']
        if 'uamport' not in chilli:
            chilli['uamport'] = 3990
        if 'coaport' not in chilli:
            chilli['coaport'] = 3799
        if 'radiusauthport' not in chilli:
            chilli['radiusauthport'] = 1812
        if 'radiusacctport' not in chilli:
            chilli['radiusacctport'] = 1813
        if 'uamanydns' not in chilli or not chilli['uamanydns']:
            chilli['uamanydns'] = True
        if 'domain' not in chilli or not chilli['domain']:
            chilli['domain'] = 'kolonisemut.com'
        if 'nasip' not in chilli:
            chilli['nasip'] = chilli['uamlisten']
        if 'uamaliasname' not in chilli:
            chilli['uamaliasname'] = chilli['radiusnasid']
        if 'location' in chilli:
            loc = chilli.pop('location')
            if 'locname' in loc and loc['locname']:
                chilli['locationname'] = loc['locname']
                chilli['radiuslocationname'] = loc['locname'].replace('.', '_')

            location = ''
            if 'locisocc' in loc and loc['locisocc']:
                location = 'isocc=' + loc['locisocc']
            if 'loccc' in loc and loc['loccc']:
                location += ',cc=' + loc['loccc']
            if 'locac' in loc and loc['locac']:
                location += ',ac=' + loc['locac']
            if 'locrealm' in loc and loc['locrealm']:
                location += ',network=' + loc['locrealm']
            else:
                location += ',network=KoloniSemut'
            chilli['radiuslocationid'] = location
        elif chilli['locationname'] and 'radiuslocationname' not in chilli:
            chilli['radiuslocationname'] = chilli['locationname'].replace('.', '_')

        if chilli['radiuslocationid']:
            chilli['radiuslocationid'] += ',' + chilli['radiuslocationname']
        
        return [self.sorted_dict(chilli)]

    def to_netjson_loop(self, block, result, index):
        result['chilli'] = self.__netjson_chilli(block)
        return result

    def __netjson_chilli(self, chilli):
        del chilli['.type']
        _name = chilli.pop('.name')
        if _name or _name != 'chilli':
            chilli['name'] = _name
        return chilli
