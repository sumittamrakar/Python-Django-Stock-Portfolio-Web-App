from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Stocks
from .models import Investors
from .forms import StockForm

# Create your views here.

def index(request):
	#Get info for the investor with investorId = 1
	investorObject = Investors.objects.get(investorid=1)
	#Get info for all stock objects
	stockObjects = Stocks.objects.all()
	context = {'stocks': stockObjects, 'investor': investorObject}
	return render(request, 'stocks_project/index.html', context)
	
def new_stock(request):
	"""Add a new stock."""
	if request.method != 'POST':
		#Creating a blank form with stock fields when no data is submitted
		form = StockForm()
	else:
		#When POST data is submitted, the data is processed.
		form = StockForm(request.POST)
		#is_valid() function checks that all required fields have been filled in
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('stocks_project:index'))
	context = {'form': form}
	return render(request, 'stocks_project/new_stock.html', context)
