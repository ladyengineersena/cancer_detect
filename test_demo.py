# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print(' KANSER TEŞHİS SİSTEMİ - HIZLI DEMO')
print('=' * 50)

# Veri oluşturma
np.random.seed(42)
n_samples = 1000

features = {
    'mean_radius': np.random.normal(14, 3, n_samples),
    'mean_texture': np.random.normal(19, 4, n_samples),
    'mean_perimeter': np.random.normal(91, 24, n_samples),
    'mean_area': np.random.normal(654, 351, n_samples),
    'mean_smoothness': np.random.normal(0.096, 0.014, n_samples)
}

malignant_prob = 0.3
target = np.random.binomial(1, malignant_prob, n_samples)

for i in range(n_samples):
    if target[i] == 1:
        for feature in features:
            features[feature][i] *= np.random.uniform(1.1, 1.5)

df = pd.DataFrame(features)
df['diagnosis'] = target

print(f'Veri seti boyutu: {df.shape}')
print(f'Kanser oranı: {df["diagnosis"].mean():.2%}')

# Veri ön işleme
X = df.drop(columns=['diagnosis'])
y = df['diagnosis']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f'Eğitim seti: {X_train.shape}')
print(f'Test seti: {X_test.shape}')

# Model eğitimi
print('Modeller eğitiliyor...')

rf = RandomForestClassifier(random_state=42, n_estimators=100)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Random Forest Sonuçları:')
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1-Score: {f1:.4f}')

# Örnek tahmin
sample_X = X_test.sample(1)
sample_y = y_test[sample_X.index[0]]

prediction = rf.predict(sample_X)[0]
probability = rf.predict_proba(sample_X)[0]

predicted_class = 'Kanserli' if prediction == 1 else 'Sağlıklı'
actual_class = 'Kanserli' if sample_y == 1 else 'Sağlıklı'
confidence = probability[1] if prediction == 1 else probability[0]

print(f'Örnek Tahmin:')
print(f'Gerçek: {actual_class}')
print(f'Tahmin: {predicted_class}')
print(f'Güven: {confidence:.2%}')

print(f'Demo başarıyla tamamlandı!')
print(f'Model Accuracy: {accuracy:.2%}')
