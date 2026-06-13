# AI Resume Intelligence System (NLP + Semantic Search)

An AI-powered system that evaluates resumes against job descriptions using semantic NLP (Sentence Transformers) and provides actionable insights for improving job fit.

## Key Highlights

- Resume ↔ JD semantic matching (not keyword-based)
- Uses Sentence Transformers (MiniLM)
- Generates ATS Score + Match Score
- Skill gap analysis (missing vs required skills)
- AI-powered resume improvement suggestions
- Explainable results (why score was given)  

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
  
## Features

- Resume ↔ Job Description matching
- ATS score calculation
- Semantic similarity (context-aware)
- Skill gap detection
- Resume rewrite suggestions
- PDF parsing and preprocessing

## Tech Stack

- **Backend:** Flask  
- **NLP:** Sentence Transformers (MiniLM)  
- **ML Tools:** Scikit-learn  
- **PDF Processing:** pdfplumber  
- **Frontend:** HTML, CSS, Bootstrap

## Key Learnings

- Semantic similarity > keyword matching for resume evaluation
- Embeddings improve contextual understanding of skills
- Explainability is important for user trust in AI systems

## Future Improvements

- Integrate LLM-based resume rewriting
- Add recruiter feedback loop
- Deploy as SaaS platform

## Installation

```bash
git clone https://github.com/yourusername/resume-intelligence-system.git
cd resume-intelligence-system
pip install -r requirements.txt
python app.py


