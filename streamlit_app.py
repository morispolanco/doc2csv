import streamlit as st
import pandas as pd
from docx import Document

def convert_doc_to_csv(file):
    doc = Document(file)
    data = []
    for page in doc.pages:
        data.append([paragraph.text for paragraph in page.paragraphs])
    df = pd.DataFrame(data, columns=["Page"])
    return df

def main():
    st.title("Conversor de archivos .doc a .csv")
    st.write("Cada página del archivo .doc se convertirá en una fila del archivo .csv")

    file = st.file_uploader("Sube un archivo .doc", type=["docx"])

    if file is not None:
        df = convert_doc_to_csv(file)
        st.write("Archivo .csv generado:")
        st.dataframe(df)

        csv_file = df.to_csv(index=False)
        st.download_button("Descargar archivo .csv", data=csv_file, file_name="converted_file.csv")

if __name__ == "__main__":
    main()
