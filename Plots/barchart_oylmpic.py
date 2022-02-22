import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Sorting values and select first 20 states
df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data: sets x value as NOC and y value as total medals. meaning you will see the total in the bar and read the name of NOC
data = [go.Bar(x=df['NOC'], y=df['Total'])]

# Preparing layout
layout = go.Layout(title='Number of Medals by NOC in 2006 Oylmpics', xaxis_title='NOC',
                   yaxis_title='Medals')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart_oylmpic.html')
