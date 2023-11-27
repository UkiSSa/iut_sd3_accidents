import pandas as pd

# Charger les fichiers CSV dans des DataFrames
carac_df = pd.read_csv('carac.csv', encoding='latin1')
lieux_df = pd.read_csv('lieux.csv', encoding='latin1')
veh_df = pd.read_csv('veh.csv', encoding='latin1')
vict_df = pd.read_csv('vict.csv', encoding='latin1')

# Fusionner les DataFrames en utilisant les colonnes appropriées
merged_df = pd.merge(carac_df, lieux_df, on='Num_Acc', how='inner')
merged_df = pd.merge(merged_df, veh_df, on='Num_Acc', how='inner')
merged_df = pd.merge(merged_df, vict_df, on='Num_Acc', how='inner')

# Enregistrez le DataFrame fusionné dans un nouveau fichier CSV
merged_df.to_csv('merged_data.csv', index=False, encoding='utf-8')

print("Fusion terminée. Le fichier merged_data.csv a été créé.")

