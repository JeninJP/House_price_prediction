import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from PIL import Image

st.set_page_config(
    page_title="Real estate",
    
    layout="wide",
    initial_sidebar_state="expanded")

def load_image_from_local(image_path, image_resize=None):
    image = Image.open(image_path)

    if isinstance(image_resize, tuple):
        image = image.resize(image_resize)
    return image


l=["1st Block Jayanagar", "1st Phase JP Nagar", "2nd Phase Judicial Layout", "2nd Stage Nagarbhavi", "5th Phase JP Nagar", "6th Phase JP Nagar", "7th Phase JP Nagar", "8th Phase JP Nagar", "9th Phase JP Nagar", "AECS Layout", "Abbigere", "Akshaya Nagar", "Ambalipura", "Ambedkar Nagar", "Amruthahalli", "Anandapura", "Ananth Nagar", "Anekal", "Anjanapura", "Ardendale", "Arekere", "Attibele", "BEML Layout", "BTM 2nd Stage", "BTM Layout", "Babusapalaya", "Badavala Nagar", "Balagere", "Banashankari", "Banashankari Stage II", "Banashankari Stage III", "Banashankari Stage V", "Banashankari Stage VI", "Banaswadi", "Banjara Layout", "Bannerghatta", "Bannerghatta Road", "Basavangudi", "Basaveshwara Nagar", "Battarahalli", "Begur", "Begur Road", "Bellandur", "Benson Town", "Bharathi Nagar", "Bhoganhalli", "Billekahalli", "Binny Pete", "Bisuvanahalli", "Bommanahalli", "Bommasandra", "Bommasandra Industrial Area", "Bommenahalli", "Brookefield", "Budigere", "CV Raman Nagar", "Chamrajpet", "Chandapura", "Channasandra", "Chikka Tirupathi", "Chikkabanavar", "Chikkalasandra", "Choodasandra", "Cooke Town", "Cox Town", "Cunningham Road", "Dasanapura", "Dasarahalli", "Devanahalli", "Dodda Nekkundi", "Doddaballapur", "Doddakallasandra", "Doddathoguru", "Domlur", "Dommasandra", "ECC Road, Whitefield,", "EPIP Zone", "Electronic City", "Electronic City Phase II", "Electronic city Phase 1,", "Electronics City Phase 1", "Frazer Town", "GM Palaya", "Garudachar Palya", "Giri Nagar", "Gollarapalya Hosahalli", "Gottigere", "Green Glen Layout", "Gubbalala", "Gunjur", "HBR Layout", "HRBR Layout", "HSR Layout", "Haralur Road", "Harlur", "Hebbal", "Hebbal Kempapura", "Hegde Nagar", "Hennur", "Hennur Road", "Hoodi", "Hoodi Circle,", "Horamavu Agara", "Horamavu Banaswadi", "Hormavu", "Hosa Road", "Hosakerehalli", "Hoskote", "Hosur Road", "Hulimavu", "ISRO Layout", "ITPL", "Iblur Village", "Indira Nagar", "JP Nagar", "JP Nagar 7th Phase,", "Jakkur", "Jalahalli", "Jalahalli East", "Jigani", "Judicial Layout", "Judicial Layout, Kanakapura Road,", "KR Puram", "Kadubeesanahalli", "Kadugodi", "Kaggadasapura", "Kaggalipura", "Kaikondrahalli", "Kalena Agrahara", "Kalyan nagar", "Kambipura", "Kammanahalli", "Kammasandra", "Kanakapura", "Kanakpura Road", "Kannamangala", "Karuna Nagar", "Kasavanhalli", "Kasturi Nagar", "Kathriguppe", "Kaval Byrasandra", "Kenchenahalli", "Kengeri", "Kengeri Satellite Town", "Kereguddadahalli", "Kodichikkanahalli", "Kodigehaali", "Kodihalli", "Kogilu", "Konanakunte", "Koramangala", "Kothannur", "Kothanur", "Kudlu", "Kudlu Gate", "Kumaraswami Layout", "Kundalahalli", "LB Shastri Nagar", "Laggere", "Lakshminarayana Pura", "Lingadheeranahalli", "Magadi Road", "Mahadevpura", "Mahalakshmi Layout", "Mallasandra", "Malleshpalya", "Malleshwaram", "Marathahalli", "Margondanahalli", "Marsur", "Mico Layout", "Munnekollal", "Murugeshpalya", "Mysore Highway", "Mysore Road", "NGR Layout", "NRI Layout", "Nagarbhavi", "Nagasandra", "Nagavara", "Nagavarapalya", "Narayanapura", "Neeladri Nagar", "OMBR Layout", "Off Sarjapur Road,", "Old Airport Road", "Old Madras Road", "Padmanabhanagar", "Pai Layout", "Panathur", "Parappana Agrahara", "Pattandur Agrahara", "Poorna Pragna Layout", "Prithvi Layout", "R.T. Nagar", "Rachenahalli", "Raja Rajeshwari Nagar", "Rajaji Nagar", "Rajiv Nagar", "Ramagondanahalli", "Ramamurthy Nagar", "Rayasandra", "Sahakara Nagar", "Sanjay nagar", "Sarakki Nagar", "Sarjapur", "Sarjapur  Road", "Sarjapur Road,", "Sarjapura - Attibele Road", "Sector 2 HSR Layout", "Sector 7 HSR Layout", "Seegehalli", "Shampura", "Shivaji Nagar", "Singasandra", "Somasundara Palya", "Sompura", "Sonnenahalli", "Subramanyapura", "Sultan Palaya", "TC Palaya", "Talaghattapura", "Thanisandra", "Thanisandra Main Road,", "Thigalarapalya", "Thubarahalli", "Thyagaraja Nagar", "Tindlu", "Tumkur Road", "Ulsoor", "Uttarahalli", "Varthur", "Varthur Road", "Varthur Road,", "Vasanthapura", "Vidyaranyapura", "Vijayanagar", "Vishveshwarya Layout", "Vishwapriya Layout", "Vittasandra", "Whitefield", "Whitefield,", "Yelachenahalli", "Yelahanka", "Yelahanka New Town", "Yelenahalli", "Yeshwanthpur", "south",'other']
col1, col2 = st.columns([6, 4])

