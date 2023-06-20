import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
import openpyxl


def page1():
    st.subheader("Attribute Information:")
    st.write("* **Age:** Age of the patient [years]")
    st.write("* **Sex:** Sex of the patient [1: Male, 0: Female]")
    st.write(
        "* **ChestPainType:** Chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, "
        "ASY: "
        "Asymptomatic]")
    st.write("* **RestingBP:** Resting blood pressure [mm Hg]")
    st.write("* **Cholesterol:** Serum cholesterol [mm/dl]")
    st.write("* **FastingBS:** Fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]")
    st.write(
        "* **RestingECG:** Resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality "
        "(T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite "
        "left ventricular hypertrophy by Estes criteria]")
    st.write("* **MaxHR:** Maximum heart rate achieved [between 60 and 202]")
    st.write("* **Exercise:** Exercise-induced angina [1: Yes, 0: No]")
    st.write("* **Oldpeak:**  ST [Numeric value measured in depression]")
    st.write(
        "* **ST_Slope:** The slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]")
    st.write("* **Output:** Output class [1: heart disease, 0: Normal]")

    @st.cache(allow_output_mutation=True)
    def get_dataset(name):
        if name == 'Défaillance Cardiaque':
            df = pd.read_excel('Data/heart.xlsx', engine= 'openpyxl')
        return df

    st.subheader('Raw Data')
    data_load_state = st.text("Load Data...")
    df = get_dataset('Défaillance Cardiaque')
    data_load_state.text("Loading Data...Done!")
    st.write(df.head())

    df1 = df

    # Data processing:
    encoder = LabelEncoder()

    df1['ChestPainType'] = encoder.fit_transform(df1['ChestPainType'])
    ChestPainType = {index: label for index, label in enumerate(encoder.classes_)}

    df1['RestingECG'] = encoder.fit_transform(df1['RestingECG'])
    RestingECG = {index: label for index, label in enumerate(encoder.classes_)}

    df1['ST_Slope'] = encoder.fit_transform(df1['ST_Slope'])
    ST_Slope = {index: label for index, label in enumerate(encoder.classes_)}

    # split the data
    x = df1.iloc[:, 0:11].values
    y = df1.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=123)


    # get the feature input

    def get_user_input():
        Age = st.sidebar.number_input('Age', 28, 77, 53)
        Sex = st.sidebar.slider('Sex', 0, 1, 1)
        ChestPainType = st.sidebar.slider('ChestPainType', 0, 3, 1)
        RestingBP = st.sidebar.number_input('RestingBP', 0, 200, 150)
        Cholesterol = st.sidebar.number_input('Cholesterol', 0, 603, 223)
        FastingBS = st.sidebar.slider('FastingBS', 0, 1, 0)
        RestingECG = st.sidebar.slider('RestingECG',0,2,1)
        MaxHR = st.sidebar.number_input('MaxHR', 60, 202, 138)
        Exercise = st.sidebar.slider('Exercise', 0, 1, 1)
        Oldpeak = st.sidebar.number_input('Oldpeak', -2.6, 6.2, 0.6)
        ST_Slope = st.sidebar.slider('ST_Slope',0,2,1)

        # store a dict into a variable
        user_data = {'Age': Age, 'Sex': Sex, 'ChestPainType': ChestPainType, 'RestingBP': RestingBP, 'Cholesterol': Cholesterol,
                     'FastingBS': FastingBS, 'RestingECG': RestingECG, 'MaxHR': MaxHR, 'Exercise': Exercise,
                     'Oldpeak': Oldpeak, 'ST_Slope': ST_Slope}

        # transform the data into a data frame
        features = pd.DataFrame(user_data, index=[0])
        return features

    rf = RandomForestClassifier(n_estimators=5000, max_depth=5, random_state=33)

    # store the user input into a variable
    user_input = get_user_input()

    # set a subheader
    st.subheader('User input : ')
    st.write(user_input)

    # create and train the model
    rf.fit(x_train, y_train)

    # show the model metrics
    st.subheader('model test accuracy score :')
    st.write(str(metrics.accuracy_score(y_test, rf.predict(x_test)) * 100) + '%')
    #st.write("95.65%")

    # store the model prediction in a varibale
    pred = rf.predict(user_input)

    # set a subheader and display the classification
    st.subheader('classification :')
    st.write(pred)
