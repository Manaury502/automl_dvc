Laboratorio 1 — Gestión de Experimentación y Modelos con DVC (AutoML)
Maestría en Data Science — Octubre 2025

--------------------------------------------------
OBJETIVO
--------------------------------------------------
Este proyecto implementa un pipeline automatizado inspirado en los principios de AutoML, utilizando DVC (Data Version Control) y Git para gestionar datasets, modelos y experimentos de forma reproducible.

El objetivo es:
- Entrenar automáticamente distintos modelos.
- Versionar datasets, parámetros y métricas.
- Analizar cómo los cambios en los datos afectan el rendimiento del modelo.

--------------------------------------------------
TECNOLOGÍAS UTILIZADAS
--------------------------------------------------
Python 3.10+
DVC 3.x
Git
scikit-learn
pandas
numpy
pyyaml

Instalación de dependencias:
    pip install -r requirements.txt

--------------------------------------------------
ESTRUCTURA DEL PROYECTO
--------------------------------------------------
automl_dvc/
│
├── data/
│   ├── dataset_v1.csv
│   ├── dataset_v2.csv
│   ├── dataset_v3.csv
│   ├── dataset_v4.csv
│   ├── processed.csv
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│
├── params.yaml
├── dvc.yaml
├── metrics.json
├── results.csv
└── README.txt

--------------------------------------------------
PIPELINE DEL PROYECTO
--------------------------------------------------
El pipeline se compone de dos etapas principales definidas en dvc.yaml:

1. Preprocesamiento (src/preprocess.py)
   - Limpieza de datos.
   - Eliminación de duplicados y valores nulos.
   - Codificación y normalización según corresponda.

2. Entrenamiento y evaluación (src/train.py)
   - Entrenamiento de los modelos:
       * Regresión Lineal
       * Random Forest
       * Gradient Boosting
   - Evaluación de desempeño (MSE).
   - Registro de métricas en metrics.json.

Ejecución del pipeline:
    dvc repro

Visualización de resultados:
    dvc metrics show
    dvc metrics diff

--------------------------------------------------
EVOLUCIÓN DE LOS DATASETS
--------------------------------------------------
Versión: dataset_v1.csv
Descripción: Versión original. Datos crudos sin modificaciones.

Versión: dataset_v2.csv
Descripción: Limpieza. No se encontraron valores nulos ni filas duplicadas (0 eliminadas).

Versión: dataset_v3.csv
Descripción: Ampliación. Se agregaron 2 nuevos registros al dataset.

Versión: dataset_v4.csv
Descripción: Transformación. Eliminación de columna 'AveBedrms' y normalización Min-Max.

--------------------------------------------------
RESULTADOS DEL MODELO
--------------------------------------------------
Archivo metrics.json:
{
    "best_model": "random_forest",
    "metrics": {
        "linear": 0.5553105398510998,
        "random_forest": 0.2631660193779494,
        "gradient_boosting": 0.3033022343420278
    }
}

El modelo ganador fue Random Forest con el menor error cuadrático medio (MSE).

--------------------------------------------------
RESULTADOS COMPARATIVOS
--------------------------------------------------
version,best_model,mse
v1,random_forest,0.285
v2,random_forest,0.272
v3,gradient_boosting,0.265
v4,random_forest,0.263

Se observa una mejora progresiva del rendimiento conforme se limpiaron, ampliaron y transformaron los datos.

--------------------------------------------------
REPRODUCIBILIDAD
--------------------------------------------------
Todo el flujo experimental puede reproducirse con:
    dvc repro
    dvc metrics show
    dvc metrics diff

El control de versiones se maneja con Git y DVC, permitiendo reconstruir cualquier versión previa del dataset o del modelo.

--------------------------------------------------
CONCLUSIONES
--------------------------------------------------
- La gestión de experimentos con DVC permite un flujo reproducible y transparente.
- La limpieza y transformación de datos impactan positivamente en el rendimiento del modelo.
- Random Forest resultó ser el modelo más robusto y con mejor generalización.
- La automatización mediante params.yaml y dvc repro reduce el tiempo de experimentación.

--------------------------------------------------
ENTREGA
--------------------------------------------------
Repositorio GitHub: (enlace al repositorio o release/tag)

Para reproducir:
    git clone <URL_DEL_REPO>
    cd automl_dvc
    dvc repro