with col1:
    st.write("""
## Know the price of your Future Home!! 
This app lets you predict the house prices in different areas of Banglore City 
""")
    loc=st.selectbox(' Location ',[x for x in l])
    st.markdown("""
    [To know about different types of area](https://housing.com/news/real-estate-basics-part-1-carpet-area-built-up-area-super-built-up-area/)
    """)

    area_type=st.selectbox('Choose your area type',('Built-up  Area','Super Built-up','Carpet  Area', 'Plot  Area'))
    sqft = st.slider('Total area (sqft)', 300,4000,1000)

with col2:
    st.image(load_image_from_local("images\Logo .jpg"), width=200)
    st.write("""We are using Machine Learning to Give you the prices for your favourate properties""")
    bhk=st.selectbox('No of Bedroom',[x for x in range(1,6)])
    
    bath=st.selectbox('No of bath rooms',[x for x in range(1,6)])

# Reads in saved classification model
lr_clf = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))

def load_saved_artifacts():
    
    global  __data_columns
    global __locations

    with open("model building\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:250]  # first 3 columns are sqft, bath, bhk

load_saved_artifacts()

def pred_price(loc,sqft,bath,bhk,area_type):
  loc_index= __data_columns.index(loc)
  try:
    area_index=__data_columns.index(area_type)
  except:
     area_index=-1 
  x=np.zeros(len(__data_columns))
  x[0]= sqft
  x[1]= bath
  x[2]=bhk
  if loc_index >=0:
    x[loc_index]=1
  if area_index >=0:
    x[area_index]=1
  return lr_clf.predict([x])[0]

st.subheader('Prediction in Lakhs ₹₹₹   ')
prediction=pred_price(loc,sqft,bath,bhk,area_type)
st.text(prediction)