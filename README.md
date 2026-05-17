# AI Resume Intelligence System

An AI-powered web application that analyzes resumes against job descriptions using semantic NLP techniques and provides actionable insights for improving job alignment.

## Features

- Resume ↔ Job Description semantic matching  
- ATS score calculation  
- Context-aware similarity using sentence embeddings  
- Skill gap analysis (required vs optional skills)  
- Explainability (why the score was given)  
- Intelligent resume rewrite suggestions  
- PDF resume parsing and preprocessing  

## How It Works

1. Extracts text from uploaded resume (PDF)
2. Processes job description input
3. Uses **sentence-transformers** to compute semantic similarity
4. Matches resume content with job requirements
5. Generates:
   - Match Score
   - ATS Score
   - Skill Gaps
   - Suggestions
   - Improved bullet points

## Tech Stack

- **Backend:** Flask  
- **NLP:** Sentence Transformers (MiniLM)  
- **ML Tools:** Scikit-learn  
- **PDF Processing:** pdfplumber  
- **Frontend:** HTML, CSS, Bootstrap

## Installation

```bash
git clone https://github.com/yourusername/resume-intelligence-system.git
cd resume-intelligence-system
pip install -r requirements.txt
python app.py
