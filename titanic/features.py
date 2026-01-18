import pandas as pd
from pathlib import Path

# -----------------------
# Папки
# -----------------------
INTERIM_DIR = Path("data/interim")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------
# Загружаем промежуточные данные
# -----------------------
train_features = pd.read_csv(INTERIM_DIR / "train_features.csv")
train_cleaned = pd.read_csv(INTERIM_DIR / "train_cleaned.csv")
test_features = pd.read_csv(INTERIM_DIR / "test_features.csv")

# -----------------------
# Разделяем X и y
# -----------------------
X_train = train_features
y_train = train_cleaned['Survived']  # целевая переменная

X_test = test_features

# -----------------------
# Сохраняем обработанные данные
# -----------------------
X_train.to_csv(PROCESSED_DIR / "X_train.csv", index=False)
y_train.to_csv(PROCESSED_DIR / "y_train.csv", index=False)
X_test.to_csv(PROCESSED_DIR / "X_test.csv", index=False)

print("Файлы успешно созданы в data/processed/")