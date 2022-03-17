# Analisis
Análisis de datos en pandemia departamento del atlántico 


# PROBLEMATICA
 
La empleabilidad en el departamento del atlántico ha disminuido durante el periodo en pandemia que inicio desde año 2020 tomando mayor fuerza desde que se decretó la cuarentena desde el mes de marzo, esto con el fin de disminuir el número de contagios, pero esto trajo consigo la perdida de un gran número de empleos en todo el departamento y se viera afectada la economía de ciento de hogares que no contaban con ingresos económicos.





# PREGUNTA PROBLEMA



¿Fueron suficientes las medidas tomadas para garantizar el empleo en el departamento?



# TIPO DE INVESTIGACION 

El tipo de investigación que se emplea es Cuantitativa - Longitudinal porque los datos son medibles y cuantificables, y longitudinal porque se centra en observar la evolución de una serie de variables a lo largo del tiempo. En este caso interesa observar períodos diferentes





# OBJETIVOS


## Objetivo general 


Evaluar como la ruta de la empleabilidad del departamento del atlántico facilito el acceso al empleo formal en años de pandemia, durante los periodos de tiempo que comprenden desde el 2020 hasta la actualidad teniendo como ultimo registro el mes de enero del presente año (2022).


## Objetivo especifico


* Obtener la base de datos ofrecida por datos.gov para iniciar el análisis de datos 

* Refinar la información para hallar la población de estudio (Empleados).

* Analizar los datos obtenidos.

* Comparar los resultados obtenidos de la contratación en los años 2020 y 2021 para determinar la población beneficiaria durante estos periodos de tiempo.

* Implementar graficas para representar los periodos de años, características de la población y lugar de residencia.


# METODOLOGIA.

Paso 1: Obtención de la base de datos para su análisis.

Para obtener la base de datos se ingresa desde un navegador y se ingresa el siguiente enlace https://bit.ly/3MFHABk y a continuación se exporta la base de datos seleccionando el botón de exportar y a continuación saldrá un menú para elegir el formato en el cual vamos a descargar nos permite la opción de CSV y JSON en nuestro caso para nuestro análisis elegiremos el formato csv.

Paso 2: Refinamiento de la información.
Se necesita crear un dataframe donde vamos a guardar la base datos que obtuvimos anteriormente.

PASO 3: Analizar los datos. 


PASO 4: Visualizar el análisis implementando graficas.


# RESULTADO. 

**CARACTERÍSTICAS Y ORIGEN DE LA BASE DE DATOS.**

Fuente de la información: www.datos.gov.co

Datos ofrecidos por : Área o dependencia	Secretaría de Desarrollo Económico, Oficina de Inclusión y Desarrollo productivo
Nombre de la Entidad	:	Alcaldía Distrital de Barranquilla, Distrito Especial, Industrial y Portuario
Departamento : Atlántico
Sector : Función Pública
Categoría :	Economía y Finanzas
Ultima Actualización	: 19 de enero de 2022
Responsable de veracidad 	: Alcaldía Distrital de Barranquilla.

**Lenguaje de programación utilizado.** 

Python  :snake:	

**Librerías utilizadas**  
```
numpy
pandas
matplotlib
seaborn
```


Luego de descargar la base de datos que se va a utilizar se procede a refinar la información e  iniciar el análisis de la información.
* creamos dataframe donde copiamos la base de datos obtenida en formato csv
```
DATA = PD.READ_CSV('EMPLEO.CSV')
```


*	se crea segundo dataframe donde se excluye la información que no necesitamos y nos enfocamos en la población a analizar .

```
DF_FILTRO=DATA[(DATA['SITUACIÓN LABORAL']!="DESEMPLEADO") & (DATA['SITUACIÓN LABORAL']!='CESANTE POR EMERGENCIA SANITARIA')]
```
En este caso excluimos a la población desempleada y a la que paso a ser cesante por el estado de emergencia.

*	se imprime el nombre cada una de las columnas para conocer los datos que vamos a manejar en el proceso .
```
DATA.COLUMNS
```

 
* se refinan los datos renombrando los encabezados de las columnas para mejorar su llamado al momento de analizar.
```
DF_FILTRO =DF_FILTRO.RENAME (COLUMNS={    
"TIPO DOCUMENTO" :"TIPO_DOCUMENTO",
    "CANAL DE REGISTRO":"CANAL_REGISTRO",
    "EDAD":"EDAD",
    'GÉNERO': 'GENERO',
    "NIVEL DE ESTUDIO": "NIVEL_ESTUDIO",
    'TÍTULO HOMOLOGADO' :'TITULO_HOMOLOGADO',
    'CIUDAD DE RESIDENCIA':'CIUDAD_RESIDENCIA',
    'FECHA REGISTRO':'FECHA_REGISTRO',
    'PROGRAMA DE GOBIERNO':'PROGRAMA_GOBIERNO',
    'CONDICIONES ESPECIALES':'CONDICIONES_ESPECIales',
    'SITUACIÓN LABORAL':'SITUACIÓN_LABORAL',
    'FECHA ACTUALIZACIÓN':'FECHA_ACTUALIZACION',
    'ZONA':'ZONA',
    'MES':'MES',
    'AÑO':"ANIO",
    'PUNTO ATENCIÓN':'PUNTO_ATENCION',
    'RANGO EDAD':'RANGO_EDAD'
})
```
	 
