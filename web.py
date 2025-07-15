import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + '\n')
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

# st.checkbox("Buy grocery.")
# st.checkbox("Do laundry.")


for todo in todos:
    st.checkbox(todo)


st.text_input(label=" ", label_visibility="collapsed", placeholder="Add a new task...", key='new_todo', on_change = add_todo)


print("hello")


st.session_state