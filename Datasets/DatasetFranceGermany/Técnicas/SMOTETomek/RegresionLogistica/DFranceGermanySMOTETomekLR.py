import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, RepeatedKFold
from Datasets.DatasetFranceGermany.DatasetFranceGermany import X_testFranceGermany, y_testFranceGermany, X_smote_tomekFranceGermany, y_smote_tomekFranceGermany, X_validFranceGermany, y_validFranceGermany

X_testFranceGermany = pd.concat([X_testFranceGermany, X_validFranceGermany])
y_testFranceGermany = pd.concat([y_testFranceGermany, y_validFranceGermany])

parametros={"C":[100], # Los valores probados en este parámetro fueron:0.00001,0.0001,0.001,0.01,0.1,1,10,100,1000,10000,100000. Y seleccionamos el que se muestra ahora.
            "penalty":["l2"]}
modelobase=LogisticRegression(solver = 'liblinear')
RLmodel=GridSearchCV(modelobase,parametros,cv=3,scoring='accuracy')

RLmodel.fit(X_smote_tomekFranceGermany, y_smote_tomekFranceGermany)
print(RLmodel.best_params_, ":",RLmodel.scoring)
RLmodel.score(X_testFranceGermany, y_testFranceGermany)
y_pred = RLmodel.predict(X_testFranceGermany)

comparacion = pd.DataFrame({'Churn real': y_testFranceGermany, 'Churn predicho': y_pred})
#print(comparacion.head(30))

print('mejor estimador:', RLmodel.best_score_)
precision = precision_score(y_testFranceGermany, y_pred)
exactitud = accuracy_score(y_testFranceGermany, y_pred)
Sensibilidad = recall_score(y_testFranceGermany, y_pred)
valorF1 = f1_score(y_testFranceGermany, y_pred)
CurvaROC = roc_auc_score(y_testFranceGermany, y_pred)
print("Precisión (Precision): ",precision,"\n","Exactitud (Accuracy): ",exactitud,"\n",
      "Sensibilidad (Recall): ",Sensibilidad,"\n","Valor F1 (f1 score): ",valorF1,"\n","Curva ROC Score: ",CurvaROC)