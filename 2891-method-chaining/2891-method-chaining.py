import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered = animals[animals['weight']>100]
    filtered = filtered.sort_values(by='weight',ascending=False)
    return filtered[['name']]
    