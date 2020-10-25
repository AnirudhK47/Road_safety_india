import pandas as pd


df = pd.read_csv(r"G:\repos\Road_Safety\Road_safety_india\Downloads\bangalore-cas-alerts.csv")


df.shape


df.drop_duplicates(inplace=True)
df.shape


df.columns = ['Device_code','Latitude', 'Longitude', 'Ward_name', 'Alarm_type', 'Speed', 'Time&Date'  ]
df.columns


df.replace({'PCW':'Pedestrian/Cycle',
            'FCW':'High Speed Collision',
            'HMW':'High Speed Collision',
            'UFCW':'Low Speed Collision',
            'LDWL':'Lane Departure',
            'LDWR':'Lane Departure',},inplace = True)


#df['Alarm_type'].head(10)
df.Alarm_type.unique()


df = df[['Device_code', 'Alarm_type', 'Speed', 'Ward_name','Latitude','Longitude','Time&Date']]
df.head(10)


df.to_csv("Bangalore accident zones - Intel Mobileye.csv")



