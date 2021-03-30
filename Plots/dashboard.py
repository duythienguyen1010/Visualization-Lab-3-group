import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar chart data
# Bar chart data
barchart_df = df1.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Total'])]

# Stack bar chart data
stackbarchart_df = df1.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Gold'], name='Gold Medals',
                              marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Silver'], name='Silver Medals',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Bronze'], name='Bronze Medals',
                              marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]

# Line Chart
line_df = df2
line_df['date'] = pd.to_datetime(line_df['date'])
new_line_df = line_df.groupby(['month']).agg(
    {'actual_max_temp': 'max'}).reset_index()
data_linechart = [go.Scatter(x=new_line_df['month'], y=new_line_df['actual_max_temp'], mode='lines', name='month')]

# Multi Line Chart
multiline_df = df2
multiline_df['date'] = pd.to_datetime(multiline_df['date'])
new_multi_df = multiline_df.groupby(['month']).agg(
    {'actual_mean_temp': 'mean', 'actual_min_temp': 'min', 'actual_max_temp': 'max'}).reset_index()

trace1_multiline = go.Scatter(x=new_multi_df['month'], y=new_multi_df['actual_max_temp'], mode='lines', name='Max Temp')
trace2_multiline = go.Scatter(x=new_multi_df['month'], y=new_multi_df['actual_min_temp'], mode='lines', name='Min Temp')
trace3_multiline = go.Scatter(x=new_multi_df['month'], y=new_multi_df['actual_mean_temp'], mode='lines',
                              name='Mean Temp')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
bubble_df = df2
bubble_df = bubble_df.groupby(['month']).agg(
    {'actual_mean_temp': 'mean', 'average_min_temp': 'min', 'average_max_temp': 'max'}).reset_index()
data_bubblechart = [
    go.Scatter(x=bubble_df['average_min_temp'],
               y=bubble_df['average_max_temp'],
               text=bubble_df['month'],
               mode='markers',
               marker=dict(size=bubble_df['actual_mean_temp'] /
                                0.5, color=bubble_df['actual_mean_temp'] / 0.5, showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df2['day'],
                           y=df2['month'],
                           z=df2['record_max_temp'].values.tolist(),
                           colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Visualization Lab 3 - ITSC 3155, Spring 2021', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This Bar Chart Represents the Total Number of Medals Won in the Top 20 Countries.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Total Number of Medals in Top 20 Countries.',
                                      xaxis={'title': 'NOC'}, yaxis={'title': 'Total Number of Medals'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This Stacked Bar Chart Shows the Division of Medals Won in the Top 20 Countries.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Division in Medals Won in Each Country.',
                                      xaxis={'title': 'NOC'}, yaxis={'title': 'Medals'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the actual max temperature of each month.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Actual Max Temperature From July 2014 to '
                                            'May 2015', xaxis_title="Month",
                                            yaxis_title="Temperature")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This multi-line chart represents the actual max, min and mean temperature of each month.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(title='The Actual Max, Min, and Mean Temperature of Each Month',
                                      xaxis_title="Date", yaxis_title="Temperature")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represent the average min and max temperature of each month in weather statistics.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title="Average min and max temperature of each month in weather statistics",
                                      xaxis_title="Average min temperature",
                                      yaxis_title="Average max temperature", hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent represent the recorded max temperature on day of week and month of year.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Recorded max temperature', xaxis_title="Day of Week",
                                      yaxis_title="Month of year")
              }
              )
])

@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart,
            'layout': go.Layout(title='Corona Virus Confirmed Cases in ' + selected_continent,
                                xaxis={'title': 'Country'},
                                yaxis={'title': 'Number of confirmed cases'})}


if __name__ == '__main__':
    app.run_server()