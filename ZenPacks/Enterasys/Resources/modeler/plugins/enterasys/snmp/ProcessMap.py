__doc__="""Processes modeler plugin for the Enterasys switches which implement the ENTERASYS-RESOURCE-UTILIZATION-MIB"""

from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )

class ProcessMap(SnmpPlugin):
    relname = 'etsys_process_instances'
    modname = 'ZenPacks.Enterasys.Resources.EtsysProcess'

    snmpGetTableMaps = (
        GetTableMap(
            'etsysResourceProcessTable', '1.3.6.1.4.1.5624.1.2.49.1.2.1.1', {
                '.2': 'etsysResourceProcessName',
                }
            ),
        )

    def process(self, device, results, log):
	
        etsys_process_table = results[1].get('etsysResourceProcessTable', {})
        rm = self.relMap()
        
        for snmpindex, row in etsys_process_table.items():
            
            etsys_proc_name = row.get('etsysResourceProcessName')
            
            if not etsys_proc_name:
                log.info('Skipping Enterasys process with no name')
                continue
                
            rm.append(self.objectMap({
                'id': self.prepId(etsys_proc_name),
                'title': str(etsys_proc_name),
                'snmpindex': snmpindex.strip('.'),
                }))
        
        return rm