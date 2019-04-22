# coding: utf-8
import pandas as pd
import numpy as np
import sys
import os
from xgboost import XGBRegressor
# print(os.getcwd())#获得当前工作目录
train_df = pd.read_csv("./input/train.csv",index_col=0)
test_df = pd.read_csv("./input/test.csv",index_col=0)
# prices = pd.DataFrame({"price":train_df["SalePrice"],"log(price+1)":np.log1p(train_df["SalePrice"])})
# prices.hist()
y_train = np.log1p(train_df.pop("SalePrice"))
all_df =  pd.concat((train_df,test_df),axis=0)
all_df["MSSubClass"] = all_df["MSSubClass"].astype(str)
all_dummy_df = pd.get_dummies(all_df)
mean_cols = all_dummy_df.mean()
all_dummy_df = all_dummy_df.fillna(mean_cols)
numeric_cols = all_df.columns[all_df.dtypes!="object"]
numeric_cols_means = all_dummy_df.loc[:,numeric_cols].mean()
numeric_col_std = all_dummy_df.loc[:,numeric_cols].std()
all_dummy_df.loc[:,numeric_cols] = (all_dummy_df.loc[:,numeric_cols]-numeric_cols_means)/numeric_col_std
dummy_train_df = all_dummy_df.loc[train_df.index]
dummy_test_df = all_dummy_df.loc[test_df.index]
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
X_train = dummy_train_df.values
X_test = dummy_test_df.values
alphas = np.logspace(-3,2,50)
test_scores = []
for alpha in alphas:
    clf = Ridge(alpha)
    test_score = np.sqrt(-cross_val_score(clf,X_train,y_train,cv=10,scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
import matplotlib.pyplot as plt
# %matplotlib inline
# print(np.array(test_scores).shape)
plt.plot(alphas,test_scores)
plt.title("Alpha vs Error")
plt.show()
from sklearn.ensemble import RandomForestRegressor
max_features = [.1, .3, .5, .7, .9, .99]
test_scores = []
for max_feat in max_features:
    clf = RandomForestRegressor(n_estimators=200, max_features=max_feat)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=5, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
plt.plot(max_features, test_scores)
plt.title("Max Features vs CV Error");
plt.show()
ridge = Ridge(alpha=15)
rf = RandomForestRegressor(n_estimators=500, max_features=.3)
y_ridge = np.expm1(ridge.predict(X_test))
y_rf = np.expm1(rf.predict(X_test))
y_final = (y_ridge + y_rf) / 2
submission_df = pd.DataFrame(data={'Id': test_df.index, 'SalePrice': y_final})
submission_df.to_csv("sample_submission.csv", index=0)
