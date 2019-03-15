from django import forms
from .models import Investors
from .models import Stocks

class StockForm(forms.ModelForm):
	class Meta:
		model = Stocks
		fields = ['stockid', 'stocksymbol', 'numshares', 'purchaseprice', 'currentprice', 'datepurchased']
		labels = {'stockid': 'Stock ID', 'stocksymbol': 'Stock Symbol', 'numshares': 'Number of Shares', 'purchaseprice': 'Purchase Price' ,'currentprice': 'Current Price','datepurchased': 'Date Purchased (MM/DD/YYYY)'}
