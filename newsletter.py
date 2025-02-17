import streamlit as st

def run():
    st.subheader("Projetos")
    st.write("Acesse nossa NewsLetter e fique por dentro das principais notícias do mundo de dados, BI e Negócios! Clique abaixo e inscreva-se 😉")
    
    newsletter_url = "https://universobi.substack.com/about#§por-que-se-inscrever"
    st.markdown(f'<a href="{newsletter_url}" target="_blank"> NewsLetter', unsafe_allow_html=True)
    
    st.write("Posts já compartilhados:")
    post1_url = "https://universobi.substack.com/p/ascensao-da-ia-no-bi-inteligencia?r=57tba2"
    st.markdown(f'<a href="{post1_url}" target="_blank"> Ascensão da IA no BI / Inteligência Artificial na Análise de Dados / Educação em Dados / Oferta de Elon Musk pela OpenAI / Vagas', unsafe_allow_html=True)
    post2_url = "https://universobi.substack.com/p/deepseek-e-sua-dificuldade-de-alta?r=57tba2"
    st.markdown(f'<a href="{post2_url}" target="_blank"> DeepSeek e sua "dificuldade" de alta demanda / Um clássico e um dos queridinhos da Apple está de volta / Apple cancela óculos de RA / Primeiro lucro anual do Spotify / Atualizações Protheus / Vagas', unsafe_allow_html=True)
    post3_url = "https://universobi.substack.com/p/a-analise-de-negocios-na-era-digital?r=57tba2"
    st.markdown(f'<a href="{post3_url}" target="_blank"> Artigo: A Análise de Negócios na Era Digital: Como a Análise de Dados Impulsiona Decisões Estratégicas', unsafe_allow_html=True)