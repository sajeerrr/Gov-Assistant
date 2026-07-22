from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from config.settings import DATA_FOLDER


class PDFLoader:

    def load_documents(self):
        documents = []
        pdf_folder = Path(DATA_FOLDER)
        pdf_files = pdf_folder.glob("*.pdf")

        for pdf in pdf_files:
            loader = PyPDFLoader(str(pdf))
            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = "pm_kisan.pdf"
            documents.extend(docs)

        return documents