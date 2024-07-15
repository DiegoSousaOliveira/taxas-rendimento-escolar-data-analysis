import streamlit as st
import plotly.graph_objects as go
import main

labels = ['Taxa de Abandono','Taxa de Reprovação','Taxa de Aprovação']
values = [main.mean_abandonment, main.mean_failure, main.mean_approval]


fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7)])


fig.update_layout(
    title_text='Taxas de Rendimento Escolar',
    annotations=[dict(text='Taxas', x=0.5, y=0.5, font_size=20, showarrow=False)],
    showlegend=True
)

st.set_page_config(layout='wide')

col1, col2 = st.columns(2, vertical_alignment='bottom')

with col1:
    with st.container(height=300, border=False):
        st.write(f"""
            Unidade Geográfica: Brasil<br>
                 Localização: Total<br>
                 Dependência Administrativa: Total<br>
                 ano: 2022
            """, unsafe_allow_html=True)

    with st.container(height=200):
        st.write("""
            # Indicador Educacional da Educação Básica - Taxas de Rendimento Escolar
            O cálculo das taxas de rendimento (aprovação, reprovação e abandono) tem 
            como referência as informações de rendimento e movimento dos alunos 
            coletadas na segunda etapa do Censo Escolar da Educação Básica, denominada
            módulo Situação do Aluno. Ao final do ano letivo, o aluno matriculado é 
            avaliado quanto ao preenchimento dos requisitos de aproveitamento e 
            frequência, podendo ser considerado aprovado, reprovado ou afastado por 
            abandono. O aluno é considerado aprovado se, ao final do ano letivo, 
            alcançou os critérios mínimos para a conclusão satisfatória da etapa de
            ensino que estava cursando, estando apto a cursar a série seguinte. Caso 
            esses requisitos mínimos não tenham sido atendidos, o aluno é considerado 
            reprovado. Por outro lado, o abandono é caracterizado quando o aluno deixou de 
            frequentar a escola antes do término do ano letivo, sem requerer formalmente a 
            transferência. O indicador apresenta o percentual de alunos aprovados 
            (taxa de aprovação), reprovados (taxa de reprovação) ou que abandonaram a escola 
            durante o ano letivo (taxa de abandono). Os arquivos constituem planilhas individuais 
            em formato Excel® (xlsx) e Open Document Sheet (ods).
        """)


with col2:
    st.plotly_chart(fig, use_container_width=True)