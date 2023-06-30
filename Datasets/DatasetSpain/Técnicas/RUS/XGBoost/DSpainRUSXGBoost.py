import pandas as pd
import xgboost
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score

from sklearn.model_selection import GridSearchCV
from Datasets.DatasetSpain.DatasetSpain import X_testSpain, y_testSpain, X_rusSpain, y_rusSpain, X_validSpain, y_validSpain
xgb = xgboost.XGBClassifier()

parametros = {'nthreads' : [1],
              'objective': ['binary:logistic'],
              'learning_rate': [0.15], #utilizamos 0.15 dado que da el mejor valor
              'n_estimators': [25]} #utilizamos 25 dado que da el mejor valor

fit_parametros = {'early_stopping_rounds': 10,
              'eval_metric': 'logloss',
              'eval_set': [(X_testSpain, y_testSpain)]}

clasificador = GridSearchCV(xgb,parametros, cv=3 , scoring = 'accuracy')

clasificador.fit(X_rusSpain, y_rusSpain, **fit_parametros)
print('mejor estimador:',clasificador.best_estimator_)
print('mejor puntaje:', clasificador.best_score_)

best_xgb = clasificador.best_estimator_
y_pred = best_xgb.predict(X_validSpain)
comparacion = pd.DataFrame({'Churn real': y_validSpain, 'Churn predicho': y_pred})
#print(comparacion.head(30))

precision = precision_score(y_validSpain, y_pred)
exactitud = accuracy_score(y_validSpain, y_pred)
Sensibilidad = recall_score(y_validSpain, y_pred)
valorF1 = f1_score(y_validSpain, y_pred)
CurvaROC = roc_auc_score(y_validSpain, y_pred)
print("Precisión (Precision): ",precision,"\n","Exactitud (Accuracy): ",exactitud,"\n",
      "Sensibilidad (Recall): ",Sensibilidad,"\n","Valor F1 (f1 score): ",valorF1,"\n","Curva ROC Score: ",CurvaROC)