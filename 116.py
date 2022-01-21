from random import random
import pandas as pd
import plotly.express as px

df = pd.read_csv("data_classification.csv")

hour_slept = df["Hours_Slept"].tolist()
hour_studied = df["Hours_studied"].tolist()

fig = px.scatter(x=hour_slept, y=hour_studied)
fig.show()

import plotly.graph_objects as go

hours_slept = df["Hours_Slept"].tolist()
hours_studied = df["Hours_studied"].tolist()

results = df["results"].tolist()
colors=[]
for data in results:
  if data == 1:
    colors.append("green")
  else:
    colors.append("red")



fig = go.Figure(data=go.Scatter(
    x=hours_studied,
    y=hours_slept,
    mode='markers',
    marker=dict(color=colors)
))
fig.show()

hours = df[["Hours_studied","Hours_Slept"]]
result = df["results"]

from sklearn.model_selection import train_test_split 

hours_train, hours_test, results_train, results_test = train_test_split(hours, results, test_size = 0.25, random_state = 0)
print(hours_train)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state = 0)
classifier.fit(hours_train,results_train)

[ ]


from sklearn.linear_model import LogisticRegression 

classifier = LogisticRegression(random_state = 0) 
classifier.fit(hours_train, results_train)

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=0, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)


results_pred = classifier.predict(hours_test)

from sklearn.metrics import accuracy_score 
print ("Accuracy : ", accuracy_score(results_test, results_pred))
