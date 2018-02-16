from django.conf.urls import url

from batch_requests.views import handle_batch_requests
from tests.test_views import SimpleView, EchoHeaderView, ExceptionView,\
    SleepingView


urlpatterns = [
    url(r'^views/', SimpleView.as_view()),
    url(r'^echo/', EchoHeaderView.as_view()),
    url(r'^exception/', ExceptionView.as_view()),
    url(r'^sleep/', SleepingView.as_view()),
    url(r'^api/v1/batch/', handle_batch_requests),
]
