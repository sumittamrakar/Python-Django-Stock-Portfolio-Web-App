#from django.urls import url

from django.conf.urls import url
from . import views


app_name = 'stocks_project'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #Page for adding a new stock
    url(r'^new_stock/$', views.new_stock, name="new_stock")

]
