import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['month'] = pd.to_datetime(df['date'])


# Preparing data: setting each line to store the month and corresponding temp and temp type. will show fluctuation of temp mean min and max over months
trace1 = go.Scatter(x=df['month'], y=df['actual_min_temp'], mode='lines', name='Min')
trace2 = go.Scatter(x=df['month'], y=df['actual_mean_temp'], mode='lines', name='Mean')
trace3 = go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Max')
data = [trace1, trace2, trace3]


# Preparing layout
layout = go.Layout(title='Actual Min, Mean, and Max of Temperature 2014-2015', xaxis_title='Month',
                   yaxis_title='Temperature')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart_weather.html')