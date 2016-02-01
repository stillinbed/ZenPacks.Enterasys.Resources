(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'EnterasysCPU',
    _t('CPU'),
    _t('CPUs'));
    
ZC.registerName(
    'EnterasysStorage',
    _t('Storage'),
    _t('Storage'));
    
ZC.registerName(
    'EnterasysProcess',
    _t('Process'),
    _t('Processes'));
    
ZC.EnterasysCPUPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EnterasysCPU',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'snmpindex'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 150
            },{
                id: 'snmpindex',
                dataIndex: 'snmpindex',
                header: _t('Resource Index'),
                sortable: true,
                width: 150
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 70
            }]
        });

        ZC.EnterasysCPUPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EnterasysStoragePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EnterasysStorage',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'description'},
                {name: 'snmpindex'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 150
            },{
                id: 'snmpindex',
                dataIndex: 'snmpindex',
                header: _t('Resource Index'),
                sortable: true,
                width: 150
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true,
                width: 150
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 70
            }]
        });

        ZC.EnterasysStoragePanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EnterasysProcessPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EnterasysProcess',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'snmpindex'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width: 150
            },{
                id: 'snmpindex',
                dataIndex: 'snmpindex',
                header: _t('Resource Index'),
                sortable: true,
                width: 150
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 70
            }]
        });

        ZC.EnterasysProcessPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('EnterasysCPUPanel', ZC.EnterasysCPUPanel);
Ext.reg('EnterasysStoragePanel', ZC.EnterasysStoragePanel);
Ext.reg('EnterasysProcessPanel', ZC.EnterasysProcessPanel);

})();