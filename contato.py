import streamlit as st

def run():
    st.subheader("Contato")
    
    st.write("Para entrar em contato, envie um e-mail para: [universobi@hotmail.com](mailto:universobi@hotmail.com)")
    st.write("Ou me siga nas redes sociais:")
    
    linkedin_url = "https://www.linkedin.com/in/danielaugustogomes/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" width="24"/> LinkedIn', unsafe_allow_html=True)
    
    whatsapp_url = "https://wa.me/47999688593"
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/128/3670/3670051.png" width="24"/> WhatsApp', unsafe_allow_html=True)
    
    st.write("Em breve, canal no Youtube!!!")