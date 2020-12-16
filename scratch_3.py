import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm

match=pd.read_csv("C:/Users/JAYANK/Desktop/NEW/College Project/matches.csv")
# create a column name homeground
match['homeground']='0'
row_remove=['Cape Town', 'Port Elizabeth', 'Durban', 'Centurion','East London', 'Johannesburg', 'Kimberley',
            'Bloemfontein','Sharjah','Abu Dhabi']
row_remove1=['Gujarat Lions','Rising Pune Supergiant','Deccan Chargers','Kochi Tuskers Kerala',
             'Pune Warriors','Rising Pune Supergiants']

for i in row_remove:
        match.drop(match.loc[match['city']==i].index,inplace=True)
for i in row_remove1:
        match.drop(match.loc[match['team1']==i].index,inplace=True)
for i in row_remove1:
        match.drop(match.loc[match['team2']==i].index,inplace=True)
for i in row_remove1:
        match.drop(match.loc[match['winner']==i].index,inplace=True)

match.replace(['Delhi Daredevils'],['Delhi Capitals'],inplace=True)

match.replace(['Sunrisers Hyderabad', 'Mumbai Indians','Royal Challengers Bangalore',
       'Kolkata Knight Riders', 'Kings XI Punjab',
       'Chennai Super Kings', 'Rajasthan Royals','Delhi Capitals'],['SRH','MI','RCB','KKR','KXIP','CSK','RR','DC'],inplace=True)

match['homeground']=match['city']

match_filter=match[['season','city','date','team1','team2','toss_winner','toss_decision','result','dl_applied','winner','homeground']]

match_filter.dropna(inplace=True)

# Label Encoding
encode={
'team1':{'CSK':0,'DC':1,'KKR':2,'KXIP':3,'MI':4,'RCB':5,'RR':6,'SRH':7},
'team2':{'CSK':0,'DC':1,'KKR':2,'KXIP':3,'MI':4,'RCB':5,'RR':6,'SRH':7},
'toss_winner':{'CSK':0,'DC':1,'KKR':2,'KXIP':3,'MI':4,'RCB':5,'RR':6,'SRH':7},
'winner':{'CSK':0,'DC':1,'KKR':2,'KXIP':3,'MI':4,'RCB':5,'RR':6,'SRH':7},
'homeground':{'CSK':0,'DC':1,'KKR':2,'KXIP':3,'MI':4,'RCB':5,'RR':6,'SRH':7}}

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
match_filter['team1']=label_encoder.fit_transform(match_filter['team1'])
match_filter['team2']=label_encoder.fit_transform(match_filter['team2'])
match_filter['toss_winner']=label_encoder.fit_transform(match_filter['toss_winner'])
match_filter['winner']=label_encoder.fit_transform(match_filter['winner'])
match_filter['homeground']=label_encoder.fit_transform(match_filter['homeground'])
match_filter['toss_decision']=label_encoder.fit_transform(match_filter['toss_decision'])

match_filter=match_filter[['team1','team2','toss_decision','toss_winner','winner','homeground','city']]

match_filter=pd.DataFrame(match_filter)


def classification_model(model, data, predictors, outcome):
    model.fit(data[predictors], data[outcome])
    predictions = model.predict(data[predictors])
    accuracy = metrics.accuracy_score(predictions, data[outcome])
    kf = KFold(3, True)
    error = []
    for train, test in kf.split(data):
        train_predictors = (data[predictors].iloc[train, :])
        train_target = data[outcome].iloc[train]
        model.fit(train_predictors, train_target)
        error.append(model.score(data[predictors].iloc[test, :], data[outcome].iloc[test]))
        print('Cross-Validation Score : %s' % '{0:.3%}'.format(np.mean(error)))
        model.fit(data[predictors], data[outcome])
    print('Accuracy : %s' % '{0:.3%}'.format(accuracy))

model=RandomForestClassifier(n_estimators=100,n_jobs=1)
output_set=['winner']
input_set=['team1','team2','toss_decision','toss_winner','homeground']
classification_model(model,match_filter,input_set,output_set)

import pickle
pickle_out=open('model1.pkl','wb')
pickle.dump(model1,pickle_out)
pickle_out.close()
