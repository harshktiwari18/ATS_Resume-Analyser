# ATS Resume Analyzer

An AI-powered ATS (Applicant Tracking System) Resume Analyzer built with **Python** and **Google Gemini API**. It compares a resume against a job description and generates a detailed Markdown report with an ATS score, missing keywords, strengths, weaknesses, improvement suggestions, interview questions, and a personalized learning roadmap.

---

## Features

- ATS Compatibility Score
- Resume Summary
- Technical & Soft Skills Extraction
- Missing Keywords Detection
- Strengths & Weaknesses Analysis
- Resume Improvement Suggestions
- Project Evaluation
- Resume Rewrite Suggestions
- Technical & HR Interview Questions
- Personalized Learning Roadmap
- Markdown Report Generation

---

## Tech Stack

- Python 3.10+
- Google Gemini API (`google-genai`)
- Markdown

---

## Project Structure

```
ATS_Resume-Analyser/
│── ats_resume_analyzer.py
│── resume_analysis_report.md
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ATS_Resume-Analyser.git
cd ATS_Resume-Analyser
```

Install dependencies:

```bash
pip install google-genai
```

---

## Setup

Generate a Gemini API key from Google AI Studio.

### Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### Windows (CMD)

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

### Linux / macOS

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

---

## Usage

1. Open `ats_resume_analyzer.py`
2. Replace `RESUME_TEXT` with your resume.
3. Replace `JOB_DESCRIPTION` with the target job description.
4. Run:

```bash
python ats_resume_analyzer.py
```

The generated report will be saved as:

```
resume_analysis_report.md
```

---

## Sample Output

The report includes:

- Resume Summary
- Technical Skills
- Soft Skills
- ATS Match Score
- Missing Keywords
- Strengths
- Weaknesses
- Improvement Suggestions
- Project Evaluation
- Resume Rewrite
- Interview Questions
- Learning Roadmap
- Final Verdict

---

## Example

```
Analysis complete.
Report saved to: resume_analysis_report.md

ATS Score: 85%

Final Verdict: Good
```

---

## Future Improvements

- Upload Resume (PDF/DOCX)
- Upload Job Description File
- Streamlit Web Interface
- Export to PDF
- Multi-language Support
- Resume Comparison
- Multiple ATS Templates

---

## License

This project is licensed under the MIT License.
