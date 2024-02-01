import streamlit
import pandas
  

streamlit.title('My Parents New healthy Diner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('Breakfast Menu')
streamlit.text('🐔 Omega 3 & Blueberry oatmeal')
streamlit.text('🥑 Kale, Spinach & Rocket Smothie')
streamlit.text('🍞 Hard-Boiled Free-Range Eggs')
streamlit.text('🥣 🥗 Avocado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
