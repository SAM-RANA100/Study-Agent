import streamlit as st

from study_agent import run_study_agent


st.set_page_config(
    page_title="Study Agent",
    page_icon="📚",
    layout="centered"
)


st.title("📚 Study Agent")

st.write(
    "Your AI study assistant for understanding, summarizing, "
    "and revising academic topics."
)


st.divider()


study_mode = st.selectbox(
    "What do you want to do?",
    [
        "Explain a topic",
        "Summarize",
        "Generate quiz questions",
        "Ask a study question",
        "Create revision notes"
    ]
)


user_input = st.text_area(
    "Enter your topic or question:",
    height=150,
    placeholder="Example: Explain reciprocal inhibition in simple language."
)


if st.button("Generate Answer"):

    if not user_input.strip():

        st.warning("Please enter a topic or question.")

    else:

        request = f"""
        Study mode: {study_mode}

        Student request:
        {user_input}
        """

        with st.spinner("Study Agent is thinking..."):

            try:

                result = run_study_agent(request)

                st.subheader("Study Agent")

                st.write(result)

            except Exception as e:

                st.error(
                    "Something went wrong. "
                    "Please check your configuration."
                )

                st.exception(e)
