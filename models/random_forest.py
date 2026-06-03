# packages
import os
import pandas as pd
import numpy as np
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score
np.random.seed(256)

# data
base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
train_path_csv = os.path.join(base, "data", "processed", "train.csv")
df_train = pd.read_csv(train_path_csv)
val_path_csv = os.path.join(base, "data", "processed", "val.csv")
df_val = pd.read_csv(val_path_csv)
test_path_csv = os.path.join(base, "data", "processed", "test.csv")
df_test = pd.read_csv(test_path_csv)
x_vars = ['contrast_level', 'eye_cat', 'hair_cat', 'skin_tone']

# Hyperparameter GridSearch
experiments = [
    # baseline
    {"rf__n_estimators": 100, "rf__max_depth": 10, "rf__min_samples_split": 5, "rf__min_samples_leaf": 2, "rf__max_features": "sqrt", "rf__class_weight": None},
    # wider/better generalize(small depth, large min sample, sqrt)
    {"rf__n_estimators": 100, "rf__max_depth": 4, "rf__min_samples_split": 10, "rf__min_samples_leaf": 2, "rf__max_features": "sqrt", "rf__class_weight": None},
    # deeper/more complex(large depth, less min samples, log2)
    {"rf__n_estimators": 100, "rf__max_depth": 20, "rf__min_samples_split": 2, "rf__min_samples_leaf": 2, "rf__max_features": "log2", "rf__class_weight": None},
    # balancing
    {"rf__n_estimators": 100, "rf__max_depth": 10, "rf__min_samples_split": 5, "rf__min_samples_leaf": 2, "rf__max_features": "sqrt", "rf__class_weight": "balanced"},
    # more trees
    {"rf__n_estimators": 200, "rf__max_depth": 10, "rf__min_samples_split": 5, "rf__min_samples_leaf": 2, "rf__max_features": "sqrt", "rf__class_weight": None},
    # less trees
    {"rf__n_estimators": 50, "rf__max_depth": 10, "rf__min_samples_split": 5, "rf__min_samples_leaf": 2, "rf__max_features": "sqrt", "rf__class_weight": None},
]

print(f"Grid defined with {len(experiments)} configurations.")

# run experiments
results = []

X_train = df_train[x_vars]
preprocess = ColumnTransformer(
    transformers = [
        ("cat", OneHotEncoder(handle_unknown="ignore"), X_train.columns.tolist())
    ]
)
le = LabelEncoder()
y_train = df_train['season']
y_train_enc = le.fit_transform(y_train)
X_val = df_val[x_vars]
y_val = df_val['season']
y_val_enc = le.transform(y_val)
for i, params in enumerate(experiments):
  print(f"\n======= Running Experiment {i+1}/{len(experiments)} =======")
  print(params)
  pipeline = Pipeline([
      ("preprocess", preprocess),
      ("rf", RandomForestClassifier(random_state=256))
  ])
  pipeline.set_params(**params)
  pipeline.fit(X_train, y_train_enc)
  y_pred = pipeline.predict(X_val)
  f1 = f1_score(y_val_enc, y_pred, average = "macro")
  accuracy = accuracy_score(y_val_enc, y_pred)
  print(f"F1 score: {f1}    |     Accuracy: {accuracy}")
  results.append({
      "experiment": i,
      "params": params,
      "f1_score": f1,
      "accuracy": accuracy
  })

# sort results and retain best model
df_results = pd.DataFrame(results)
best_model = df_results.sort_values("accuracy", ascending = False).iloc[0]['params']

# retrain
pipeline.set_params(**best_model)
pipeline.fit(X_train, y_train_enc)

# score on test
X_test = df_test[x_vars]
y_test = df_test["season"]
y_test_enc = le.transform(y_test)
y_pred = pipeline.predict(X_test)
f1 = f1_score(y_test_enc, y_pred, average = "macro")
accuracy = accuracy_score(y_test_enc, y_pred)
print(f"F1 score: {f1}    |     Accuracy: {accuracy}")

# save model to pkl
os.makedirs("models", exist_ok=True)
model_bundle = {
  "pipeline": pipeline,
  "label_encoder": le,
  "best_params": best_model
}
with open("models/rf.pkl", "wb") as f:
  pickle.dump(model_bundle, f)

rf_model = pipeline.named_steps["rf"]
ohe = pipeline.named_steps["preprocess"].named_transformers_["cat"]
feature_names = ohe.get_feature_names_out(X_train.columns)
importances = rf_model.feature_importances_
importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
}).sort_values("importance", ascending=False)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 12))
plt.barh(importance_df["feature"], importance_df["importance"])
plt.gca().invert_yaxis()
plt.title("Random Forest Feature Importance")
plt.xlabel("Importance")
plt.savefig("visualizations/rf_varImp.png", dpi=300, bbox_inches="tight")


