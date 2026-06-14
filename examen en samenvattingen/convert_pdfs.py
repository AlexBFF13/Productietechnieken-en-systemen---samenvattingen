import fitz
import os

pdfs = [
    "Examenvragen 2022-2024 (Maxim Bijnens).pdf",
    "Formularium updated 2020.pdf",
    "Productietechnieken_en_systemen_examenvragen 2019 2021.pdf",
    "Richtlijnen examen H01O1.pdf",
    "Samenvatting 2024-2025 (Lisa Corten updated) (1).pdf",
]

for pdf in pdfs:
    out_path = os.path.splitext(pdf)[0] + ".md"
    doc = fitz.open(pdf)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {os.path.splitext(pdf)[0]}\n\n")
        for i, page in enumerate(doc, start=1):
            f.write(f"\n\n## Pagina {i}\n\n")
            f.write(page.get_text())
    print(f"{pdf} -> {out_path}")
