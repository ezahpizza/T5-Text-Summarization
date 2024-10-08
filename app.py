import streamlit as st
import numpy as np
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import torch

import warnings
warnings.filterwarnings('ignore')

checkpoint = "ezahpizza/billsum_model"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

text = st.text_area('Enter text to summarize: use the format \"summarise: [your text]\"')
button = st.button("Summarize")


if text and button :
    y_pred =  summarizer(text)
    st.write("Summary: ",y_pred[0]['summary_text'])