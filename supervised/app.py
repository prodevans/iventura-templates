# Import libraries
import pandas as pd
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from os import listdir
from os.path import isfile, join
import numpy as np
from plotly import graph_objs as go
import plotly_express as px

import pickle

infile = open("files/senti_prediction_NB.pickle",'rb')
data = pickle.load(infile)
infile.close()
#print('im')
xx=data[data==2]

#print(x)
yy=data[data==1]
zz=data[data==0]
######################################
infile = open("files/CCC.pickle",'rb')
data1 = pickle.load(infile)
infile.close()
print(data1.head())
y_val=list(data1['cc_cons'])
x_val=list(data1['id'])
#print(x_val)
#print(y_val)
USERNAME_PASSWORD_PAIRS=[
    ['ajay','prodevans'],['priyag','prodevans'],['iventura','prodevans']
    ]
app=dash.Dash(
     __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
auth=dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

##########################################################33
tips=pd.read_csv('/app/files/train.csv')
print(tips.head())
print(type(tips))
col_options = [dict(label=x, value=x) for x in tips.columns]
dimensions = ["x", "y", "color", "facet_col", "facet_row"]
gapminder = px.data.gapminder()
##################################################################
#types=['scatter','bar']
#col_options = [dict(label=x, value=x) for x in types]
#dimensions = ["x", "y", "color", "facet_col", "facet_row"]
mypath = '/app/files/'


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

dimensions = ["x", "y", "color", "facet_col", "facet_row"]
app.layout = html.Div([
    html.H1(children='Welcome to Iventura Platform',style={
        'textAlign': 'center',
        'color': colors['text']}),
    dcc.Graph(id='project1',
        figure={
            'data': [
                {'x ':yy,'y': [1],'type': 'bar', 'name': 'Negative sentiment'},
                {'x ':zz,'y':[0],'type': 'bar', 'name': 'Positive sentiment'},
                
                {'x ':xx,'y': [2],'type': 'bar', 'name': 'Neutral sentiment'},
            ],
            'layout': {
                'title': 'Sentiment Analysis for drugs/medicines',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']}
            }
        }
           ),
    html.Div(
    [
        html.H4(" Consumption scatter Plot"),
        html.Div(dcc.Input(
        id='Credit card consumption',
        value='Loan ID ',
            style={"width": "25%", "float": "left"},
        ),
    ),
            
        dcc.Graph(id="loan_graph", style={"width": "75%", "display": "inline-block"}),
    ]
),
    html.Hr(),  # add a horizontal rule
    html.Div(
        [
            dcc.Dropdown(
                id="dataFH",
                options=[{
                    'label': i,
                    'value': i
                } for i in onlyfiles],
                value=" "),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
   
    html.Div(id='output'),
    html.Div(
    [
        html.H2(" Data Detective Platform"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
),
    html.Div(
    [
        html.H3(" animations example"),
        html.Div(dcc.Input(
        id='number-in',
        value='animation ',
            style={"width": "25%", "float": "left"},
        ),
    ),
            
        dcc.Graph(id="animat_graph", style={"width": "75%", "display": "inline-block"}),
    ]
)
     
])
@app.callback(
    Output('loan_graph', 'figure'),
    [Input('Credit card consumption', 'value')])
def output(Creditcardconsumption):
    

    return px.scatter(data1, x="id", y="cc_cons")
                                    

@app.callback(Output('output', 'children'),
              
[Input('dataFH', 'value')])

def update_graph(dataFH):
    path=mypath+dataFH
    
    if isfile(path):
        
        df = pd.read_csv(path)# path, delimiter=';',encoding='cp1252'
        #df=df.isnull().fillna(0, inplace=True)
        # aggregate
        
        col_option = [dict(label=x, value=x) for x in df.columns]
        return  'You\'ve Selected  "{}" as a output file'.format(dataFH)
    #return col_option


#

@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color, facet_col, facet_row):
    return px.scatter(
        tips,
        x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,


         )
@app.callback(
    Output('animat_graph', 'figure'),
    [Input('number-in', 'value')])
def output(number):
    

    return px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
                                    

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
    