* se procede hacer separación por años y guardarla de manera individual.
```
ANIO2021=MDATOS[MDATOS['ANIO']=="2,021"]
ANIO2020=MDATOS[MDATOS['ANIO']=="2,020"]
```
esto con el fin de manejar la información de manera individual para cada año y hacer su proceso de análisis mas rápido y fácil

*	Se procede a realizar el primer análisis de la población viendo cuales fueron los rangos de edades beneficiarias.
```
PROGRAMA = DF_FILTRO.GROUPBY("RANGO_EDAD")["SITUACIÓN_LABORAL"].COUNT()
PROGRAMA.HEAD(7).PLOT.BARH(EDGECOLOR="BLACK",COLOR="#0B3861",  FIGSIZE =(18,8))
PLT.GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
PLT.TITLE("BENEFICIARIOS POR EDAD",FONTDICT=FONT1)
PLT.YLABEL("RANGO DE EDADES", FONTDICT= FONT2)
PLT.XLABEL('CANTIDAD BENEFICIARIOS',FONTDICT=FONT2)
PLT.FIGURE( FIGSIZE =(18,8))
PLT.SHOW()
``` 
<img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/beneficiario%20por%20edad.png" width="1000px" align="center">


* Se separa la información años utilizando los dataframe creados anteriormente.
```
F, AX =PLT.SUBPLOTS(1,2 , FIGSIZE=(18,8))
PROGRAMA = ANIO2020.GROUPBY("RANGO_EDAD")["SITUACIÓN_LABORAL"].COUNT()
PROGRAMA.HEAD(7).PLOT.BARH(EDGECOLOR="BLACK",COLOR="#0B3861",  FIGSIZE =(18,8), AX=AX[0])
AX[0].GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
AX[0].SET_TITLE("BENEFICIARIOS POR EDAD AÑO 2020",FONTDICT=FONT1)
AX[0].SET_YLABEL("RANGO DE EDADES", FONTDICT= FONT2)
AX[0].SET_XLABEL('CANTIDAD BENEFICIARIOS',FONTDICT=FONT2)

PROGRAMA = ANIO2021.GROUPBY("RANGO_EDAD")["SITUACIÓN_LABORAL"].COUNT()
PROGRAMA.HEAD(7).PLOT.BARH(EDGECOLOR="BLACK",COLOR="#F7D358",  FIGSIZE =(18,8), AX=AX[1])
AX[1].GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
AX[1].SET_TITLE("BENEFICIARIOS POR EDAD AÑO 2020",FONTDICT=FONT1)
AX[1].SET_YLABEL("RANGO DE EDADES", FONTDICT= FONT2)
AX[1].SET_XLABEL('CANTIDAD BENEFICIARIOS',FONTDICT=FONT2)
PLT.SHOW()
 ```
<img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/beneficiario%20por%20edad%202020%20-%202021.png" width="1000px" align="center">


*	Se realiza también el análisis para determinar los niveles educativos de la población beneficiaria.

```
VALOR_PORCARRERA = DF_FILTRO.GROUPBY("NIVEL_ESTUDIO")["TIPO_DOCUMENTO"].COUNT()
VALOR_PORCARRERA.HEAD(20).PLOT.BARH(EDGECOLOR='BLACK',FIGSIZE=(18,8),COLOR="TEAL")
PLT.GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
PLT.SHOW()

 ```
<img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/nivel%20educativo.png" width="1000px" align="center">






