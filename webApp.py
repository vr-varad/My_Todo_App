import streamlit as st
import functions

todos = functions.get_todos()


def add_Todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todo(todos)
    st.session_state['new_todo'] = ""


st.title('My Todo App')
st.subheader('This is my Todo app')
st.write('This app is to increase your productivity.')
for index,todo in enumerate(todos):
    agree = st.checkbox(f'{todo}', key=todo)
    if agree:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(placeholder='Enter a todo....', label="Enter a todo down here.", on_change=add_Todo, key='new_todo')
