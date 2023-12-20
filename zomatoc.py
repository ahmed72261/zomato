import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("model", "rb"))

# Function to make predictions
def predict_success(df):
    value_predict = model.predict(df)[0]
    if value_predict == 1:
        return "This restaurant will be successful"
    else:
        return "This restaurant will not be successful"

# Streamlit app
def main():
    st.title("Restaurant Success Prediction")

    # Input form
    st.subheader("Enter Restaurant Details:")
    online_order = st.radio("Online Order?", ["Yes", "No"])
    book_table = st.radio("Book Table?", ["Yes", "No"])
    phone = st.radio("Phone?", ["have phone", "not have phone"])
    location = st.text_input("Location", "")
    rest_type = st.text_input("Rest Type", "")
    cuisines = st.text_input("Cuisines", "")
    cost_for_two = st.number_input("Approx Cost (for two people)", min_value=0.0, max_value=10000.0, step=100.0)
    menu_item = st.radio("Menu Item?", ["have menu", "not have menu"])

    # Unique values for listed_in_type and listed_in_city
    unique_cities = ['Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur', 'Brigade Road', 'Brookefield', 'BTM', 'Church Street', 'Electronic City', 'Frazer Town', 'HSR', 'Indiranagar', 'Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli', 'Koramangala 4th Block', 'Koramangala 5th Block', 'Koramangala 6th Block', 'Koramangala 7th Block', 'Lavelle Road', 'Malleshwaram', 'Marathahalli', 'MG Road', 'New BEL Road', 'Old Airport Road', 'Rajajinagar', 'Residency Road', 'Sarjapur Road', 'Whitefield']
    unique_types = ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out', 'Drinks & nightlife', 'Pubs and bars']

    # Options for selectbox
    listed_in_type = st.selectbox("Listed In Type", unique_types)
    listed_in_city = st.selectbox("Listed In City", unique_cities)

    # Create a DataFrame with user input
    user_data = {
        "online_order": online_order,
        "book_table": book_table,
        "phone": phone,
        "location": location,
        "rest_type": rest_type,
        "cuisines": cuisines,
        "approx_cost(for two people)": cost_for_two,
        "menu_item": menu_item,
        "listed_in(type)": listed_in_type,
        "listed_in(city)": listed_in_city,
    }

    df_test = pd.DataFrame(user_data, index=[0])

    # Predict button
    if st.button("Predict"):
        prediction_result = predict_success(df_test)
        st.subheader("Prediction Result:")
        st.write(prediction_result)

if __name__ == "__main__":
    main()
