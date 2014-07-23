# -*- coding: utf-8 -*-

from icebergsdk.resources.base import IcebergObject

class OrderItem(IcebergObject):
    endpoint = 'order_item'

    def cancel(self):
        raise NotImplementedError()

    def confirm(self):
        raise NotImplementedError()

    def send(self):
        raise NotImplementedError()



class MerchantOrder(IcebergObject):
    endpoint = 'merchant_order'

    def cancel(self):
        raise NotImplementedError()

    def confirm(self):
        raise NotImplementedError()

    def send(self):
        raise NotImplementedError()


class Order(IcebergObject):
    endpoint = 'order'

    def authorizeOrder(self, params = None):
        params = params or {}
        data = self.request("%s%s/" % (self.resource_uri, 'authorizeOrder'), method = "post", post_args = params)
        return self._load_attributes_from_response(**data)

    def updateOrderPayment(self):
        data = self.request("%s%s/" % (self.resource_uri, 'updateOrderPayment'), method = "post")
        return self._load_attributes_from_response(**data)

    def cancel(self):
        raise NotImplementedError()

    # Seller Related
    def confirm(self):
        raise NotImplementedError()



