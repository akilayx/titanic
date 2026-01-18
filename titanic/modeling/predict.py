import pandas as pd
from pathlib import Path
import joblib

# -----------------------
# Папки
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data/processed"
MODELS_DIR = BASE_DIR / "models"
PREDICTIONS_DIR = BASE_DIR / "data/predictions"
PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------
# Загружаем тестовые данные и модель
# -----------------------
X_test = pd.read_csv(PROCESSED_DIR / "X_test.csv")
model = joblib.load(MODELS_DIR / "logreg_model.pkl")

# -----------------------
# Делаем предсказания
# -----------------------
y_pred = model.predict(X_test)

# -----------------------
# Сохраняем в submission.csv
# -----------------------
submission = pd.DataFrame({
    "PassengerId": pd.read_csv(BASE_DIR / "data/raw/test.csv")["PassengerId"],
    "Survived": y_pred
})

submission.to_csv(PREDICTIONS_DIR / "submission.csv", index=False)
print(f"Файл submission.csv создан в {PREDICTIONS_DIR}")
