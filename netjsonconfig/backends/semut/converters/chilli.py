from .base import OpenWrtConverter

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
        if 'chilli' not in chilli:
            return

        chilli.update({
            '.type': 'chilli',
            '.name': chilli.pop('name', 'chilli'),
        })

        chilli['acctupdate'] = True
        chilli['macauth'] = True
        if 'uamport' not in chilli:
            chilli['uamport'] = 3990
        if 'coaport' not in chilli:
            chilli['coaport'] = 3799
        if 'radiusauthport' not in chilli:
            chilli['radiusauthport'] = 1812
        if 'radiusacctport' not in chilli:
            chilli['radiusacctport'] = 1813
        if 'uamanydns' not in chilli:
            chilli['uamanydns'] = True
        if 'domain' not in chilli or not chilli['domain']:
            chilli['domain'] = 'kolonisemut.com'
        if 'nasip' not in chilli:
            chilli['nasip'] = chilli['uamlisten']
        if 'uamaliasname' not in chilli:
            chilli['uamaliasname'] = chilli['radiusnasid']
        if 'radiuslocationname' not in chilli:
            chilli['radiuslocationname'] = chilli['locationname'].replace('.', '_')
        if chilli['radiuslocationid']:
            chilli['radiuslocationid'] += ',' + chilli['radiuslocationname']
        
        return [self.sorted_dict(chilli)]

    def to_netjson_loop(self, block, result, index):
        result['chilli'] = self.__netjson_chilli(block)
        return result

    def __netjson_chilli(self, chilli):
        del chilli['.type']
        _name = system.pop('.name')
        if _name or _name != 'chilli':
            chilli['name'] = _name
        return chilli
