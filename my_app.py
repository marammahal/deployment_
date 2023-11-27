# Streamlit Documentation: https://chat.openai.com/c/57fe51d5-5eac-4bf1-a912-4a5519f10bcb


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library

# Title

st.sidebar.title('Car Price Prediction')
html_temp = """
<div style="background-color:red;padding:10px">
<h2 style="color:white;text-align:center;">Maram's first app </h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

# Date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())
date=st.date_input("Enter the date")

# Time input
the_time=st.time_input("The time is", datetime.time(8, 45))
hour=st.time_input(str(pd.Timestamp.now()))
st.write("Hour is", hour)


# Markdown
col1, col2 = st.columns(2)
col1.markdown("# Do you like cats?")
# Add button
if col1.button("Yes, I do") :
    col1.success("Great!, watch this vedio")
if col1.button("No, I'm not") :
    col1.success("Mybe you do when you watch this vedio")

# Add video
col2.markdown("____________________________________")
col2.video("https://www.youtube.com/watch?v=uHKfrz65KSU")




col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("                                    ")
col1.markdown("### What about this image")

# Add image
img = Image.open("images.jpeg")
col2.image(img, caption="cattie", width=300)

# Add checkbox/Success/Info/Error
col1.write("Is she cute?")
cbox= col1.checkbox("Yes, she is")
cboz= col1.checkbox("No, she isn't")
if cbox :
    col1.info('You too')
if cboz :
    col1.error("You need glasses!")
else :
    col1.write("choose one")



# Text_input/Success/write
name = st.text_input("write your feelings", placeholder="express here")
if st.button("Submit"):
   st.write("your feeling submited {}".format(name.title()))
   st.success('Submited successed !')




# Add radio button
status = st.radio("Select your favorite ",("cats","dogs","birds"))
st.write("My favorite pet is ", status)


# Add select box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("Your Occupation is ", occupation)

# Multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])
st.write(f"You selected {len(multi_select)} number(s)")
st.write("Your selection is/are", multi_select)
for i in range(len(multi_select)):
    st.write(f"Your {i+1}. selection is {multi_select[i]}")

# Slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)

result=option1*option2
st.write("multiplication of two options is:",result)


    
# Code  # to show as if code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")

# Echo  # it is used "with block" to draw some code on the app, then execute it
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df




# Sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")

# Sidebar with slider
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)

# Dataframe
df=pd.read_csv("Advertising.csv")

# To display dataframe there are 3 methods

# Method 1
st.table(df.head())
# Method 2
st.write(df.head())  # dynamic, you can sort
st.write(df.isnull().sum())
# Method 3
st.dataframe(df.describe().T)  # dynamic, you can sort

# To load machine learning model
import pickle
filename = "my_model"
model=pickle.load(open(filename, "rb"))

# To take feature inputs
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

# Create a dataframe using feature inputs
my_dict = {"TV":TV,
           "radio":radio,
           "newspaper":newspaper}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)



if st.button("Predict"):
    pred = model.predict(df)
    col1, col2 = st.columns(2)
    col1.write("Prediction value")
    col2.success(pred[0].astype(int))
