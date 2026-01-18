import pandas as pd
from pathlib import Path
import joblib

# -----------------------
# Папки
# -----------------------
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
MODELS_DIR = PROJECT_DIR / "models"

# -----------------------
# Загружаем тестовые данные
# -----------------------
X_test = pd.read_csv(PROCESSED_DIR / "X_test.csv")

# -----------------------
# Загружаем модель
# -----------------------
model = joblib.load(MODELS_DIR / "logreg_model.pkl")

# -----------------------
# Делаем предсказания
# -----------------------
y_pred = model.predict(X_test)

# -----------------------
# Сохраняем предсказания
# -----------------------
SUBMISSION_DIR = PROJECT_DIR / "data" / "predictions"
SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)

submission = pd.DataFrame({
    "PassengerId": X_test.index + 892,  # если индексы не совпадают с PassengerId
    "Survived": y_pred
})
submission.to_csv(SUBMISSION_DIR / "submission.csv", index=False)
print(f"Предсказания сохранены в {SUBMISSION_DIR / 'submission.csv'}")
