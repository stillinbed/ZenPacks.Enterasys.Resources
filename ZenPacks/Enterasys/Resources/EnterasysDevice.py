from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class EnterasysDevice(Device):

    _relations = Device._relations + (
        ('etsys_cpu_units', ToManyCont(ToOne,
            'ZenPacks.Enterasys.Resources.EtsysCPU',
            'etsys_cpu_device',
            )),
        ('etsys_storage_units', ToManyCont(ToOne,
            'ZenPacks.Enterasys.Resources.EtsysStorage',
            'etsys_storage_device',
            )),
        ('etsys_process_instances', ToManyCont(ToOne,
            'ZenPacks.Enterasys.Resources.EtsysProcess',
            'etsys_process_device',
            )),
        )