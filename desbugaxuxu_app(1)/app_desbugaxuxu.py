import streamlit as st
import base64
import os

st.set_page_config(page_title="DesbugaXuxu", layout="centered")

st.title("🧠 DesbugaXuxu")
st.markdown("### Aperte o play e desbugue sua mente em até 33 segundos")

AUDIO_DIR = "audios"
if not os.path.exists(AUDIO_DIR):
    st.error("Pasta de áudios não encontrada.")
    st.stop()

audio_files = [f for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")]
audio_files.sort()

if not audio_files:
    st.warning("Nenhum áudio disponível.")
else:
    selected_audio = st.selectbox("Escolha um áudio", audio_files)
    audio_path = os.path.join(AUDIO_DIR, selected_audio)
    
    # Método 1: Usando st.audio diretamente com o caminho do arquivo
    st.audio(audio_path, format="audio/mp3")
    
    # Método 2: Usando base64 encoding (alternativo)
    # with open(audio_path, "rb") as audio_file:
    #     audio_bytes = audio_file.read()
    #     audio_b64 = base64.b64encode(audio_bytes).decode()
    #     audio_html = f"""
    #     <audio controls>
    #         <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    #         Seu navegador não suporta o elemento de áudio.
    #     </audio>
    #     """
    #     st.markdown(audio_html, unsafe_allow_html=True)
    
    st.success(f"Tocando: {selected_audio}")

