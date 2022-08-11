![Header](./header.png)

# Space Titanic Streamlit
Predict if you will be transported to a different dimension or not during your space trip

## Tech Stack
![Visual Studio Code Badge](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=plastic)
![Google Colab Badge](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=fff&style=plastic)
![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=plastic)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic)

## Dataset
**Source:**
![Kaggle Badge](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=fff&style=flat): https://www.kaggle.com/competitions/spaceship-titanic

**Columns Description**

- PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp where gggg indicates a group the passenger is travelling with and pp is their number within the group. People in a group are often family members, but not always.
- HomePlanet - The planet the passenger departed from, typically their planet of permanent residence.
- CryoSleep - Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.
- Cabin - The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for Port or S for Starboard.
- Destination - The planet the passenger will be debarking to.
- Age - The age of the passenger.
- VIP - Whether the passenger has paid for special VIP service during the voyage.
- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.
- Name - The first and last names of the passenger.
- Transported - Whether the passenger was transported to another dimension.

## Model
**CatBoost**

```python
model=CatBoostClassifier(iterations=1500,eval_metric='Accuracy',verbose=0)
```

```python
model.fit(X_train,y_train)
```

**Train Accuracy:** 0.88

**Validation Accuracy:** 0.81

---
## 💰You can help me by becoming a sponsor on GitHub
[![GitHub Sponsor](https://img.shields.io/badge/GitHub%20Sponsors-EA4AAA?logo=githubsponsors&logoColor=fff&style=square)](https://github.com/sponsors/pangineering) 

## 💰You can help me by Donating
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https:buymeacoffee.com/pangineering)  
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/pangineering)  
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/pangineering) 
