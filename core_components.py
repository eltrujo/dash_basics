#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source: https://www.datacamp.com/community/tutorials/learn-build-dash-python
Core Components:
    Dropdown
    Multi-Select Dropdown
    Ratio Items
    Checklist
    Text Input
Help:
    help(dcc.Slider)
"""

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://fonts.googleapis.com/css?family=Roboto&display=swap' # to load the 'Roboto' font
    ]

# # # Core Components # # #

import dash
import dash_core_components as dcc  # it has the Graph class
import dash_html_components as html  # it has all the HTML tags

bold_label = lambda x: html.Label(x, style={'fontWeight': 'bold'})

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

options_list = [
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montréal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
]

app.layout = html.Div(style={'fontFamily': "'Roboto', sans-serif;", 'columnCount': 2}, children=[
    html.Div([
        bold_label('Dropdown'),
        dcc.Dropdown(
            options = options_list,
            value = 'MTL'
            )
    ]),
    html.Div([
        bold_label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options = options_list,
            value = ['MTL', 'SF'],
            multi = True
        )
    ]),
    html.Div([
        bold_label('Radio Items'),
        dcc.RadioItems(
            options = options_list,
            value = 'MTL',
        ),
    ]),
    html.Div([
        bold_label('Checklist'),
        dcc.Checklist(
            options = options_list,
            value = ['MTL', 'SF']
        )
    ],
    style={'overflow': 'hidden'} # to avoid braking across columns 
    ),
    html.Div([
        bold_label('Text Box'),
        html.Div(dcc.Input(value = 'MTL', type = 'text')),
    ]),
    html.Div([
        bold_label('Slider'),
        dcc.Slider(
            id='my-slider',
            min=0,
            max=10,
            step=0.5,
            value=5,
            marks={
                0: '0',
                5: '5',
                10: '10'
            }
        )
    ]),
    html.Div(id='slider-output-container')
])

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return f"You have selected {value}"


if __name__ == '__main__':
    app.run_server(debug=True)