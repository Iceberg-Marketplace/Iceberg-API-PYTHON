# -*- coding: utf-8 -*-

from icebergsdk.resources.base import IcebergObject

class HipayTransaction(IcebergObject):
    endpoint = 'hipay_transaction'

    def update_order_status(self, orderid):
        return self.request("%s/updateOrderStatus/?order_id=%s" % (
            self.endpoint,
            orderid,
        ))
