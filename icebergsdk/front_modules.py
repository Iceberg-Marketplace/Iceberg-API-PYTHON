# -*- coding: utf-8 -*-
import logging

from icebergsdk.mixins.request_mixin import IcebergRequestBase

logger = logging.getLogger('icebergsdk.frontmodules')

class FrontModules(IcebergRequestBase):
    cache_key = "icebergsdk:frontmodule:data"
    cache_expire = 60*60 # one hour

    def __init__(self, *args, **kwargs):
        super(FrontModules, self).__init__(*args, **kwargs)
        self.cache = kwargs.get('cache', None)


    def get_module_data(self, module_name):
        return self.modules_data['modules'][module_name]

    ####
    #   Loader
    ####
    @property
    def modules_data(self):
        """
        Helper to fetch Iceberg client side javascript templates
        """
        if hasattr(self, "_modules_data"):
            return getattr(self, "_modules_data")

        if self.cache:
            data = self.cache.get(self.cache_key, False)
            if data:
                setattr(self, '_modules_data', data)
                return data

        data = self.request(self.conf.ICEBERG_MODULES_URL)
        setattr(self, '_modules_data', data)
        if self.cache:
            self.cache.set(self.cache_key, data, self.cache_expire)

        return data

