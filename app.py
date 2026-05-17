from flask import Flask, render_template, request
from utilities.text_extractor import extract_text_from_pdf, extract_bullets, split_sections
from utilities.similarity import compute_similarity, bullet_analysis, section_scores
from utilities.skill_extractor import extract_weighted_skills, weighted_skill_matching
from utilities.ats import advanced_ats_score
from utilities.suggestions import generate_suggestions
from utilities.explain import generate_explanation
from utilities.skill_gap import skill_gap_analysis
from utilities.semantic_match import match_bullets_to_jd
from utilities.rewrite import intelligent_rewrite

app = Flask(__name__)

# In-memory users
users = {}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    users[username] = password
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    # Validate file
    resume_file = request.files.get('resume')
    if not resume_file:
        return render_template('index.html', error="Please upload a resume")

    # Validate JD
    jd_text = request.form.get('jd', "")
    if not jd_text.strip():
        return render_template('index.html', error="Please enter a job description")

    # Extract resume text
    resume_text = extract_text_from_pdf(resume_file)

    # Compute similarity
    score = compute_similarity(resume_text, jd_text) or 0

    # Skill extraction
    required, optional = extract_weighted_skills(jd_text)

    matched_req, total_req, matched_opt, total_opt = weighted_skill_matching(
        resume_text, required, optional
    )

    # ATS score
    ats = advanced_ats_score(
        score,
        matched_req, total_req,
        matched_opt, total_opt
    ) or 0

    # Section analysis
    sections = split_sections(resume_text)
    section_result = section_scores(sections, jd_text)

    if not section_result:
        section_result = {
            "skills": 0,
            "experience": 0,
            "projects": 0
        }

    # Suggestions
    suggestions = generate_suggestions(
        score,
        matched_req, total_req,
        matched_opt, total_opt,
        section_result
    ) or []

    # Extract bullets
    bullets = extract_bullets(resume_text)

    # fallback if bullets empty
    if not bullets:
        bullets = [resume_text[:200]]

    # Bullet analysis
    strong, weak = bullet_analysis(bullets, jd_text)
    strong = strong or []
    weak = weak or []

    # Explanation
    explanations = generate_explanation(
        score,
        matched_req, total_req,
        matched_opt, total_opt
    )

    # Skill gap analysis
    skill_gaps = skill_gap_analysis(
        matched_req, total_req,
        matched_opt, total_opt
    )

    # Semantic matching + intelligent rewrite
    matched_pairs = match_bullets_to_jd(bullets, jd_text)
    rewrites = intelligent_rewrite(matched_pairs)

    # Debug logs
    print("Score:", score)
    print("ATS:", ats)
    print("Section:", section_result)

    # Render result
    return render_template(
        'result.html',
        score=score,
        ats=ats,
        matched_req=matched_req or 0,
        total_req=total_req or 0,
        matched_opt=matched_opt or 0,
        total_opt=total_opt or 0,
        section_result=section_result,
        suggestions=suggestions,
        strong=strong,
        weak=weak,
        explanations=explanations,
        skill_gaps=skill_gaps,
        rewrites=rewrites
    )


if __name__ == '__main__':
    app.run(debug=True)