import pandas as pd
import yaml, json
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

params = yaml.safe_load(open("params.yaml"))
data = pd.read_csv(params["data"]["processed"])

X = data.drop(columns=[params["train"]["target"]])
y = data[params["train"]["target"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "linear": LinearRegression(),
    "random_forest": RandomForestRegressor(),
    "gradient_boosting": GradientBoostingRegressor()
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    results[name] = mean_squared_error(y_test, pred)

best = min(results, key=results.get)
json.dump({"best_model": best, "metrics": results}, open("metrics.json", "w"), indent=4)
print("✅ Entrenamiento completado. Mejor modelo:", best)
