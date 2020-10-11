import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_uf = pd.read_csv(DATA_PATH.joinpath("df_uf.csv"))
df_municipio = pd.read_csv(DATA_PATH.joinpath("df_municipio.csv"))
uf_max = df_uf['Quantidade'].max()


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 1 - Por UF
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Acidentes por UF",
                                        className="subtitle padded",
                                    ),
									dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=df_uf['UF'],
                                                    y=df_uf['Quantidade'],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Eventos",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.4,
                                                font={"family": "Raleway", "size": 10},
                                                height=400,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=660,
                                                xaxis={
                                                    "autorange": True,
                                                    #"range": [-0.5, 2000],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [0, uf_max],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
									html.P(
                                        [
                                            "TEXTO EXPLICATIVO DO GRÁFICO"
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2 - Muinícipios
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Top 5 Munícípios"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_municipio.head(5))),
									html.P(
                                        [
                                            "TEXTO EXPLICATIVO DO GRÁFICO"
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Top 5 Munícípios MG"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_municipio.query('UF == "MG"').head(5))),
									html.P(
                                        [
                                            "TEXTO EXPLICATIVO DO GRÁFICO"
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )