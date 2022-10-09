import pickle
import pandas as pd

filename = "uploadTipsApp/models/final_model.pkl"
loaded_model=pickle.load(open(filename, 'rb'))

def main(d):
    df = pd.DataFrame(d)
    loaded_model=pickle.load(open(filename, 'rb'))
    y_pred=loaded_model.predict(df)
    tips =""
    if 500 < y_pred <= 1000:
        tips = "A"
    elif 1000 < y_pred <= 2000:
        tips = "B"
    elif 2000 < y_pred <= 3000:
        tips = "C"
    elif 3000 < y_pred <= 4000:
        tips = "D"
    elif 4000 < y_pred <= 5000:
        tips = "E"  

    return tips,y_pred

# print(main([{
#   "noOfMembers": 4,
#   "noOofTimesUsingTheIron(1week)": 7,
#   "noOfTimesUsingTheWashingMachine(1 week)": 5,
#   "1monthUnits": 140,
#   "2monthUnits": 142,
#   "3monthUnits": 202,
#   "1monthCost": 3000.0,
#   "2monthCost": 3085.7,
#   "3monthCost": 4409.3,
#   "averageUnits" : 161.33,
#   "microwave_Yes": 0,
#   "hairDryer_Yes": 0,
#   "electricOven_Yes": 0,
#   "windowType_Yes": 0,
#   "waterGeyser_Yes": 0,
#   "electricWaterHeater_Yes": 0,
#   "cielingFan_Yes": 0,
#   "standFan_Yes" : 0,
#   "tableFan_Yes" : 0,
#   "exhaustFan_Yes": 0
# }]))