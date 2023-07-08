# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:38:29 2023

@author: thepe
"""

from dash import Dash, html, dcc, Input, Output, callback

import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px


url = 'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv'
df = pd.read_csv(url, nrows = 3000)

df2 = df.groupby(by = ['authors', 'title']).agg({'language_code' : 'first', '  num_pages' : 'mean'}).reset_index()
fig = px.scatter(df2, x="authors", y="  num_pages")
fig.update_layout(
    title=dict(text="Nombre moyen de pages par auteur", font=dict(size=30), automargin=True, yref='paper'),
    font_color='#119DFF',
        title_font_color='#F71016',
        xaxis_title="Auteur",
    yaxis_title="Nombre de pages")




app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    html.H4(children='Books'),
    dcc.Graph(
                figure=fig
    ,id ='graph'),
    
    dbc.Row([
        dbc.Col(
                           
            dcc.Markdown('''                   
               
                 
               
                 Choix de l'auteur :

                     '''),
                     width=6),
        dbc.Col(
            dcc.Markdown('''                   
                 
              
                 
              Choix de la langue :

                  '''),
                  width = 6)
                ]),
                
    dbc.Row([
        dbc.Col(
            # choix auteur
    
            dcc.Dropdown(options = [{'label':nom, 'value': nom} for nom in list(df['authors'].unique())],
                                value =list(df['authors'].unique())[0],
                                    id ="drop-authors"                                    
                                    ),
            width = 6),
        dbc.Col(
    
        # choix langue
        dcc.RadioItems(options = [{'label':nom, 'value': nom} for nom in list(df['language_code'].unique())],
                   value =list(df['language_code'].unique())[0],                                     
                   id = 'radio-lang'),
            width = 6)
        ])
    ])
                 
                 
@callback(
    Output('graph', 'figure'),
    [Input('drop-authors', 'value'),
    Input('radio-lang', 'value')]
)

def update_graph(auteur, langue):
   
    df3 = df2[(df2['authors'] == auteur) & (df2['language_code'] == langue)]
    fig = px.scatter(df3, x="title", y="  num_pages")
    return fig



                 

if __name__ == '__main__':
    app.run(debug=True)
