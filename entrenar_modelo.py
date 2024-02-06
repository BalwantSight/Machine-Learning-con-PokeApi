from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('pokemon_data.csv')

# División del conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(
    df.drop('tipo', axis=1), df['tipo'], test_size=0.2, random_state=42)

# Entrenamiento del modelo
model = RandomForestClassifier()
model.fit(X_train[['experiencia_base', 'altura', 'peso']], y_train)

# Guardar el modelo entrenado
joblib.dump(model, 'pokemon_model.joblib')

# Gráficos de dispersión
scatter_plot = sns.pairplot(df[['experiencia_base', 'altura', 'peso']])
scatter_plot.savefig('scatter_plot.png')
