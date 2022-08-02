# Import Libraries
import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

# Choose the fruits name column as the Index
my_fruits_list = my_fruits_list.set_index('Fruit')

# Let's put list here so they can pick the fruits they want to include
fruits_selected = streamlit.multiselect("Pick Some Fruits : ", list(my_fruits_list.index), ['Avocado', 'Strawberries'])

# Filter The Table Data
fruits_to_show = my_fruits_list.loc[fruits_selected]

# Data
streamlit.dataframe(fruits_to_show)

# Create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  # Fruityvice Response
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

  # Returns normalized data with columns prefixed with the given string.
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  
  return fruityvice_normalized

# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function) 

except URLError as e:
  streamlit.error()
  # Don't run anything past here while we troubleshoot




# Don't run anything past here while we troubleshoot
#streamlit.stop()

# Header
streamlit.header("The fruit load list contains:")
# Snowflake Related Function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM fruit_load_list")
    return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

# New section to display fruityvice api response
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

#fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
#streamlit.write('Thanks for adding ', fruit_choice)

# This will not work correctly, but just go with it for now
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
