import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# -----------------------
# Папки
# -----------------------
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent  # корень проекта titanic/
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
MODELS_DIR = PROJECT_DIR / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------
# Загружаем данные
# -----------------------
X = pd.read_csv(PROCESSED_DIR / "X_train.csv")
y = pd.read_csv(PROCESSED_DIR / "y_train.csv").squeeze()  # превращаем в 1D array

# -----------------------
# Делим на train/validation
# -----------------------
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------
# Обучаем модель
# -----------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------
# Оцениваем модель
# -----------------------
y_pred = model.predict(X_val)
acc = accuracy_score(y_val, y_pred)
print(f"Validation Accuracy: {acc:.4f}")

# -----------------------
# Сохраняем модель
# -----------------------
joblib.dump(model, MODELS_DIR / "logreg_model.pkl")
print(f"Модель сохранена в {MODELS_DIR / 'logreg_model.pkl'}")
