"""Vue post-crise des prévisions existantes, sans réentraînement ni réglage."""
import json
from pathlib import Path
from statistics import mean
METHODS = ['persistence', 'momentum', 'station_ai', 'oil_ai', 'context_ai']
START = '2026-02-28'

def metrics(rows):
    stations = sorted({r['station'] for r in rows})
    changed = [r for r in rows if abs(r['actual']-r['known']) > 1e-9]
    sign = lambda x: (x > 0) - (x < 0)
    return dict(n=len(rows), stations=len(stations), **{
        k: dict(mae=mean(abs(r[k]-r['actual']) for r in rows),
                station_weighted_mae=mean(mean(abs(r[k]-r['actual']) for r in rows if r['station']==s) for s in stations),
                direction_accuracy=mean(sign(r[k]-r['known'])==sign(r['actual']-r['known']) for r in changed),
                changed_n=len(changed)) for k in METHODS})

def subset(full):
    rows = [r for r in full['predictions'] if r['origin'] >= START]
    return dict(country='France', period=START+'/2026-09-30',
        selection='Forecast origin on or after 2026-02-28; retrospective subset selected after full-period results were seen; no model tuning.',
        first_target=min(r['date'] for r in rows), last_target=max(r['date'] for r in rows),
        macro_delay_days=full['macro_delay_days'], predictions=rows,
        fuels={f: dict(metrics=metrics([r for r in rows if r['fuel']==f]), quarters={str(q):metrics([r for r in rows if r['fuel']==f and (int(r['date'][5:7])-1)//3+1==q]) for q in [1,2,3]}) for f in full['fuels']})

if __name__ == '__main__':
    root=Path(__file__).resolve().parent
    result=subset(json.loads((root/'results.json').read_text()))
    (root/'crisis-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(f"{len(result['predictions'])} prévisions : {result['first_target']} au {result['last_target']}")
