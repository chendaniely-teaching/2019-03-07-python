import pandas as pd

billboard = pd.read_csv('billboard_tidy.csv')

print(billboard.head())

print(billboard
	.groupby('week')
	['rank']
	.mean()
)
