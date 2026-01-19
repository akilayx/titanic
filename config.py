from pathlib import Path

# Берём корень проекта (две папки выше файла config.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Папка с данными
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"               # train.csv, test.csv, submission.csv
INTERIM_DIR = DATA_DIR / "interim"       # промежуточные очищенные файлы
PROCESSED_DIR = DATA_DIR / "processed"   # X_train.csv, y_train.csv, X_test.csv
PREDICTIONS_DIR = DATA_DIR / "predictions"  # финальные предсказания

# Папки для моделей и отчётов
MODELS_DIR = BASE_DIR / "models"         # логистическая регрессия и др.
REPORTS_DIR = BASE_DIR / "reports"       # отчёты
FIGURES_DIR = REPORTS_DIR / "figures"    # графики и визуализации

