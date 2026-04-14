
import json
import os
import requests
import streamlit as st

from app.parsers import parse_resume_file, parse_job_description_file

API_URL = st.secrets.get("API_URL", os.getenv("API_URL", "https://llm-resume-analyzer-api.onrender.com/analyze"))

st.set_page_config(
    page_title="LLM Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 LLM Resume Analyzer")
st.write(
    "Upload a resume, add a job description by paste or file upload, and get ATS-style insights."
)
st.caption(
    "Built for early-career candidates and freshers, while still supporting general resume analysis."
)

col_left, col_right = st.columns(2)

resume_text = ""
job_description = ""
jd_from_file = ""

with col_left:
    st.subheader("Resume Input")
    uploaded_resume = st.file_uploader(
        "Upload Resume (PDF, DOCX, TXT)",
        type=["pdf", "docx", "txt"],
        key="resume_uploader",
    )

    if uploaded_resume is not None:
        try:
            resume_text = parse_resume_file(
                uploaded_resume.name,
                uploaded_resume.getvalue(),
            )
            st.success("Resume parsed successfully.")

            with st.expander("Preview Resume Text"):
                preview_text = resume_text[:3000] if resume_text else "No text extracted."
                st.text(preview_text)

        except Exception as e:
            st.error(f"Failed to parse resume: {e}")

with col_right:
    st.subheader("Job Description Input")

    uploaded_jd = st.file_uploader(
        "Upload Job Description (PDF, DOCX, TXT) - Optional",
        type=["pdf", "docx", "txt"],
        key="jd_uploader",
    )

    if uploaded_jd is not None:
        try:
            jd_from_file = parse_job_description_file(
                uploaded_jd.name,
                uploaded_jd.getvalue(),
            )
            st.success("Job description file parsed successfully.")

            with st.expander("Preview Job Description from File"):
                preview_jd = jd_from_file[:3000] if jd_from_file else "No text extracted."
                st.text(preview_jd)

        except Exception as e:
            st.error(f"Failed to parse job description file: {e}")

    job_description_text = st.text_area(
        "Or Paste Job Description",
        height=220,
        placeholder="Paste the job description here...",
    )

# Priority: pasted JD > uploaded JD file
if job_description_text.strip():
    job_description = job_description_text.strip()
elif jd_from_file.strip():
    job_description = jd_from_file.strip()

analyze_clicked = st.button("Analyze Resume")

if analyze_clicked:
    if not uploaded_resume:
        st.error("Please upload a valid resume file.")
    elif not resume_text.strip():
        st.error("Resume text could not be extracted.")
    elif not job_description.strip():
        st.error("Please either paste a job description or upload a job description file.")
    else:
        payload = {
            "resume_text": resume_text,
            "job_description": job_description,
        }

        try:
            response = requests.post(API_URL, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()

            st.subheader("📊 Analysis Result")

            st.metric("ATS Match Score", f"{data['score']}%")
            st.progress(min(data["score"], 100) / 100)
            st.caption("Score is calculated using a combination of AI analysis and keyword matching.")

            if data["score"] >= 80:
                st.success("Strong match 🚀")
            elif data["score"] >= 60:
                st.warning("Moderate match ⚠")
            else:
                st.error("Low match ❌")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Strengths")
                for item in data["strengths"]:
                    st.write(f"✔ {item}")

                st.markdown("### ⚠ Missing Keywords")
                for item in data["missing_keywords"]:
                    st.write(f"• {item}")

            with col2:
                st.markdown("### 🚀 Improvements")
                for item in data["improvements"]:
                    st.write(f"• {item}")

            st.markdown("### ✨ Tailored Summary")
            st.info(data["tailored_summary"])

            st.download_button(
                label="📥 Download Analysis Report",
                data=json.dumps(data, indent=2),
                file_name="analysis_report.json",
                mime="application/json",
            )

        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")