import streamlit as st
from chart import ChartTable
from main import Table

def generate_chart(name_table = '2022'):
    table = Table(name_file=name_table)
    chartTable = ChartTable(
        values=table.values_of_the_mean(), 
        labels=table.labels_of_the_mean())
    st.session_state['chart_pie'] = chartTable.generate_pie_chart()

if 'chart_pie' not in st.session_state:
    generate_chart()

st.set_page_config(layout='wide')

with open('styles.css') as arquivo:
    st.markdown('<style>' + arquivo.read() + '</style>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap='medium')

with col1:
    with st.container(border=False):
        st.write(f"""<h4>
            Unidade Geográfica: Brasil<br>
                 Localização: Total<br>
                 Dependência Administrativa: Total<br>
                 ano: 2022</h4>
            """, unsafe_allow_html=True)
        
    with st.container(height=200,border=False):
        st.button('2021', on_click=lambda : generate_chart("2021"))
        st.button('2020', on_click=lambda : generate_chart("2020"))
        st.button('2019', on_click=lambda : generate_chart("2019"))
        st.button('2018', on_click=lambda : generate_chart("2018"))
        st.button('2017', on_click=lambda : generate_chart("2017"))

    with st.container(height=200):
        st.write("""
            ## Indicador Educacional da Educação Básica - Taxas de Rendimento Escolar
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
    st.plotly_chart(st.session_state['chart_pie'], use_container_width=True)
