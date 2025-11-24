import os
from docx import Document
from openai import OpenAI

# ---------------------------
# CONFIGURATION
# ---------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
INPUT_FOLDER = os.getenv("cover_path") 
OUTPUT_DOCX = "JSON_Consolidated_STAR_Answers.docx"
MODEL = "gpt-5-mini"   # or another model you want to use

client = OpenAI(api_key=OPENAI_API_KEY)


# ---------------------------
# FUNCTION: Read DOCX content
# ---------------------------
def read_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs]).strip()

# ---------------------------
# FUNCTION: Process content via GPT
# ---------------------------
def extract_star_summary(text):
    prompt = f"""
You are helping consolidate job application cover notes.

Given the following cover note text, do the following:
1. Identify the each TOPIC / PROBLEM being addressed.
2. Produce a structured STAR (Situation, Task, Action, Result) answer summarising the candidates experience.

Note: as these are cover notes there may be multiple topics / problem.

Extract all STAR examples from the document.

Return JSON array only.
Each item:
"topic": "","situation": "","task": "","action": "","result": "","source_snippet": ""

Text to analyze:
{text}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ---------------------------
# MAIN PROCESS
# ---------------------------
def consolidate_notes():
    output_document = Document()
    output_document.add_heading("Consolidated Cover Notes in STAR Format", level=1)

    for root, dirs, files in os.walk(INPUT_FOLDER):
        for file in files:
            if file.lower().endswith(".docx"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")

                # 1. Read content
                content = read_docx(file_path)

                # 2. Ask GPT to summarize & structure
                summary = extract_star_summary(content)

                # 3. Add to final document
                output_document.add_heading(file, level=2)
                for line in summary.split("\n"):
                    output_document.add_paragraph(line)

    # Save the output
    output_document.save(OUTPUT_DOCX)
    print(f"Done! Output saved to: {OUTPUT_DOCX}")


# ---------------------------
# RUN
# ---------------------------
if __name__ == "__main__":
    consolidate_notes()
