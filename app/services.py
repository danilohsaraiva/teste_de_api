import pandas as pd
import os

df = pd.read_csv("data/Relatorio_cadop.csv", delimiter=";")

# Caminho do arquivo CSV dentro do diretório "data"
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "Relatorio_cadop.csv")

def buscar_operadoras(termo):
    df = pd.read_csv(CSV_PATH, delimiter=";")  # Ajuste o delimitador conforme necessário
    resultado = df[df["Nome_Fantasia"].str.lower().str.contains(termo, na=False)]
    return resultado.to_dict(orient="records")