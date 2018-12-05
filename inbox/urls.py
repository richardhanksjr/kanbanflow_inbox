from django.conf.urls import url
from .views import InboxItem

urlpatterns = [
    url(r'^$', InboxItem.as_view(), name='inbox'),
]
