import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def read_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def log_changes(log, old_data, new_data):
    changes = []
    for row in range(len(old_data)):
        for col in old_data.columns:
            old_value = old_data.at[row, col]
            new_value = new_data.at[row, col]
            if isinstance(old_value, (int, float)) and isinstance(
                new_value, (int, float)
            ):
                if round(old_value, 2) != round(new_value, 2):
                    changes.append(
                        f"Change of {col}: from {old_value} to"
                        f" {new_value} in row {row}"
                    )
            else:
                if old_value != new_value:
                    changes.append(
                        f"Change of {col}: from {old_value} to"
                        f" {new_value} in row {row}"
                    )
    log.extend(changes)
    return log


st.title("The iris dataset")

contents = {}
contents["intro"] = read_markdown_file("intro.md")
contents["play"] = read_markdown_file("play.md")
tab_intro, tab_data, tab_play = st.tabs(
    [
        "Introduction",
        "See the data",
        "Play with the data",
    ]
)

iris = pd.read_csv("iris.csv")

# Initialize session state if not already done
if "iris_edit" not in st.session_state:
    st.session_state["iris_edit"] = iris.copy()
if "log" not in st.session_state:
    st.session_state["log"] = []


def reset_data():
    st.session_state["iris_edit"] = iris.copy()
    st.session_state["log"] = []


with tab_intro:
    st.markdown(contents["intro"])

with tab_data:
    st.write("This is the famous iris dataset:")
    st.dataframe(iris)

with tab_play:
    st.subheader("Play with the Iris data")
    st.markdown(contents["play"])

    # Editable dataframe
    old_data = st.session_state["iris_edit"].copy()
    iris_edit = st.data_editor(
        st.session_state["iris_edit"], num_rows="dynamic"
    )
    st.session_state["iris_edit"] = iris_edit

    # Log changes
    st.session_state["log"] = log_changes(
        st.session_state["log"], old_data, iris_edit
    )

    st.subheader("Summary Statistics")
    st.write(st.session_state["iris_edit"].describe())

    st.subheader("Visualize the Iris data")

    # SPLOM (Scatterplot Matrix)
    st.write("### Scatterplot Matrix (SPLOM)")
    fig = sns.pairplot(st.session_state["iris_edit"], hue="species")
    st.pyplot(fig)

    # Trait selection for box plot
    trait = st.selectbox("Select trait for box plot:", iris.columns[:-1])

    # Box plot for selected trait
    train_name = trait.replace('_', ' ').title()
    st.write(
        f"### Box Plot: Distribution of {train_name} by Species"
    )
    fig, ax = plt.subplots()
    sns.boxplot(
        data=st.session_state["iris_edit"], x="species", y=trait, ax=ax
    )
    st.pyplot(fig)

    # Refresh button to reset the dataframe
    if st.button("Refresh"):
        reset_data()
        st.rerun()

    # Display change logs
    st.subheader("Change Logs")
    if st.session_state["log"]:
        for log_entry in st.session_state["log"]:
            st.write(log_entry)
    else:
        st.write("No changes made yet.")
