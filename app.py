import os
from openai import OpenAI
import streamlit as st

# Initialize the OpenAI client
# Assuming that the API key is set as an environment variable, you can omit the explicit api_key assignment
client = OpenAI()

# Define the function to generate test cases using the new client instance
def generate_test_cases(requirement):
    response = client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant capable of generating software test cases."},
            {"role": "user", "content": requirement}
        ]
    )
    # Access the response using the updated attribute access method
    return response.choices[0].message.content

# Streamlit app layout
st.title('AI-powered Test Case Generator')
st.write('Enter your software requirement to generate test cases.')

# Text area for user to enter the software requirement
requirement = st.text_area("Requirement", height=150)

# Button to generate test cases
if st.button('Generate Test Cases'):
    if requirement:
        with st.spinner('Generating...'):
            try:
                test_cases = generate_test_cases(requirement)
                st.success('Generated Test Cases')
                st.write(test_cases)
            except Exception as e:
                st.error('An error occurred while generating test cases.')
                st.error(str(e))  # Ensure the exception is converted to string for proper display
    else:
        st.error('Please enter a requirement to generate test cases.')
