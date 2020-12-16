import streamlit as st
import pandas as pd
import numpy as np
import pickle
import cv
pickle_in=open('classifier2.pkl','rb')
classifier2=pickle.load(pickle_in)



def predict_note_authentication(team1,team2,toss_decision,toss_winner,city,homegorund,dl_applied):
    prediction = classifier2.predict([[team1,team2,toss_decision,toss_winner,city,homegorund,dl_applied]])
    ans=prediction[0]
    dct={0:'CHENNAI SUPER KINGS',1:'DELHI CAPITALS',2:'KOLKATA KNIGHT RIDERS',3:'KINGS XI PUNJAB',4:'MUMBAI INDIANS',5:'ROYAL CHALLENGES BANGALORE',6:'RAJASTHAN ROYALS',7:'SUN RISERS HYDERABAD'}
    print(dct[ans])
    return dct[ans]



def main():
    st.sidebar.text('@author-jayank chandil 24-10-2020')
    st.sidebar.title("IPL MATCH PREDICTION  ")
    st.sidebar.success('**MACHINE LEARNING WEB APPLICATION**')

    page_bg_img = '''
    <style>
    body {
    background-image: url("https://wallpapercave.com/wp/wp4059913.jpg");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    a = st.sidebar.selectbox('SELECT TEAM 1',("CSK",'DC','KKR','KXIP','MI','RCB','RR','SRH'))
    b = st.sidebar.selectbox('SELECT TEAM 2',("CSK",'DC','KKR','KXIP','MI','RCB','RR','SRH'))
    c = st.sidebar.selectbox('TOSS DECISION',('BAT','FIELD'))
    d = st.sidebar.selectbox('WHICH SELECTED TEAM WON THE TOSS',("CSK",'DC','KKR','KXIP','MI','RCB','RR','SRH'))
    e = st.sidebar.selectbox('CITY OF THE MATCH',('Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Ahmedabad', 'Dharamsala',
       'Pune', 'Raipur', 'Ranchi', 'Cuttack', 'Visakhapatnam',
       'Mohali'))
    f= st.sidebar.selectbox('FOR WHICH TEAM SELECTED CITY IS HOMEGROUND',("CSK",'DC','KKR','KXIP','MI','RCB','RR','SRH'))
    g=st.sidebar.selectbox('IF DUCKWORTH-LEWIS METHOD WILL APPLY ',('0','1'))
    dct1={'CSK': 0, 'DC': 1, 'KKR': 2, 'KXIP': 3, 'MI': 4, 'RCB': 5, 'RR': 6, 'SRH': 7,'BAT':0,'FIELD':1}
    dct2={'Hyderabad':7, 'Bangalore':1, 'Mumbai':12, 'Indore':8, 'Kolkata':10, 'Delhi':5,
       'Chandigarh':2, 'Jaipur':9, 'Chennai':3, 'Ahmedabad':0, 'Dharamsala':6,
       'Pune':13, 'Raipur':14, 'Ranchi':15,'Cuttack':4,'Visakhapatnam':16,
       'Mohali':11}
    team1=dct1[a]
    team2=dct1[b]
    toss_decision=dct1[c]
    toss_winner=dct1[d]
    city=dct2[e]
    homegorund=dct1[f]
    dl_applied=int(g)
    result=""

    if st.sidebar.button("Predict"):
        result=predict_note_authentication(team1,team2,toss_decision,toss_winner,city,homegorund,dl_applied)
        if(result=='CHENNAI SUPER KINGS'):

            page_bg_img = '''
                <style>
                body {
                background-image: url("https://www.teahub.io/photos/full/286-2869340_support-chennai-super-kings.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='ROYAL CHALLENGES BANGALORE'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://wallpapercave.com/wp/wp3995828.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='MUMBAI INDIANS'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://wallpapercave.com/wp/wp7509970.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='KINGS XI PUNJAB'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://www.dailyvedas.com/wp-content/uploads/2014/04/Kings-XI-Punjab-HD-Logo.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='RAJASTHAN ROYALS'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://www.kreedon.com/wp-content/uploads/2018/12/New-poster-of-team-Rajasthan-Royals-1024x630.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='KOLKATA KNIGHT RIDERS'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://wallpapercave.com/wp/wp2682672.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='SUN RISERS HYDERABAD'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://wallpaperaccess.com/full/2142542.jpg");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
        elif(result=='DELHI CAPITALS'):
            page_bg_img = '''
                <style>
                body {
                background-image: url("https://fsb.zobj.net/crop.php?r=ZKQL9ATH_NoVD_iBY3e7ZU3k4eg3uxSBzAmSroOIxkOymHDVKCDE5XaH6kBqzxtdrYb1b2380Y44stErwZQCRSGJgHww4_oe3V-w28Oqpj8yr5FgFQuxM_trYAkl26P8KewOUurzViwb1nXw");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)






    st.sidebar.success('OUR MODEL BEST TO PREDICT THE WINNING TEAM WILL BE --->>> {}'.format(result))
    if st.sidebar.button("About"):
        page_bg_img = '''
        <style>
        body {
        background-image: url("https://wallpapercave.com/wp/wp4059913.jpg");
        background-size: cover;
        }
        </style>
        '''

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.sidebar.text("Made by Jayank chandil")
        st.sidebar.text("Electronics and communication engineering")
        st.sidebar.text("EN17EL301066@medicaps.ac.in // no-9131352361")
        st.sidebar.text("MEDICAPS UNIVERSITY INDORE MADHYAPRADESH 453331")
    st.sidebar.success('**VISUALIZATION DASHBOARD**')
    if st.sidebar.button("TOSS DECISION IN CITIES"):
        page_bg_img = '''
                <style>
                body {
                background-image: url("https://i.pinimg.com/originals/ab/1f/f3/ab1ff3ec32022f981e308a54fa50f2ae.jpg");
                background-size: cover;
                }
                </style>
                '''

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.image('toss_new.png')
    if st.sidebar.button("TOSS DECISION IN TEAMS"):
        page_bg_img = '''
                <style>
                body {
                background-image: url("https://i.pinimg.com/originals/ab/1f/f3/ab1ff3ec32022f981e308a54fa50f2ae.jpg");
                background-size: cover;
                }
                </style>
                '''

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.image('toss_decision.png')
    if st.sidebar.button("TEAMS COMPARE"):
        page_bg_img = '''
                <style>
                body {
                background-image: url("https://i.pinimg.com/originals/ab/1f/f3/ab1ff3ec32022f981e308a54fa50f2ae.jpg");
                background-size: cover;
                }
                </style>
                '''

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.image('team_count.png')
    if st.sidebar.button("DUCK-LEWIS RULE"):
        page_bg_img = '''
                <style>
                body {
                background-image: url("https://i.pinimg.com/originals/ab/1f/f3/ab1ff3ec32022f981e308a54fa50f2ae.jpg");
                background-size: cover;
                }
                </style>
                '''

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.image('dl_applied.png')

    if st.sidebar.button("HOMEGROUND EFFECT "):
        page_bg_img = '''
                <style>
                body {
                background-image: url("https://i.pinimg.com/originals/ab/1f/f3/ab1ff3ec32022f981e308a54fa50f2ae.jpg");
                background-size: cover;
                }
                </style>
                '''

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.image('homeground.png')
if __name__=='__main__':
    main()