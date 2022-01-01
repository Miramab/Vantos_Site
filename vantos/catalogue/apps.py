# from django.apps import AppConfig


# class CatalogueConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'catalogue'



# from oscar.apps.catalogue.apps import CatalogueConfig as CoreCatalogueConfig
import oscar.apps.catalogue.apps as apps
# from .views import IndexView
from django.conf.urls import url
from oscar.core.application import OscarConfig
from oscar.core.loading import get_class



class CatalogueConfig(apps.CatalogueConfig):
    name = 'catalogue'
    label = 'catalogue'
    verbose_name = 'Catalogue'


# class CatalogueConfig(CoreCatalogueConfig):
    def ready(self):
        super().ready()
        from catalogue.views import IndexView 
        # This is all - you don't need to mess with the URLs.
        self.home_view = get_class('catalogue.views','IndexView')
        self.detail_view = get_class('catalogue.views', 'ProductDetailView')
        self.catalogue_view = get_class('catalogue.views', 'CatalogueView')
        self.category_view = get_class('catalogue.views', 'ProductCategoryView')
        self.range_view = get_class('offer.views', 'RangeDetailView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            url(r'^$', self.home_view.as_view(), name='index'),
             url(r'catalogue/', self.catalogue_view.as_view(), name='index'),
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                self.detail_view.as_view(), name='detail'),
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                self.category_view.as_view(), name='category'),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range'),
        ]
        return self.post_process_urls(urls)
