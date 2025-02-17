import streamlit as st
import importlib
from PIL import Image

st.set_page_config(page_title="Seu Portfólio", page_icon=":bar_chart:", layout="wide")

# Define o CSS para alterar a cor de fundo
st.markdown(
    """
    <style>
    body {
        background-color: #FEF4E8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Função para mostrar o conteúdo da página selecionada
def show_pages(page_name):
    modules = {
        'Início': 'inicio',
        'Projetos': 'projetos',
        'Newsletter': 'newsletter',
        'Contato': 'contato'
    }

    module_name = modules.get(page_name)
    if module_name:
        module = importlib.import_module(module_name)

        # Assumindo que o módulo já tem a função run

        if hasattr(module, 'run'):
            module.run()
        else:
            st.write("O módulo não tem uma função 'run' para exibir o conteúdo.")
    else:
        st.write('Página não encontrada!')


# Criando aba de navegação
page = st.sidebar.selectbox(
    'Navegação',
    ['Início', 'Projetos', 'Newsletter', 'Contato']
)

# Criando resumo

if page == 'Início':
    
    # Adicionando foto aqui do perfil
    st.image("https://github.com/daniel-gomess/portifolio/blob/main/Daniel.png?raw=true", width=350)
    
    st.title("Daniel Augusto Gomes")
    st.write("""
    📊 Analista de Dados apaixonado por transformar informações em RESULTADOS, com experiência sólida em Business Intelligence e visualização de dados.
    
    💼 Domino as principais ferramentas do mercado: 
    • SQL Server & Excel Avançado (10+ anos) 
    • Power BI (4+ anos)
    
    👨🏽‍🎓 Graduando em Inteligência de Mercado e Análise de dados, e em paralelo focando um pouco mais em IA e como ela pode ajudar a automatizar tarefas e facilitar o dia a dia.
    
    🚀 Minha MISSÃO é clara: Transformar dados complexos em INSIGHTS PODEROSOS que fazem seu negócio DECOLAR!
    """)

else:
    show_pages(page)
