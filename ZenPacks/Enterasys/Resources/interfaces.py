from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IEtsysCPUInfo(IComponentInfo):
    snmpindex = schema.TextLine(title=_t('Resource Index'))

class IEtsysStorageInfo(IComponentInfo):
    description = schema.TextLine(title=_t('Description'))
    snmpindex = schema.TextLine(title=_t('Resource Index'))
    availableStorageSize = schema.TextLine(title=_t('Available Storage Size'))
    totalStorageSize = schema.TextLine(title=_t('Total Storage Size'))
    
class IEtsysProcessInfo(IComponentInfo):
    snmpindex = schema.TextLine(title=_t('Resource Index'))
