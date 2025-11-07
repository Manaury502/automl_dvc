import pandas as pd
import yaml

params = yaml.safe_load(open("params.yaml"))["data"]
df = pd.read_csv(params["raw"])

df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))
df.to_csv(params["processed"], index=False)

print("✅ Preprocesamiento completado.")
