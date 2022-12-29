
from pathlib import Path 
import streamlit as st
from PIL import Image 
# Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir /"assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# Stream lit Settings
PAGE_TITLE = "Digital CV | Jacob Pointon" 
PAGE_ICON = ":wave:"
NAME = "Jacob Pointon"
DESCRIPTION = """
Loml loml loml loml
"""
EMAIL = "Jacobp1997@live.co.uk"
SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/jacob-pointon-722399207/" ,
    "GitHub":  "https://github.com/Jacobp93"
}
PROJECTS ={
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# CSS / Assets settings
st.title("Hello There!")
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
#
col1 , col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Downlaod Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="applications/ocet-stream",
)
    st.write(" ", EMAIL)
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 2 Years Experience in Data Management roles 
- ✔️ Strong hands on experience in SQL , Application Support , Python  
- ✔️ Good understanding and exposure to Business Strategy , Marketing , Sales 
- ✔️ Excellent team-player and creative innovator 
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Experienced SQL , Excel , Python / Go-Lang at Junior level
- 📊 Data Visualization: PowerBi, Streamlit , 
- 📚 Project Management: Linkedin Strategies , Target Demographic , Sales analysis
- 🗄️ Databases: MySQL , SQL Management Studio 
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")
# --- JOB 1
st.write("🚧", "**SDR Data Researcher | Big Change**")
st.write("06/2022 - Present")
st.write(
    """
- ► Using PowerBI and SQL to gather and present data to build foundational pillars for Quarterly/Yearly Marketing Strategies  
- ► Internal analysis of stored data to refine Lead generation software, presenting problems to Senior Leadership as well as outlining recommendations to solve said problem
- ► Support an SDR team through application support, ensuring applications are set up correctly and most efficient ways of working are applied to daily processes
"""
)
# --- JOB 2
st.write('\n')
st.write("🚧", "**Application Support / Data Management | Leeds City Council (Education Sector) **")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Application Help Desk Support for 7 different applications, Problem Solving and presenting a solution to the end user  
- ► Data Management of Educational data, importing data into a bespoke system , Quality analysis / Communicating with schools to source correct information
- ► Supporting on application development projects, testing new upgrade builds , Using SQL for identifying problems with stored data
"""
)
# --- JOB 3
st.write('\n')
st.write("🚧", "**Administrative Officer | Leeds City Council (Education Sector) **")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Monitoring a team email inbox , carrying out admin duties to facilitate support for SEN Children and Parents 
- ► Communicating and outlining available SEN support for Stakeholders , including outlining processes and time lines for said support
- ► Organisation of Children's documents on behalf of school admissions for school placements, Carrying out FOI requests with associated deadlines
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Professional Goals")
st.write(
    """
- ► 
- ► 
- ► 
"""
)
