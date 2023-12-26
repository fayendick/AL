import streamlit as st
import pandas as pd
import neuralprophet
import matplotlib.pyplot as plt
import math 
import stats
#excel download
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

from ipywidgets import widgets


#import seaborn as sns


from neuralprophet import NeuralProphet


import numpy as np
#background-color: #ff000050;
import math
from PIL import Image

def main():

   ###### st.backgroundColor = "#F0F0FF0"
   ######  D3D3D3  ####  couleur gris

   st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FF0000;
    }
</style>
""", unsafe_allow_html=True)
   

   
   

   
   
   #from PIL import Image

   #image = Image.open('camo.jpg')

   #st.image(image)

   #st.markdown("<h2 style='text-align: center; color: RED;'>Machine Learning De Prévision Des Depots et Retraits </h2>", unsafe_allow_html=True)

   st.markdown("<h1 style='text-align: center; color: RED;'>Machine Learning De Prévision Des Dépots et Retraits</h1>", unsafe_allow_html=True)
   #st.markdown("<h1 style='text-align: center; color: grey;'>Machine Learning De Prévision Des Depots et Retraits</h1>", unsafe_allow_html=True)
   #st.markdown("<h2 style='text-align: center; color: RED;'>Machine Learning De Prévision Des Depots et Retraits </h2>", unsafe_allow_html=True)



   #st.title('Machine Learning De Prévision Des Depots et Retraits')
   st.subheader("Auteur : FAYE NDICK")
   def load_data():
      data=pd.read_excel('RETRAIT VERSEMENT.xlsx', dtype={'Name': int, 'Value': float}, index_col=0)
      #data=pd.read_excel('RETRAIT VERSEMENT.xlsx', sheet_name='Retraits et Versements',sep=';')
      return data
   # Echantillon
   dfa = load_data()
   #df=dfa.sample(100)
   
   
   df1=dfa.sort_values("DATE OPERATION")
   grp=df1.groupby(["AGENCE"]).sum().reset_index()
   
   tt=df1.groupby(["AGENCE","DATE OPERATION"]).sum().sort_values("DATE OPERATION").reset_index()
   DF = pd.pivot(tt, index="DATE OPERATION", columns="AGENCE", values="VOLUME TRANSACTION")
   DF=DF.reset_index(drop=False)
   #DF["DATE OPERATION"]
   DF.fillna(0).head(2)
   DFg=DF.drop("DATE OPERATION", axis='columns')
   
   
   


   ##ag1e=DF["AGENCE PARCELLES"]
   ag1e=DF[input('Veuillez valider le nom de l agence choisi avec exit : '  )]
   ag1=ag1e.copy()
   ag1=ag1.fillna(0)
   ag11=pd.DataFrame(ag1)
   ag11=ag11.fillna(0).head(3)
   d=DF["DATE OPERATION"]
   dd=pd.DataFrame(d)
   agdt=pd.DataFrame(ag1)
   a1=agdt.copy()
   ag1t=np.sqrt(a1) ## Rendre la série stationnaire
   ag1tt=pd.DataFrame(ag1t)
   agge=pd.concat([dd,ag1tt], axis=1)
   
   #Visualisation
   #st.write(agge)
   agge.to_excel("car.xlsx")
   
   
   
   
   
   
   
   
   
   #@st.cache
   #def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
      #return df.to_csv().encode('utf-8')

   #csv = convert_df(agge)

   #st.download_button(
      #label="Download data as CSV",
      #data=csv,
      #file_name='large_df.csv',
      #mime='text/csv',
   #)
   
   #st.write(agge)
   
   #fig, ax = plt.subplots()
   #ax.hist(agge, bins=20)
   #st.pyplot(agge)
   #st.pyplot(fig)
   
   
#Mois
#Visualisation de la cellule :
   #st.plt.figure(figsize=(16,4))
   #st.plt.title("AGENCE PARCELLES")
   #st.sns.lineplot(x=agge.index,y=agge["AGENCE PARCELLES"],label="Prevision Du Retrait Espece",color="red",marker="o",linewidth=0.3, data=agge) 
   #st.plt.legend()
   #st.plt.show()
   
   
#
#
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

   st.sidebar.image("camo.jpg", use_column_width=True)

   if st.sidebar.checkbox("Afficher Données", False):
      

      st.subheader("Données Historiques : Dépôt et Retrait")
      st.write(df1)





   if  st.sidebar.checkbox("Agence", False):
       st.subheader("Prévision Transaction")
       st.write(ag1e)
       
       
       
   if  st.sidebar.checkbox("Choix Transaction", False):
       st.sidebar.selectbox('Type Transaction',['Dépôt','Retrait'])
   
       
   #Prévision
   
   if st.sidebar.checkbox("Prévision", False):
      st.subheader("Résultat Prévision")
      st.write(agge)
      

   
   
   
   
   
   
   
   
       
   #Download excel
   def to_excel(df):
      output = BytesIO()
      writer = pd.ExcelWriter(output, engine='xlsxwriter')
      df.to_excel(writer, index=False, sheet_name='Sheet1')
      workbook = writer.book
      worksheet = writer.sheets['Sheet1']
      format1 = workbook.add_format({'num_format': '0.00'}) 
      worksheet.set_column('A:A', None, format1)  
      writer.save()
      processed_data = output.getvalue()
      return processed_data
   df_xlsx = to_excel(agge)
   st.sidebar.download_button(label='Télécharger Prévision',
                                data=df_xlsx ,
                                file_name= 'Donnees_Predites.xlsx')
   
   
   

   if  st.sidebar.checkbox("Visualisation", False):
       st.subheader("Diagramme de l'évolution des Transactions")


   


   
       
      

       #imag = Image.open('camo.jpj')
       #st.image()
       #st.image(imag)

if __name__== '__main__':
   main()