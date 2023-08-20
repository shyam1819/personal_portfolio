import streamlit as st
import json
from streamlit_lottie import st_lottie
import time
import streamlit.components.v1 as components
#from st_on_hover_tabs import on_hover_tabs

st.set_page_config(page_title="Personal Portfolio",page_icon=":bar_chart:",layout="wide")



hide_menu="""
    <style>
        #MainMenu {visibility: hidden;}
    </style>
"""

#st.markdown(hide_menu,unsafe_allow_html=True)

def load_json(path):
    with open(path,"r") as f:
        return json.load(f)
    
def dummy():
    initialize = [0]
    return initialize

if 'initialize' not in st.session_state:
    
    intro_animation=load_json("intro.json")
    animation_container=st.empty()
    with animation_container:
        st_lottie(
            intro_animation,
            speed=1,
            reverse=False,
            loop=False,
            quality="high",
            key="intro"
        )
    st.session_state.initialize=dummy()
    time.sleep(4)
    animation_container.empty()
st.title("Welcome! 👨‍💻")
#st.markdown("---")

tabs=[" My Portfolio "," Blog "," Projects "]
whitespace=38

portfolio, blog, projects = st.tabs([t.center(whitespace,"\u2001") for t in tabs])
with portfolio:
    L1_column, R1_column = st.columns(2)

    with R1_column:
        hi_animation=load_json("spaceman.json")
        st_lottie(
                hi_animation,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",
                key="Space_man"
            )
        
    with L1_column:
        st.markdown("""
            <div>
                <h2> Hey guys, I'm Kasi Viswanadha! </h2>
                <h2> I work as a senior software engineer at LTIMindtree company and I've been crushing it for the past 1 year.</h2>
            </div>
            <h2>  </h2>""",unsafe_allow_html=True)
        
        
        L1_1,R1_1 = st.columns([2,2])
        L1_1.image("Python_logo.png",use_column_width=True)
        
        R1_1.markdown("""<p style="
                font-size:22px;" 
                align="justify"> 
                As a Python enthusiast, I love nothing more than diving into some code and pushing the limits of what's possible. I'm always on the lookout for new challenges and ways to improve my skills, so if you have any cool projects in mind, hit me up! </p>""",unsafe_allow_html=True)
        

        st.markdown("""
            <p align="justify" style="
                font-size:20px"> Over the past four years, I've had the pleasure of working on all sorts of cool projects. I've become quite proficient with some of the most powerful Python libraries out there like numpy, pandas, seaborn, matplotlib, plotly, and sklearn, just to name a few. </p>""", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("## Work experience:-")

    with st.expander("Senior Software Engineer - DATA @ LTI Mindtree",expanded=True):
        el1, em1,er1 = st.columns([0.7,0.05,0.25])
        el1.markdown("""
            <div>
                <h5> <b>Duration:</b> July 2022 - Present. </h5>
                <h5> Project: Center of Excellence. </h5>
                <h5> Description: Bringing life to new ideas. Worked on multiple POCs, learning new tools quickly and adopting them for the use cases. </h5>
                <h5> Skills: Python, Snowflake, AWS, Docker. </h5>
            </div>""",unsafe_allow_html=True)
        er1.image("LTIMindtree.png",use_column_width=True)

    with st.expander("Research Intern @ IIT Madras",expanded=True):
        el2, er2 = st.columns([4,1])
        el2.markdown("""
            <div>
                <h5> Duration: May 2021 - August 2021. </h5>
                <h5> Project: Simulation of Triaxial Test. </h5>
                <h5> Description: Validation of numerical simulation with experimental results. </h5>
                <h5> Result: Stress - Strain curves under various confined pressures were observed to follow the same trend as experiments </h5>
                <h5> Skills: Python, Yade DEM </h5>
            </div>""",unsafe_allow_html=True)
        er2.image("IIT_Madras.png",use_column_width=True)
        
    st.markdown("---")

    st.markdown("## Education:- ")

    with st.expander("B.Tech - Mechanical Engineering @ IIT Tirpuati",expanded=True):
        sl1, sr1= st.columns([4,1])
        sl1.markdown("""
            <div>
                <h5> Duration: August 2018 - May 2022. </h5>
                <h5> Branch: Mechanical Engineering. </h5>
                <h5> CGPA: 8.33 </h5>
        </div>""", unsafe_allow_html=True)
        #sr1.image("IITTP_logo.png",use_column_width=True)
        sr1.image("IIT_Tirupati.png",use_column_width=True)
        
    st.markdown("---")

    st.markdown("## Skills and Tools:- ")



    # Python
    # Tableau
    # Snowflake
    # Matlab
    # C language
    # Docker
    # AWS

    L2_column, R2_column = st.columns(2)

    with L2_column:
        st.markdown("""
            - Python
            - Fast API
            - Matlab
            - C language
            """)
        
    with R2_column:
        st.markdown("""
            - Snowflake
            - Tableau
            - Docker
            - AWS
            """)
        
    st.markdown("---")
    
    st.markdown("## Certifications:-")

    # AWS Cloud Practitioner
    # Snowflake Pluralsight
    # Geeks For Geek Basic to Advanced Machine learning.
    # Leetcode SQL badge.
    
    L3_2_column, L3_1_column, M3_column, R3_1_column, R3_2_column=st.columns(5)

    L3_2_column.markdown("* AWS Cloud Practitioner")
    L3_1_column.markdown("* Snowflake - Pluralsight")
    R3_1_column.markdown("* GFG Basic to Advanced Machine Learning")
    R3_2_column.markdown("* Leetcode SQL badge")
    M3_column.markdown("* Tableau - Pluralsight")


    st.markdown("---")

    st.markdown("## Get in touch:-")

    con1, con2 = st.columns(2)
    embed_component={'linkedin':"""<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="light" data-type="HORIZONTAL" data-vanity="kasi-viswanadha-nerella-7306a91b0" data-version="v1">
                        <a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/kasi-viswanadha-nerella-7306a91b0?trk=profile-badge">KASI VISWANADHA NERELLA</a>
                    </div>
              """}
    with con1:
        components.html(embed_component['linkedin'],height=310)
with blog:
    st.markdown("""
        <div>
            <center>
                <h1> Working under progress! </h1>
                <h3> I will be coming back with few reviews on the books and places I have visited, So stay tuned. </h3>
            </center>
        </div>
    """,unsafe_allow_html=True)

with projects:
    st.markdown("""
        <div>
            <center>
                <h1> Working under progress! </h1>
                <h3> stay tuned </h3>
            </center>
        </div>
    """,unsafe_allow_html=True)



st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
