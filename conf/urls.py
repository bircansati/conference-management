from django.urls import path, include
from .views import *

urlpatterns = [
    path('', conf_index, name='home'),
    path('<int:id>/', conf_detail, name='detail'),
    path('create/', conf_create, name="create"),
    path('smartcfp', smartcfp_view, name="smartcfp"),
    path('myconferences', myconference_view, name='myconferences'),
]
