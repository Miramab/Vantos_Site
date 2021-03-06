from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from oscar.core.application import *

from . import views


class RazorpayDashboardApplication():
    name = None
    list_view = views.TransactionListView
    detail_view = views.TransactionDetailView

    def get_urls(self):
        urlpatterns = (
            url(r'^transactions/$', self.list_view.as_view(),
                name='razorpay-list'),
            url(r'^transactions/(?P<pk>\d+)/$', self.detail_view.as_view(),
                name='razorpay-detail'),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = RazorpayDashboardApplication()
