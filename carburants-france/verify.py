import json,math,statistics
from datetime import date,timedelta
from run import R,inputs,panel,macro,enrich,predict,METHODS,OIL,GEO
r=json.loads((R/'results.json').read_text());rows=r['predictions'];seen=set()
for p in rows:
 key=(p['fuel'],p['station'],p['date']);assert key not in seen;seen.add(key)
 assert date.fromisoformat(p['date'])-date.fromisoformat(p['origin'])==timedelta(days=7)
 assert p['training_last_target']<=p['origin']<p['date']
 assert date.fromisoformat(p['origin'])-date.fromisoformat(p['macro_observation'])>=timedelta(days=14)
 assert p['date'].startswith('2026') and p['date']<='2026-09-30'
 assert 0<=p['age_days']<=7 and p['persistence']==p['known']
 assert all(math.isfinite(p[k]) for k in METHODS+['known','actual'])
for fuel,v in r['fuels'].items():
 rr=[p for p in rows if p['fuel']==fuel];assert len(rr)==v['metrics']['n']
 for k in METHODS:assert abs(statistics.mean(abs(p[k]-p['actual']) for p in rr)-v['metrics'][k]['mae'])<1e-12
raw=inputs();t,_=panel(raw);m=macro();jan=enrich(t[t.target<'2026-02-01'],m);before=predict(jan)
raw.loc[raw.date>='2026-02-01','prix']*=3;m.loc[m.available>='2026-02-01',OIL+GEO]*=3
t,_=panel(raw);after=predict(enrich(t[t.target<'2026-02-01'],m))
assert before==after
assert sorted(before,key=lambda p:(p['fuel'],p['date'],p['station']))==sorted([p for p in rows if p['date']<'2026-02-01'],key=lambda p:(p['fuel'],p['date'],p['station']))
print('PASS : empreintes, cinq méthodes appariées, délai macro 14 jours, métriques indépendantes, invariance aux informations futures.')
