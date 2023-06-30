import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, RepeatedKFold
from Datasets.DatasetGermany.DatasetGermany import X_testGermany, y_testGermany, X_smote_ennGermany, y_smote_ennGermany, X_validGermany, y_validGermany

X_testGermany = pd.concat([X_testGermany, X_validGermany])
y_testGermany = pd.concat([y_testGermany, y_validGermany])

knn = KNeighborsClassifier()
parametros = {'n_neighbors': [2], # Los valores probados en este parámetro fueron: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30. Y seleccionamos el que se muestra ahora.
            }

grid = GridSearchCV(knn, parametros, cv=3, scoring='accuracy', return_train_score=False, verbose=1)

KNN_model = grid.fit(X_smote_ennGermany, y_smote_ennGermany)

print(KNN_model.best_params_, ":",KNN_model.scoring)
KNN_model.score(X_testGermany, y_testGermany)
y_pred = KNN_model.predict(X_testGermany)

comparacion = pd.DataFrame({'Churn real': y_testGermany, 'Churn predicho': y_pred})
#print(comparacion.head(30))

print('mejor estimador:', KNN_model.best_score_)
precision = precision_score(y_testGermany, y_pred)
exactitud = accuracy_score(y_testGermany, y_pred)
Sensibilidad = recall_score(y_testGermany, y_pred)
valorF1 = f1_score(y_testGermany, y_pred)
CurvaROC = roc_auc_score(y_testGermany, y_pred)
print("Precisión (Precision): ",precision,"\n","Exactitud (Accuracy): ",exactitud,"\n",
      "Sensibilidad (Recall): ",Sensibilidad,"\n","Valor F1 (f1 score): ",valorF1,"\n","Curva ROC Score: ",CurvaROC)