import streamlit as st
import importlib


#st.title('Portifólio de Análise de Dados')

#Função para mostrar o conteúdo da página selecionada

def show_pages(page_name):
    modules= {
        'Início':'inicio',
        'Projetos':'projetos',
        'Newsletter':'newsletter',
        'Contato':'contato'
    }

    module_name = modules.get(page_name)
    if module_name:
        module = importlib.import_module(module_name)
        
        #assumindo que o modulo ja tem a função run
        
        if hasattr(module, 'run'):
            module.run()
        else:
            st.write("O módulo não tem uma função 'run' para exibir o conteúdo.")
    else:
        st.write('Página não encontrada!')
        
#Criando aba de navegação

page = st.sidebar.selectbox(
    'Navegação',
    ['Início', 'Projetos', 'Newsletter', 'Contato']
)

# criando resumo

if page == 'Início':
    
    st.title("Daniel Augusto Gomes")
    st.write("""
    📊 Analista de Dados apaixonado por transformar informações em RESULTADOS, com experiência sólida em Business Intelligence e visualização de dados.
    
    💼 Domino as principais ferramentas do mercado: • SQL Server & Excel Avançado (10+ anos) • Power BI (4+ anos)
    
    👨🏽‍🎓 Graduando em Inteligência de Mercado e Análise de dados, e em paralelo focando um pouco mais em IA e como ela pode ajudar a automatizar tarefas e facilitar o dia a dia.
    
    🚀 Minha MISSÃO é clara: Transformar dados complexos em INSIGHTS PODEROSOS que fazem seu negócio DECOLAR!
    
    💡 Quer descobrir como seus dados podem gerar mais LUCRO e CRESCIMENTO para sua empresa?
""")
    
else:
    show_pages(page)