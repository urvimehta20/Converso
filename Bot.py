import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]

# This function uses the OpenAI Completion API to generate a 
# response based on the given prompt. The temperature parameter controls 
# the randomness of the generated response. A higher temperature will result 
# in more random responses, while a lower temperature will result in more predictable responses.

st.image("https://media.giphy.com/media/lrhawnngiA74DgpSJu/giphy.gif", width=200)
def generate_response(prompt):
    completions = openai.Completion.create (
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None, 
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


st.title("Converso")


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("Hello, how may I help you? ", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    
    st.session_state.generated.append(output)
    st.session_state.past.append(user_input)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')