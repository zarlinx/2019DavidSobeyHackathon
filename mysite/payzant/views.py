import matplotlib
matplotlib.use("Agg")

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from math import sqrt

from .models import DbSalesDetailCustomerType, DbItemByStore

import pandas as pd
import itertools
import statsmodels.api as sm
import matplotlib.pyplot as plt
from io import BytesIO
import base64
#from pylab import rcParams

def index(request):
    return HttpResponse("Just a test!")

def remove_outlier(df_in, col_name):
    threshold = 3
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-threshold*iqr
    fence_high = q3+threshold*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out

def getClassName(storenumber, itemnumber):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    className = qs[0].classname
    return className

def getFinelineName(storenumber, itemnumber):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    finelineName = qs[0].finelinename
    return finelineName

def getClassCode(storenumber, itemnumber):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    classCode = qs[0].classcode
    return classCode

def getFinelineCode(storenumber, itemnumber):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    finelineCode = qs[0].finelinecode
    return finelineCode

def getDescription(storenumber, itemnumber):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    description = qs[0].itemdescription
    return description

def getFact(storenumber, itemnumber):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    price = qs[0].retail_price
    demand = qs[0].forecast_demand_per_day
    return price*demand

def getQuantity(storenumber, itemnumber, demand):
    qs = DbItemByStore.objects.filter(item_number=itemnumber).filter(
        store=storenumber)
    k = qs[0].replacement_cost*qs[0].qoh
    h = qs[0].average_cost
    return sqrt(2*demand*k/h)

def getItems(storenumber, date):
    qs = DbItemByStore.objects.filter(store=storenumber).filter(
        new_order_point__gt=F('qoh')).order_by('-netsales2018','-netsales2017',
                                               '-netsales2016','-netsales2015',
                                               '-netsales2014')
    return qs

def getFig1(storenumber, itemnumber, date):
    qs = DbSalesDetailCustomerType.objects.filter(itemnumber=itemnumber).filter(
        storenumber=storenumber).values_list('date', 'sales')
    df = pd.DataFrame.from_records(qs)
    df.columns = ['Date', 'Sales']

    df['Date'] = pd.to_datetime(df['Date'])
    dt = pd.to_datetime(date)

    df = df.sort_values('Date')
    #df.isnull().sum()
    df = df.groupby('Date')['Sales'].sum().reset_index()
    df = df.set_index('Date')

    #Our current datetime data can be tricky to work with, therefore, we will use the averages daily sales value for that month instead, and we are using the start of each month as the timestamp.
    y = df['Sales'].resample('MS').mean()
    y.plot(figsize=(15, 6))

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()    

    return image_base64

