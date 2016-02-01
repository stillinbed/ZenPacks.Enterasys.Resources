from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EtsysStorage(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EnterasysStorage'

    description = ""
    availableStorageSize = 0
    totalStorageSize = 0
 
    _properties = ManagedEntity._properties + (
        {'id': 'description', 'type': 'string'},
        {'id': 'availableStorageSize', 'type': 'int'},
        {'id': 'totalStorageSize', 'type': 'int'},
        )

    _relations = ManagedEntity._relations + (
        ('etsys_storage_device', ToOne(ToManyCont,
            'ZenPacks.Enterasys.Resources.EnterasysDevice',
            'etsys_storage_units',
            )),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.etsys_storage_device()

    def getRRDTemplateName(self):
        return 'Storage'

