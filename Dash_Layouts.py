# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:38:29 2023

@author: thepe
"""

from dash import Dash, html, dcc, Input, Output, callback

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





app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H4(children='Books'),
    dcc.Graph(
                figure=fig
    ,id ='graph'),
                           
    dcc.Markdown('''                   
               
                 
               
                 Choix de l'auteur :

'''), 
    # choix auteur
    dcc.Dropdown(list(df['authors'].unique()), 'J.K. Rowling',
                 id = 'drop-authors'),
   
    dcc.Markdown('''
                   
                 
              
                 
Choix de la langue :

'''), 
    # choix langue
    dcc.RadioItems(list(df['language_code'].unique()), 'eng',
                   id = 'radio-lang')
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
