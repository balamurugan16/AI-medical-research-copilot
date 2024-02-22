import streamlit as st
from app.load_datasource import create_embeddings


if "datasources" not in st.session_state:
    st.session_state["datasources"] = []

datasources = st.session_state["datasources"]
domains = ["PubMed", "DrugBank", "FDA", "DailyMed"]


def create_data_source():
    datasources.append({"url": "", "domain": ""})


def update_data_source(id):
    text_key = "text_{id}".format(id=id)
    select_key = "select_{id}".format(id=id)
    datasources[id]["url"] = st.session_state[text_key]
    datasources[id]["domain"] = st.session_state[select_key]


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
    col1, col2 = cont.columns([0.7, 0.3])
    text_key = "text_{id}".format(id=id)
    select_key = "select_{id}".format(id=id)
    col1.text_input(
        label="URL",
        placeholder="Enter the url",
        key=text_key,
        on_change=lambda: update_data_source(id),
    )
    col2.selectbox(
        on_change=lambda: update_data_source(id),
        label="Domain",
        options=domains,
        key=select_key,
    )
    # col3.button("X", key=id, type="primary", on_click=lambda: delete_data_source(id))
