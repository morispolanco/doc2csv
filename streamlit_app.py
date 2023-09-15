import streamlit as st
import pandas as pd
from docx import Document

def convert_docx_to_csv(file):
    doc = Document(file)
    data = []
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text:
            data.append(text)
    df = pd.DataFrame(data, columns=["QUERY"])
    return df

def main():
    st.title("Conversor de archivos .docx a .csv")
    st.write("Cada párrafo del archivo .docx se convertirá en una fila del archivo .csv")

    file = st.file_uploader("Sube un archivo .docx", type=["docx"])

    if file is not None:
        df = convert_docx_to_csv(file)
        st.write("Archivo .csv generado:")
        st.dataframe(df)

        csv_file = df.to_csv(index=False)
        st.download_button("Descargar archivo .csv", data=csv_file, file_name="converted_file.csv")

if __name__ == "__main__":
    main()
