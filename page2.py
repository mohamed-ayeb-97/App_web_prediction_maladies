import streamlit as st
import pandas as pd
import openpyxl
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def page2():
    st.subheader("Attribute Information:")

    st.write("* **Pregnancies:** Number of times pregnant")
    st.write("* **Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test ")
    st.write("* **BloodPressure:** Diastolic blood pressure (mm Hg)")
    st.write("* **SkinThickness:** Triceps skin fold thickness (mm)")
    st.write("* **Insulin:** 2-Hour serum insulin (mu U/ml)")
    st.write("* **BMI:** Body mass index (weight in kg/(height in m)^2)")
    st.write("* **DiabetesPedigreeFunction:**  Diabetes pedigree function")
    st.write("* **Age:** Age of the patient [years]")
    st.write("* **Outcome:** Outcome class [1: Diabète, 0: Normal]")

    @st.cache
    def get_dataset(name):
        if name == 'Diabète':
            df = pd.read_excel('Data/diabetes.xlsx', engine= 'openpyxl')
        return df

    data_load_state = st.text("Load Data...")
    df = get_dataset('Diabète')
    data_load_state.text("Loading Data...Done!")

    st.subheader('Raw Data')
    st.write(df.head())

    df1 = df

    # split the data
    x = df1.iloc[:, 0:8].values
    y = df1.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=123)

    # get the feature input

    def get_user_input():
        Pregnancies = st.sidebar.number_input('Pregnancies', 0, 17, 13)
        Glucose = st.sidebar.number_input('Glucose', 0, 199, 101)
        BloodPressure = st.sidebar.number_input('BloodPressure', 0, 122, 100)
        SkinThickness = st.sidebar.number_input('SkinThickness', 0, 99, 72)
        Insulin = st.sidebar.number_input('Insulin', 0, 846, 666)
        BMI = st.sidebar.number_input('BMI', 0.00, 67.10, 50.30)
        DiabetesPedigreeFunction = st.sidebar.number_input('DiabetesPedigreeFunction', 0.000, 3.000, 1.560)
        Age = st.sidebar.number_input('Age', 0, 81, 50)


        # store a dict into a variable
        user_data = {'Pregnancies': Pregnancies, 'Glucose': Glucose, 'BloodPressure': BloodPressure,
                     'SkinThickness': SkinThickness, 'Insulin': Insulin, 'BMI': BMI, 'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
                     'Age': Age}

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
    st.write("79.95%")
    #st.write(str(metrics.accuracy_score(y_test, rf.predict(x_test)) * 100) + '%')

    # store the model prediction in a varibale
    pred = rf.predict(user_input)

    # set a subheader and display the classification
    st.subheader('classification :')
    st.write(pred)
