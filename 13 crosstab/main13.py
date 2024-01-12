import pandas as pd

df = pd.read_excel('13 crosstab/survey.xls'); df
#crosstab # of repetition
pd.crosstab(df.Sex, df.Handedness)
pd.crosstab(df.Sex, df.Handedness, margins=True)
pd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins=True)
round(pd.crosstab(df.Sex, [df.Handedness, df.Nationality], normalize='index'),2)
pd.crosstab([df.Nationality, df.Sex], df.Handedness)
import numpy as np
pd.crosstab([df.Nationality],[df.Sex], values=df.Age, aggfunc=np.average)