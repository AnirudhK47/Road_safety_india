import pandas as pd


df = pd.read_csv(r"G:\repos\Road_Safety\Road_safety_india\Downloads\InjuriesFatalitiesChennai2016to2018.csv")


df = pd.melt(df, id_vars=['City Name'] )


df[['Year','Variable']] = df.variable.str.split("-",n=1,expand=True)


df.drop(['variable'], axis=1)


df[['Accident_type','variable']] = df.Variable.str.split("-",n=1,expand=True)


df.drop(['Variable'], axis=1, inplace=True)


def atp(val):
    if "Injuries" in val:
        return "Injuries"
    else:
        return "Fatalities"


df['Accident_type'] = df['Accident_type'].apply(lambda x: atp(x))


df



