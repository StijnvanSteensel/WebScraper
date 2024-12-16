import streamlit as st
from scrape import (
    Scrape_website, 
    split_dom_content, 
    clean_dom_content, 
    extract_body_content,
)

st.title ("AI Web Scraper")
url = st.text_input("Enter a website URL: ")


if st.button("Scrape site"):
    st.write("Scraping the website")
    result = Scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_dom_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM Content", cleaned_content, height=300)