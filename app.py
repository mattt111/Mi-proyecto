import streamlit as st
import Funciones as Fun
st.title("Aplicacion de Funciones")
Capital=st.number_input("Ingrese la capital:",100,1000)
Tiempo=st.number_input("Ingrese la Ingrese el tiempo")
tasa_Interes=st.number_input("Ingrese la tasa de interes")
Interes=Fun.interes_simple(capital_inicial=Capital,tiempo_meses=Tiempo,tasa_interes=tasa_Interes)
st.write("El interes simple es:",int(Interes))






