import streamlit as st

# Configuracao focada em mobile
st.set_page_config(
    page_title="Calculadora MI",
    layout="centered"
)

# --- A Magia do CSS: Frutiger Aero & Classic iOS ---
st.markdown("""
<style>
    /* Fundo Frutiger Aero: Simulando ceu/agua brilhante com gradiente puro */
    .stApp {
        background: linear-gradient(180deg, #d4e8fc 0%, #e6f1fc 40%, #b3d5fc 41%, #8bc0fb 100%);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Painel de Vidro Translúcido (Aero Glass) */
    .st-emotion-cache-z5fcl4, .css-1d391kg {
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-top: 2px solid rgba(255, 255, 255, 0.8);
        border-left: 1px solid rgba(255, 255, 255, 0.6);
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        border-right: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0, 50, 100, 0.2);
    }

    /* Títulos em Relevo (Estilo texto gravado no metal/vidro) */
    h1, h2, h3, p, label {
        color: #1a3b5c !important;
        text-shadow: 0px 1px 1px rgba(255, 255, 255, 0.9);
    }

    /* Inputs de Texto Afundados (Skeuomorphism) */
    .stNumberInput input {
        background-color: #f8fcfd !important;
        border: 1px solid #7a9cb8 !important;
        border-top: 2px solid #5a7b99 !important; /* Borda superior mais escura para sombra */
        border-radius: 6px !important;
        box-shadow: inset 0 3px 5px rgba(0,0,0,0.15) !important;
        color: #333 !important;
        font-weight: bold;
    }

    /* O Clássico Botão Glossy do iOS Antigo */
    .stButton > button {
        background: linear-gradient(to bottom, #7dd2fa 0%, #309bea 49%, #1078cd 50%, #1588de 100%) !important;
        border: 1px solid #0b4e8a !important;
        border-radius: 10px !important;
        color: white !important;
        font-weight: bold !important;
        text-shadow: 0 -1px 1px rgba(0,0,0,0.6) !important;
        box-shadow: inset 0 1px 2px rgba(255,255,255,0.7), 0 3px 5px rgba(0,0,0,0.3) !important;
        padding: 10px 20px !important;
        transition: none !important; /* Sem animacoes modernas suaves */
    }
    
    /* Efeito de clique físico no botão */
    .stButton > button:active {
        background: linear-gradient(to bottom, #1078cd 0%, #0d6ab5 100%) !important;
        box-shadow: inset 0 3px 6px rgba(0,0,0,0.4) !important;
        padding-top: 12px !important; /* Simula o botão descendo */
        padding-bottom: 8px !important;
    }

    /* Caixas de Alerta (Status Final) com textura plástica */
    .status-aprovado { 
        background: linear-gradient(to bottom, #a8e063 0%, #5fac03 100%);
        color: white; font-weight: bold; padding: 15px; border-radius: 10px; text-align: center;
        border: 1px solid #4a8700;
        box-shadow: inset 0 1px 2px rgba(255,255,255,0.8), 0 4px 6px rgba(0,0,0,0.2);
        text-shadow: 0 -1px 1px rgba(0,0,0,0.4);
    }
    .status-final { 
        background: linear-gradient(to bottom, #f6d365 0%, #ffb347 100%);
        color: #5c3c00; font-weight: bold; padding: 15px; border-radius: 10px; text-align: center;
        border: 1px solid #c98200;
        box-shadow: inset 0 1px 2px rgba(255,255,255,0.8), 0 4px 6px rgba(0,0,0,0.2);
        text-shadow: 0 1px 1px rgba(255,255,255,0.6);
    }
    .status-perdeu { 
        background: linear-gradient(to bottom, #ff7878 0%, #d62828 100%);
        color: white; font-weight: bold; padding: 15px; border-radius: 10px; text-align: center;
        border: 1px solid #9c1515;
        box-shadow: inset 0 1px 2px rgba(255,255,255,0.8), 0 4px 6px rgba(0,0,0,0.2);
        text-shadow: 0 -1px 1px rgba(0,0,0,0.4);
    }
    
    /* Medidores (Simulando telas de cristal líquido antigas) */
    .stMetric {
        background-color: #eaf3e8;
        border: 2px inset #a2bba0;
        border-radius: 4px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Interface do Aplicativo ---

st.title("Calculadora de MI")
st.markdown("Descubra sua media parcial e projecoes para o semestre.")

# Selecao de unidades com radio buttons nativos (o CSS ja vai aplicar um fundo de vidro)
unidades_concluidas = st.radio(
    "Unidades ja concluidas:",
    options=[1, 2, 3],
    horizontal=True
)

st.markdown("---")
st.subheader("Entrada de Notas")

soma_mi = 0.0

for i in range(unidades_concluidas):
    st.markdown(f"**Unidade {i+1}**")
    col1, col2 = st.columns(2)
    
    with col1:
        pratica = st.number_input(f"MI Pratica (70%) - U{i+1}", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key=f"p_{i}")
    with col2:
        teorica = st.number_input(f"Teorica (30%) - U{i+1}", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key=f"t_{i}")
    
    nota_unidade = (pratica * 0.7) + (teorica * 0.3)
    soma_mi += nota_unidade
    
    st.caption(f"Resultado Unidade {i+1}: {nota_unidade:.2f}")

st.markdown("---")

# Botao Glossy
calcular = st.button("Processar Resultados", type="primary")

# Area de Resultados
if calcular or unidades_concluidas > 0:
    st.subheader("Painel de Resultados")
    
    if unidades_concluidas == 3:
        media_final = soma_mi / 3
        st.metric(label="Media Final Obtida", value=f"{media_final:.2f}")
        
        st.write("") # Espaçamento
        
        if media_final >= 7.0:
            st.markdown('<div class="status-aprovado">STATUS: APROVADO</div>', unsafe_allow_html=True)
        elif media_final >= 3.0:
            st.markdown('<div class="status-final">STATUS: FINAL</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-perdeu">STATUS: REPROVADO</div>', unsafe_allow_html=True)
            
    else:
        media_parcial = soma_mi / unidades_concluidas
        st.metric(label="Media Parcial (Atual)", value=f"{media_parcial:.2f}")
        
        pontos_para_passar = 21.0 - soma_mi
        pontos_para_final = 9.0 - soma_mi
        unidades_restantes = 3 - unidades_concluidas
        
        st.write("")
        st.markdown("**Projecoes para Aprovacao Direta:**")
        
        if pontos_para_passar <= 0:
            st.markdown('<div class="status-aprovado">Pontuacao garantida para aprovacao direta.</div>', unsafe_allow_html=True)
        else:
            media_necessaria = pontos_para_passar / unidades_restantes
            if media_necessaria > 10:
                st.markdown('<div class="status-perdeu">Aprovacao direta matematicamente impossivel.</div>', unsafe_allow_html=True)
            else:
                st.info(f"Faltam {pontos_para_passar:.2f} pontos. Media necessaria: {media_necessaria:.2f} nas proximas unidades.")
                
        st.write("")
        st.markdown("**Projecoes para Prova Final:**")
        
        if pontos_para_final <= 0:
            st.markdown('<div class="status-final">Pontuacao minima garantida para a prova final.</div>', unsafe_allow_html=True)
        else:
            media_final_necessaria = pontos_para_final / unidades_restantes
            if media_final_necessaria > 10:
                 st.markdown('<div class="status-perdeu">Prova final matematicamente impossivel.</div>', unsafe_allow_html=True)
            else:
                st.warning(f"Faltam {pontos_para_final:.2f} pontos. Media necessaria: {media_final_necessaria:.2f} nas proximas unidades.")
