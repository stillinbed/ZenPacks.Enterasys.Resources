__doc__="""CPU modeler plugin for the Enterasys switches which implement the ENTERASYS-RESOURCE-UTILIZATION-MIB"""

from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )

class CPUMap(SnmpPlugin):
    relname = 'etsys_cpu_units'
    modname = 'ZenPacks.Enterasys.Resources.EtsysCPU'

    snmpGetTableMaps = (
        GetTableMap(
            'etsysResourceCpuTable', '1.3.6.1.4.1.5624.1.2.49.1.1.1.1', {
                '.2': 'etsysResourceCpuLoad5sec',
                '.3': 'etsysResourceCpuLoad1min',
                '.4': 'etsysResourceCpuLoad5min',
                }
            ),
        )

    def process(self, device, results, log):
    
        cpus = results[1].get('etsysResourceCpuTable', {})

        rm = self.relMap()
        cpu_num = 0

        for snmpindex, row in cpus.items():
            #log.info(cpus.items())  
            cpu_num += 1
            
            rm.append(self.objectMap({
                'id': self.prepId("%s%0.2d" % ('cpu_', cpu_num)),
                'title': "%s%0.2d" % ('cpu_', cpu_num),
                'snmpindex': snmpindex.strip('.'),
                'cpuLoad5sec': row.get('etsysResourceCpuLoad5sec'),
                'cpuLoad1min': row.get('etsysResourceCpuLoad1min'),
                'cpuLoad5min': row.get('etsysResourceCpuLoad5min'),
                }))
				
        return rm
