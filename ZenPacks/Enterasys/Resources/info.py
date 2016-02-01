from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.Enterasys.Resources.interfaces import (
        IEtsysCPUInfo,
        IEtsysStorageInfo,
        IEtsysProcessInfo,
        )
    
class EtsysCPUInfo(ComponentInfo):
    implements(IEtsysCPUInfo)

    snmpindex = ProxyProperty('snmpindex')
    
class EtsysStorageInfo(ComponentInfo):
    implements(IEtsysStorageInfo)

    description = ProxyProperty('description')
    snmpindex = ProxyProperty('snmpindex')
    availableStorageSize = ProxyProperty('availableStorageSize')
    totalStorageSize = ProxyProperty('totalStorageSize')
    
class EtsysProcessInfo(ComponentInfo):
    implements(IEtsysProcessInfo)
    
    snmpindex = ProxyProperty('snmpindex')