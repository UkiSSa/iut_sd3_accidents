import pandas as pd

one_hot_encoding = pd.read_csv("step4/gps_encoding.csv", sep=",", low_memory=False)

y = one_hot_encoding['grav']

features = ['catu','sexe','trajet','secu',
            'catv','an_nais','mois',
            'occutc','obs','obsm','choc','manv',
            'lum','agg','int','atm','col','gps',
            'catr','circ','vosp','prof','plan',
            'surf','infra','situ','hrmn','geo']

one_hot_encoding = pd.get_dummies(one_hot_encoding[features].astype(str))

one_hot_encoding.to_csv("step5/one_hot_encoding.csv", index=False)