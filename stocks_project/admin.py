from django.contrib import admin

# Import models for stocks and investors information

from stocks_project.models import Stocks
from stocks_project.models import Investors

# Register your models here.
admin.site.register(Stocks)
admin.site.register(Investors)
