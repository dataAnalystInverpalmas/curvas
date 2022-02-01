import numpy as np
from scipy.signal import savgol_filter

#arr = [0,0,0,0.01,0.04,0.1,0.25,0.48,0.65,0.82,0.83,0.75,0.59,0.43,0.3,0.18,0.12,0.1,0.06,0.04,0.03,0.02,0.01,0,0,0,0,0,0.01,0.02,0.05,0.07,0.12,0.17,0.24,0.3,0.37,0.43,0.46,0.48,0.49,0.46,0.45,0.44,0.37,0.31,0.31,0.23,0.18,0.11,0.08,0.06,0.07,0.05,0.04,0.09,0.08,0.1,0.09,0.07,0.11,0.09,0.07,0.1,0.11,0.14,0.13,0.21,0.24,0.25,0.3,0.3,0.27,0.31,0.36,0.3,0.3,0.33,0.24,0.18,0.19,0.15,0.17,0.12,0.13]

EDAD_INI = 18
SEM_VALLE = 8

def datos_curva(curva):
  #diccionario con los ciclos y datos para usar de acuerdo a estos se define la curva final
  dic = {
    24: [-4,6,8],
    25: [-3,6,8],
    26: [-2,7,8],
    27: [-1,7,8],
    28: [0,7,7],
    29: [1,8,6],
    30: [2,8,6],
    31: [3,8,6],
    32: [4,8,6]
  }
  curva = np.array(curva)
  t_lista = 0
  i_final = 0
  largo = len(curva)
#recorrer la curva y hallar curvas más altas y ciclo
  for i in range(largo):
    lista = list(curva[i:i+4])
    res = np.sum(lista)
    if res > t_lista:
      t_lista = res
      i_final = i + 3

  ppi_zeros = i_final - dic.get(i_final + EDAD_INI)[1] 
  ppf_izeros = i_final + dic.get(i_final + EDAD_INI)[2]
  ppf_fzeros = i_final + 8 + SEM_VALLE
  
  spf_izeros = ((ppf_izeros) * 2) + EDAD_INI + dic.get(i_final + EDAD_INI)[0]
  spf_fzeros = spf_izeros + SEM_VALLE
  
  np.set_printoptions(precision=2)  # For compact display.
  #en el primer array se suaviza el primer pico
  a = np.array(savgol_filter(curva[:ppf_izeros + int(SEM_VALLE/2)],5,3))
  #en el segundo array se suzavizan 2do y 3er pico
  b = np.array(savgol_filter(curva[ppf_izeros + int(SEM_VALLE/2):],15,3))

  result = np.array(np.concatenate((a,b)))

  #total de flor mata que queda en el valle
  #tot_2v = np.sum(result[spf_izeros:spf_fzeros])
  #tot_3pico = np.sum(result[spf_fzeros:])
  #dist_3pico = [np.round((i/tot_3pico*tot_2v)+i,2) for i in result[spf_fzeros+1:]]

  #poner ceros en donde corresponda
  for i in range(largo):
    if (i<ppi_zeros) or (i>ppf_izeros and i<=ppf_fzeros) or (i >= spf_izeros and i <= spf_fzeros):
      result[i] = 0
      
  #si el num es negativo pone un cero
  result = zeros(result)

  #c = np.array(result[:spf_fzeros+1])
  #d = np.array(dist_3pico)

  c = np.array(savgol_filter(result[:ppf_izeros + int(SEM_VALLE/2)],5,3))
  d = np.array(savgol_filter(result[ppf_izeros + int(SEM_VALLE/2):],15,3))

  nresult = np.concatenate((c,d))
  #nresult = np.array(savgol_filter(result,7,3))
  #poner ceros en donde corresponda
  for i in range(largo):
    if (i<ppi_zeros) or (i>ppf_izeros and i<=ppf_fzeros) or (i >= spf_izeros and i <= spf_fzeros):
      nresult[i] = 0
  #si el num es negativo pone un cero
  nresult = zeros(nresult)

  return result,i_final,nresult

def zeros(x):
    nx = []
    x = np.array(x)
    for i in x:
        if i < 0:
            nx.append(0)
        else:
            nx.append(i)
    return np.array(nx)