*	Se logra identificar la población por sexo por cada año.
```
COLORS = ['#F7D358','#0B3861']
COLORS1=['#53A9A3','#97367A']
FIG, (AX1, AX2) = PLT.SUBPLOTS(1,2, FIGSIZE =(18,8))
ANIO2020['GENERO'].VALUE_COUNTS().PLOT.PIE(AX =AX1,EXPLODE =[0,0.1],  SHADOW =TRUE,STARTANGLE=90,COLORS=COLORS)
AX1.SET_TITLE('ATENCIÓN POR AÑO 2020',FONTDICT= FONT1)
PLT.SHOW
ANIO2021['GENERO'].VALUE_COUNTS().PLOT.PIE(AX =AX2,EXPLODE =[0,0.1], SHADOW =TRUE,STARTANGLE=90,COLORS=COLORS)
AX2.SET_TITLE('ATENCION POR  GENERO 2021',FONTDICT= FONT1)
PLT.SHOW
DF_FILTRO.GROUPBY(["ANIO","GENERO"])["SITUACIÓN_LABORAL"].COUNT()

```
 <img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/Atencion%20por%20genero%20a%C3%B1o.png" width="1000px" align="center">

* Se muestra la población por género en total atendida sin distinción de años.
```
DF_FILTRO.GENERO.VALUE_COUNTS().PLOT.PIE(EXPLODE =[0,0.1] , SHADOW =TRUE,STARTANGLE=90,  FIGSIZE =(18,8), COLORS=COLORS)
PLT.TITLE('CONTRATACIÓN POR GENERO',FONTDICT= FONT1)
PLT.SHOW()
DF_FILTRO.GROUPBY(["GENERO"])["SITUACIÓN_LABORAL"].COUNT()
 ```
  <img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/Atencion%20por%20genero%20total.png" width="400px" height="300px" align="center">
 
* Histograma por año 2020 y 2021 sobre personas contratadas durante cada mes de cada año.

```
COLORS = ['#F7D358','#0B3861']
F , AX =PLT.SUBPLOTS(1,2,FIGSIZE=(30,10))
ANIO2020.MES.PLOT.HIST(EDGECOLOR='WHITE',COLOR='#F7D358',AX=AX[0],)
ANIO2021.MES.PLOT.HIST(EDGECOLOR='WHITE',COLOR='#0B3861',AX=AX[1])
AX[0].SET_TITLE ('EMPLEABILIDAD EN EL AÑO 2020',FONTDICT = FONT1)
AX[0].SET_XLABEL('MESES', FONTDICT = FONT2)
AX[0].SET_YLABEL('')
AX[0].GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
AX[1].SET_TITLE ('EMPLEABILIDAD EN EL AÑO 2021',FONTDICT = FONT1)
AX[1].SET_XLABEL('MESES', FONTDICT = FONT2)
AX[1].GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
PLT.SHOW
```
   <img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/empleabilidad%20a%C3%B1o%202020-2021.png" width="1000px" align="center">

* Se compara la información de manera paralela

```
PLT.FIGURE(FIGSIZE=(30,10))
SNS.HISTPLOT(DATA=ANIO2021 , X="MES" ,COLOR="#0B3861", KDE=TRUE, LABEL="AÑO 2021",EDGECOLOR='WHITE')
SNS.HISTPLOT(DATA=ANIO2020 , X="MES",COLOR="#F7D358", KDE=TRUE, LABEL="AÑO 2020",EDGECOLOR='WHITE')
PLT.TITLE("EMPLEABILIDAD AÑOS 2020-2021", FONT=FONT1)
PLT.LEGEND() 
PLT.GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
PLT.SHOW()
``` 
 <img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/empleabilidad%20a%C3%B1o%202020-2021%20comparativa.png" width="1000px" align="center">

* Beneficiarios en todos los municipios del departamento del atlántico.

```
PLT.FIGURE(FIGSIZE=(10,5))
VALOR_POR_CIUDAD=DF_FILTRO.GROUPBY("CIUDAD_RESIDENCIA")["SITUACIÓN_LABORAL"].COUNT()
VALOR_POR_CIUDAD.HEAD(20).PLOT.BARH(EDGECOLOR="BLACK",COLOR="#0B3861")
PLT.TITLE("BENEFICIARIOS POR MUNICIPIOS",FONTDICT=FONT1)
PLT.GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
PLT.YLABEL("MUNICIPIOS", FONTDICT= FONT2)
PLT.XLABEL('CANTIDAD DE BENEFICIARIOS 2020-2021',FONTDICT=FONT2)
PLT.FIGURE( FIGSIZE =(18,8))
PLT.SHOW()
 ```
   <img src="https://github.com/SaukB/Analisis/blob/main/Graficas/Beneficiarios%20municipios.png?raw=true" width="1000px" align="center">

 <img src="https://github.com/SaukB/Analisis/blob/main/Graficas/Beneficiarios%20municipios%20barras.png?raw=true" width="1000px" align="center">
 
* Beneficiarios en todos los municipios del departamento del atlántico sin la capital .

