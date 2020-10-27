import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_resumo = pd.read_csv(DATA_PATH.joinpath("df_resumo.csv"))
df_tipo_evento = pd.read_csv(DATA_PATH.joinpath("df_tipo_evento.csv"))
df_institiuicoes_atuando = pd.read_csv(DATA_PATH.joinpath("df_institiuicoes_atuando.csv"))
df_origem = pd.read_csv(DATA_PATH.joinpath("df_origem.csv"))

tipo_evento_max = df_tipo_evento['Quantidade'].max()
origem_max = df_origem['Quantidade'].max()


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 1 - Texto
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Resumo do App"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    Por meio dos dados abertos é disponibilizado pelo IBAMA uma base de registros de comunicação de acidentes ambientais. Aqui temos uma análise desses dados afim de encontrar informações relevantes e insights importantes sobre acidentes ambientais no Brasil.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 2 - Resumo e Tipos Eventos
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Resumo dos Acidentes"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_resumo)),
									html.P(
                                        [
                                            "Um resumo geral de algumas informações que chamam atenção e podem ser relavantes. Podemos identificar o periodo dos registros, o total de registros, o estado com maior número de acidentes dentre outras informações."
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Top 5 Tipos de Eventos",
                                        className="subtitle padded",
                                    ),
									dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    y=df_tipo_evento['Quantidade'],
                                                    x=df_tipo_evento['Tipo Evento'],
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
                                                height=200,
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
                                                width=330,
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
                                                    "range": [0, tipo_evento_max],
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
                                            "Informações de quais são os tipos de acidentes mais comuns. Aqui já podemos ver que o tipo mais comum, não podemos identificar e ele corresponde a mais de 50% dos acidentes."
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
                    # Row 3 - Instituições e Origens
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Top 5 Origens Acidentes",
                                        className="subtitle padded",
                                    ),
									dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=df_origem['Origem'],
                                                    y=df_origem['Quantidade'],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Origens",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.4,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
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
                                                width=330,
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
                                                    "range": [0, origem_max],
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
                                            "Na origem dos acidentes, o notável é que são as rodovias a mais comum das origens, revelando outros problemas do Brasil. Problemas de educação no trânsito, problemas nas estradas que são problemas não só para acidentes ambientais."
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Porcentagem Atuação das Principais Instituições"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_institiuicoes_atuando)),
									html.P(
                                        [
                                            "Nas instituições fica um pensamento, por que em mais de 50% dos acidentes ambientais, não tem atuação de orgão oficiais do governo? Logo pensamos, será que a maioria dos acidentes ambientais os culpados não são punidos?"
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