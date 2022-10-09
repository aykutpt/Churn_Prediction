#%%
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib
# %%
model = joblib.load("churn5.pkl") 

st.title("Churn Prediction Model")
# %%
ONTRequired = st.selectbox("Please enter ONTRequired", (0,1))
endclientsystem = st.sidebar.selectbox("Please enter endclientsystem", ('endclientsystem_ADX', 'endclientsystem_COA2GO', 'endclientsystem_COFEEANYWHERE', 'endclientsystem_ERDMN', 'endclientsystem_GBCOM', 'endclientsystem_IVAPPECMADX', 'endclientsystem_MAT', 'endclientsystem_NETXADX','endclientsystem_NETXADX','endclientsystem_PRISM','endclientsystem_SSP_OPS','endclientsystem_VZCOM','endclientsystem_VZOT','endclientsystem_WHATSNEXT','endclientsystem_WHATSNEXT','endclientsystem_WKF','endclientsystem_iVAPP-Controller'))
saleschannel = st.sidebar.selectbox("Please enter saleschannel", ('saleschannel_BIG BOX', 'saleschannel_BSBC', 'saleschannel_CSSC', 'saleschannel_CUS CARE MEDIUM BUS', 'saleschannel_D2D CON', 'saleschannel_ENG MGRS', 'saleschannel_EVENTS', 'saleschannel_FSC','saleschannel_INET ACQ BUS','saleschannel_INET ACQ CON','saleschannel_LA CON','saleschannel_ONLINE BUS','saleschannel_ONLINE CON','saleschannel_OTHER BUS','saleschannel_OTHER CON','saleschannel_OTM BUS','saleschannel_OTM CON','saleschannel_RED VENTURES','saleschannel_SBS'))
BUNDLE = st.sidebar.selectbox("Please enter bundle", ('D', 'TDV', 'DV', 'TD', 'V', 'T', 'DT', 'TV'))
smartcart = st.selectbox("Please enter smartcart", (0,1))
ContractType=st.selectbox("Contract type (MONTHTOMONTH:0, CONTRACT:1)", (0,1))
waitingdayofcustomers = st.slider("Please enter waitingdayofcustomers(day)",1, 60)
# %%
df = pd.DataFrame([{"ContractType":ContractType,"waitingdayofcustomers":waitingdayofcustomers, "ONTRequired":ONTRequired, "smartcart":smartcart,"endclientsystem":endclientsystem,"saleschannel":saleschannel, "BUNDLE":BUNDLE}])

columns = ["ContractType","waitingdayofcustomers","ONTRequired","smartcart",'endclientsystem_ADX', 'endclientsystem_COA2GO', 'endclientsystem_COFEEANYWHERE', 'endclientsystem_ERDMN', 'endclientsystem_GBCOM', 'endclientsystem_IVAPPECMADX', 'endclientsystem_MAT', 'endclientsystem_NETXADX','endclientsystem_NETXADX','endclientsystem_PRISM','endclientsystem_SSP_OPS','endclientsystem_VZCOM','endclientsystem_VZOT','endclientsystem_WHATSNEXT','endclientsystem_WHATSNEXT','endclientsystem_WKF','endclientsystem_iVAPP-Controller','saleschannel_BIG BOX', 'saleschannel_BSBC', 'saleschannel_CSSC', 'saleschannel_CUS CARE MEDIUM BUS', 'saleschannel_D2D CON', 'saleschannel_ENG MGRS', 'saleschannel_EVENTS', 'saleschannel_FSC','saleschannel_INET ACQ BUS','saleschannel_INET ACQ CON','saleschannel_LA CON','saleschannel_ONLINE BUS','saleschannel_ONLINE CON','saleschannel_OTHER BUS','saleschannel_OTHER CON','saleschannel_OTM BUS','saleschannel_OTM CON','saleschannel_RED VENTURES','saleschannel_SBS',"BUNDLE_D","BUNDLE_DT","BUNDLE_DV","BUNDLE_T","BUNDLE_TD","BUNDLE_TDV","BUNDLE_TV","BUNDLE_V"]

df2 = pd.get_dummies(df).reindex(columns=columns,fill_value=0)


#%%
prediction = model.predict(df2)

if prediction == 1:

       st.warning("Yes, the customer will terminate the service")

else :
       st.success("No, the customer is happy from the Services.")
# %%
df

# %%
