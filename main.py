import streamlit as st
from scrape import Scrape_website

st.title ("AI Web Scraper")
url = st.text_input("Enter a website URL: ")


if st.button("Scrape site"):
    st.write("Scraping the website")
    result = Scrape_website(url)
    print (result)
