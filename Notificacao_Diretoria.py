import streamlit as st

# Configuração da página
st.set_page_config(page_title="Guia de Comunicação Executiva MV", layout="wide", page_icon="📊")

# --- BANCO DE DADOS DINÂMICO (Baseado no documento INS) ---
dados_cenarios = {
    "1. Atraso Crítico no Go-Live (OnePass)": {
        "status": "CRÍTICO 🔴",
        "evasao": "R$ 12.100.000,00",
        "atraso": "164 dias",
        "impacto_mensal": "R$ 314.000,00",
        "causa": "Erros recorrentes na funcionalidade OnePass e recusa de homologação pelo GAAT[cite: 110, 106].",
        "acao": "Concluir homologação técnica até 14/11 para garantir Go-Live em 24/11[cite: 112].",
        "responsavel": "Rodrigo Vasconcelos e Cliente INS[cite: 93]."
    },
    "2. Retrabalho e Centro de Custo (CeosGo)": {
        "status": "SUSPENSO 🟡",
        "evasao": "R$ 11.000.000,00 (estimada)",
        "atraso": "60 dias",
        "impacto_mensal": "Não mensurado",
        "causa": "Novas exigências do cliente sobre configurações de centro de custo após homologação e treinamento[cite: 10, 11].",
        "acao": "Suspensão imediata por retrabalho conforme instrução da diretoria (Francisco Figueiredo)[cite: 204].",
        "responsavel": "José Alexandre[cite: 16]."
    },
    "3. Impasse de Escopo Internacional (Costa Rica)": {
        "status": "CRÍTICO 🔴",
        "evasao": "US$ 177.000,00 (Total)",
        "atraso": "N/A (Bloqueio)",
        "impacto_mensal": "US$ 107.784,00 (Subscrição)",
        "causa": "Divergência entre protótipo apresentado em 23/06/25 e entrega final do Dashboard de licenças[cite: 168, 171].",
        "acao": "Definição técnica sobre viabilidade da tela e elaboração de resposta formal/legal[cite: 173, 174].",
        "responsavel": "Time de Tecnologia e Jean Karr[cite: 176, 177]."
    },
    "4. Atrasos Internos (Universidade/Fábrica)": {
        "status": "ALERTA 🟡",
        "evasao": "R$ 12.000.000,00",
        "atraso": "Efeito 'Bola de Neve'",
        "impacto_mensal": "R$ 314.000,00",
        "causa": "Troca de plataforma da Universidade (idioma espanhol) e demora na devolução de documentos pela Fábrica[cite: 205, 206].",
        "acao": "Escalar imediatamente atrasos com impacto financeiro e realizar reuniões mais recorrentes[cite: 208, 211].",
        "responsavel": "José Alexandre e Paulo Lima[cite: 207, 48]."
    }
}

# --- INTERFACE STREAMLIT ---
st.title("🏆 Guia de Comunicação Executiva - Ecossistema MV")
st.markdown("---")

# Seleção de Cenário pelo Analista
escolha = st.selectbox("Selecione o cenário de crise atual:", list(dados_cenarios.keys()))
dados = dados_cenarios[escolha]

# --- SIDEBAR DINÂMICA (Painel de Controle) ---
st.sidebar.header("📊 Painel de Controle Real")
st.sidebar.subheader(f"Status: {dados['status']}")

if "R$" in dados['evasao']:
    st.sidebar.error(f"Evasão de Receita:\n{dados['evasao']}")
else:
    st.sidebar.error(f"Retenção Financeira:\n{dados['evasao']}")

st.sidebar.warning(f"Dias de Atraso: {dados['atraso']}")
st.sidebar.info(f"Impacto p/ Mês: {dados['impacto_mensal']}")

# --- ÁREA PRINCIPAL: RESUMO EXECUTIVO ---
st.header("📝 Resumo Executivo para a Diretoria")

# Container de destaque para o Resumo
with st.container():
    st.markdown(f"""
    **Assunto:** [STATUS: {dados['status']}] Notificação de Impacto e Plano de Ação - Projeto INS
    
    **1. RESUMO DA SITUAÇÃO**
    * {dados['causa']}
    
    **2. IMPACTO NO NEGÓCIO**
    * **Financeiro:** {dados['evasao']} (Perda acumulada até o momento).
    * **Cronograma:** Atraso de {dados['atraso']} impactando diretamente a meta de faturamento de 50% da subscrição[cite: 63, 106].
    
    **3. PLANO DE MITIGAÇÃO**
    * **Ação:** {dados['acao']}
    * **Responsável Direto:** {dados['responsavel']}
    """)

st.divider()

# --- QUADRO COMPARATIVO ---
st.subheader("💡 Comparativo de Comunicação")
col1, col2 = st.columns(2)

with col1:
    st.error("❌ O que o Analista NÃO deve escrever")
    st.info("Focar apenas na técnica ou 'culpar' o sistema.")
    if "OnePass" in escolha:
        st.write("'O código do OnePass está com bug e o cliente não aceita.'")
    elif "Retrabalho" in escolha:
        st.write("'O cliente mudou de ideia sobre o centro de custo e vamos refazer.'")
    else:
        st.write("'Estamos esperando a fábrica/universidade responder os tickets.'")

with col2:
    st.success("✅ Como o Analista DEVE escrever")
    st.info("Focar no impacto financeiro e na solução estratégica.")
    st.write(f"Conforme o resumo acima, destaque que a perda de {dados['impacto_mensal']} é o principal motivador da urgência e peça o apoio da diretoria para a ação definida.")

# --- REFERÊNCIAS DE MERCADO ---
st.divider()
st.markdown("### 📚 Boas Práticas Recomendadas")
st.markdown("""
1.  **Princípio de Minto:** Comece pela conclusão (Impacto Financeiro) e termine com o suporte técnico.
2.  **Radical Candor:** Seja direto sobre atrasos internos (Fábrica/Universidade) para que a diretoria possa agir[cite: 206, 211].
3.  **Gestão de Stakeholders:** Utilize dados reais de evasão (R$ 12M) para priorizar agendas com o cliente[cite: 92, 98].
4.  **Matriz de Responsabilidade (RACI):** Sempre aponte um responsável nominal por ação[cite: 175, 176].
5.  **Comunicação Propositiva:** Nunca apresente o atraso de 164 dias sem o novo cronograma realista[cite: 200, 201].
""")

