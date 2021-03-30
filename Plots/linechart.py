import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

new_df = df.groupby(['month']).agg(
    {'actual_max_temp' : 'max'}).reset_index()

# Preparing Data
data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='month')]

# Preparing layout
layout = go.Layout(title='Actual Max Temperature From July 2014 to '
                         'May 2015', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')

Message #coding