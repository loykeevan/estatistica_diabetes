from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# Caminho para os arquivos de dados de seu projeto
DADOS_ORIGINAIS = PASTA_DADOS / "diabetes_binary_5050split_health_indicators_BRFSS2015.csv"

# Caminho para os arquivos de dados de seu projeto
DADOS_TRATADOS = PASTA_DADOS / "diabetes_tratado.parquet"

# Caminhos que você julgar necessário
PASTA_IMAGENS = PASTA_PROJETO / "imagens"
