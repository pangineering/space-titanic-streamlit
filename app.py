# Import Libraries
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Streamli
import streamlit as st


# Sklearn

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder

# Models

from catboost import CatBoostClassifier


# load model
from_file = CatBoostClassifier()

model = from_file.load_model("model/model")

st.title('Space Titatic')

st.text('Predict if you will be transported to a different dimension or not during your space trip')

passengerId = st.text_input('Your Passenger Id')
st.write('Your Passenger Id: ', passengerId)

name = st.text_input('Your Name', '')
st.write('Your name: ', name)

age = st.slider('Your Age', 0.0, 130.0, 25.0)
st.write("Your Age ", age, 'years old')

home_planet = st.selectbox(
     'home planet',
     ('Europa', 'Earth', 'Mars'))

st.write('Your home_planet: ', home_planet)

destination = st.selectbox(
     'destination',
     ('TRAPPIST-1e', 'PSO J318.5-22', '55 Cancri e'))

st.write('Your destination: ', destination)

cabin = st.selectbox(
     'cabin',
     ('B/0/P', 'F/0/S', 'A/0/S', 'G/1499/S', 'G/1500/S', 'E/608/S'))
st.write('Your cabin: ', cabin)


vip = st.checkbox('Yes',key=1)
st.write('vip: ',vip)

CryoSleep = st.checkbox('Yes',key=2)
st.write('CryoSleep: ',CryoSleep)

st.write('How much do you spend?')

roomService = st.slider('Your spending on room services', 0.0, 1000.0, 25.0)
st.write('Room Service: ', roomService)

FoodCourt = st.slider('Your spending in food court', 0.0, 1000.0, 25.0)

st.write('Food Court: ', FoodCourt)

ShoppingMall = st.slider('Your spending on shopping', 0.0, 1000.0, 25.0)

st.write('Shopping Mall: ', ShoppingMall)

Spa = st.slider('Your spending on spa', 0.0, 1000.0, 25.0)

st.write('Spa: ', Spa)

VRDeck = st.slider('Your spending on VR Deck', 0.0, 1000.0, 25.0)

st.write('VRDeck: ', VRDeck)






if st.button('Submit'):
     #Input -> Dict
     data = [{
     "passengerId": passengerId,
     "name": name,
     
     "HomePlanet": home_planet,
     "CryoSleep": CryoSleep,
     "Destination": destination,
     "cabin": cabin,
     "Age": age,
     "VIP": vip,
     
     "RoomService": float(roomService),
     "FoodCourt": float(FoodCourt),
     "ShoppingMall": float(ShoppingMall),
     "Spa": float(Spa),
     "VRDeck": float(VRDeck) 
     }]
     print(data)
     df = pd.DataFrame(data=data)


     st.dataframe(df)

     df_user = df
     df_user[['Deck','Num','Side']] = df_user.cabin.str.split('/',expand=True)
     df_user['AgeGroup'] = 0
     for i in range(6):
          df_user.loc[(df_user.Age >= 10*i) & (df_user.Age < 10*(i + 1)), 'AgeGroup'] = i

     categorical_cols= ['HomePlanet','CryoSleep','Destination','VIP','Deck','Side','Num']
     for i in categorical_cols:
          le =LabelEncoder()
          arr = (df_user[i]).astype(str)
          le.fit(arr)
          df_user[i]=le.transform(df_user[i].astype(str))

     df_user['total_spent']=df_user['RoomService']+df_user['FoodCourt']+df_user['ShoppingMall']+df_user['Spa']+df_user['VRDeck']
     df_user = df_user.drop(['name','cabin','passengerId'],axis=1)
  


     pred=model.predict(df_user)
     result = pd.DataFrame({'passenger_id': passengerId,'Transported':pred.astype(bool)},index=df_user.index)
     st.dataframe(result)