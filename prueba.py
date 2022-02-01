""" import pandas as pd
from sklearn import linear_model
import pickle

# cargar el dataset en memoria
training_dataset = pd.read_csv("files/areas.csv")

# crear un modelo que use el algoritmo de regresion lineal
# y entrenarlo con los datos de nuestro csv
regression_model = linear_model.LinearRegression()
print ("Training model...")

# entrenamiento del modelo
regression_model.fit(training_dataset[['area']], training_dataset.price) 
print ("Model trained.")

# pedir al usuario que introduzca un area y calcular
# su precio usando nuestro modelo
input_area = int(input("Enter area: "))
proped_price = regression_model.predict([[input_area]])
print ("Proped price:", round(proped_price[0], 2))

# serializar nuestro modelo y salvarlo en el fichero area_model.pickle
print ("Model trained. Saving model to area_model.pickle")
with open("area_model.pickle", "wb") as file:
    pickle.dump(regression_model, file)
print ("Model saved.") """

import os

route_delete = "C:/Temp"
str_file = './img/' + 'cosecha' + '.txt'

try:
    os.remove(route_delete + str_file[1:])
    print("Eliminado")
except:
    print("No hay nada")
    pass

