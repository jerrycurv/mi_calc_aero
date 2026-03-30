import streamlit as st
from PIL import Image

# --- Configuração da Página para Mobile-First ---
st.set_page_config(
    page_title="MI Calculator Aero v1.0",
    page_icon="🎓",
    layout="centered"
)

# --- Definição dos Ícones e Texturas (Caminhos Locais ou URLs) ---
# Você precisará desses arquivos na mesma pasta ou alterar o caminho
# Usei URLs de exemplo para ícones públicos com estética 2010.
icons = {
    "cap": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Icon_Graduation_Cap_with_Diplom.png", # Exemplo
    "book": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Icon_Book.png", # Exemplo
    "calc": "https://upload.wikimedia.org/wikipedia/commons/d/df/Icon_Calculator.png", # Exemplo
}

# --- CSS Skeuomorphic / Frutiger Aero (Injeção) ---
# O truque aqui é usar gradients lineares, sombras projetadas e border-radius
st.markdown(f"""
<style>
    /* Chassi Principal (Skeuomorphic - Plástico Brilhante) */
    .stApp {{
        background-color: #f1f5f9;
        background-image: url('https://www.transparenttextures.com/patterns/brushed-alum.png'); /* Sutil textura metálica de fundo */
        font-family: 'Trebuchet MS', sans-serif; /* Fonte comum em 2010 */
        color: #333;
    }}

    /* Títulos com dimensionality (Skeuomorphic) */
    h1, h2, h3 {{
        color: #111;
        text-align: center;
        text-shadow: 1px 1px 0px rgba(255,255,255,0.8), 2px 2px 10px rgba(0,0,0,0.3);
    }}

    /* Painel Central (Frutiger Aero - Vidro) */
    .st-emotion-cache-z5fcl4 {{
        background: linear-gradient(135deg, rgba(255,255,255,0.7) 0%, rgba(200,220,240,0.7) 100%);
        border: 2px solid rgba(255,255,255,0.4);
        border-radius: 15px;
        padding: 25px;
        box-shadow: inset 5px 5px 15px rgba(255,255,255,0.9), 
                    5px 5px 20px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        margin-top: 20px;
    }}

    /* Controles de Entrada (Skeuomorphic) */
    .stNumberInput input, .stSlider > div > div > div > div {{
        background: linear-gradient(145deg, #e6e6e6, #c0c0c0) !important;
        border: 2px solid #aaa !important;
        border-radius: 8px !important;
        box-shadow: inset 3px 3px 6px rgba(0,0,0,0.6) !important;
        text-align: center;
        padding: 10px !important;
    }}

    /* Botões Físicos (Skeuomorphic) */
    .stButton>button {{
        background: linear-gradient(145deg, #00CFFF, #008080) !important; /* Cores Frutiger (Ciano/Teal) */
        color: #fff !important;
        border: 2px solid #005050 !important;
        border-radius: 10px !important;
        box-shadow: 4px 4px 8px rgba(0,0,0,0.5), inset 1px 1px 2px rgba(255,255,255,0.5) !important;
        font-weight: bold;
        transition: all 0.1s ease;
    }}
    .stButton>button:active {{
        box-shadow: inset 4px 4px 8px rgba(0,0,0,0.7) !important;
        transform: translateY(2px);
    }}

    /* Métricas e Resultados (Frutiger Aero) */
    .stMetric {{
        background: linear-gradient(145deg, #dcfce7, #a7f3d0);
        border: 2px solid #22c55e;
        border-radius: 10px;
        box-shadow: inset 1px 1px 1px rgba(255,255,255,0.9), 
                    3px 3px 6px rgba(0,0,0,0.4);
        padding: 15px;
        text-align: center;
    }}

    /* Ícones de Imagem (customizados) */
    .icon-header {{
        max-width: 64px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 10px;
        filter: drop-shadow(2px 2px 5px rgba(0,0,0,0.5));
    }}
</style>
""", unsafe_allow_html=True)

# --- Estrutura da Interface ---
# Título com dimensionality
st.title("MI Calculator Aero v1.0")

# Coleta de Unidades Concluídas (Slider Skeuomorphic)
unidades_concluidas = st.slider("Quantas unidades você já concluiu?", 1, 3, 2)
st.markdown(f'<div style="text-align:center;">Unidades: **{unidades_concluidas}**</div>', unsafe_allow_html=True)
st.write("---")

