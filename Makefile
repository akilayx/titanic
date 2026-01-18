.PHONY: data features train predict all clean

# Python
PYTHON = python

# Scripts
DATASET_SCRIPT = titanic/dataset.py
FEATURES_SCRIPT = titanic/features.py
TRAIN_SCRIPT = titanic/modeling/train.py
PREDICT_SCRIPT = titanic/modeling/predict.py

# -------------------------
# Prepare raw and processed data
# -------------------------
data:
	@echo "Подготовка данных..."
	$(PYTHON) $(DATASET_SCRIPT)
	$(MAKE) features

features:
	@echo "Создание признаков..."
	$(PYTHON) $(FEATURES_SCRIPT)

# -------------------------
# Train model
# -------------------------
train:
	@echo "Обучение модели..."
	$(PYTHON) $(TRAIN_SCRIPT)

# -------------------------
# Predict using trained model
# -------------------------
predict:
	@echo "Предсказание модели..."
	$(PYTHON) $(PREDICT_SCRIPT)

# -------------------------
# Run all steps
# -------------------------
all: data train predict

# -------------------------
# Clean all generated files
# -------------------------
clean:
	@echo "Очистка временных и выходных файлов..."
	rm -rf data/interim/*
	rm -rf data/processed/*
	rm -rf data/predictions/*
	rm -rf models/*
