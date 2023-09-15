import streamlit as st
import pandas as pd
import docx
from docx import Document
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key

def correct_paragraphs(df):
    corrected_paragraphs = []
    for paragraph in df['paragraph']:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=paragraph,
            max_tokens=250,
            n=1,
            stop=None,
            temperature=0.7
        )
        corrected_paragraph = response.choices[0].text.strip()
        corrected_paragraphs.append(corrected_paragraph)
    df['corrected_paragraph'] = corrected_paragraphs
    return df

def create_docx(df):
    doc = Document()
    for paragraph in df['corrected_paragraph']:
        doc.add_paragraph(paragraph)
    return doc

def main():
    st.title("Corrección de errores gramaticales y de puntuación")
    st.write("Esta aplicación utiliza OpenAI Text Da Vinci 0.0.3 para corregir los errores gramaticales y de puntuación en el contenido de cada fila de un archivo CSV.")

    file = st.file_uploader("Sube un archivo CSV", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)
        st.write("Párrafos originales:")
        st.dataframe(df)

        df = correct_paragraphs(df)
        st.write("Párrafos corregidos:")
        st.dataframe(df)

        doc = create_docx(df)
        st.write("Archivo DOCX generado:")
        st.download_button("Descargar archivo DOCX", data=doc, file_name="corrected_file.docx")

if __name__ == "__main__":
    main()
