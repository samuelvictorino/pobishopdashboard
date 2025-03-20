import pandas as pd
import numpy as np

def load_market_overview_data():
    """Carrega dados para visão geral do mercado."""
    # Dados geográficos
    regions = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
    df_geo = pd.DataFrame({
        "Regiao": regions,
        "Publico": [5000, 15000, 7000, 30000, 10000]
    })
    
    # Projeção de crescimento
    df_growth = pd.DataFrame({
        "Ano": [2024, 2025, 2026],
        "Faturamento": [200, 235, 260]  # Valores em bilhões
    })
    
    # KPIs principais
    kpis = {
        "Mercado Total": "R$ 235 Bilhões",
        "Taxa de Crescimento": "10.5%",
        "Ticket Médio": "R$ 492,40",
        "Inflação": "5.06%",
        "Taxa Selic": "15%"
    }
    
    return df_geo, df_growth, kpis

def load_target_audience_data():
    """Carrega dados do público-alvo."""
    # Dados demográficos
    df_demo = pd.DataFrame({
        "Faixa_Etaria": ["25-30", "31-35", "36-40", "41-45"],
        "Masculino": [40, 35, 30, 25],
        "Feminino": [38, 32, 28, 20]
    })
    
    # Renda média por classe
    df_income = pd.DataFrame({
        "Classe": ["C", "D", "E"],
        "Renda_Media": [3500, 2500, 1500]
    })
    
    # Perfil de comportamento
    df_behavior = pd.DataFrame({
        "Categoria": ["Organização Doméstica", "Economia de Recursos", 
                     "Mobilidade", "Conectividade", "Qualidade"],
        "Pontuacao": [80, 70, 60, 50, 65]
    })
    
    # Dados das personas
    personas = [
        {"Nome": "Leozito", "Idade": 28, "Ocupacao": "Auxiliar de cozinha", 
         "Descricao": "Valoriza praticidade e economia."},
        {"Nome": "Juju", "Idade": 32, "Ocupacao": "Administrativa", 
         "Descricao": "Focada em orçamento e organização."},
        {"Nome": "Enzo", "Idade": 25, "Ocupacao": "Entregador", 
         "Descricao": "Busca produtos duráveis para mobilidade."},
        {"Nome": "Val", "Idade": 33, "Ocupacao": "Vendedora", 
         "Descricao": "Procura itens multifuncionais."},
        {"Nome": "Tulinho", "Idade": 30, "Ocupacao": "Técnico de informática", 
         "Descricao": "Valoriza tecnologia com custo acessível."}
    ]
    
    return df_demo, df_income, df_behavior, personas

def load_competitive_data():
    """Carrega dados da análise competitiva."""
    df_competitors = pd.DataFrame({
        "Concorrente": ["Shopee", "AliExpress", "Shein", "Mercado Livre", 
                       "Americanas", "Utilidomésticos"],
        "Preco": [30, 25, 35, 40, 38, 28],
        "Qualidade": [60, 55, 65, 70, 68, 50],
        "Market_Share": [25, 30, 20, 15, 10, 5]
    })
    
    return df_competitors

def load_products_data():
    """Carrega dados de produtos e precificação."""
    df_products = pd.DataFrame({
        "Produto": ["Organizador", "Carregador", "Fones", "Processador", "Timer"],
        "Categoria": ["Utilidade", "Eletrônico", "Eletrônico", "Eletrônico", "Utilidade"],
        "Preco": [50, 60, 40, 80, 35],
        "Margem": [75, 70, 80, 65, 78],  # percentuais
        "Demanda": [85, 90, 75, 60, 80]
    })
    
    return df_products

def load_financial_data():
    """Carrega dados financeiros."""
    df_revenue = pd.DataFrame({
        "Trimestre": ["T1", "T2", "T3", "T4"],
        "Receita": [16000, 37000, 64000, 105000]
    })
    
    df_investment = pd.DataFrame({
        "Categoria": ["Plataforma", "Marketing", "Produtos", 
                     "Administrativo", "Reserva"],
        "Investimento": [5800, 13200, 8000, 3000, 5000]
    })
    
    return df_revenue, df_investment

def load_swot_data():
    """Carrega dados da análise SWOT."""
    swot = {
        "Forcas": ["Posicionamento Diferenciado", "Curadoria Especializada", 
                  "Marketing Eficiente", "Operação Enxuta"],
        "Fraquezas": ["Modelo dropshipping limitado", "Recursos financeiros restritos", 
                      "Marca nova"],
        "Oportunidades": ["Crescimento e-commerce classes C/D", 
                          "Demanda por economia real", 
                          "Fornecedores nacionais ampliados"],
        "Ameacas": ["Novas taxas de importação", "Alta concorrência", 
                   "Ambiente econômico volátil"]
    }
    
    df_risk = pd.DataFrame({
        "Risco": ["Importação", "Qualidade", "Entrega", "Concorrência"],
        "Probabilidade": [0.7, 0.5, 0.6, 0.8],
        "Impacto": [0.8, 0.7, 0.6, 0.9]
    })
    
    return swot, df_risk

def load_supplier_data():
    """Carrega dados de fornecedores e logística."""
    df_suppliers = pd.DataFrame({
        "Fornecedor": ["AliExpress", "DSers", "Zendrop", 
                      "Mais Que Distribuidora", "Kaisan"],
        "Origem": ["Internacional", "Internacional", "Internacional", 
                  "Nacional", "Nacional"],
        "Prazo_Entrega": [40, 35, 30, 5, 7]
    })
    
    return df_suppliers
