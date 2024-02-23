import streamlit as st
from app.load_datasource import create_embeddings


if "datasources" not in st.session_state:
    st.session_state["datasources"] = []

datasources = st.session_state["datasources"]


def create_data_source():
    datasources.append("")


def update_data_source(id):
    key = "url_{id}".format(id=id)
    datasources[id] = st.session_state[key]


def delete_data_source(id):
    datasources.pop(id)


def clear_datasources():
    datasources.clear()


st.title("Datasources")

c1, _, c2 = st.columns([0.7, 0.1, 0.2])

container = c2.container()
container.button("Add Datasource", on_click=create_data_source)
container.button("Clear Datasources", on_click=clear_datasources)
isClicked = container.button(
    "Generate Embeddings", on_click=lambda: create_embeddings(datasources)
)

if isClicked:
    st.spinner("loading...")
    st.toast("🙌 Generated Embeddings!")
    clear_datasources()

if len(datasources) == 0:
    c1.write("There are no datasources")

for id, key in enumerate(datasources):
    cont = c1.container()
    cont.text_input(
        label="URL",
        placeholder="Enter the url",
        key="url_{id}".format(id=id),
        on_change=lambda: update_data_source(id),
    )
    # col3.button("X", key=id, type="primary", on_click=lambda: delete_data_source(id))
