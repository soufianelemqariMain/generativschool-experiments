"""Frozen calendar forecasting experiment. Replay needs only the aggregated CSV."""
from pathlib import Path
import json,sys,platform
import numpy as np,pandas as pd,sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
P=Path(__file__).parent

def features(raw):
 d=raw.copy();d['date']=pd.to_datetime(dict(year=d.year,month=d.month,day=1));d=d.sort_values(['department','date'])
 # Explicit calendar joins: missing 2024 must never compress time.
 for lag in [24,36,48]:
  lookup=d[['department','date','accidents']].copy();lookup['date']+=pd.DateOffset(months=lag);lookup=lookup.rename(columns={'accidents':f'lag{lag}'})
  d=d.merge(lookup,on=['department','date'],how='left',validate='one_to_one')
 d['mean3']=d[['lag24','lag36','lag48']].mean(axis=1);d['sin']=np.sin(2*np.pi*d.month/12);d['cos']=np.cos(2*np.pi*d.month/12)
 return d.dropna(subset=['lag24','lag36','lag48']).sort_values(['date','department']).reset_index(drop=True)

def main():
 raw=pd.read_csv(P/'data/monthly.csv',dtype={'department':str});d=features(raw)
 train=d[d.year<=2023].copy();test=d[d.year==2025].copy();assert len(test)==96*12
 cols=['lag24','lag36','lag48','mean3','sin','cos'];X=pd.concat([d[cols],pd.get_dummies(d.department,prefix='dep',dtype=float)],axis=1)
 assert train.date.max()<test.date.min();assert 2024 not in raw.year.values
 modified=raw.copy();modified.loc[modified.year==2025,'accidents']+=9999;changed=features(modified)
 assert np.array_equal(d[cols].to_numpy(),changed[cols].to_numpy()),'future targets leaked into features'
 model=RandomForestRegressor(n_estimators=120,max_depth=8,min_samples_leaf=12,random_state=42,n_jobs=2)
 model.fit(X.loc[train.index],train.accidents)
 pred=model.predict(X.loc[test.index]);test['forest']=pred;test['same_month_2y']=test.lag24;test['historical_mean']=test.mean3
 names=['forest','same_month_2y','historical_mean']
 def metrics(frame):return {n:{'mae_accidents':float(mean_absolute_error(frame.accidents,frame[n])),'total_predicted':float(frame[n].sum())} for n in names}
 result={'status':'evaluated_prototype','train_rows':len(train),'test_rows':len(test),'departments':test.department.nunique(),'train_years':[int(train.year.min()),int(train.year.max())],'test_year':2025,'forecast_origin':'2025-01-01','latest_target_information':'2023-12','total_observed':int(test.accidents.sum()),'metrics':metrics(test),'by_quarter':{str(q):metrics(g) for q,g in test.groupby((test.month-1)//3+1)},'checks':{'no_future_target_leakage':True,'same_test_rows':True,'nonnegative_predictions':bool((pred>=0).all())},'environment':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'sklearn':sklearn.__version__},'limits':['Historical revised snapshots, not vintage archives','Recorded bodily injury accidents, not exposure-adjusted individual risk','No causal effect of prevention evaluated','2024 unavailable at forecast origin and excluded','Metropolitan France only']}
 (P/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');test[['year','month','department','accidents']+names].to_csv(P/'predictions.csv',index=False)
 pd.DataFrame([{'department':code,**{n:v['mae_accidents'] for n,v in metrics(g).items()}} for code,g in test.groupby('department')]).to_csv(P/'department-errors.csv',index=False)
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
