# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from oscar.app import application
from djangocms_apphook_setup.base import AutoCMSAppMixin 
from .menu import CategoriesMenu


@apphook_pool.register
class OscarApp(AutoCMSAppMixin,CMSApp):
    """
    Allows "mounting" the oscar shop and all of its urls to a specific CMS page.
    e.g at "/shop/"
    """
    name = _("Oscar App")
    exclude_permissions = ['dashboard']
    
    # djangocms-apphook-setup attribute
    auto_setup = {
        'enabled': True,
        'home title': 'home title',
        'page title': 'Shop',
        'sites': True,
    }
    
    def get_menus(self, page=None, language=None, **kwargs):
        return [CategoriesMenu]
    
    def get_urls(self, page=None, language=None, **kwargs):
        return application.urls[0]

# trigger djangocms-apphook-setup function
OscarApp.setup()
