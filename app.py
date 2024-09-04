import streamlit as st
from PIL import Image 
img = Image.open("bmi.png")
st.image(img,width=400)
st.title(':red[ Welcome to BMI Calculator!!!]')

st.markdown("### Body mass index (BMI) is a tool that healthcare providers use to estimate the amount of body fat by using your height and weight measurements")

st.text_input('Type your name')
status=st.radio("Select your gender:",('MALE','FEMALE','Prefer Not To Say'))
if(status=='MALE'):
    st.success("MALE")
elif(status=='FEMALE'):
    st.success("FEMALE")
else:
    st.success("Prefer Not To Say")    

physical_activity=st.multiselect("Physical_activity that you do for healthy body :",['Running','Yoga','Gym','Dancing',
                                                                                     'Cycling','Other','Nothing'])

st.write("Daily Food Intake:")
water=st.slider("Select the amount of water you intake (in litres):",1,6)


weight=st.number_input("  Enter your weight(in kgs)")

status= st.radio('Select your height format: ',('cms','metres','feet'))

if(status=='cms'):
    height=st.number_input('centimeters')

    try:
        bmi=weight/((height/100)**2)
    except:
        st.text("Enter some value of height") 

elif(status=='meters'):
    height=st.number_input('Meters')


    try:
        bmi=weight/(height**2)
    except:
        st.text("Enter some value of height")

else:
    height=st.number_input('Feet')

    try:
        bmi= weight/(((height/3.28))**2) 

    except:
        st.text("Enter some value of height")

if(st.button('Calculate BMI')):

    st.text("Your Body Mass Index is {}.".format(bmi)) 

    if(bmi<16):
        st.error("You are Extremely Underweight")
    elif(bmi>=16 and bmi<= 18.5):
        st.warning("You are Underweight") 
    elif(bmi>=18.5 and bmi<= 25):
        st.success("You are Healthy") 
    elif(bmi>= 25 and bmi <= 30):
        st.warning("You are Overweight")  
    elif(bmi>=30):
        st.error("You are Extremely Overweight")   



