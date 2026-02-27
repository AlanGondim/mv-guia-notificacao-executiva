import streamlit as st
import pandas as pd

# Configuração da página para máxima performance visual
st.set_page_config(page_title="Cockpit Executivo MV", layout="wide", page_icon="📈")

# --- ESTILO CSS PARA ALTA GESTÃO ---
st.markdown("""
    <style>
    /* Redução de fonte para métricas financeiras */
    [data-testid="stMetricValue"] { font-size: 22px !important; font-weight: 700; color: #1E3A8A; }
    [data-testid="stMetricLabel"] { font-size: 14px !important; text-transform: uppercase; letter-spacing: 1px; }
    /* Estilização de títulos de seção */
    .section-header { font-size: 18px; font-weight: bold; color: #111827; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; margin-bottom: 15px; margin-top: 20px; }
    .status-card { padding: 15px; border-radius: 8px; border: 1px solid #E5E7EB; background-color: #F9FAFB; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS REAL (Extraída dos documentos INS) ---
# Em produção, conectar via st.connection("gsheets", type=GSheetsConnection)
data = {
    "Data": ["17/12/2026", "05/12/2025", "29/09/2025", "12/09/2025", "22/08/2025"],
    "Programa": ["INS Costa Rica", "INS Costa Rica", "INS Costa Rica", "INS Costa Rica", "INS Costa Rica"],
    "Status": ["SUSPENSO 🔴", "CRÍTICO 🔴", "CRÍTICO 🔴", "CRÍTICO 🔴", "ALERTA 🟡"],
    "Resumo_Situacao": [
        "Atraso acumulado de 164 dias. Exigência de novo cronograma realista devido a falhas internas e do cliente.",
        "Impasse na entrega do One Pass License; cliente recusa liberar 'Gerenciamento de Usuários'.",
        "Atraso na entrega do OnePass por necessidade de confirmação do modelo de licença.",
        "Go live de 16/09 cancelado por falta de homologação das correções pelo cliente.",
        "Risco de replanejamento do go live caso erros na versão não sejam corrigidos até 29/08."
    ],
    "Evasao_Receita": ["R$ 12.100.000,00", "US$ 177.000,00", "R$ 12.100.000,00", "R$ 12.000.000,00", "R$ 11.000.000,00"],
    "Receita_Atual": ["R$ 0,00", "US$ 107.784,00", "R$ 12.100.000,00", "R$ 314.000,00", "R$ 314.000,00"],
    "Atrasado": ["SIM", "SIM", "SIM", "SIM", "SIM"],
    "Dias_Atraso": [164, 110, 85, 68, 45],
    "Grau_Impacto": ["MÁXIMO", "CRÍTICO", "CRÍTICO", "CRÍTICO", "ALTO"],
    "Recomendacao_1": [
        "Suspensão imediata por retrabalho não pago.",
        "Elaborar resposta formal para resguardo legal.",
        "Apresentação de cronograma realista em reunião executiva.",
        "Definição de nova data após aprovação de correções.",
        "Liberar nova versão com correções de rollback."
    ],
    "Recomendacao_2": [
        "Escalar atrasos financeiros imediatamente à diretoria.",
        "Análise técnica sobre viabilidade da tela de gestão.",
        "Formalizar modelo de licença por usuário.",
        "Acompanhar testes de provas do sistema pelo cliente.",
        "Garantir faturamento de 50% da subscrição."
    ],
    "Custo_Total": ["R$ 2.8 MM", "US$ 177k", "R$ 2.5 MM", "R$ 2.5 MM", "R$ 2.5 MM"],
    "Prazo": ["Dez/2027", "TBD", "29/09/25", "16/09/25", "25/08/25"]
}
df = pd.DataFrame(data)

# --- SIDEBAR: CONTROLE ---
st.sidebar.markdown("### 🏢 Governança de Programas")
programa_selecionado = st.sidebar.selectbox("Seleção do Programa", df["Programa"].unique())
df_selecionado = df[df["Programa"] == programa_selecionado].reset_index(drop=True)
recente = df_selecionado.iloc[0]

# --- MAIN PAGE: COCKPIT DO PROGRAMA ---
st.title(f"🚀 Cockpit | Programa {programa_selecionado}")

# 1. STATUS ATUAL DO PROGRAMA (KPIs de impacto imediato)
st.markdown('<div class="section-header">Status Atual do Programa</div>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    color = "inverse" if "🔴" in recente["Status"] else "normal"
    st.metric("Status", recente["Status"])
with c2:
    st.metric("Atrasado?", f"{recente['Atrasado']} ({recente['Dias_Atraso']} dias)")
with c3:
    st.metric("Evasão de Receita", recente["Evasao_Receita"])
with c4:
    st.metric("Grau de Impacto", recente["Grau_Impacto"])

# 2. RESUMO DA SITUAÇÃO & RECOMENDAÇÕES ESTRATÉGICAS
st.markdown('<div class="section-header">Resumo da Situação & Recomendações Estratégicas</div>', unsafe_allow_html=True)
col_sit, col_rec = st.columns([1.5, 1])

with col_sit:
    st.markdown("**Resumo da Situação**")
    st.info(recente["Resumo_Situacao"])
    st.markdown(f"**Data do Reporte:** {recente['Data']}")

with col_rec:
    st.markdown("**Ações Prioritárias para Escalonamento**")
    st.warning(f"🎯 **Estratégia 1:** {recente['Recomendacao_1']}")
    st.warning(f"⚖️ **Estratégia 2:** {recente['Recomendacao_2']}")

# 3. VISÃO DE CUSTOS E PRAZOS
st.markdown('<div class="section-header">Visão de Custos e Prazos</div>', unsafe_allow_html=True)
ca, cb, cc = st.columns(3)
with ca:
    st.write("**Custo Total Estimado:**")
    st.markdown(f"### {recente['Custo_Total']}")
with cb:
    st.write("**Impacto Financeiro Mensal:**")
    st.markdown(f"### {recente['Receita_Atual']}")
with cc:
    st.write("**Nova Linha de Base (Deadline):**")
    st.markdown(f"### {recente['Prazo']}")

# 4. HISTÓRICO DE EVOLUÇÃO DO PROGRAMA
st.markdown('<div class="section-header">Histórico de Evolução do Programa</div>', unsafe_allow_html=True)
st.dataframe(
    df_selecionado[["Data", "Status", "Evasao_Receita", "Resumo_Situacao"]], 
    use_container_width=True, 
    hide_index=True
)

st.sidebar.divider()
st.sidebar.caption("Responsável: José Alexandre")
st.sidebar.info("Diretiva: Suspensão imediata por retrabalho.")
