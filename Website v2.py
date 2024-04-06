import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json
import smtplib


st.set_page_config(page_title="Lets Grow Together", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()



lottie_coding = ("https://lottie.host/e5c04562-56b2-46ff-8a85-eb9309183bd4/Q12AI3wM0Y.json")





st.subheader("Hi, We are so exicted you are here :wave:")

st.title("Let Us Make The Calls :telephone:")

st.write("Our team makes hundreds of cold calls per day. We strive to provide as many new leads for your businesses as possible. Simply provide the zip code in which you are trying to grow and we will take it from there. When you grow, we grow. So lets grow together.")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Do")
        st.write("We resarch the zip code in which you provide, and identify a list of businesses that potentially benefit from your products or services. Once we have this list established we send this list to you for approval. After you approve the list, we start calling and advertising your business.")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("Select Your Calling Package")
    st.write("Which ever package you decide is best for you, scroll to the bottom and send us an email. We are excited to work with you!")
    image_column, text_column = st.columns((1, 2))

    with text_column:

        st.subheader("The New Business Package")
        st.write("For this package we will generate 25 businesses for you to approve based on your submitted zip code. Once you approve of the locations we will start calling. This package costs $25.00")
        st.subheader("The Growing Business Package")
        st.write("For this package we will generate 50 businesses for you to approve based on your submitted zip code. Once you approve of the locations we will start calling. This package costs $45.00")
        st.subheader("The Big Business Package")
        st.write("For this package we will generate 100 businesses for you to approve based on your submitted zip code. Once you approve of the locations we will start calling. This package costs $90.00")

with st.container():
    st.write("---")
    st.header(":star: Testimonials :star:")
    st.write(":thumbsup: I selected the new business package and they called 25 businesses in my area, which generated me three new leads. Best 25 dollars I ever spent")
    st.write(":thumbsup: I was skeptical, but I hate making cold calls. So I tried the the new business package and they which generated me two new leads from the 25 businesses I approved. well worth the money")
    st.write(":thumbsup: I reached out and asked if they would call 500 businesses for me. Sure enough we agreed on the price and I made my money back from that investment within a week")
    st.write(":thumbsup: I tried other people on fiver to cold call, and they were terrible. This team was kind and patient with me and generated new leads")
    st.write(":thumbsup: Honestly just spend the 90 dollars get the list of 100 businesses and have them cold call. Even one lead makes your money back fast")
    st.write(":thumbsup: within a week I had a list of businesses, have used this service three different times. Will keep using them")
    st.write(":thumbsup: Repeat user, have them generate 100 businesses, then expand and come back for me. Growth is through word of mouth")
    st.write(":thumbsup: I hate cold calling but am passionate about my business. Will use again")
    st.write(":thumbsup: paid for the 25 dollar package and was provided 25 businesses, I didn't get any new leads from there. so I expanded the distance on my location and paid for the 50 businesses. Sure enough four new leads. Great investment")


import streamlit as st
with st.container():
    st.write("---")
def main():
    st.title(":e-mail: Get In Touch With Us")
    st.markdown("Just send me an email with the package you are interested in at [leadgenerator_1@aol.com](mailto:leadgenerator_1@aol.com)")

if __name__ == "__main__":
    main()





