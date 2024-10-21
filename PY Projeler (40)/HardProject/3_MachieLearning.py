#Proje Açıklaması: scikit-learn kullanarak bir makine öğrenmesi modeli oluşturun
#  ve iris veri seti üzerinde sınıflandırma yapın.


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Veri setini yükler
iris = load_iris()
X = iris.data
y = iris.target

# Eğitim ve test setlerine böler
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Veriyi ölçeklendirir
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modeli oluşturur
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Tahmin yapar
y_pred = model.predict(X_test)

# Sonuçları değerlendirir
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))



# scikit-learn ile veri seti yüklenir ve ön işleme tabi tutulur.
# Eğitim ve test setlerine ayrılır.
# RandomForestClassifier modeli oluşturulur ve eğitilir.
# Modelin performansı confusion matrix ve classification report ile değerlendirilir.