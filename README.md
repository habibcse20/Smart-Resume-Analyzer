#Smart Resume Analyzer

An **AI-powered Resume Analyzer** built with **Python and Streamlit** that evaluates how well a resume matches a given job description.  
The system uses **Natural Language Processing (NLP)** techniques such as **TF-IDF** and **Cosine Similarity** to calculate an **ATS-style match score**, extract key skills, and provide resume improvement suggestions.

---

## 🚀 Features

- 📄 Upload resume in **PDF format**
- 📝 Paste any **job description**
- 📊 **ATS Match Score** using TF-IDF & Cosine Similarity
- 🔑 **Keyword Extraction** from resume and job description
- ✅ **Matched Skills Identification**
- ❌ **Missing Skill / Skill Gap Analysis**
- 📈 Visual score representation
- 🛠 Resume improvement suggestions
- 🎨 Clean and user-friendly Streamlit UI

---

## 🧠 How It Works

1. Resume PDF text is extracted using **PyPDF2**
2. Text is cleaned and preprocessed using **NLTK**
3. Important keywords are extracted
4. Resume and job description are converted into **TF-IDF vectors**
5. **Cosine Similarity** is calculated to generate the match score
6. Skill gaps and suggestions are displayed

---

## 🛠 Technologies Used

- **Python**
- **Streamlit**
- **Scikit-learn**
- **NLTK**
- **PyPDF2**
- **Matplotlib**

---

## 📂 Project Structure

