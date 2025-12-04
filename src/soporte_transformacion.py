#IMPORTACIONES
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

# CON ESTA FUNCIÓN REALIZAMOS UN ANÁLISIS EXPLORATORIO DE UNA COLUMNA NUMÉRICA, CON CALCULOS ESTADÍSTICOS CLAVE(MÉTRICAS DE TENDENCIA CENTRAL Y DISPERSIÓN)
def exploracion_numerica(df, col):
    print(f'{'='*20} ANALISIS ESTADÍSTICO COLUMNA: {col} {'='*20}')
    print('-'*75)
    print(f'El mínimo de {col} es: {df[col].min()}')
    print('-'*75)
    print(f'El máximo de {col} es: {df[col].max()}')
    print('-'*75)
    print(f'La media de {col} es: {df[col].mean()}')
    print('-'*75)
    print(f'La mediana de {col} es: {df[col].median()}')
    print('-'*75)
    print(f'La Desviación Estandar de {col} es: {df[col].std()}')
    print('-'*75)
    print(f'{'='*20} VALORES NULOS COLUMNA: {col} {'='*20}')
    print('-'*75)
    print(f'Porcentaje nulos de {col}: {round(df[col].isna().sum()/df.shape[0],2)}') #PORCENTAJE DE NULOS RESPECTO AL TOTAL DE FILAS
    print('-'*75)


    print(f'{'='*20} VISUALIZACIONES: {col} {'='*20}')
    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (20,5))
    sns.histplot(data=df, 
                 x=col, 
                 ax = axes[0], 
                 kde=True, 
                 color = "mediumseagreen")
    axes[0].axvline(df[col].mean(), color = 'pink', label='media')
    axes[0].axvline(df[col].median(), color = 'purple', label='mediana')
    
    sns.boxplot(data=df, 
                x=col, 
                ax = axes[1], 
                color = "seagreen")
    plt.show();


# CON ESTA FUNCIÓN REALIZAMOS UN ANÁLISIS EXPLORATORIO DE UNA COLUMNA NUMÉRICA, CENTRADO EN PERCEPTILES Y OUTLIERS
def exploracion_outliers(df, col):
    print(f'{'='*20} ANALISIS PERCEPTILES Y OUTLIERS COLUMNA: {col} {'='*20}')
    print('-'*75)
    Q1 = np.nanpercentile(df[col],25)
    print(f'El Q1 de {col} es: {Q1}')
    print('-'*75)
    Q3 = np.nanpercentile(df[col],75)
    print(f'El Q3 de {col} es: {Q3}')
    print('-'*75)
    IQR = Q3-Q1
    print(f'El IQR de {col} es: {IQR}')
    print('-'*75)
    SALTO = IQR*1.5
    print(f'El Salto de {col} es: {SALTO}') #distancia que voy a saltar para calcular el bigote
    print('-'*75)
    bigote_derecha = Q3 + SALTO
    print(f'El bigote derecho de {col} es: {bigote_derecha}') #todo lo que este por encima de este valor es un outlier
    print('-'*75)
    bigote_izquierda = Q3 - SALTO
    print(f'El bigote izquierdo de {col} es: {bigote_izquierda}')
    print('-'*75)
    df_outliers = df[df[col]>bigote_derecha] #aislamos los registros atípicos en la columna por el extremo superior.
    print(f'registros inualmente altos de la columna {col}:')
    
    print(f'{'='*20} ANALISIS PERCEPTILES Y OUTLIERS COLUMNA: {col} {'='*20}')
          
    print(df_outliers)
    plt.show(); 


    # CON ESTA FUNCIÓN REALIZAMOS UN ANÁLISIS EXPLORATORIO DE UNA COLUMNA CATEGÓRICA, CON CALCULOS ESTADÍSTICOS CLAVE(MÉTRICAS DE TENDENCIA CENTRAL Y DISPERSIÓN)
def exploracion_categorica(df, col):
    print(f'{'='*20} ANALISIS ESTADÍSTICO COLUMNA: {col} {'='*20}')
    print('-'*75)
    print(f'Conteo de categorías unicas de {col}: {df[col].nunique()}')
    print('-'*75)
    print(f'Valores únicos de {col} es: {df[col].unique()}')
    print('-'*75)
    print(f'La Categoría más frecuente/moda de {col} es: {df[col].mode()}')
    print('-'*75)
    print(f'Número total de registros de {col} es: {df[col].shape[0]}')
    print('-'*75)
    print(f'{'='*20} VALORES NULOS COLUMNA: {col} {'='*20}')
    print('-'*75)
    porcentaje_nulos = (df[col].isna().sum()/df.shape[0])*100
    print(f'Porcentaje nulos de {col}: {round(porcentaje_nulos,2)}') #PORCENTAJE DE NULOS RESPECTO AL TOTAL DE FILAS
    print('-'*75)
  

    display(Markdown(f' ###VISUALIZACIÓN: {col}'))
    sns.countplot(data=df, 
                 x=col, 
                 palette= "mako")
    plt.xticks(rotation=90)
    plt.show();



# CON ESTA FUNCIÓN OBTENEMOS LA VISUALIZACIÓN DEL PORCENTAJE DE NULOS Y NO NULOS DE UN GRUPO DE COLUMNAS.

def visualizacion_nulos(df, cols):

    total_filas = len(df) #TOTAL FILAS DEL DF PARA PODER CALCULAR LOS NO NULOS

    # DEFINIMOS EL FORMATO PARA NUESTRO PIE

    colores = ["mediumseagreen", "seagreen"]

    fix, axes = plt.subplots(1, len(cols), figsize=(10, 5))

    for i, col in enumerate(cols): #GENERAMOS UN CONTEO DE NULOS Y NO NULOS PARA EL PIE

        num_nulos = df[col].isnull().sum()
        num_no_nulos = total_filas - num_nulos

        valores = [num_no_nulos, num_nulos]
        etiquetas = ['No nulos', 'Nulos']

        axes[i].pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
        axes[i].set_title(f'Nulos en {col}')

plt.tight_layout()
plt.show();