# --- Painel Central (Vidro) ---
with st.container():
    # Coleta de Notas
    st.subheader("📝 Suas Notas (U1 e U2)")
    
    # Exemplo de ícone de calculadora brillante
    st.markdown(f'<img src="{icons["calc"]}" class="icon-header" alt="Calculadora">', unsafe_allow_html=True)
    
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        st.markdown("**Unidade 1**")
        p1 = st.number_input("MI (Prática 70%) U1", 0.0, 10.0, 8.0, 0.1, key="p1")
        t1 = st.number_input("Teórica (30%) U1", 0.0, 10.0, 6.5, 0.1, key="t1")
    with col_u2:
        st.markdown("**Unidade 2**")
        p2 = st.number_input("MI (Prática 70%) U2", 0.0, 10.0, 7.5, 0.1, key="p2")
        t2 = st.number_input("Teórica (30%) U2", 0.0, 10.0, 5.0, 0.1, key="t2")
    
    if unidades_concluidas == 3:
        # Adiciona a Unidade 3 se necessário
        st.divider()
        st.markdown("**Unidade 3**")
        col_u3_p, col_u3_t = st.columns(2)
        with col_u3_p:
            p3 = st.number_input("MI (Prática 70%) U3", 0.0, 10.0, 0.0, 0.1, key="p3")
        with col_u3_t:
            t3 = st.number_input("Teórica (30%) U3", 0.0, 10.0, 0.0, 0.1, key="t3")
        
    st.write("---")

    # Botão de Calcular (Skeuomorphic)
    col_btn_calc = st.columns([2, 1, 2])
    with col_btn_calc[1]:
        st.button("Calcular Média", type="primary")

# --- COLUNA 3: Results & Predictions (Painéis de Vidro Separados) ---
st.write("---")
st.subheader("📊 Resultado e Projeções")

# Painel Parcial (Vidro)
with st.container():
    col_metrics = st.columns([1, 1, 1])
    
    # Cálculo das Notas
    soma_mi = 0.0
    u1_mi = (p1 * 0.7) + (t1 * 0.3)
    u2_mi = (p2 * 0.7) + (t2 * 0.3)
    soma_mi = u1_mi + u2_mi
    
    with col_metrics[0]:
        st.metric(label="MI Unidade 1", value=f"{u1_mi:.2f}")
    with col_metrics[1]:
        st.metric(label="MI Unidade 2", value=f"{u2_mi:.2f}")
        
    if unidades_concluidas == 3:
        u3_mi = (p3 * 0.7) + (t3 * 0.3)
        soma_mi += u3_mi
        with col_metrics[2]:
             st.metric(label="MI Unidade 3", value=f"{u3_mi:.2f}")
        media_final = soma_mi / 3
        
        st.divider()
        st.markdown("**Média Final**")
        st.markdown(f'<div class="stDisplay">{media_final:.2f}</div>', unsafe_allow_html=True)

        if media_final >= 7.0:
            st.success("🎯 APROVADO! Parabéns!")
        elif media_final >= 3.0:
            st.warning("⚠️ FINAL. Foque nos estudos!")
        else:
            st.error("📉 PERDEU NO MI. Não desanime!")

    else:
        # Previsões
        st.divider()
        st.markdown("**Projeções (Média Final)**")
        
        pontos_passar = 21.0 - soma_mi
        pontos_final = 9.0 - soma_mi
        unidades_restantes = 3 - unidades_concluidas
        
        col_pre_p, col_gauge = st.columns([2, 1])
        with col_pre_p:
            if pontos_passar <= 0:
                # Exemplo de ícone de chapéu de formatura brilhante
                st.markdown(f'<img src="{icons["cap"]}" class="icon-header" alt="Formatura">', unsafe_allow_html=True)
                st.write("Você já atingiu os pontos necessários para passar direto! (Basta não zerar o resto).")
            else:
                st.write(f"Para passar DIRETO: Faltam **{pontos_passar:.2f}** pontos.")
                st.write(f"Média de **{(pontos_passar/unidades_restantes):.2f}** nas próximas {unidades_restantes} unidades.")
                
            if pontos_final <= 0:
                 # Exemplo de ícone de livro brilhante
                 st.markdown(f'<img src="{icons["book"]}" class="icon-header" alt="Livro">', unsafe_allow_html=True)
                 st.write("Você já garantiu, no mínimo, a ida para a Final.")
            else:
                st.write(f"Para ir para a FINAL: Faltam **{pontos_final:.2f}** pontos.")
                st.write(f"Média de **{(pontos_final/unidades_restantes):.2f}** nas próximas {unidades_restantes} unidades.")
