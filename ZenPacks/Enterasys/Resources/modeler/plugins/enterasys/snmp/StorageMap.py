__doc__="""Storage modeler plugin for the Enterasys switches which implement the ENTERASYS-RESOURCE-UTILIZATION-MIB"""

from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )

class StorageMap(SnmpPlugin):
    relname = 'etsys_storage_units'
    modname = 'ZenPacks.Enterasys.Resources.EtsysStorage'

    snmpGetTableMaps = (
        GetTableMap(
            'etsysResourceStorageTable', '1.3.6.1.4.1.5624.1.2.49.1.3.1.1', {
                '.3': 'etsysResourceStorageDescr',
                '.4': 'etsysResourceStorageSize',
                '.5': 'etsysResourceStorageAvailable',
                }
            ),
        )

    def process(self, device, results, log):
        
        storage = results[1].get('etsysResourceStorageTable', {})
        rm = self.relMap()
        stor_num = 0
        
        for snmpindex, row in storage.items():    
            etsys_stor_size = row.get('etsysResourceStorageSize')
            
            if etsys_stor_size < 1:
                log.info('Skipping Enterasys storage unit with zero storage size')
                continue
            #log.info(storage.items())    
            stor_num += 1
            
            rm.append(self.objectMap({
                'id': self.prepId("%s%0.2d" % ('storage_', stor_num)),
                'title': "%s%0.2d" % ('storage_', stor_num),
                'snmpindex': snmpindex.strip('.'),
                'description': row.get('etsysResourceStorageDescr'),
                'availableStorageSize': row.get('etsysResourceStorageAvailable'),
                'totalStorageSize': row.get('etsysResourceStorageSize'),
                }))

        return rm