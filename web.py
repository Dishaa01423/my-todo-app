import streamlit as st
import python12

todos = python12.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    python12.write_todos(todos)

todos = python12.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to denote the task you have to complete.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        python12.write_todos(todos)

st.text_input(label="",placeholder=" Add a new todo...",
              on_change=add_todo, key ="new_todo")