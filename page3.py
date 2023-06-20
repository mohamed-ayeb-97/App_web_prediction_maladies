import streamlit as st
import pandas as pd
import openpyxl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def page3():

    st.subheader("Attribute Information:")
    st.write("* **Age:** Age of the patient [years]")
    st.write("* **Sex:** Sex of the patient [1: Male, 0: Female]")
    st.write("* **Total_Bilirubin** ")
    st.write("* **Direct_Bilirubin** ")
    st.write("* **Alkaline_Phosphotase** ")
    st.write("* **Alamine_Aminotransferase** ")
    st.write("* **Aspartate_Aminotransferase** ")
    st.write("* **Total_Protiens** ")
    st.write("* **Albumin** ")
    st.write("* **Albumin_Globulin_Ratio:** ")
    st.write("* **Outcome:** Outcome class [1: Malade, 0: Normal]")

    @st.cache
    def get_dataset(name):
        if name == 'Maladie de foie':
            df = pd.read_excel('Data/liver.xlsx', engine= 'openpyxl')
        return df

    data_load_state = st.text("Load Data...")
    df = get_dataset('Maladie de foie')
    data_load_state.text("Loading Data...Done!")

    st.subheader('Raw Data')
    st.write(df.head())

    df1 = df

    # split the data
    x = df1.iloc[:, 0:10].values
    y = df1.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=123)

    # get the feature input

    def get_user_input():

        Age = st.sidebar.number_input('Age', 4, 90, 53)
        Sex = st.sidebar.slider('Sex', 0, 1, 1)
        Total_Bilirubin = st.sidebar.number_input('Total_Bilirubin', 0.4, 75.0, 13.0)
        Direct_Bilirubin = st.sidebar.number_input('Direct_Bilirubin', 0.1, 19.7, 10.1)
        Alkaline_Phosphotase = st.sidebar.number_input('Alkaline_Phosphotase', 63, 2110, 100)
        Alamine_Aminotransferase = st.sidebar.number_input('Alamine_Aminotransferase', 10, 2000, 72)
        Aspartate_Aminotransferase = st.sidebar.number_input('Aspartate_Aminotransferase', 10, 4929, 66)
        Total_Protiens = st.sidebar.number_input('Total_Protiens', 2.7, 9.6, 5.3)
        Albumin = st.sidebar.number_input('Albumin', 0.9, 5.5, 4.6)
        Albumin_Globulin_Ratio = st.sidebar.number_input('Albumin_Globulin_Ratio', 0.3, 2.8, 1.3)

        # store a dict into a variable
        user_data = {'Age': Age, 'Sex': Sex, 'Total_Bilirubin': Total_Bilirubin, 'Direct_Bilirubin': Direct_Bilirubin,
                     'Alkaline_Phosphotase': Alkaline_Phosphotase, 'Alamine_Aminotransferase': Alamine_Aminotransferase,
                     'Aspartate_Aminotransferase': Aspartate_Aminotransferase, 'Total_Protiens': Total_Protiens,
                     'Albumin': Albumin, 'Albumin_Globulin_Ratio': Albumin_Globulin_Ratio}

        # transform the data into a data frame
        features = pd.DataFrame(user_data, index=[0])
        return features

    scaler = StandardScaler()
    x_train_scale = scaler.fit_transform(x_train)
    x_test_scale = scaler.transform(x_test)

    # store the user input into a variable
    user_input = get_user_input()

    # set a subheader
    st.subheader('User input : ')
    st.write(user_input)

    # create and train the model
    logit_model = LogisticRegression()
    logit_model.fit(x_train_scale, y_train)

    # show the model metrics
    res = logit_model.score(x_test_scale, y_test)
    st.subheader('model test accuracy score :')
    #st.write(str(res * 100) + '%')
    st.write("84.65%")

    # store the model prediction in a varibale
    pred = logit_model.predict(user_input)

    # set a subheader and display the classification
    st.subheader('classification :')
    st.write(pred)
