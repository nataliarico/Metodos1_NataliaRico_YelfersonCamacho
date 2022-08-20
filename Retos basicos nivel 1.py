# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:33:16 2021

@author: LENOVO 4
"""

def altura_en_mts(pies: int, pulgadas: int)->float:
    """ Altura de una persona
    Parámetros:
      pies (int): Número de pies que componen la altura de la persona
      pulgadas (int): Número de pulgadas que componen la altura de la persona
    Retorno:
      float: Altura de la persona en metros, la cual debe estar redondeada a dos cifras decimales.
    """
    pass
    incht = (pies*12) + pulgadas
    hm = round(((incht * 2.54)/100),2)
    return hm

def saludar_repetidas_veces(nombre: str, veces: int)->str:
    """ Saludo prolongado
    Parámetros:
      nombre (str): Nombre a incluir en el saludo
      veces (int): Cantidad de veces a repetir las letras
    Retorno:
      str: Cadena con el saludo con letras repetidas
    """
    pass
    o = "o"*veces
    a = "a"*round(veces/2)
    saludo = "H" + o + "l" + a + " " + nombre
    return saludo

def tiempo_a_segundos(dias: int, horas: int, mins: int, seg: int)->int:
    """ Unidades de tiempo a segundos
    Parámetros:
      dias (int): Número de dias del periodo de tiempo
      horas (int): Número de horas del periodo de tiempo
      mins (int): Número de minutos del periodo de tiempo
      seg (int): Número de segundos del periodo de tiempo
    Retorno:
      int: Número de segundos al que equivale el periodo de tiempo dado como parámetro
    """
    pass
    horast = (dias*24) + horas
    minst = (horast*60) + mins
    segt = (minst*60) + seg
    return segt

def calcular_iva_propina_total_factura(costo_factura: int)->str:
    """ IVA y propina
    Parámetros:
      costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina
    Retorno:
      str: Cadena con el iva, propina y total de la factura, separados por coma
    """
    pass
    IVA = costo_factura * 0.19
    propina = costo_factura *0.1
    valor_total = costo_factura + IVA + propina
    respuesta = str(round(IVA)) + "," + str(round(propina)) + "," + str(round(valor_total))
    return respuesta

def calcular_tarifa_taxi(kms_recorridos: float)->int:
    """ Tarifa de un taxi
    Parámetros:
      kms_recorridos (float): Kilómetros recorridos en el viaje
    Retorno:
      int: Tarifa a cobrar por el recorrido en taxi, la cual debe estar redondeada al entero mas cercano.
    """
    pass
    metros = kms_recorridos*1000    
    costot = round((82 * (metros/100)) + 4000)
    return costot

def area_habitacion(largo: float, ancho: float)->float:
    """ Área de una habitación
    Parámetros:
      largo (float): Largo de la habitación
      ancho (float): Ancho de la habitación
    Retorno:
      float: Número (float) que representa el área de la habitación redondeada con dos decimales.
    """
    pass
    area = round((largo * ancho), 2)
    return area

def suma_n_enteros_positivos(n: int)->int:
    """ Suma de los primeros n enteros positivos
    Parámetros:
      n (int): Número entero hasta el cual se quiere calcular la suma, desde 1
    Retorno:
      int: Suma de los primeros n enteros positivos.
    """
    pass
    suma = round((n*(n+1)) / 2)
    return suma

def volumen_cilindro(radio: float, altura: float)->float:
    """ Volumen de un cilindro
    Parámetros:
      radio (float): Radio de la base del cilindro
      altura (float): Altura del cilindro
    Retorno:
      float: El volumen del cilindro redondeado a un decimal
    """
    pass
    ar = 3.14159*(radio**2)
    vol = round(ar * altura, 1)
    return vol