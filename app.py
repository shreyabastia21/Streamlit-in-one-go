import streamlit as st

st.title('Title -> GeeksforGeeks')                                   #Title
st.header('Header -> GeeksForGeeks')                                 #Header
st.subheader('Subheader -> GeeksForGeeks')                           #subheader
st.text('Text -> GeeksForGeeks')                                     #Text

st.markdown('# Hi')                                                  #markdown  
"""
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

"""
st.success('Success !')                                             #success
st.info('Information')                                              #info
st.warning('Warning !')                                             #warning
st.error('Error !')                                                 #error

exp = ZeroDivisionError('Divison not possible with 0')
st.exception(exp)                                                   #exception

st.subheader('Help')
st.help(ZeroDivisionError)

st.write("range(1,10)")                                             #write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.subheader('Code')
st.code('x = 10\n'                                                  #code
        'for i in range(x):\n'
        '\tprint(i)')

st.subheader('Checkbox')
st.checkbox('Male')                                                #checkbox
if(st.checkbox('Adult')):
    st.write("You're an adult !")

st.subheader('Radio Button')
radioButton = st.radio('Select :', ('Male','Female','Other'))      #Radio Button
if(radioButton == 'Male'):
   st.write("You're a Male.")
elif(radioButton == 'Female'):
    st.write("You're a Female.")
elif(radioButton == 'Other'):
    st.write("You're an Other Gender.")

st.subheader('Select Box')                                          #selectbox
selectBox = st.selectbox("Data Science : ", ['Data Analysis','Web Scraping','Machine Learning','Deep Learning',
                                 'Natural Language Processing','Computer Vision','Image Processing'])

st.write("You've selected : ", selectBox)

st.subheader('MultiSelect Box')                                      #multi select box
multiSelBox = st.multiselect("Data Science : ", ['Data Analysis','Web Scraping','Machine Learning','Deep Learning',
                                 'Natural Language Processing','Computer Vision','Image Processing'])

st.write("You've selected : ", len(multiSelBox) , "courses.")

st.subheader('Button')                                               #Button
if(st.button('Click me')):
    st.write('Thanks for clicking me !')

st.subheader('Slider')                                               #slider
vol = st.slider('Select the volume',1,100,step=1)
st.write('Volume is : ',vol)

st.subheader('Text Input')                                           #text input
username=st.text_input('Username: ')
password=st.text_input('Password: ', type='password')

st.subheader('Text Area')
textArea = st.text_area('Write something about yourself in 20 words.')
st.write(textArea)

st.subheader('Input Number')
st.number_input('Select your age :',18,110)

st.subheader('Input Date')
st.date_input('Date')

st.subheader('Input Time')
st.time_input('Time')
