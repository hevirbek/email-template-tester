import streamlit as st
from jinja2 import Template
import json
import streamlit.components.v1 as components  # Import Streamlit



email_template_text_area = st.text_area("Email Template", height=300)
comments = st.text_area("Comments", height=100)

data_file = st.file_uploader("Upload JSON Data", type=['json'])

if data_file is not None:
    data = json.load(data_file)

    rendered_template = Template(email_template_text_area).render(event=data, comments=comments)
    components.html(rendered_template, height=1000, scrolling=True)