from pathlib import Path
import hashlib,json
import numpy as np,pandas as pd
from sklearn.metrics import mean_absolute_error
from run import features
P=Path(__file__).parent
manifest=json.loads((P/'manifest.json').read_text())
for name,digest in manifest['sha256'].items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,name
r=json.loads((P/'results.json').read_text());p=pd.read_csv(P/'predictions.csv',dtype={'department':str});assert len(p)==1152 and not p.duplicated(['year','month','department']).any()
assert p.department.nunique()==96 and set(p.year)=={2025} and set(p.month)==set(range(1,13))
for key in ['forest','same_month_2y','historical_mean']:assert np.isclose(mean_absolute_error(p.accidents,p[key]),r['metrics'][key]['mae_accidents'])
raw=pd.read_csv(P/'data/monthly.csv',dtype={'department':str});altered=raw.copy();altered.loc[altered.year==2025,'accidents']+=999999
cols=['lag24','lag36','lag48','mean3','sin','cos'];assert np.array_equal(features(raw)[cols].values,features(altered)[cols].values)
assert 2024 not in raw.year.values and raw.accidents.sum()>0
print('PASS: input hashes, 96 departments, 1152 rows, recomputed metrics, no future feature leakage')
