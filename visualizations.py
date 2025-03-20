import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_region_map(df_geo):
    """Cria mapa de calor para distribuição do público por região."""
    # Como não temos um mapa do Brasil pronto no Plotly,
    # vamos criar um gráfico de barras simples
    fig = px.bar(df_geo, x="Regiao", y="Publico", 
                color="Publico",
                title="Distribuição do Público-Alvo por Região")
    fig.update_layout(xaxis_title="Região", 
                     yaxis_title="Potencial de Público")
    return fig

def create_growth_chart(df_growth):
    """Cria gráfico de tendência de crescimento."""
    fig = px.line(df_growth, x="Ano", y="Faturamento", 
                 markers=True, 
                 title="Projeção de Crescimento do E-commerce (2024-2026)")
    fig.update_layout(xaxis_title="Ano", 
                     yaxis_title="Faturamento (R$ bilhões)")
    return fig

def create_age_pyramid(df_demo):
    """Cria pirâmide demográfica."""
    fig = go.Figure()
    
    # Masculino (valores negativos para pirâmide)
    fig.add_trace(go.Bar(
        y=df_demo["Faixa_Etaria"],
        x=[-value for value in df_demo["Masculino"]],
        name="Masculino",
        orientation="h",
        marker=dict(color="blue")
    ))
    
    # Feminino
    fig.add_trace(go.Bar(
        y=df_demo["Faixa_Etaria"],
        x=df_demo["Feminino"],
        name="Feminino",
        orientation="h",
        marker=dict(color="pink")
    ))
    
    fig.update_layout(
        title="Pirâmide Demográfica por Faixa Etária",
        barmode="overlay",
        bargap=0.1,
        xaxis=dict(
            title="População",
            tickvals=[-40, -30, -20, -10, 0, 10, 20, 30, 40],
            ticktext=["40", "30", "20", "10", "0", "10", "20", "30", "40"]
        )
    )
    
    return fig

def create_income_chart(df_income):
    """Cria gráfico de renda média por classe social."""
    fig = px.bar(df_income, x="Classe", y="Renda_Media",
                color="Classe",
                title="Renda Média por Classe Social")
    fig.update_layout(xaxis_title="Classe Social", 
                     yaxis_title="Renda Média (R$)")
    return fig

def create_behavior_radar(df_behavior):
    """Cria radar chart para dores/comportamentos."""
    fig = px.line_polar(df_behavior, r="Pontuacao", 
                       theta="Categoria", 
                       line_close=True,
                       title="Perfil de Necessidades do Público-Alvo")
    return fig

def create_competitor_map(df_competitors):
    """Cria mapa de posicionamento dos concorrentes."""
    fig = px.scatter(df_competitors, x="Preco", y="Qualidade",
                    size="Market_Share", 
                    text="Concorrente",
                    title="Mapa de Posicionamento Competitivo")
    
    # Adiciona Pobishop (posição estimada)
    fig.add_trace(go.Scatter(
        x=[32], y=[63],
        mode="markers+text",
        marker=dict(size=15, color="red"),
        text=["Pobishop"],
        name="Pobishop"
    ))
    
    fig.update_layout(xaxis_title="Preço (menor é mais caro)", 
                     yaxis_title="Qualidade Percebida")
    return fig

def create_market_share(df_competitors):
    """Cria gráfico de market share."""
    fig = px.pie(df_competitors, values="Market_Share", 
                names="Concorrente",
                title="Market Share dos Concorrentes")
    return fig

def create_product_treemap(df_products):
    """Cria treemap de produtos por categoria e margem."""
    fig = px.treemap(df_products, 
                    path=["Categoria", "Produto"],
                    values="Margem",
                    color="Demanda",
                    title="Volume e Margem por Categoria/Produto")
    return fig

def create_price_demand(df_products):
    """Cria scatter plot de preço vs. demanda."""
    fig = px.scatter(df_products, x="Preco", y="Demanda",
                    size="Margem", 
                    text="Produto",
                    title="Preço vs. Demanda Potencial")
    fig.update_layout(xaxis_title="Preço (R$)", 
                     yaxis_title="Demanda Potencial")
    return fig

def create_revenue_chart(df_revenue):
    """Cria gráfico de área para receita projetada."""
    fig = px.area(df_revenue, x="Trimestre", y="Receita",
                 title="Projeção de Receita Trimestral - Ano 1")
    fig.update_layout(xaxis_title="Trimestre", 
                     yaxis_title="Receita (R$)")
    return fig

def create_investment_chart(df_investment):
    """Cria gráfico de barras para investimento inicial."""
    fig = px.bar(df_investment, x="Categoria", y="Investimento",
                title="Distribuição do Investimento Inicial (R$35.000)")
    fig.update_layout(xaxis_title="Categoria", 
                     yaxis_title="Investimento (R$)")
    return fig

def create_risk_heatmap(df_risk):
    """Cria mapa de calor para riscos."""
    fig = px.density_heatmap(df_risk, x="Probabilidade", y="Impacto",
                            z=df_risk["Probabilidade"] * df_risk["Impacto"],
                            hover_name="Risco", 
                            title="Matriz de Riscos")
    
    # Adiciona os nomes dos riscos
    for i, row in df_risk.iterrows():
        fig.add_annotation(
            x=row["Probabilidade"],
            y=row["Impacto"],
            text=row["Risco"],
            showarrow=False
        )
    
    fig.update_layout(xaxis_title="Probabilidade", 
                     yaxis_title="Impacto")
    return fig

def create_supplier_chart(df_suppliers):
    """Cria gráfico de barras para prazos de entrega."""
    fig = px.bar(df_suppliers, x="Fornecedor", y="Prazo_Entrega",
                color="Origem",
                title="Prazos de Entrega por Fornecedor")
    fig.update_layout(xaxis_title="Fornecedor", 
                     yaxis_title="Prazo de Entrega (dias)")
    return fig

def create_product_flow(df_suppliers):
    """Cria gráfico de fluxo de produtos (sunburst)."""
    fig = px.sunburst(df_suppliers,
                     path=["Origem", "Fornecedor"],
                     values="Prazo_Entrega",
                     title="Fluxo de Fornecimento de Produtos")
    return fig
