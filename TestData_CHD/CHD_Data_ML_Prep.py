import pandas as pd
import numpy as np

df = pd.read_csv('CHOP_features_1104.txt', delim_whitespace=True)
df.shape
df.insert(1, "InstanceID", [i for i in range(len(df))])

result = df.isna().sum().sum()
print(result)

cells = 810*184527
naPerc = result/float(cells)
print(naPerc)

df2 = df.fillna(-1)
df2 = df2.astype(int)

df2.loc[:, "PHENOTYPE"] = df2["PHENOTYPE"].apply(lambda x: x - 1)

df2 = df2.astype(str)
df2 = df2.replace('-1', np.nan)

df2.rename(columns={"PHENOTYPE": "Class"}, inplace=True)

significance = pd.read_csv("Significance_CHD_underThreshold.csv")
features = significance['InstanceID'].to_numpy()
features = features + 2

df3 = df2.iloc[:,features]
df3.insert(0,'Class',df2['Class'])
df3.insert(1,'InstanceID',df2['InstanceID'])

df3.to_csv('CHOP_features_1104_CHD_underThreshold.txt', sep='\t', index=False)



