# Import Libraries
import streamlit
import pandas as pd

# Title
streamlit.title('My Parents New Healthy Dinner')

# BreakFast Information - START
# BreakFast Header
streamlit.header('BreakFast Favorites')

# Simple Text
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')
# BreakFast Information - END

# Your Own Fruit Header
streamlit.header('Build Your Own Fruit Smoothie')

# Load CSV Data Into Variable
my_fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Let's put list here so they can pick the fruits they want to include
streamlit.multiselect("Pick Some Fruits : ", list(my_fruits_list.index))

# Choose the fruits name column as the Index
my_fruits_list = my_fruits_list.set_index('Fruits')

# Data
streamlit.dataframe(my_fruits_list)
