import streamlit as st
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

import pip
pip.main(['install', 'nltk'])

# Download NLTK resources
nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")

#PAGE CONFIG =====================
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

#HEADER =====================
st.markdown("""
<h1 style='text-align:center;'>Smart Resume Analyzer</h1>
<p style='text-align:center;color:gray;'>
Analyze your resume against any job description using AI & NLP
</p>
<hr>
""", unsafe_allow_html=True)

#SIDEBAR =====================
with st.sidebar:
    st.header("⚙️ Settings")
    keyword_limit = st.slider("Top Keywords to Extract", 5, 30, 15)
    st.markdown("---")
    st.info("""
    **Features**
    - ATS Match Score
    - Skill Gap Analysis
    - Keyword Matching
    - Resume Improvement Tips
    """)

#HELPER FUNCTIONS =====================
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess(text):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(clean_text(text))
    return [w for w in tokens if w not in stop_words and len(w) > 2]


def calculate_similarity(resume, job):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume, job])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100
    return round(score, 2)


def extract_keywords(tokens, limit):
    return Counter(tokens).most_common(limit)

#MAIN APP =====================
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste Job Description", height=200)

if st.button("🚀 Analyze Resume"):
    if not uploaded_file or not job_description:
        st.warning("Please upload resume and job description.")
        st.stop()

    with st.spinner("Analyzing Resume with AI..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        resume_tokens = preprocess(resume_text)
        job_tokens = preprocess(job_description)

        similarity_score = calculate_similarity(
            " ".join(resume_tokens),
            " ".join(job_tokens)
        )

        resume_keywords = extract_keywords(resume_tokens, keyword_limit)
        job_keywords = extract_keywords(job_tokens, keyword_limit)

        resume_kw_set = set([k for k, _ in resume_keywords])
        job_kw_set = set([k for k, _ in job_keywords])

        missing_skills = job_kw_set - resume_kw_set
        matched_skills = job_kw_set & resume_kw_set

    #RESULT TABS =====================
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "🔑 Keywords", "🛠 Suggestions"])

    #OVERVIEW TAB =====================
    with tab1:
        st.subheader("📊 ATS Match Score")
        st.progress(int(similarity_score))
        st.metric("Match Percentage", f"{similarity_score}%")

        if similarity_score < 40:
            st.error("❌ Low Match – Resume needs significant improvement.")
        elif similarity_score < 70:
            st.warning("⚠️ Moderate Match – Improve keywords & skills.")
        else:
            st.success("✅ Excellent Match – Resume is ATS friendly.")

        # Chart
        fig, ax = plt.subplots()
        ax.barh(["Match Score"], [similarity_score])
        ax.set_xlim(0, 100)
        st.pyplot(fig)

    #KEYWORDS TAB =====================
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📄 Resume Keywords")
            st.write(resume_keywords)

        with col2:
            st.subheader("📝 Job Keywords")
            st.write(job_keywords)

        st.subheader("✅ Matched Skills")
        st.success(", ".join(matched_skills) if matched_skills else "No strong matches found")

        st.subheader("❌ Missing Skills")
        st.error(", ".join(missing_skills) if missing_skills else "No missing skills 🎉")

    #SUGGESTIONS TAB =====================
    with tab3:
        st.subheader("🛠 Resume Improvement Suggestions")

        if missing_skills:
            st.write("🔹 Add these keywords to your resume naturally:")
            for skill in missing_skills:
                st.markdown(f"- **{skill}**")
        else:
            st.success("Your resume already covers the required skills!")

        st.markdown("""
        **General Tips**
        - Use action verbs (developed, implemented, optimized)
        - Match job role keywords exactly
        - Keep resume ATS-friendly (no tables/images)
        - Quantify achievements with numbers
        """)

#FOOTER =====================
st.markdown("""
<hr>
<p style='text-align:center;color:gray;'>
Developed By Habibur Rahman | © 2024 All Rights Reserved
</p>
             """, unsafe_allow_html=True)




