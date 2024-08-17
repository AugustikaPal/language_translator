import requests
import streamlit as st
import base64

def get_groq_response(input_text, target_language):
    json_body = {
        "input": {
            "language": target_language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
    result = response.json()
    
    return result.get("output", "No output returned")

def download_link(text, filename="translation.txt"):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download text file</a>'
    return href

## Streamlit app
st.title("Language Translation Application Using LCEL")

# Language selection
target_language = st.selectbox(
    "Select the language you want to translate to",
    ["French", "Spanish", "German", "Italian", "Hindi", "Punjabi"]  # Add more languages as needed
)

# Main input box
input_text = st.text_input("Enter the text you want to translate", key="main_input")

# Handle the input submission
if st.button("Translate"):
    if input_text:
        with st.spinner('Translating...'):
            output_text = get_groq_response(input_text, target_language)
        
        st.write(output_text)
        
        # Provide download link for the text
        st.markdown(download_link(output_text), unsafe_allow_html=True)

#         # Provide download link for the text
#         st.markdown(download_link(output_text), unsafe_allow_html=True)
