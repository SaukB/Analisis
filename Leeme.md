# PLANTEAMIENTO DEL PROBLEMA 	:kaaba:
 


La empleabilidad en el departamento del atlántico ha disminuido durante el periodo en pandemia que ha afectado diferentes campos como lo es la contratación de personal practicante egresado de instituciones educativas, así como la vinculación de personas que se desempeña en campos laborales de manera independientes con experiencia, pero con carencias de estudios certificados.
A raíz de esta causa el desempleo aumento en esta población que en la actualidad no cuentan con ingresos fijos mensuales para su sustento.

El problema es el aumento del desempleo en la población en los municipios del departamento del atlántico, mediante este trabajo se busca hallar el número de personas beneficiarias que pudieron acceder a su primer empleo.



# PREGUNTA PROBLEMA :grey_question:	



¿cómo se vieron beneficiados los municipios del departamento del atlántico durante el periodo en pandemia por la ruta de empleabilidad?	





# Objetivo general.  :bookmark_tabs:	


Evaluar el impacto que tuvo la obtención del primer empleo en el periodo de pandemia en el departamento del atlántico en la población egresada de las diferentes instituciones educativas y la población que transita del empleo informal al empleo formal, durante los periodos de tiempo que comprenden desde el 2020 hasta la actualidad teniendo como ultimo registro el mes de enero del presente año (2022).



# Objetivo específico.  :dart:	




•	Obtener la base de datos ofrecida por datos.gov para iniciar el análisis de datos 

•	Refinar la información para hallar la población de estudio (primer empleo).

•	Analizar cuál fue el impacto de contratación de la población beneficiaria teniendo en cuenta la edad, el sexo y el nivel educativo de la muestra seleccionada.

•	Calcular el nivel de acceso a la estrategia y cuál fue el mayor índice de porcentaje de contratación por municipio.

•	Comparar los resultados obtenidos de la contratación en los años 2020 y 2021 para determinar el balance en la cantidad de beneficiarios atendidos por municipios.

•	Implementar graficas para representar los periodos de años, características de la población y lugar de residencia.



# RESULTADO.  :green_book:	



**CARACTERÍSTICAS Y ORIGEN DE LA BASE DE DATOS.**

Fuente de la información: www.datos.gov.co

Datos ofrecidos por : Área o dependencia	Secretaría de Desarrollo Económico, Oficina de Inclusión y Desarrollo productivo
Nombre de la Entidad	:	Alcaldía Distrital de Barranquilla, Distrito Especial, Industrial y Portuario
Departamento : Atlántico
Sector : Función Pública
Categoría :	Economía y Finanzas
Ultima Actualización	: 19 de enero de 2022
Responsable de veracidad 	: Alcaldía Distrital de Barranquilla.


![1](https://user-images.githubusercontent.com/59390917/157063913-4738c357-c48b-4013-a81d-773c6d6230fd.PNG)

**Lenguaje de programación utilizado.**   :computer:	

Python  :snake:	

**Librerías utilizadas**  :books:	
```
numpy
pandas
matplotlib
seaborn
```
# METODOLOGIA.

**Paso 1:**  Obtener la base de datos ofrecida por datos.gov para iniciar el análisis de datos.

Para obtener la base de datos se ingresa desde un navegador y se ingresa el siguiente enlace https://bit.ly/3MFHABk se exporta la base de datos seleccionando el botón de exportar y a continuación saldrá un menú para escoger el formato en nuestro caso escogemos el formato csv.

**Paso 2:**  Refinar la información para hallar la población de estudio (primer empleo).

Inicialmente se crea un dataframe donde vamos a guardar la base datos que obtuvimos anteriormente , a continuación, se filtra la información que esta tiene para hallar la población la cual va a ser nuestro enfoque de estudio.

creamos dataframe donde copiamos la base de datos obtenida en formato csv
```
data = pd.read_csv('empleo.csv')
```

se crea segundo dataframe donde está la información ya filtrada 
```
ndata=data[data['Situación Laboral']=='Primer Empleo']
```
se renombran los encabezados de las columnas para mejorar su llamado al momento de analizar

```
mdatos =ndata.rename (columns={
    "Tipo Documento" :"Tipo_Documento",
    "Canal de Registro":"Canal_Registro",
    "Edad":"Edad",
    'Género': 'Genero',
    "Nivel de Estudio": "Nivel_Estudio",
    'Título Homologado' :'Titulo_Homologado',
    'Ciudad de Residencia':'Ciudad_Residencia',
    'Fecha Registro':'Fecha_Registro',
    'Programa de Gobierno':'Programa_Gobierno',
    'Condiciones Especiales':'Condiciones_Especiales',
    'Situación Laboral':'Situación_Laboral',
    'Fecha Actualización':'Fecha_Actualizacion',
    'Zona':'Zona',
    'Mes':'Mes',
    'Año':"anio",
    'Punto Atención':'Punto_Atencion',
    'Rango Edad':'Rango_Edad'
})
```

se procede hacer separacion por años y guardarla de manera individual.

```
anio2021=mdatos[mdatos['anio']=="2,021"]
anio2020=mdatos[mdatos['anio']=="2,020"]
```



# BIBLIOGRAFÍA. :pencil:

**Artículo sobre ley del primer empleo en Colombia - Noticias RCN**

https://www.noticiasrcn.com/economia/ley-del-primer-empleo-puntos-clave-en-el-proceso-de-reactivacion-378606


**Artículo sobre crisis económica debido al COVID - Universidad del bosque**

https://www.unbosque.edu.co/centro-informacion/noticias/como-afecta-la-crisis-del-covid-19-la-economia-colombiana

**Fuente de base de datos - datos.gov.co**

https://www.datos.gov.co/Econom-a-y-Finanzas/Ruta-Empleabilidad-Secretar-a-de-Desarrollo-Econ-m/qh5k-tnjm



#pip install pandas-alive
https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md
