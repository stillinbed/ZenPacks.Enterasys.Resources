from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EtsysProcess(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EnterasysProcess'
    
    snmpindex = None

    _properties = ManagedEntity._properties + (
        )

    _relations = ManagedEntity._relations + (
        ('etsys_process_device', ToOne(ToManyCont,
            'ZenPacks.Enterasys.Resources.EnterasysDevice',
            'etsys_process_instances',
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
        return self.etsys_process_device()

    def getRRDTemplateName(self):
        return 'ProcessCPULoad'

