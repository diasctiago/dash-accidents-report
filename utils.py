import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("dash-accidents-logov3.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Outros Exemplos", id="learn-more-button"),
                        href="https://github.com/plotly/dash-sample-apps/tree/master/apps/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Comunicação de Acidentes Ambientais")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Visão Completa",
                                href="/dash-accidents-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Visão Geral",
                href="/dash-accidents-report/page1",
                className="tab first",
            ),
            dcc.Link(
                "Detalhes por Período",
                href="/dash-accidents-report/page2",
                className="tab",
            ),
            dcc.Link(
                "Detalhes por Localização",
                href="/dash-accidents-report/page3",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table