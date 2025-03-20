import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from data_loader import *
from visualizations import *

# Configuração da página
st.set_page_config(
    page_title="Dashboard Pobishop",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("Dashboard Interativo - Análise de Mercado Pobishop")
st.markdown("#### Visualização de dados estratégicos para tomada de decisão")

# Filtros na sidebar
st.sidebar.title("Filtros")
classe_social = st.sidebar.multiselect(
    "Classe Social",
    options=["C", "D", "E"],
    default=["C", "D"]
)

faixa_etaria = st.sidebar.slider(
    "Faixa Etária",
    min_value=25,
    max_value=45,
    value=(25, 35)
)

regiao = st.sidebar.selectbox(
    "Região",
    options=["Todas", "Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
    index=0
)

# Download botão
st.sidebar.markdown("---")
st.sidebar.markdown("### Exportar Dados")
st.sidebar.download_button(
    label="Download PDF",
    data=b"Placeholder para PDF real",
    file_name="pobishop_analise.pdf",
    mime="application/pdf"
)

# Abas principais
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Visão Geral", 
    "Público-Alvo", 
    "Competitivo", 
    "Produtos", 
    "Finanças",
    "SWOT",
    "Fornecedores"
])

# Tab 1: Visão Geral do Mercado
with tab1:
    st.header("Visão Geral do Mercado")
    
    # Carregar dados
    df_geo, df_growth, kpis = load_market_overview_data()
    
    # KPIs em colunas
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Mercado Total", kpis["Mercado Total"])
    with col2:
        st.metric("Taxa de Crescimento", kpis["Taxa de Crescimento"])
    with col3:
        st.metric("Ticket Médio", kpis["Ticket Médio"])
    with col4:
        st.metric("Inflação", kpis["Inflação"])
    with col5:
        st.metric("Taxa Selic", kpis["Taxa Selic"])
    
    # Mapa e gráfico de tendência
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_region_map(df_geo), use_container_width=True)
    with col2:
        st.plotly_chart(create_growth_chart(df_growth), use_container_width=True)
    
    # Contexto do mercado
    st.subheader("Contexto do Mercado")
    st.markdown("""
    O e-commerce brasileiro continua em crescimento, mesmo com desafios econômicos.
    Com o aumento do acesso à internet (88% da população) e o crescimento das
    classes C e D, há uma oportunidade significativa para a Pobishop atender
    este mercado com produtos acessíveis e de qualidade.
    """)

# Tab 2: Público-Alvo
with tab2:
    st.header("Análise do Público-Alvo")
    
    # Carregar dados
    df_demo, df_income, df_behavior, personas = load_target_audience_data()
    
    # Gráficos demográficos
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_age_pyramid(df_demo), use_container_width=True)
    with col2:
        st.plotly_chart(create_income_chart(df_income), use_container_width=True)
    
    # Radar de comportamento
    st.plotly_chart(create_behavior_radar(df_behavior), use_container_width=True)
    
    # Personas
    st.subheader("Personas da Pobishop")
    cols = st.columns(5)
    for i, persona in enumerate(personas):
        with cols[i]:
            st.markdown(f"### {persona['Nome']}")
            st.markdown(f"**Idade:** {persona['Idade']}")
            st.markdown(f"**Ocupação:** {persona['Ocupacao']}")
            st.markdown(f"**Perfil:** {persona['Descricao']}")

# Tab 3: Análise Competitiva
with tab3:
    st.header("Análise Competitiva")
    
    # Carregar dados
    df_competitors = load_competitive_data()
    
    # Gráficos de competidores
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_competitor_map(df_competitors), use_container_width=True)
    with col2:
        st.plotly_chart(create_market_share(df_competitors), use_container_width=True)
    
    # Análise de diferenciação
    st.subheader("Diferencial Competitivo da Pobishop")
    st.markdown("""
    **Principais diferenciais:**
    
    1. **Posicionamento "smartpobi"**: Ressignificação positiva do conceito "pobi" (pobre) como escolha inteligente
    2. **Curadoria especializada**: Foco em produtos realmente úteis, não apenas baratos
    3. **Comunicação autêntica**: Tom bem-humorado e próximo da realidade do público
    4. **Comunidade**: Criação de senso de pertencimento entre consumidores
    """)

