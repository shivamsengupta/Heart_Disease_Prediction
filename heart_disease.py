import streamlit as st
import joblib
import pickle
import numpy as np
import pandas as pd

def loadModel():
    model=joblib.load('model_joblib_heart.joblib')
    return model

def main():
    st.set_page_config(page_title="Heart Disease Prediction",page_icon="❤")
    
    model=loadModel()
    st.title("Heart Disease Prediction")

    
    age = st.number_input('Enter your age in Years',min_value=0,max_value=100)
    sex= st.selectbox('Sex',('Female','Male'))
    cp=st.selectbox('Chest Pain Type',('Typical Angina','Atypical Angina','Non-Anginal','Asymptomatic'))
    trestbps=st.number_input('Resting Blood Pressure in mmHg (Higher value only)',min_value=0,max_value=200)
    chol=st.number_input('Serum Cholestrol in mg/dL',min_value=0,max_value=600)
    fbs=st.selectbox('Fasting Blood Sugar',('Less than 120 mg/dL','Greater than 120 mg/dL'))
    restecg=st.selectbox('Resting ECG Result',('Normal','Abnormal','Significantly Abnormal'))
    thalach=st.number_input('Maximum Heart Rate Received',min_value=0,max_value=220)
    exang=st.selectbox('Exercise Induced Angina',('No','Yes'))
    oldpeak=st.number_input('ST depression induced by Exercise',min_value=0.0,max_value=10.0)
    slope=st.number_input('Slope of the peak exercise ST Segment',min_value=0.0,max_value=2.0)
    ca=st.selectbox('Number of Major Vessels colored by Flouroscopy',(0,1,2,3))
    thal=st.selectbox('Thalassemia',('Normal','Fixed Defect','Reversible Defect'))

    Analysis_Result='No Results Found !!!'

    if(sex and cp and trestbps and chol and fbs and restecg  and thal):
        if(age==0):
            st.warning("Age can't be 0")
        elif(thalach==0):
            st.warning("Heart Beat can't be 0 !")
        else:
            if (sex=='Female'):
                sex1=0
            else:
                sex1=1
    
            if(cp=='Typical Angina'):
                cp1=0
            elif(cp=='Atypical Angina'):
                cp1=1
            elif(cp=='Non-Anginal'):
                cp1=2
            else:
                cp1=3

            if(fbs=='Less than 120 mg/dL'):
                fbs1=0
            else:
                fbs1=1
    
            if(restecg=='Normal'):
                restecg1=0
            elif(restecg=='Abnormal'):
                restecg1=1
            else:
                restecg1=2
    
            if(exang=='No'):
                exang1=0
            else:
                exang1=1
    
            if(thal=='Normal'):
                thal1=0
            elif(thal=='Fixed Defect'):
                thal1=1
            else:
                thal1=2
    

            new_data=pd.DataFrame({
            'age':age,
            'sex':sex1,
            'cp':cp1,
            'trestbps':trestbps,
            'chol':chol,
            'fbs':fbs1,
            'restecg':restecg1,
            'thalach':thalach,
            'exang':exang1,
            'oldpeak':oldpeak,
            'slope':slope,
            'ca':int(ca),
            'thal':thal1
            },index=[0])    
    
            result=model.predict(new_data)
            if(result[0]==0):
                Analysis_Result='You are Safe ❣'
            else:
                Analysis_Result='Heart Patient Detected 💔'

        
    else:
        Analysis_Result="Please Fill-Up all the values to get the prediction !"
        
    if st.button('Predict'):
            st.write(Analysis_Result)


if __name__=="__main__":
    main()