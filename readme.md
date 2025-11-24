# Consolidated STAR Cover Notes Processor

This project processes multiple `.docx` cover notes, extracts STAR (Situation, Task, Action, Result) examples using an OpenAI model, and consolidates the structured results into a single Word document.

---

## 📌 Overview

This script recursively scans a folder for `.docx` files, reads each document, and uses an OpenAI GPT model to:

1. Identify topics / problems described in the candidate's cover notes.
2. Extract STAR-formatted experience summaries.
3. Return a clean JSON structure for each STAR example.
4. Append all output into a final consolidated Word document.

The result is a unified file (`JSON_Consolidated_STAR_Answers.docx`) containing structured STAR analysis for all input documents.

---

## 📁 Folder Structure

```
project/
│
├── your_script.py
├── README.md
└── cover_notes_folder/
    ├── file1.docx
    ├── file2.docx
    └── ...
```

---

## ⚙️ Requirements

### Python Packages

* `python-docx`
* `openai` (latest Python client)
* `os` and `json` (built-in)

Install dependencies:

```bash
pip install python-docx openai
```

### Environment Variables

You must set:

* `OPENAI_API_KEY` — your OpenAI API key
* `cover_path` — folder containing `.docx` files

Example (macOS/Linux):

```bash
export OPENAI_API_KEY="your_key_here"
export cover_path="/path/to/cover/notes"
```

Windows (PowerShell):

```powershell
setx OPENAI_API_KEY "your_key_here"
setx cover_path "C:\path\to\cover\notes"
```

---

## ▶️ How It Works

1. The script walks through the input folder.
2. Reads every `.docx` file.
3. Sends the content to an OpenAI model with a strict prompt requiring JSON output.
4. Attempts to parse the JSON; falls back to raw text if invalid.
5. Appends the results to a consolidated document.
6. Saves the final file: `JSON_Consolidated_STAR_Answers.docx`.

---

## 🧠 Model Configuration

You can change the model used:

```python
MODEL = "gpt-5.1-mini"
```

Use any valid model available to your API key.

---

## 📄 Output

The final generated file contains:

* One section per processed `.docx`
* JSON-formatted STAR summaries

Example entry:

```json
[
  {
    "topic": "Customer escalation",
    "situation": "A major client reported system outages...",
    "task": "I needed to restore service within SLA...",
    "action": "Coordinated engineers, ran diagnostics...",
    "result": "Resolved the issue in 45 minutes...",
    "source_snippet": "..."
  }
]
```

---

## 🚀 Running the Script

```bash
python your_script.py
```

You should see console output showing each file being processed.

---

## 🛠️ Troubleshooting

### Issue: "Invalid JSON returned"

LLM outputs are sometimes imperfect. The script already attempts to:

* clean markdown formatting
* parse JSON
* fall back to raw text

For 100% reliability, consider switching to function-calling.

### Issue: "Environment variable missing"

Ensure `OPENAI_API_KEY` and `cover_path` are set.


---

## 🧩 Possible Enhancements

* Export STAR entries into Excel
* Add logging and error reports
* Group results by theme
* Generate recruiter-ready summaries
* Use OpenAI function-calling for guaranteed JSON output

---