# Tab 4: Produtos e Precificação
with tab4:
    st.header("Análise de Produtos e Precificação")
    
    # Carregar dados
    df_products = load_products_data()
    
    # Gráficos de produtos
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_product_treemap(df_products), use_container_width=True)
    with col2:
        st.plotly_chart(create_price_demand(df_products), use_container_width=True)
    
    # Simulador de margem
    st.subheader("Simulador de Margem de Produto")
    col1, col2, col3 = st.columns(3)
    with col1:
        preco_custo = st.number_input("Preço de Custo (R$)", min_value=10.0, max_value=1000.0, value=50.0)
    with col2:
        taxa_imposto = st.slider("Taxa de Importação (%)", min_value=0, max_value=100, value=20)
    with col3:
        margem_desejada = st.slider("Margem Desejada (%)", min_value=10, max_value=200, value=70)
    
    # Cálculo da margem
    custo_imposto = preco_custo * (taxa_imposto / 100)
    custo_total = preco_custo + custo_imposto
    preco_venda = custo_total / (1 - (margem_desejada / 100))
    
    st.metric("Preço de Venda Sugerido", f"R$ {preco_venda:.2f}")
    
    # Tabela de produtos populares
    st.subheader("Produtos com Maior Potencial")
    st.dataframe(df_products.sort_values("Demanda", ascending=False))

# Tab 5: Projeções Financeiras
with tab5:
    st.header("Projeções Financeiras")
    
    # Carregar dados
    df_revenue, df_investment = load_financial_data()
    
    # Gráficos financeiros
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_revenue_chart(df_revenue), use_container_width=True)
    with col2:
        st.plotly_chart(create_investment_chart(df_investment), use_container_width=True)
    
    # Projeção ano 1
    st.subheader("Projeção Simplificada - Ano 1")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Receita Total Projetada", "R$ 222.000")
    with col2:
        st.metric("Custos Totais", "R$ 175.560")
    with col3:
        st.metric("Resultado Operacional", "R$ 46.440")
    
    # Ponto de equilíbrio
    st.success("**Ponto de Equilíbrio:** Será atingido entre os meses 6 e 9 de operação.")

# Tab 6: Análise SWOT
with tab6:
    st.header("Análise SWOT e Riscos")
    
    # Carregar dados
    swot, df_risk = load_swot_data()
    
    # SWOT em grid
    st.subheader("Matriz SWOT")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Forças")
        for item in swot["Forcas"]:
            st.markdown(f"- {item}")
        
        st.markdown("### Fraquezas")
        for item in swot["Fraquezas"]:
            st.markdown(f"- {item}")
    
    with col2:
        st.markdown("### Oportunidades")
        for item in swot["Oportunidades"]:
            st.markdown(f"- {item}")
        
        st.markdown("### Ameaças")
        for item in swot["Ameacas"]:
            st.markdown(f"- {item}")
    
    # Mapa de risco
    st.subheader("Matriz de Riscos")
    st.plotly_chart(create_risk_heatmap(df_risk), use_container_width=True)
    
    # Plano de mitigação
    st.subheader("Plano de Mitigação de Riscos Prioritários")
    st.markdown("""
    **Novas taxas de importação:**
    - Diversificação para fornecedores nacionais
    - Repasse gradual para preços
    - Comunicação transparente com clientes
    
    **Alta concorrência:**
    - Fortalecimento da identidade "smartpobi"
    - Foco em nichos específicos
    - Investimento em conteúdo educativo diferenciado
    """)

# Tab 7: Fornecedores e Logística
with tab7:
    st.header("Fornecedores e Logística")
    
    # Carregar dados
    df_suppliers = load_supplier_data()
    
    # Gráficos de fornecedores
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_supplier_chart(df_suppliers), use_container_width=True)
    with col2:
        st.plotly_chart(create_product_flow(df_suppliers), use_container_width=True)
    
    # Calculadora de importação
    st.subheader("Calculadora de Custos de Importação")
    col1, col2, col3 = st.columns(3)
    with col1:
        valor_produto = st.number_input("Valor do Produto (USD)", min_value=1.0, max_value=500.0, value=20.0)
    with col2:
        taxa_cambio = st.number_input("Taxa de Câmbio (R$/USD)", min_value=1.0, max_value=10.0, value=5.2)
    with col3:
        taxa_importacao = st.slider("Imposto de Importação (%)", min_value=0, max_value=100, value=60)
    
    # Cálculos
    valor_reais = valor_produto * taxa_cambio
    imposto = valor_reais * (taxa_importacao / 100)
    valor_final = valor_reais + imposto
    
    # Resultados
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Valor em Reais", f"R$ {valor_reais:.2f}")
    with col2:
        st.metric("Imposto", f"R$ {imposto:.2f}")
    with col3:
        st.metric("Valor Final", f"R$ {valor_final:.2f}")
    
    # Estratégia de fornecimento
    st.subheader("Estratégia de Fornecimento")
    st.markdown("""
    **Composição inicial:** 60% produtos internacionais / 40% nacionais
    
    **Evolução planejada:** Atingir 40% internacionais / 60% nacionais até final de 2025
    
    **Critérios de seleção de fornecedores:**
    - Confiabilidade de entrega
    - Qualidade consistente dos produtos
    - Comunicação eficiente
    - Flexibilidade em pequenos pedidos
    """)

# Footer
st.markdown("---")
st.markdown("Dashboard desenvolvido para a Pobishop © 2025")
