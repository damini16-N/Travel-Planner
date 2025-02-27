#logic1
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    messages=[
    ("""system", "You are an AI-powered travel planner that provides the best travel options 
                  including cab, train, bus, and flights along with estimated costs."""), 
    ("human", "Suggest the best travel options from {source} to {destination}, including estimated prices.")
    ],
    
)


#logic 2
#Import Google ChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
f = open('keys/.gemini.txt')
GOOGLE_API_KEY=f.read()


#Set the OpenAI Key and initialize a ChatModel
chat_model = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model = "gemini-2.0-flash-exp")

#logic 3
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

chain = chat_template | chat_model | parser



import streamlit as st
# Streamlit UI Setup
st.title("AI-Powered Travel Planner")
st.markdown("Find the best travel options between your source and destination!")

# User Input for Travel Planning
source = st.text_input("Enter your Source")
destination = st.text_input("Enter your Destination")

if st.button("Get Travel Options"):
    if source and destination:
        st.write("Fetching travel recommendations...")

        # Invoke the model
        recommendations = chain.invoke({"source": source, "destination": destination})

        #Get the response
        st.write("Recommended Travel Options:")
        st.write(str(recommendations))  

    else:
        st.warning("Please enter both **source** and **destination**.")