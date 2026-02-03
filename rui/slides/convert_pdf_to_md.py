#!/usr/bin/env python3
"""Convert PDF files to Markdown format"""

import pypdf
import os

pdf_files = [
    "SiteWise-Retail Location OptimizationFather's Day Infographics A3 Poster.pdf",
    "SiteWise_Retail Optimization.pdf"
]

for pdf_file in pdf_files:
    try:
        if not os.path.exists(pdf_file):
            print(f"✗ {pdf_file}: File not found")
            continue
            
        reader = pypdf.PdfReader(pdf_file)
        markdown_file = pdf_file.replace('.pdf', '.md')
        
        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write(f"# {pdf_file}\n\n")
            
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                f.write(f"## Page {page_num}\n\n")
                f.write(text)
                f.write("\n\n---\n\n")
        
        print(f"✓ {pdf_file} → {markdown_file}")
    except Exception as e:
        print(f"✗ {pdf_file}: {e}")
