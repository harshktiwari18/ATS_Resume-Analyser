"""
ATS Resume Analyzer
--------------------
Analyzes a candidate's resume against a target job description using the
Google Gemini API and generates a detailed ATS evaluation report.

Features:
- Resume Summary
- Skills Extraction
- ATS Match Score
- Missing Keywords
- Resume Improvement Suggestions
- Project Evaluation
- Interview Questions
- Learning Roadmap

Requirements:
    pip install google-genai

Usage:
    1. Set the GEMINI_API_KEY environment variable.
    2. Add your resume and job description.
    3. Run:
       python ats_resume_analyzer.py
"""

import os
from google import genai

# ---------------------------------------------------------------------------
# 1. CONFIGURE YOUR INPUTS HERE
# ---------------------------------------------------------------------------

# Option A: paste text directly
RESUME_TEXT = """
PASTE THE FULL RESUME TEXT HERE
"""




JOB_DESCRIPTION = """
PASTE THE FULL JOB DESCRIPTION TEXT HERE
"""



# Option B: load from local .txt files instead (uncomment to use)
# with open("resume.txt", "r", encoding="utf-8") as f:
#     RESUME_TEXT = f.read()
# with open("job_description.txt", "r", encoding="utf-8") as f:
#     JOB_DESCRIPTION = f.read()

# ---------------------------------------------------------------------------
# 2. SYSTEM PROMPT — the analyzer persona and instructions
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an expert ATS (Applicant Tracking System) Resume Analyzer and Career Coach.
Your task is to analyze a candidate's resume against a provided job description and generate a
professional evaluation.

Perform the following tasks:

1. Resume Summary
- Provide a 3-5 sentence professional summary of the candidate.
- Identify years of experience (if available).
- Mention the primary domain and strongest skills.

2. Skills Extraction
Extract all technical and soft skills from the resume. Return them in two categories:
- Technical Skills
- Soft Skills

3. ATS Match Score
Calculate an estimated ATS compatibility score (0-100%). Consider:
- Skill matching
- Relevant experience
- Education
- Certifications
- Keyword relevance
- Project relevance
Explain why this score was assigned.

4. Missing Keywords
Compare the resume with the job description. List:
- Important missing technical skills
- Missing tools
- Missing certifications
- Missing action keywords

5. Strengths
Identify the strongest aspects of the resume (projects, experience, certifications, leadership,
technical expertise).

6. Weaknesses
Identify areas that could reduce interview chances (missing keywords, weak project descriptions,
lack of measurable achievements, formatting concerns, missing certifications).

7. Improvement Suggestions
Provide at least 10 specific, practical, actionable recommendations.

8. Project Evaluation
Evaluate all projects in the resume. For each project, explain strengths, suggest improvements,
and recommend technologies or features to add.

9. Resume Rewrite Suggestions
Rewrite the Professional Summary to make it stronger. Rewrite one project description using
strong action verbs and quantified achievements.

10. Interview Preparation
Generate 10 likely technical interview questions and 5 HR interview questions based on the
resume and job description.

11. Learning Roadmap
Recommend skills to learn, certifications, projects to build, and resources for improvement.

12. Final Verdict
Categorize the resume as one of: Excellent, Good, Average, Needs Improvement.
Explain the reason for the classification.

Output Format:
Return the response in clean Markdown using exactly these headings:
# Resume Summary
# Technical Skills
# Soft Skills
# ATS Score
# Missing Keywords
# Strengths
# Weaknesses
# Improvement Suggestions
# Project Evaluation
# Resume Rewrite
# Interview Questions
# Learning Roadmap
# Final Verdict

Keep the tone professional, constructive, and specific. Do not fabricate information that is not
present in the resume. If any required information is missing, clearly state that it was not
found rather than making assumptions.
"""

# ---------------------------------------------------------------------------
# 3. BUILD THE USER MESSAGE
# ---------------------------------------------------------------------------

def build_user_message(resume_text: str, job_description: str) -> str:
    return f"""Resume Text:
{resume_text}

Job Description:
{job_description}

Please perform the full analysis as instructed."""



# 4. CALL THE API

def analyze_resume(resume_text: str, job_description: str) -> str:
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable not found."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
System Instructions:
{SYSTEM_PROMPT}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text


# ---------------------------------------------------------------------------
# 5. RUN AND SAVE OUTPUT
# ---------------------------------------------------------------------------

def main():
    if "PASTE THE FULL" in RESUME_TEXT or "PASTE THE FULL" in JOB_DESCRIPTION:
        raise SystemExit(
            "Please fill in RESUME_TEXT and JOB_DESCRIPTION before running."
        )

    report = analyze_resume(RESUME_TEXT, JOB_DESCRIPTION)

    output_path = os.getenv("OUTPUT_FILE", "resume_analysis_report.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Analysis complete. Report saved to: {output_path}\n")
    print(report)


if __name__ == "__main__":
    main()