def prediction(storenumber, itemnumber, date):
    qs = DbSalesDetailCustomerType.objects.filter(itemnumber=itemnumber).filter(
        storenumber=storenumber).values_list('date', 'sales')
    df = pd.DataFrame.from_records(qs)
    df.columns = ['Date', 'Sales']

    df['Date'] = pd.to_datetime(df['Date'])
    dt = pd.to_datetime(date)

    df = df.sort_values('Date')
    #df.isnull().sum()
    df = df.groupby('Date')['Sales'].sum().reset_index()
    df = df.set_index('Date')
    df.index

    #Our current datetime data can be tricky to work with, therefore, we will use the averages daily sales value for that month instead, and we are using the start of each month as the timestamp.
    y = df['Sales'].resample('MS').mean()
    #y['2016':]
    #y[17] = (y[5]+y[29])/2
    #y.plot(figsize=(15, 6))
    #plt.show()

    # remove outliers
    df_emp = pd.DataFrame()
    df_emp['Date'] = pd.date_range('1/1/2016', periods=36, freq='MS')
    df_emp = df_emp.set_index('Date')
    df_emp['Sales'] = y
    df_emp = remove_outlier(df_emp, 'Sales')
    # replace missing values
    df_emp2 = pd.DataFrame()
    df_emp2['Date'] = pd.date_range('1/1/2016', periods=36, freq='MS')
    df_emp2 = df_emp2.set_index('Date')
    df_emp2['Sales'] = df_emp['Sales']
    df_emp2.fillna(df_emp2.groupby(df_emp2.index.month).transform('mean'), inplace=True)
    # replace null values
    df_emp2 = df_emp2.fillna(0)
    y = df_emp2['Sales']
    print('///////////////////')
    print('///////////////////')
    print(y)
    print('///////////////////')
    print('///////////////////')
    #We can also visualize our data using a method called time-series decomposition that allows us to decompose our time series into three distinct components: trend, seasonality, and noise.
    #rcParams['figure.figsize'] = 18, 8
    #decomposition = sm.tsa.seasonal_decompose(y, model='additive')
    #fig = decomposition.plot()
    #plt.show()

    #We are going to apply one of the most commonly used method for time-series forecasting, known as ARIMA, which stands for Autoregressive Integrated Moving Average.
    #ARIMA models are denoted with the notation ARIMA(p, d, q). These three parameters account for seasonality, trend, and noise in data:
    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
    #print('Examples of parameter combinations for Seasonal ARIMA...')
    #print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
    #print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
    #print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
    #print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

    #This step is parameter Selection for our furniture’s sales ARIMA Time Series Model. Our goal here is to use a “grid search” to find the optimal set of parameters that yields the best performance for our model.
    # mod = sm.tsa.statespace.SARIMAX(y,
    #                             order=(0,0,0),
    #                             seasonal_order=(0,0,0,12),
    #                             enforce_stationarity=False,
    #                             enforce_invertibility=False)
    # results = mod.fit()
    # #print('ARIMA{}x{}12 - AIC:{}'.format((0,0,0), (0,0,0,12), results.aic))

    aic_final = 100000
    # param_final=(0,0,0)
    # param_seasonal_final=(0,0,0,12)

    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
                results = mod.fit()
                if results.aic<aic_final:
                    param_final=param
                    param_seasonal_final=param_seasonal
                    aic_final=results.aic
            except:
                continue

    #print('ARIMA{}x{}12 - AIC:{}'.format(param_final, param_seasonal_final, aic_final))


    #The above output suggests that SARIMAX(1, 1, 0)x(1, 1, 0, 12) yields the lowest AIC value of 106.167. Therefore we should consider this to be optimal option.
    mod = sm.tsa.statespace.SARIMAX(y,
                                order=param_final,
                                seasonal_order=param_seasonal_final,
                                enforce_stationarity=False,
                                enforce_invertibility=False)
    results = mod.fit()
    #print(results.summary().tables[1])

    #We should always run model diagnostics to investigate any unusual behavior.
    #results.plot_diagnostics(figsize=(16, 8))
    #plt.show()


    #To help us understand the accuracy of our forecasts, we compare predicted sales to real sales of the time series, and we set forecasts to start at 2018–01–01 to 2019-12-31.
    # pred = results.get_prediction(start=pd.to_datetime('2018-01-01'), dynamic=False)
    # pred_ci = pred.conf_int()
    # ax = y['2016':].plot(label='observed')
    # pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
    # ax.fill_between(pred_ci.index,
    #             pred_ci.iloc[:, 0],
    #             pred_ci.iloc[:, 1], color='k', alpha=.2)
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Paint Sales')
    # plt.legend()
    # #plt.yticks(np.arange(0, 300))
    # plt.show()


    # y_forecasted = pred.predicted_mean
    # y_truth = y['2017-01-01':]
    # mse = ((y_forecasted - y_truth) ** 2).mean()
    # print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
    # print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

    pred_uc = results.get_forecast(steps=12)
    pred_ci = pred_uc.conf_int()
    fig = plt.figure()
    ax = y.plot(label='Observed', figsize=(14, 7))
    pred_uc.predicted_mean.plot(ax=ax, label='Predicted')
    ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    plt.legend()
    plt.show()
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()

    yf=pred_uc.predicted_mean
    predictedValue = yf[dt.month-1]
    #print(yf)
    # yf = 123.753
    #yo=3.1*39.99
    # yo = 123.969
    #print(yo)
    #accuracy=yf/yo
    # 99.83%



    #return HttpResponse("You're looking at item %s. It's start date is %s, end date is %s" % (itemnumber, start_date, end_date))
    return image_base64, predictedValue
    #return HttpResponse("Testing...")

