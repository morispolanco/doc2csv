import streamlit as st
import docx
import pandas as pd

def docx_to_csv(docx_file):
    doc = docx.Document(docx_file)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    df = pd.DataFrame(paragraphs, columns=['paragraph'])
    return df

def main():
    st.title("Conversor de documento DOCX a CSV")
    st.write("Esta aplicación convierte un documento DOCX en un archivo CSV, donde cada párrafo se guarda como una fila.")

    file = st.file_uploader("Sube un archivo DOCX", type=["docx"])

    if file is not None:
        df = docx_to_csv(file)
        st.write("Párrafos convertidos:")
        st.dataframe(df)

        csv_file = df.to_csv(index=False)
        st.write("Descargar archivo CSV:")
        st.download_button("Descargar archivo CSV", data=csv_file, file_name="converted_doc.csv")

if __name__ == "__main__":
    main()
