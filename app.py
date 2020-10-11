# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from pages import (
    page1,
    page2,
    page3,
)

#Carga DADOS
'''
df = pd.read_csv('http://siscom.ibama.gov.br/geoserver/publica/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=publica:adm_comunicacidente_p&outputFormat=csv'
                 ,usecols=['dt_registro','origem','uf','tipos_danos_identificados','tipo_evento','institiuicoes_atuando_local','municipio',] ,low_memory=False)
df['mes_registro'] = pd.DatetimeIndex(pd.to_datetime(df['dt_registro'])).month
df['ano_registro'] = pd.DatetimeIndex(pd.to_datetime(df['dt_registro'])).year

### Resumo - page1
resumo=[['Período de Registro dos Acidentes',str(df['ano_registro'].min()) + ' até ' + str(df['ano_registro'].max())],
        ['Total de Acidentes Registrados', df.shape[0]],
        ['Ano com Mais Acidentes Registrados', df['ano_registro'].value_counts().idxmax()],
        ['Origem mais Comum dos Acidentes', df['origem'].value_counts().idxmax()],
        ['Estado com Mais Acidentes Registrados', df['uf'].value_counts().idxmax()],
        ['Tipos de Danos Mais Comuns', ', '.join(df['tipos_danos_identificados'].value_counts().head(3).index)]]
df_resumo = pd.DataFrame(resumo, columns=['Fato','Informação'])
df_resumo.to_csv('data/df_resumo.csv', index=False)

### Tipo Evento - page1
tipo_evento = {'Tipo Evento': df['tipo_evento'].value_counts().head(5).index,
               'Quantidade':  df['tipo_evento'].value_counts().head(5).values
               }
df_tipo_evento = pd.DataFrame(tipo_evento)
df_tipo_evento.to_csv('data/df_tipo_evento.csv', index=False)

### Instiruições - page1
institiuicoes_atuando = {'Instituição': (df['institiuicoes_atuando_local'].value_counts()/df.shape[0]*100).head(5).index,
                         'Percentual':  (df['institiuicoes_atuando_local'].value_counts()/df.shape[0]*100).head(5).values
              }
df_institiuicoes_atuando = pd.DataFrame(institiuicoes_atuando)
df_institiuicoes_atuando.to_csv('data/df_institiuicoes_atuando.csv', index=False)

### Origens - page1
origem = {'Origem':      df['origem'].value_counts().head(5).index,
          'Quantidade':  df['origem'].value_counts().head(5).values
          }
df_origem = pd.DataFrame(origem)
df_origem.to_csv('data/df_origem.csv', index=False)

### Por ano - page2
ano_evento = {'Ano': df['ano_registro'].value_counts().sort_index(ascending=True).index,
              'Quantidade':  df['ano_registro'].value_counts().sort_index(ascending=True).values
              }
df_ano_evento = pd.DataFrame(ano_evento)
df_ano_evento.to_csv('data/df_ano_evento.csv', index=False)

### Por mês - page2
meses=[[1,'JAN'],[2,'FEV'],[3,'MAR'],[4,'ABR'],[5,'MAI'],[6,'JUN'],
       [7,'JUL'],[8,'AGO'],[9,'SET'],[10,'OUT'],[11,'NOV'],[12,'DEZ']]

df_meses = pd.DataFrame(meses, columns=['mes_registro','mes'])

total_mes = df[['mes_registro']].join(df_meses.set_index('mes_registro'), on='mes_registro')['mes'].value_counts()
mes_evento = {'Mês': total_mes.index,
              'Quantidade':  total_mes.values
              }

df_mes_evento = pd.DataFrame(mes_evento)
df_mes_evento.to_csv('data/df_mes_evento.csv', index=False)

### Por UF - page3
uf = {'UF': df['uf'].value_counts().index,
      'Quantidade': df['uf'].value_counts().values}
df_uf = pd.DataFrame(uf)
df_uf.to_csv('data/df_uf.csv', index=False)

### Por município - page3
municipio = {'Posição': list(range(1, df[['municipio','uf']].value_counts().shape[0] + 1)),
             'Município': df[['municipio','uf']].value_counts().index.to_frame(index=False)['municipio'],
             'UF': df[['municipio','uf']].value_counts().index.to_frame(index=False)['uf'],
             'Quantidade': df[['municipio','uf']].value_counts().values}
df_municipio = pd.DataFrame(municipio)
df_municipio.to_csv('data/df_municipio.csv', index=False)
'''

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-accidents-report/page2":
        return page2.create_layout(app)
    elif pathname == "/dash-accidents-report/page3":
        return page3.create_layout(app)
    elif pathname == "/dash-accidents-report/full-view":
        return (
            page1.create_layout(app),
            page2.create_layout(app),
            page3.create_layout(app),
        )
    else:
        return page1.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)