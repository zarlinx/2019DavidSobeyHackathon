from django.http import HttpResponse
from django.shortcuts import render

from payzant.forms import InputForm
from payzant.views import prediction, remove_outlier, getQuantity, getFact, getItems, getClassName, getFinelineName, getClassCode, getFinelineCode, getDescription, getFig1

from django.views.generic import View

from django.template import Context, loader

import csv
from django.http import StreamingHttpResponse

# Create your views here.

# Model form of index.html
# def index_view(request, *args, **kwargs):
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
#             prdct = round(prediction(storenumber, itemnumber, date),2)
#             fact = round(getFact(storenumber, itemnumber),2)
#             quantity = round(getQuantity(storenumber, itemnumber,prdct))
#             time = 0
#             context = {
#                 'form' : form,
#                 'prediction' : prdct,
#                 'fact' : fact,
#                 'quantity' : quantity,
#                 'time' : time,
#             }
#             #return HttpResponseRedirect('calculation/')
#             return render(request, 'index.html', context)

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         return home_view(request)


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
    #if request.method == 'POST':
    storenumber = request.GET.get('storenumber')
    itemnumber = request.GET.get('itemnumber')
    date = request.GET.get('date')

    #prdct = round(prediction(storenumber, itemnumber, date),2)
    image_base64, predictedValue = prediction(storenumber, itemnumber, date)
    prdct = round(predictedValue,2)
    quantity = round(getQuantity(storenumber, itemnumber,prdct))
    className = getClassName(storenumber, itemnumber)
    classCode = getClassCode(storenumber, itemnumber)
    finelineName = getFinelineName(storenumber, itemnumber)
    finelineCode = getFinelineCode(storenumber, itemnumber)
    description = getDescription(storenumber, itemnumber)
    context = {
                'prediction' : prdct,
                'quantity' : quantity,
                'className' : className,
                'finelineName' : finelineName,
                'classCode' : classCode,
                'finelineCode' : finelineCode,
                'description' : description,
                'fig1' : image_base64,
                'itemNumber' : itemnumber,
            }
    return render(request, 'output.html', context)
    #form = None
    #return render(request, 'input.html', {'form':form})

# Html Form of class_view.html
def class_view(request, *args, **kwargs):
    if request.method == 'POST':
        storenumber = request.POST.get('storenumber')
        itemnumber = request.POST.get('itemnumber')
        date = request.POST.get('date')

    #prdct = round(prediction(storenumber, itemnumber, date),2)
        image_base64, predictedValue = prediction(storenumber, itemnumber, date)
        prdct = round(predictedValue,2)
        quantity = round(getQuantity(storenumber, itemnumber,prdct))
        className = getClassName(storenumber, itemnumber)
        classCode = getClassCode(storenumber, itemnumber)
        finelineName = getFinelineName(storenumber, itemnumber)
        finelineCode = getFinelineCode(storenumber, itemnumber)
        description = getDescription(storenumber, itemnumber)
        context = {
                    'prediction' : prdct,
                    'quantity' : quantity,
                    'className' : className,
                    'finelineName' : finelineName,
                    'classCode' : classCode,
                    'finelineCode' : finelineCode,
                    'description' : description,
                    'fig1' : image_base64,
                    'itemNumber' : itemnumber,
                }
        return render(request, 'output.html', context)
    form = None
    return render(request, 'class.html', {'form':form})



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

# Html Form of storewise.html
def storewise_view(request, *args, **kwargs):
    if request.method == 'POST': # get rid of first load when GET is default and POST is None
        storenumber = request.POST.get('storenumber')
        date = request.POST.get('date')
        items = getItems(storenumber, date)

        # for item in  items:
        #  <tbody>
        #     <tr>
        #     <td>{{item.store}}</td>
        #     <td>{{item.item_number}}</td>
        #     <td> {{item.itemdescription}} </td>
        #     <td>{{item.new_order_point}}</td>
        #     <td>{{item.qoh}}</td>
        #     <td> {% if item.qoh|div:item.new_order_point > 0.8 %}
        #         <font color='green'>Low</font>
        #        {% elif item.qoh|div:item.new_order_point > 0.5 %}
        #         <font color=#FFFF00>Mediun</font>
        #        {% else %}
        #         <font color='red'>High</font>
        #        {% endif %}

        
        context = {
            'items' : items,
        }
        return render(request, 'storewiseout.html', context)
    form = None
    return render(request, 'storewise.html', {'form':form})

def store_view(request, *args, **kwargs):
    
    return render(request, 'store.html', {})

def index_view(request, *args, **kwargs):
    
    return render(request, 'index.html', {})

# def csvStore_view(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

#     # The data is hard-coded here, but you could load it from a database or
#     # some other source.
#     csv_data = (
#         ('First row', 'Foo', 'Bar', 'Baz'),
#         ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
#     )

#     t = loader.get_template('csvStore.txt')
#     # c = Context({
#     #     'data': csv_data,
#     # })
#     c = {
#          'data': csv_data,
#      }
#     response.write(t.render(c))
#     return response


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def csvStore_view(request, *args, **kwargs):
    storeNumber = request.GET.get('storenumber')
    date = request.GET.get('date')
    items = getItems(storeNumber, date)
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    # rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    rows = ([item.store, item.item_number, item.itemdescription, item.new_order_point, item.qoh] for item in items)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="store.csv"'
    return response

def csvProduct_view(request):
    classNumber = request.GET.get('classNumber')
    className = request.GET.get('className')
    finelineNumber = request.GET.get('finelineNumber')
    finelineName = request.GET.get('finelineName')
    itemNumber = request.GET.get('itemNumber')
    description = request.GET.get('description')
    prediction = request.GET.get('prediction')
    quantity = request.GET.get('quantity')

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'

    writer = csv.writer(response)
    writer.writerow(['Class Number', 'Class Name', 'Fineline Number', 'Fineline Name', 'Item Number', 'Description', 'Prediction', 'Quantity To Order'])
    writer.writerow([classNumber, className, finelineNumber, finelineName, itemNumber, description, prediction, quantity])

    return response
    


