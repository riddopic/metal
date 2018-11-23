#
# Copyright (c) 2015 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

# -*- encoding: utf-8 -*-
#

from inventoryclient.common import base
import json


class PciDevice(base.Resource):
    def __repr__(self):
        return "<PciDevice %s>" % self._info


class PciDeviceManager(base.Manager):
    resource_class = PciDevice

    def list(self, host_id):
        path = '/v1/hosts/%s/pci_devices' % host_id
        return self._list(path, "pci_devices")

    def list_all(self):
        path = '/v1/pci_devices'
        return self._list(path, "pci_devices")

    def get(self, pci_id):
        path = '/v1/pci_devices/%s' % pci_id
        try:
            return self._list(path)[0]
        except IndexError:
            return None

    def update(self, pci_id, patch):
        path = '/v1/pci_devices/%s' % pci_id
        return self._update(path,
                            data=(json.dumps(patch)))


def get_pci_device_display_name(p):
    if p.name:
        return p.name
    else:
        return '(' + str(p.uuid)[-8:] + ')'
