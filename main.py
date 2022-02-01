import numpy as np
import pandas as pd
import os
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from functions import datos_curva

#y = np.array([0.1, 0.15, 0.2, 0.3, 0.45, 0.75, 0.7, 1, 0.9, 0.8, 0.45, 0.3, 0.35, 0.2, 0.15, 0.1, 0.05,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0.1, 0.15, 0.2,0.35 ,0.4 , 0.45, 0.3, 0.2, 0.1 ])

file = pd.read_excel('files/datos.xlsx','bd_python',header=0)
df = pd.DataFrame(file)
EDAD_INI = 18

def graficar(df,finca,vari,option):
  #----------------------------
  df = df[ df.nvariedad==vari ]
  df = df[ df.finca==finca ]
  y = df['fm_aj']

  curve = np.array(y)
  largo = len(curve)
  maxi = np.max(curve)
  x = np.arange(EDAD_INI,EDAD_INI+largo,1)
  xticks = np.arange(EDAD_INI,EDAD_INI+largo,2)
  #datos de la curva
  results = datos_curva(curve)[0]
  #trae el ciclo, se debe sumar 18 de inicio de producción
  i_final = datos_curva(curve)[1]
  #nuevos resultados
  nresults = datos_curva(curve)[2]
  #-----------GRAFICAR-------------------#
  fig, ax = plt.subplots()
    #----------define ejes---------------------#
  y_tick = np.arange(0,maxi + 0.2,0.05)
  #graficar datos
  ax.plot(x,curve, label='inicial')
  ax.plot(x,results, label='final')
  ax.plot(x,nresults, label='corregida')
  ax.bar(i_final + EDAD_INI - 2,maxi,width=4,align='center',alpha=0.2)
  ax.grid()
  ax.legend()
  ax.set_xticks(xticks)
  ax.set_yticks(y_tick)
  ax.set_title( vari )
  ax.set_xlabel('edad')
  ax.set_ylabel('flor mata')
  fig.set_figheight(10)
  fig.set_figwidth(15)

  df['fm_suave'] = results

  if int(option)==0:
    route_delete = "C:/Users/ESTADISTICA/Desktop/py/curvas"
    str_file = './img/' + str(vari) + '_' + str(finca) + '.png'
    #eliminar archivos en carpeta destino 
    try:
      os.remove(route_delete + str_file[1:])   # Opt.: os.system("rm "+strFile)
    except OSError as error:
      print(error)
      print("File path can not be removed")
    #guarda grafico en la carpeta /img
    plt.savefig(str_file, transparent=True, bbox_inches='tight')
    
    
  else:
    plt.show()

  plt.close('all')

  return df

if __name__ == '__main__':
  while True:
      try:
          option = int(input("Seleccione opciones:\n 0: Graficar todo \n 1:Graficar manualmente \n Escriba: "))
          break
      except ValueError:
          print("¡Debe ingresar un número de 0 a 1!")

  if option==0:
      #graficar todo
      varieties = df.nvariedad.unique().tolist()
      ''' farms = df.finca.unique().tolist()
      for finca in farms:
          for vari in varieties:
              try:
                  graficar(df,finca,vari,option)
              except:
                  print(f'La variedad {vari} no existe en la finca {finca}') '''
      df_out = pd.DataFrame(columns=['finca','cflor','nvariedad','edad','pico','fm_real','fm_proy','fm_aj','fm_suave'])
      for vari in varieties:
          try:
              finca = 0
              graficar(df,finca,vari,option)
              res = graficar(df,finca,vari,option)
              #añade datos al dataframe de salida
              df_out = df_out.append(res, ignore_index=True)
              #graficar(df,0,vari,option)
          except:
              print(f'Ha ocurrido un error con: {vari}')
      
      df_out.to_excel('./files/bd.xlsx', sheet_name="bd_python", index=False)
  elif option==1:

      while True:
          try:
              vari = input("Ingrese el nombre de la variedad a graficar: ").upper().rstrip()
              finca = int(input("Ingrese: 0 - Total finca, 1 - Palmas, 2 - Palermo: "))
              graficar(df,finca,vari,option)
              break
          except:
              print("Algo está mal, pruebe de nuevo..")
        
  else:
      print("Seleccione entre 0 y 1, como indica el menú.")          

    