import pickle
import pandas as pd
import numpy as np


# filename = "/home/aloka/Documents/Bill reading/Server/uploadSolarApp/models/final_model.pkl"
filename ="uploadSolarApp/models/final_model.pkl"
loaded_model=pickle.load(open(filename, 'rb'))
def PreProcess(df):     
    ################## 'wind speed' ########################
    df['wind speed'] = df['wind speed'].str.split('(', n = 1, expand = True)[0].astype(np.float64)
    
     ################## 'humidity' ########################
    df['humidity'] = df['humidity'].str.split('%', n = 1, expand = True)[0].astype(np.int64)
    
     ################## 'Temperature' ########################
    df['Temperature'] = df['Temperature'].str.split('c', n = 1, expand = True)[0].astype(np.int64)
    
     ################## 'elevation' ########################
    df['elevation'] = df['elevation'].str.split('m', n = 1, expand = True)[0].astype(np.int64)
    
     ################## 'radiation' ########################
    df['radiation'] = df['radiation'].str.split('k', n = 1, expand = True)[0].astype(np.float64)
    
     ################## 'Vapor Pressure' ########################
    df['Vapor Pressure'] = df['Vapor Pressure'].str.split('k', n = 1, expand = True)[0].astype(np.float64)
    
     ################## 'Surface Temperature' ########################
    df['Surface Temperature'] = df['Surface Temperature'].str.split('c', n = 1, expand = True)[0].astype(np.int64)
    
     ################## 'Atmosphere Pressure' ########################
    df['Atmosphere Pressure'] = df['Atmosphere Pressure'].str.split(' ', n = 1, expand = True)[0].astype(np.int64)
    
     ################## 'usage' ########################
    df['usage'] = df['usage'].str.split('k', n = 1, expand = True)[0].astype(np.float64)
    
    return df

def main(list_row):
  data=pd.read_csv('uploadSolarApp/models/Dataset_New.csv')
  data.loc[len(data)] = list_row
  data_new = PreProcess(data)
  data_new = data_new[['Province','rain fall type','sky type','wind direction','wind speed','humidity','Temperature','elevation','radiation','Vapor Pressure','Surface Temperature','Atmosphere Pressure','Bulbs','Fan','Iron','TV','Refrigerator','Blender','Air conditioner','Water Heater','Microwave Oven','Rice Cooker','usage']]
  x=data_new.iloc[:,:22]
  x = x.astype({"Province":'category',"rain fall type":'category',"sky type":'category',"wind direction":'category',"Bulbs":'category',"Fan":'category',"Iron":'category',"TV":'category',"Refrigerator":'category',"Blender":'category',"Air conditioner":'category',"Water Heater":'category',"Microwave Oven":'category',"Rice Cooker":'category'})
  x = pd.get_dummies(x,columns = ['Province', 'rain fall type', 'sky type','wind direction','Bulbs','Fan','Iron','TV','Refrigerator','Blender','Air conditioner','Water Heater','Microwave Oven','Rice Cooker'],
                    prefix=['Province', 'rain fall type', 'sky type','wind direction','Bulbs','Fan','Iron','TV','Refrigerator','Blender','Air conditioner','Water Heater','Microwave Oven','Rice Cooker'])
  return(loaded_model.predict(x.iloc[-1:]))

# main(list_row= ['Anuradhapura','0kWh','Rain','Little Cloudy','South West','8(m/s)','54%','27c','81m','3.94kWh/m2','3.4958935011kPa','28c','1008 mb','Yes','Yes','Yes','Yes','Yes','No','Yes','No','No','No']
# )