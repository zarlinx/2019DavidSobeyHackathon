from django.http import HttpResponse
from django.shortcuts import render

from payzant.forms import InputForm, ItemForm
from payzant.views import prediction, remove_outlier, getQuantity, getFact

from django.views.generic import View

# Create your views here.
def home_view(request, *args, **kwargs):
    form = InputForm()

    context = {
        'form' : form,        
    }

    return render(request, "index.html", context)

# Model form of index.html
def index_view(request, *args, **kwargs):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            storenumber = form.cleaned_data['storenumber']
            itemnumber = form.cleaned_data['itemnumber']
            date = form.cleaned_data['date']
            prdct = round(prediction(storenumber, itemnumber, date),2)
            fact = round(getFact(storenumber, itemnumber),2)
            quantity = round(getQuantity(storenumber, itemnumber,prdct))
            time = 0
            context = {
                'form' : form,
                'prediction' : prdct,
                'fact' : fact,
                'quantity' : quantity,
                'time' : time,
            }
            #return HttpResponseRedirect('calculation/')
            return render(request, 'index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        return home_view(request)


# def item_calculation_view(request):
#     form = ItemForm(request.GET or None)
#     if form.is_valid():
#         form.save()

#     context = {
#         "form" : form
#     }
    
#     return render(request, "calculation.html", context)

# class LoadTemplateView(View):

#     template_name = ['Payzant/index.html']
#     #You put any code you may need here
#     def get(self, request, *args, **kwargs):

#         return render(request, self.template_name)



# Html Form of input.html
def input_view(request, *args, **kwargs):
    if request.method == 'POST':
        storenumber = request.POST.get('storenumber')
        itemnumber = request.POST.get('itemnumber')
        date = request.POST.get('date')
        print('////////////////') 
        print(request.GET)
        print(request.POST)
        print(request)
        print('////////////////') 
        prdct = prediction(storenumber, itemnumber, date)
        context = {
            'prediction' : prdct
        }
        return render(request, 'output.html', context)
    form = None
    return render(request, 'input.html', {'form':form})


# # Model Form of input.html
# def input_view(request):
#         # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = InputForm(request.POST or None)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             storenumber = form.cleaned_data['storenumber']
#             itemnumber = form.cleaned_data['itemnumber']
#             date = form.cleaned_data['date']
#             prdct = prediction(storenumber, itemnumber, date)
#             context = {
#                 'prediction' : prdct
#             }
#             #return HttpResponseRedirect('calculation/')
#             return render(request, 'output.html', context)

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = InputForm()

#     return render(request, 'input.html', {'form': form})


