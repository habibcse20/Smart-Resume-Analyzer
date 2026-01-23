## Smart Resume Analyzer

An **AI-powered Resume Analyzer** built with **Python and Streamlit** that evaluates how well a resume matches a given job description.  
The system uses **Natural Language Processing (NLP)** techniques such as **TF-IDF** and **Cosine Similarity** to calculate an **ATS-style match score**, extract key skills, and provide resume improvement suggestions.

---

## Features:

- Upload resume in **PDF format**
- Paste any **job description**
- **ATS Match Score** using TF-IDF & Cosine Similarity
- **Keyword Extraction** from resume and job description
- **Matched Skills Identification**
- **Missing Skill / Skill Gap Analysis**
- Visual score representation
- Resume improvement suggestions
- Clean and user-friendly Streamlit UI

---

## How It Works:

1. Resume PDF text is extracted using **PyPDF2**
2. Text is cleaned and preprocessed using **NLTK**
3. Important keywords are extracted
4. Resume and job description are converted into **TF-IDF vectors**
5. **Cosine Similarity** is calculated to generate the match score
6. Skill gaps and suggestions are displayed

---

## Technologies Used:

- **Python**
- **Streamlit**
- **Scikit-learn**
- **NLTK**
- **PyPDF2**
- **Matplotlib**

## Project Structure

Smart-Resume-Analyzer/
│
├── app.py
├── README.md
├── requirements.txt
└── sample_resume.pdf


## Installation & Setup:

1️ Clone the Repository
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
streamlit run app.py

## Sample Use Case:
- Job seekers optimizing resumes for ATS systems
- HR teams performing resume screening
- Students creating AI / NLP projects
- Internship & placement preparation

## Future Enhancements:
- Section-wise resume analysis (Skills, Experience, Education)

- LLM-based resume feedback (ChatGPT integration)

- Resume ranking system

- Job recommendation engine

- Deployment on Streamlit Cloud / HuggingFace

## Author:
Md. Habibur Rahman
B.Sc. in Computer Science & Engineering
Dhaka University of Engineering & Technology (DUET)




