import pandas as pd
from pathlib import Path

# -----------------------
# Папки
# -----------------------
RAW_DIR = Path("data/raw")
INTERIM_DIR = Path("data/interim")
INTERIM_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------
# Загружаем исходные данные
# -----------------------
train_df = pd.read_csv(RAW_DIR / "train.csv")
test_df = pd.read_csv(RAW_DIR / "test.csv")

# -----------------------
# Обработка train
# -----------------------
train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})
train_df['FamilySize'] = train_df['SibSp'] + train_df['Parch'] + 1

# Сохраняем промежуточные файлы
train_df.to_csv(INTERIM_DIR / "train_cleaned.csv", index=False)
train_df[['Pclass', 'Sex', 'Age', 'FamilySize']].to_csv(INTERIM_DIR / "train_features.csv", index=False)

# -----------------------
# Обработка test
# -----------------------
test_df['Age'] = test_df['Age'].fillna(test_df['Age'].median())
test_df['Sex'] = test_df['Sex'].map({'male': 0, 'female': 1})
test_df['FamilySize'] = test_df['SibSp'] + test_df['Parch'] + 1

test_df.to_csv(INTERIM_DIR / "test_cleaned.csv", index=False)
test_df[['Pclass', 'Sex', 'Age', 'FamilySize']].to_csv(INTERIM_DIR / "test_features.csv", index=False)

print("Файлы успешно созданы в data/interim/")
