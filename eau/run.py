import json,zipfile,io,hashlib
from pathlib import Path
import numpy as np,pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
P=Path(__file__).resolve().parent
meta=json.loads((P/'data/extraction.json').read_text());f=pd.read_csv(P/'data/entrees.csv');flags=meta['flags']
x=f.copy();x[['P106.3','VP.056','VP.077']]=np.log1p(x[['P106.3','VP.056','VP.077']]);x=StandardScaler().fit_transform(x);models=[IsolationForest(n_estimators=200,contamination=.05,random_state=seed,n_jobs=2).fit(x) for seed in [42,7]];score=-models[0].score_samples(x);other=-models[1].score_samples(x);k=int(np.ceil(.05*len(f)));a=set(np.argsort(-score)[:k]);b=set(np.argsort(-other)[:k]);low=set(np.argsort(f['P104.3'].to_numpy())[:k]);f['anomaly_score']=score;f['selected']=False;f.iloc[list(a),f.columns.get_loc('selected')]=True;f.to_csv(P/'data/profils-anonymes.csv',index=False);result={'source_rows':meta['source_rows'],'complete_distribution_services':len(f),'selected_count':k,'overlap_seeds_count':len(a&b),'overlap_low_yield_count':len(a&low),'yield_median_all':float(f['P104.3'].median()),'yield_median_selected':float(f.iloc[list(a)]['P104.3'].median()),'flags':{c:{str(k):int(v) for k,v in vals.items()} for c,vals in flags.items()},'snapshot_sha256':meta['snapshot_sha256'],'status':'exploratoire sans vérité terrain'};(P/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
