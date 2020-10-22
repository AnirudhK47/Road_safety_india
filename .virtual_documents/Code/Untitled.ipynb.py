import pandas as pd


df = pd.read_csv(r"G:\repos\Road_Safety\Road_safety_india\Downloads\InjuriesFatalitiesChennai2016to2018.csv")


df.head()


df = pd.melt(df, id_vars=['City Name'] )


df.rename(columns={"City Name":"City"})


df[['Year','Variable']] = df.variable.str.split("-",n=1,expand=True)


df.drop(['variable'], axis=1)