```
NB1=DF_FILTRO[DF_FILTRO['CIUDAD_RESIDENCIA']!="BARRANQUILLA"]
NB2=NB1[DF_FILTRO['CIUDAD_RESIDENCIA']!="SOLEDAD"]
F , AX =PLT.SUBPLOTS(1,2,FIGSIZE=(30,10))
VALOR_POR_CIUDAD =   NB1.GROUPBY("CIUDAD_RESIDENCIA")["SITUACIÓN_LABORAL"].COUNT()
VALOR_POR_CIUDAD.HEAD(20).PLOT.BARH(EDGECOLOR="BLACK",COLOR="#F7D358",AX=AX[0])
AX[0].SET_TITLE("BENEFICIARIOS POR MUNICIPIOS SIN BARRANQUILLA",FONTDICT=FONT1)
AX[0].SET_YLABEL("MUNICIPIOS", FONTDICT= FONT2)
AX[0].SET_XLABEL('CANTIDAD DE BENEFICIARIOS 2020-2021',FONTDICT=FONT2)
AX[0].GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)

VALOR_POR_CIUDAD2 = NB2.GROUPBY("CIUDAD_RESIDENCIA")["SITUACIÓN_LABORAL"].COUNT()
VALOR_POR_CIUDAD2.HEAD(20).PLOT.BARH(EDGECOLOR="BLACK",COLOR="#0B3861",AX=AX[1])
AX[1].SET_TITLE("BENEFICIARIOS POR MUNICIPIOS SIN SOLEDAD",FONTDICT=FONT1)
AX[1].SET_YLABEL("MUNICIPIOS", FONTDICT= FONT2)
AX[1].GRID(B = TRUE, COLOR ='GREY',LINESTYLE ='-.', LINEWIDTH = 0.5,ALPHA = 0.6)
PLT.XLABEL('CANTIDAD DE BENEFICIARIOS 2020-2021',FONTDICT=FONT2)
PLT.SHOW()
```

 <img src="https://github.com/SaukB/Analisis/blob/main/Graficas/Beneficiarios%20municipios%20sin%20la%20capital%20.png?raw=true" width="1000px" align="center">
 <br>
 <img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/municipios%20sin%20la%20capital%201%20barras%20.png?raw=true"width="1000px"align="center">
 <br>
 <img src="https://raw.githubusercontent.com/SaukB/Analisis/main/Graficas/municipios%20sin%20la%20capital%202%20barras%20.png"width="1000px"align="center">
<br>

* listado de beneficiarios por departamento.

```
TABL1=df_filtro.GROUPBY(["CIUDAD_RESIDENCIA"])["SITUACIÓN_LABORAL"].COUNT()
```
| Municipio| # Beneficiarios|
| ----- | ---- |
| BARANOA | 11 |          
|BARRANQUILLA | 2256 |
|CAMPO DE LA CRUZ  | 2 |
|CANDELARIA | 2 |
|GALAPA | 13 |
|JUAN DE ACOSTA | 1 |
|LURUACO | 4 |
|MALAMBO | 15 |
|MANATÍ | 1 |
|PALMAR DE VARELA | 3 |
|POLONUEVO | 4 |
|PONEDERA | 3 |
|PUERTO COLOMBIA | 15 |
|SABANAGRANDE | 6 |
|SABANALARGA | 8 |
|SANTO TOMÁS | 12 |
|SINCELEJO | 1 |
|SOLEDAD | 225 |
|TUBARÁ | 1 |
|USIACURÍ | 2 |




#   CONCLUSIÓN 

Finalmente, luego de realizar el refinamiento de la información y  terminado el análisis se puede demostrar que “Ruta Empleabilidad” del departamento del atlántico ayudo en menor medida a mitigar el impacto que tuvo la pandemia en el desempleo, beneficiando a `2569` beneficiarios en total a lo largo de los dos años (2020-2021), también se logra identificar que el numero de personas de sexo femenino contratado fue mayor al sexo masculino teniendo 1396 y 1191 personas contratadas respectivamente, adicionalmente se evidencia que mayoritariamente la población contratada este en el rango de edad de `18 – 28` años de edad siendo `1844` el número de contratados representando el `71%` de toda la población atendida a lo largo de estos dos años.

También se puede observar a través de los resultados que barranquilla al ser la capital fue el lugar donde mas personas accedieron a un empleo seguido del municipio de soledad y malambo .








Contratación por nivel educativo 

# BIBLIOGRAFÍA




### Artículo sobre crisis económica debido al covid - Universidad del bosque

https://www.unbosque.edu.co/centro-informacion/noticias/como-afecta-la-crisis-del-covid-19-la-economia-colombiana	


### Fuente de base de datos - datos.gov.co

https://www.datos.gov.co/Econom-a-y-Finanzas/Ruta-Empleabilidad-Secretar-a-de-Desarrollo-Econ-m/qh5k-tnjm	

