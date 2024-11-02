from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="NEXUS", page_icon=":robot:",layout='wide',)

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

#local css
def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


#load assets
lottie_coding= load_lottieurl("https://lottie.host/ff8c6dfc-20b4-458d-9534-63a33ee0a78f/YVypuM2DSm.json")
img_contact_form= Image.open("images/yt_contact_form.png")
img_lottie_animation= Image.open("images/yt_lottie_animation.png")
img_contact_form1= Image.open("images/yt_contact_form1.png")
img_contact_form2= Image.open("images/yt_contact_form2.png")





#header
with st.container():
    st.subheader("NEXUS")
    st.title("A tech club at PES University Bangalore")
    st.write("Unlocking Tomorrow's Technology Today!")
    st.write(""" Our socials :  
             Instagram : https://www.instagram.com/nexus.pesu?igsh=aXJjeWg5N3NqbWNy
             LinkedIn : https://in.linkedin.com/company/nexus-pes
             """)

#what its about
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("Our Story: Pioneering Progress in Technology and Innovation")
        st.write("##")
        st.write("""Welcome to NEXUS, where innovation knows no bounds 
                 and creativity fuels our passion for making a difference
                 in the world of technology and engineering.""")
        st.write("""OurGoal
                 CSE Tech Innovators: Building a Unified Community
                     Establishing a dedicated community committed to leveraging technology
                     in order to address the challenges faced by both the CSE department 
                     and the college.""")
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")


with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column,text_column= st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)


    with text_column:
        st.subheader("Hear are our projects -")
        st.write("---")

with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("NoteVault")
        st.write("https://nexus-pes.vercel.app/projects/1")
        st.write("""NoteVault is a versatile note-taking platform designed to enhance organization and idea connectivity. 
                 It empowers users to create, link, and manage notes efficiently, fostering better understanding and 
                 exploration of their thoughts.NoteVault is a versatile note-taking platform designed to enhance 
                 organization and idea connectivity. It empowers users to create, link, and manage notes efficiently, 
                 fostering better understanding and exploration of their thoughts.NoteVault is a versatile note-taking 
                 platform designed to enhance organization and idea connectivity. It empowers users to create, link,
                 and manage notes efficiently, fostering better understanding and exploration of their thoughts.
                 NoteVault is a versatile note-taking platform designed to enhance organization and idea connectivity. 
                 It empowers users to create, link, and manage notes efficiently, fostering better understanding and 
                 exploration of their thoughts.NoteVault is a versatile note-taking platform designed to enhance 
                 organization and idea connectivity. It empowers users to create, link, and manage notes efficiently, 
                 fostering better understanding and exploration of their thoughts.NoteVault is a versatile note-taking 
                 platform designed to enhance organization and idea connectivity. It empowers users to create, link, 
                 and manage notes efficiently, fostering better understanding and exploration of their thoughts.""")
        st.write("---")


with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form1)
    with text_column:
        st.subheader("Nexus Website")
        st.write("https://nexus-pes.vercel.app/projects/2")
        st.write("""Dive into the immersive world of our Next.js-powered website, a testament to the expertise of the
                 Nexus Tech Club's web development team. This platform is meticulously designed to showcase and 
                celebrate our technological endeavors. The website not only serves as a visual portfolio but also
                as a dynamic archive, capturing the essence of our past events. Engage with the success stories,
                relive the moments, and understand the impact created by the Nexus Tech Club in the world of technology. 
                Stay informed and connected by receiving real-time updates on upcoming events, workshops, and collaborative
                opportunities.""")
        st.write("---")

        
with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("NexHunt Website")
        st.write("https://nexus-pes.vercel.app/projects/3")
        st.write("""Dive into the NexHunt Project, a purpose-built Next.js website dedicated to hosting NexHunt—an exceptional 
                 2-hour Treasure Hunt held on March 9th. Beyond a sleek design, this platform stands out for its real-time 
                 leaderboard updates, creating an interactive experience for participants. The primary objective of NexHunt 
                 was to engage students in a playful exploration of various Computer Science domains, fostering awareness and 
                 knowledge in a uniquely enjoyable manner. Discover the fusion of technology and fun, as NexHunt Project 
                 continues to captivate participants with its engaging features and real-time excitement.""")

#contact
with st.container():
    st.write("---")
    st.header("Get in touch with the team!")
    st.write("##")

    contact_form= '''
    <form action="https://formsubmit.co/nexus@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder ="Your name" required>
     <input type="email" name="email" placeholder="Your email"  required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
'''

left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()



        



