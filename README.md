# ATS Resume Analyzer

A Python-based ATS (Applicant Tracking System) Resume Analyzer that evaluates a candidate's resume against a job description using the Anthropic Claude API and generates a detailed Markdown report.

## Features

- Resume summary generation
- Technical & soft skills extraction
- ATS match score estimation
- Missing keywords detection
- Strengths & weaknesses analysis
- Resume improvement suggestions
- Project evaluation
- Resume rewrite suggestions
- Technical & HR interview questions
- Learning roadmap generation
- Final resume verdict
- Markdown report generation

 ## Tech Stack

- Python 3.10+
- Anthropic Claude API 
- Markdown

 ## Project Structure

```
ATS_Resume-Analyser/
│
├── ats_resume_analyzer.py
├── resume.txt.pages
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/harshktiwari18/ATS_Resume-Analyser.git
cd ATS_Resume-Analyser
```

Install dependencies:

```bash
pip install anthropic
```

## Configuration

Set your Anthropic API Key.

### Windows (PowerShell)

```powershell
$env:ANTHROPIC_API_KEY="your-api-key"
```

### Linux / macOS

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

## Usage

Paste your resume and job description into:

```python
RESUME_TEXT = """
...
"""

JOB_DESCRIPTION = """
...
"""
```

Run the script:

```bash
python ats_resume_analyzer.py
```

The generated report will be saved as:

```
resume_analysis_report.md
```

## Output

The generated report includes:

- Resume Summary
- Technical Skills
- Soft Skills
- ATS Score
- Missing Keywords
- Strengths
- Weaknesses
- Improvement Suggestions
- Project Evaluation
- Resume Rewrite
- Interview Questions
- Learning Roadmap
- Final Verdict

## Future Improvements

- PDF Resume Upload
- DOCX Resume Support
- Streamlit Web Interface
- Batch Resume Analysis
- Keyword Highlighting
- Resume Comparison
- Export to PDF
- Docker Support

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

## License

This project is intended for educational and learning purposes.
