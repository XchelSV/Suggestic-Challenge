from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^flattnes/sequence/$', FlattnesSequenceView.as_view()),
    url(r'^sequence/$', FlattnesSequenceListView.as_view()),
]
