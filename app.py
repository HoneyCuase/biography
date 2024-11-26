import streamlit as st
import datetime

st.set_page_config(page_title="Honey's Biography", layout="wide")

# Initialize session state if not already initialized
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False
if 'name' not in st.session_state:
    st.session_state.name = "Honey Faith L. Cuase"
if 'about_me' not in st.session_state:
    st.session_state.about_me = ("Hi, I'm Honey Faith L. Cuase, I am doing great in my studies. I manage to have a balance social and academic life. And I make sure to have a leisure time so that I am a more productive and innovative student. I once believe that if you trust God, whatever obstacle or challenges you faced, God will help you know matter what situation you in because in the end “God is with you ")
if 'mother_name' not in st.session_state:
    st.session_state.mother_name = "Myshel L. Cuase"
if 'father_name' not in st.session_state:
    st.session_state.father_name = "Luisito S. Cuase"
if 'mother_bday' not in st.session_state:
    st.session_state.mother_bday = datetime.date(1981, 6, 21)
if 'father_bday' not in st.session_state:
    st.session_state.father_bday = datetime.date(1980, 3, 16)
if 'high_school' not in st.session_state:
    st.session_state.high_school = "Toledo S. Pantilo Sr. Memorial National Highschool"
if 'senior_high_school' not in st.session_state:
    st.session_state.senior_high_school = "Toledo S. Pantilo Sr. Memorial National High School"
if 'college' not in st.session_state:
    st.session_state.college = "Surigao del Norte State University"
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = "- I Play online games\n- Watch One Piece\n- Play Volleyball"
if 'gender' not in st.session_state:
    st.session_state.gender = "Female"
if 'birthplace' not in st.session_state:
    st.session_state.birthplace = "San pablo, Sison, Surigao del Norte"
if 'current_address' not in st.session_state:
    st.session_state.current_address = "Purok-3 San pablo, Sison, Surigao del Norte"
if 'mybirthday' not in st.session_state:
    st.session_state.mybirthday = datetime.date(2006, 9, 13) # Default birthdate (can be updated)

def toggle_button():
    st.session_state.toggle_state = not st.session_state.toggle_state

st.markdown(
    """
    <div style="text-align: center; font-size: 40px;">
        <strong> Honey's Biography </strong>  
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Get to know me</strong>
            </div>
        """, unsafe_allow_html=True)
        
        st.session_state.name = st.text_input("My Name", st.session_state.name)

        st.text_area("What I do", st.session_state.hobbies, height=125, key='hobbies')
        
        # Add the new fields for Age, Place of Birth, and Current Address
        st.subheader("Personal Details")
        
        # Make the birthdate editable
        birth_date = st.date_input("Date of Birth", st.session_state.mybirthday)
        st.session_state.mybirthday = birth_date  # Update the session state with the new date

        # Calculate age based on the selected birthdate
        st.session_state.age = (datetime.date.today() - birth_date).days // 365  # Calculate age
        st.write(f"Age: {st.session_state.age} years old")
        
        st.session_state.birthplace = st.text_input("Place of Birth", st.session_state.birthplace)
        st.session_state.current_address = st.text_input("Current Address", st.session_state.current_address)
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Click to see hobbies and achievements</strong>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Click here"):
            toggle_button()
        
        if st.session_state.toggle_state:
            st.markdown(""" 
            <div style="text-align: center; font-size: 25px;">
               <strong>Details about hobbies and achievements</strong>
            </div>
            """, unsafe_allow_html=True)
            st.text_area("Achievements", "- With Highest\n", height=125)
            st.text_area("Academic Achievements", "- Researcher\n- Math Enthusiast \n - Research Officers \n - Achiever since Elementary \n - Church Officer \n - Leader in Tambourine dancer", height=125)
        
        st.write("---")
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Social Media Accounts</strong>
            </div>
        """, unsafe_allow_html=True)

        social_media_html = """
            <a href="https://www.facebook.com/honeycuase.lozada">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" width="40" height="40" />
            </a>
            <a href="https://www.instagram.com/najaaa0.0?igsh=dmFpdmg1dTVybmgx" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/174/174855.png" alt="Instagram" width="40" height="40" />
            </a>
        """
        st.markdown(social_media_html, unsafe_allow_html=True)

    with right_column:
        st.image("https://scontent.fmnl8-4.fna.fbcdn.net/v/t39.30808-1/467027618_1932016050616441_4950739363074378939_n.jpg?stp=c0.0.720.720a_dst-jpg_s200x200&_nc_cat=107&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeHBp2Ppn4XHuAwulAHNnZpvy-izudzzFyXL6LO53PMXJW4-qSPqUaWDXbMhmWqDZFFHVyAp84zmzdvs57eWWzLz&_nc_ohc=v3GiBDW4rj4Q7kNvgEb9PLy&_nc_zt=24&_nc_ht=scontent.fmnl8-4.fna&_nc_gid=ALuDqCyp79Z1iyP5sXsYeXC&oh=00_AYCe1vR4Tz8Fup4UGHpThu5yLYo68mMcqdTa5YL2pwj_cA&oe=674A0E3C", width=250)
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>ABOUT ME</strong>
            </div>
        """, unsafe_allow_html=True)       
        
        st.session_state.about_me = st.text_area("About Me", st.session_state.about_me, height=200)
        st.session_state.gender = st.radio("Gender", ["Male", "Female"], index=0 if st.session_state.gender == "Male" else 1)

        st.subheader("Family Background")
        st.session_state.mother_name = st.text_input("Mother's Name", st.session_state.mother_name)
        st.session_state.mother_bday = st.date_input("Mother's Birthday", st.session_state.mother_bday)
        st.session_state.father_name = st.text_input("Father's Name", st.session_state.father_name)
        st.session_state.father_bday = st.date_input("Father's Birthday", st.session_state.father_bday)
        
        st.subheader("Educational Attainment")
        st.session_state.high_school = st.text_input("High School", st.session_state.high_school)
        st.session_state.senior_high_school = st.text_input("Senior High School", st.session_state.senior_high_school)
        st.session_state.college = st.text_input("College", st.session_state.college)
        
        st.write("---")