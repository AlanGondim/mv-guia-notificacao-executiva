import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Repositório de Notificações Executivas", layout="wide", page_icon="🏢")

# --- CONEXÃO COM GOOGLE SHEETS ---
# Nota: O link da planilha deve estar configurado no arquivo .streamlit/secrets.toml
# Ou ser passado como uma URL pública de visualização.
conn = st.connection("gsheets", type=GSheetsConnection)

try:
    # Lendo os dados da planilha
    # Certifique-se de que sua planilha tenha colunas com os nomes exatos usados abaixo
    df = conn.read()
except Exception as e:
    st.error("Erro ao conectar com a planilha. Verifique o link e as permissões.")
    st.stop()

# --- INTERFACE ---
st.title("📊 Repositório de Notificações para Diretoria")
st.markdown("Consulta histórica e acompanhamento de impactos financeiros do ecossistema MV.")

# --- FILTROS ---
st.sidebar.header("🔍 Filtros de Consulta")
programas_disponiveis = df["Programa"].unique()
programa_selecionado = st.sidebar.selectbox("Selecione o Programa:", programas_disponiveis)

# Filtrando dados pelo programa selecionado
dados_programa = df[df["Programa"] == programa_selecionado].sort_values(by="Data_Notificacao", ascending=False)

if not dados_programa.empty:
    # Pegamos a notificação mais recente para o painel principal
    recente = dados_programa.iloc[0]
    
    # --- PAINEL DE CONTROLE (INDICADORES) ---
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Status Atual", recente["Status"])
    with col2:
        atrasado_label = "🚨 SIM" if recente["Atrasado"].upper() == "SIM" else "✅ NÃO"
        st.metric("Atrasado?", atrasado_label)
    with col3:
        st.metric("Evasão de Receita", recente["Evasao_Receita"])
    with col4:
        st.metric("Grau de Impacto", recente["Grau_Impacto"])

    # --- CORPO DA NOTIFICAÇÃO ---
    st.divider()
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("📝 Resumo Consolidado para Diretoria")
        st.info(recente["Resumo_Consolidado"])
        
        st.markdown("### 🔍 Detalhamento da Situação")
        st.write(recente["Resumo_Situacao"])
        
        st.markdown(f"**O que está sendo impactado:** {recente['O_Que_Impacta']}")

    with col_right:
        st.markdown("### 💰 Dados Financeiros")
        st.write(f"**Receita Atual:** {recente['Receita_Atual']}")
        st.write(f"**Custo Total do Programa:** {recente['Custo_Total']}")
        st.write(f"**Prazo (Deadline):** {recente['Prazo']}")
        
        st.divider()
        st.markdown("### ⚖️ Recomendações de Decisão")
        st.warning(f"**1.** {recente['Recomendacao_1']}")
        st.warning(f"**2.** {recente['Recomendacao_2']}")

    # --- HISTÓRICO DE EVOLUÇÃO ---
    st.divider()
    with st.expander("📂 Ver Histórico de Evolução deste Programa"):
        st.dataframe(dados_programa[["Data_Notificacao", "Status", "Evasao_Receita", "Resumo_Consolidado"]], 
                     use_container_width=True, hide_index=True)

else:
    st.warning("Nenhum dado encontrado para o programa selecionado.")

# Rodapé informando a fonte
st.sidebar.markdown("---")
st.sidebar.caption("Dados sincronizados via Google Drive (Sheets)")
