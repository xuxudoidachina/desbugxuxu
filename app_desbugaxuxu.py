import streamlit as st
import os
import random

# Configuração da página
st.set_page_config(page_title="DesbugaXuxu", layout="centered")
st.title("🧠 DesbugaXuxu")
st.markdown("### Escolha sua vibe e desbugue sua mente em até 33 segundos")

# Diretórios
AUDIO_DIR = "audios"
REVOLTS_DIR = os.path.join(AUDIO_DIR, "revolts")

# Frases Revolts (pode editar ou carregar de arquivo .txt se quiser depois)
frases_revolts = [
    "Teoria do Caos: nada é tão ruim que não possa piorar.",
    "Hoje o Fusca ronca porque a paciência acabou.",
    "Não é bug, é revolta programada.",
    "Se melhorar, estraga. Se travar, reinicia a mente.",
    "Quem nunca falou com a parede, nunca tentou programar sem café.",
    "Calma é para quem tem tempo, aqui é pressão e bug."
]

# Vibes disponíveis
vibes = ["😠 Revolts", "😎 Calmo (em breve)", "👻 Caótico (em breve)"]
modo = st.radio("Escolha o Modo de Desbuga:", vibes, horizontal=True)

# Função para tocar áudio
def tocar_audio(pasta):
    if not os.path.exists(pasta):
        st.error("❌ Pasta de áudio não encontrada.")
        return

    arquivos = [f for f in os.listdir(pasta) if f.endswith(".mp3")]
    arquivos.sort()

    if not arquivos:
        st.warning("⚠️ Nenhum áudio disponível.")
        return

    audio_escolhido = st.selectbox("Escolha um áudio", arquivos)
    caminho_audio = os.path.join(pasta, audio_escolhido)

    with open(caminho_audio, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
        st.success(f"✅ Tocando agora: **{audio_escolhido}**")

# Ação do modo
if modo == "😠 Revolts":
    frase = random.choice(frases_revolts)
    st.markdown(f"### 💥 Frase do dia: _{frase}_")
    tocar_audio(REVOLTS_DIR)
elif modo == "😎 Calmo (em breve)":
    st.info("Modo Calmo ainda está em meditação profunda... volte depois.")
elif modo == "👻 Caótico (em breve)":
    st.warning("Modo Caótico ainda está se organizando no meio do caos.")


