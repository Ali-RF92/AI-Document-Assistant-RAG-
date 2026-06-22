from pypdf import PdfReader


def load_pdf(pdf_path: str) -> str:

    reader = PdfReader(pdf_path)

    print("Pages:", len(reader.pages))

    text = ""

    for i, page in enumerate(reader.pages):

        page_text = page.extract_text()

        print(f"Page {i+1} chars:", len(page_text or ""))

        text += page_text or ""

    return text