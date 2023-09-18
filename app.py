from pathlib import Path
import streamlit as st
from PIL import Image
import json

# FILE PATHS

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "picture.jpg"
icon_pic = current_dir / "assets" / "icon.png"
sections_file = current_dir / "assets" / "01_sections.json"
header_file = current_dir / "assets" / "02_header.json"
social_media_file = current_dir / "assets" / "03_social_media.json"
skills_file = current_dir / "assets" / "04_skills.json"
work_experience_file = current_dir / "assets" / "05_work_experience.json"
education_file = current_dir / "assets" / "06_education.json"
project_file = current_dir / "assets" / "07_projects.json"
publication_file = current_dir / "assets" / "08_publications.json"
public_speaking_file = current_dir / "assets" / "09_public_speaking.json"
certificates_file = current_dir / "assets" / "10_certificates.json"
accomplishments_file = current_dir / "assets" / "11_accomplishments.json"

with open(sections_file, "r") as sections_raw:
    sections_data = json.load(sections_raw)

# HEADER SECTION

with open(header_file, "r") as header_raw:
    header_data = json.load(header_raw)
st.set_page_config(page_title=header_data["PAGE_TITLE"], page_icon=Image.open(icon_pic))
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic)
with col2:
    st.title(header_data["NAME"])
    st.write(header_data["DESCRIPTION"])
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.write('\n')

# SOCIAL MEDIA SECTION

if sections_data["SOCIAL_MEDIA"]:
    with open(social_media_file, "r") as social_media_raw:
        social_media_data = json.load(social_media_raw)
    if len(social_media_data["SOCIAL_MEDIA"]) > social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"]:
        for row in range((len(social_media_data["SOCIAL_MEDIA"]) // social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"]) + 1):
            cols = st.columns(social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"])
            for index, (platform, link) in enumerate(social_media_data["SOCIAL_MEDIA"].items()):
                if index // social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"] == row:
                    cols[index % social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"]].write(f"🔖 [{platform}]({link})")
    else:
        cols = st.columns(len(social_media_data["SOCIAL_MEDIA"]))
        for index, (platform, link) in enumerate(social_media_data["SOCIAL_MEDIA"].items()):
            cols[index].write(f"🔖 [{platform}]({link})")
    st.write('\n')
    st.write('\n')

# SKILLS SECTION

if sections_data["SKILLS"]:
    st.subheader("📎 Skills")
    with open(skills_file, "r") as skills_raw:
        skills_data = json.load(skills_raw)
    if len(skills_data["SKILLS"]) > skills_data["MAX_SKILLS_COLUMNS"]:
        for row in range((len(skills_data["SKILLS"]) // skills_data["MAX_SKILLS_COLUMNS"]) + 1):
            cols = st.columns(skills_data["MAX_SKILLS_COLUMNS"])
            for index, skill in enumerate(skills_data["SKILLS"]):
                if index // skills_data["MAX_SKILLS_COLUMNS"] == row:
                    cols[index % skills_data["MAX_SKILLS_COLUMNS"]].write(f"🏷️ **{skill}**")
    else:
        cols = st.columns(len(skills_data["SKILLS"]))
        for index, skill in enumerate(skills_data["SKILLS"]):
            cols[index].write(f"🏷️ **{skill}**")
    st.write('\n')
    st.write('\n')

# WORK EXPERIENCE SECTION

if sections_data["WORK_EXPERIENCE"]:
    st.subheader("📎 Work Experience")
    with open(work_experience_file, "r") as work_experience_raw:
        work_experience_data = json.load(work_experience_raw)
    for description in work_experience_data["WORK_EXPERIENCE"]:
        cols = st.columns(3)
        cols[0].write(f"💼 **{description['DESIGNATION']}**")
        cols[1].write(f"🏢 **{description['COMPANY']}**")
        cols[2].write(f"🕰️ **{description['DURATION']}**")
        for item in description['DETAILS']:
            st.write(f"📌 {item}")
        st.write('\n')
    st.write('\n')

# EDUCATION SECTION

if sections_data["EDUCATION"]:
    st.subheader("📎 Education")
    with open(education_file, "r") as education_raw:
        education_data = json.load(education_raw)
    for description in education_data["EDUCATION"]:
        cols = st.columns(3)
        cols[0].write(f"🎓 **{description['COURSE']}**")
        cols[1].write(f"🏢 **{description['COLLEGE']}**")
        cols[2].write(f"🕰️ **{description['DURATION']}**")
        for item in description['DETAILS']:
            st.write(f"✒️ {item}")
        st.write('\n')
    st.write('\n')

# PROJECTS SECTION

if sections_data["PROJECTS"]:
    st.subheader("📎 Projects")
    with open(project_file, "r") as project_raw:
        project_data = json.load(project_raw)
    for item in project_data["PROJECTS"]:
        st.write(f"🖥️ {item}")
    st.write('\n')
    st.write('\n')

# PUBLICATIONS SECTION

if sections_data["PUBLICATIONS"]:
    st.subheader("📎 Publications")
    with open(publication_file, "r") as publication_raw:
        publication_data = json.load(publication_raw)
    for item in publication_data["PUBLICATIONS"]:
        st.write(f"📝 {item}")
    st.write('\n')
    st.write('\n')

# PUBLICATIONS SECTION

if sections_data["PUBLIC_SPEAKING"]:
    st.subheader("📎 Public Speaking")
    with open(public_speaking_file, "r") as public_speaking_raw:
        public_speaking_data = json.load(public_speaking_raw)
    for item in public_speaking_data["PUBLIC_SPEAKING"]:
        st.write(f"🎙️ {item}")
    st.write('\n')
    st.write('\n')

# CERTIFICATES SECTION

if sections_data["CERTIFICATES"]:
    with open(certificates_file, "r") as certificates_raw:
        certificates_data = json.load(certificates_raw)
    st.subheader("📎 Certificates")
    if len(certificates_data["CERTIFICATES"]) > certificates_data["MAX_CERTIFICATES_COLUMNS"]:
        for row in range((len(certificates_data["CERTIFICATES"]) // certificates_data["MAX_CERTIFICATES_COLUMNS"]) + 1):
            cols = st.columns(certificates_data["MAX_CERTIFICATES_COLUMNS"])
            for index, (certificate, link) in enumerate(certificates_data["CERTIFICATES"].items()):
                if index // certificates_data["MAX_CERTIFICATES_COLUMNS"] == row:
                    cols[index % certificates_data["MAX_CERTIFICATES_COLUMNS"]].write(f"📜 [{certificate}]({link})")
    else:
        cols = st.columns(len(certificates_data["CERTIFICATES"]))
        for index, (certificate, link) in enumerate(certificates_data["CERTIFICATES"].items()):
            cols[index].write(f"📜 [{certificate}]({link})")
    st.write('\n')
    st.write('\n')

# ACCOMPLISHMENTS SECTION

if sections_data["ACCOMPLISHMENTS"]:
    st.subheader("📎 Accomplishments")
    with open(accomplishments_file, "r") as accomplishments_raw:
        accomplishments_data = json.load(accomplishments_raw)
    for item in accomplishments_data["ACCOMPLISHMENTS"]:
        st.write(f"🏆 {item}")
    st.write('\n')
    st.write('\n')

# KINDLY SUPPORT THE EFFORTS

st.write('\n')
st.caption('Developed with ❤️ by [Sandip Palit](https://www.linkedin.com/in/sandip-palit/). Kindly support this [Resume Template](https://github.com/SandipPalit/Resume-Template) by giving a 🌟.')