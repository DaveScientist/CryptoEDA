# CryptoEDA
## EDA_Kapital&Markets_Cryptos

<img src="https://d3uir0eo9qeeuq.cloudfront.net/blog/wp-content/uploads/2017/01/19122144/bitcoin-768x461.jpg" alt="drawing" width="600"/>

### INTRODUCCIÓN

Vamos a realizar un estudio de cómo la divisa que está en boca de todos a día de hoy, se ha convertido en aquella moneda que se ha multiplicado por 70 veces su valor desbancando las ya cotidianas y aburridas divisas reguladas.

En dicho estudio, además, contaremos con una Start-Up ficticia, Kapital & Markets donde analizaremos las ventajas y desventajas de que ésta y otras divisas estén en un mercado descentralizado y no regulado. Hallaremos un plan que no conoce todo el mundo para saber cómo sacar rentabilidad 100% fiable y sin trucos.

Hablaremos de minería de datos y de cómo es posible que con un buen equipo informático y buenos procesadores,tarjetas gráficas, etc... la gente pueda obtener "porciones" de éstas divisas virtuales.

Comprobaremos cómo se han comportado las principales divisas a lo largo de estos últimos 10 años, viendo un modus operandi en la mayoría de ellas y realizaremos un análisis técnico para darnos cuenta de que finalmente y en diferente proporción, acaban teniendo un apartado gráfico parecido.

Las Criptomonedas principales que vamos a estudiar son: 

**- Bitcoin**
**- Cardano**
**- Ethereum**
**- BNB**

Estudiaremos a través de este análisis gráfico, mencionado antes, un indicador fundamental para comprobar los comportamientos al alza y a la baja que sufre una moneda. Lo llamaremos Media Móvil y veremos para qué sirve.

Comentaremos qué son las ICO (Initial Coin Offering) y aquí precisamente es cuando entra en escena nuestra empresa llamada Kapital & Markets que nos va a hacer ganar mucho dinero con su maravilloso asesoramiento y ventajas de ser un cliente suyo.

El notebook es el fichero principal del proyecto. En él, hacemos algunas de las transformaciones menores. El resto de las transformaciones y la realización de los gráficos las vamos guardando en diferentes ficheros (.py).


### ÍNDICE
1. [DECLARACIÓN DE LIBRERÍAS](#DECLARACION_DE_LIBRERIAS)
2. [LECTURA DEL FICHERO](#LECTURA_DEL_FICHERO)
3. [CRIPTOMONEDAS PRINCIPALES](#CRIPTOMONEDAS_PRINCIPALES)
4. [FILTRO DE CRIPTOMONEDAS](#FILTRO_DE_CRIPTOMONEDAS)
5. [HISTOGRAMAS DE CRIPTOMONEDAS PRINCIPALES](#HISTOGRAMAS_DE_CRIPTOMONEDAS_PRINCIPALES)
6. [DATOS EN PANDAS](#DATOS_EN_PANDAS)
7. [COMPROBACIÓN DE CORRELACIONES](#COMPROBACIÓN_DE_CORRELACIONES)
8. [MEDIAS MÓVILES](#MEDIAS_MÓVILES)
9. [ICO (INITIAL COIN OFFERING)](#ICO_INITIAL_COIN_OFFERING)
10. [OBTENCIÓN DE INFORMACIÓN E HIPÓTESIS FINAL CON SU CONCLUSIÓN](#OBTENCIÓN_DE_INFORMACIÓN_E_HIPÓTESIS_FINAL_CON_SU_CONCLUSIÓN)



### 1. DECLARACIÓN DE LIBRERíAS <a id='DECLARACION_DE_LIBRERIAS'></a>

Declaración de todas las librerías que se han utilizado para limpiar los datos y dibujar los gráficos que nos han ayudado a la realización del estudio, además de importar las funciones que hemos creado y los datos de los que hemos hablado anteriormente.

Tendremos que importar y hacer un **!pip install** de las siguientes librerías:

**- pandas**
**- requests**
**- csv**
**- matplotlib.pyplot**
**- yfinance**
**- investpy**


### 2. LECTURA DEL FICHERO <a id='LECTURA_DEL_FICHERO'></a>

Abrimos el notebook principal **PROYECTO_EDA_CRIPTOS.ipynb** en el que se encuentra todo nuestro código desde donde vamos a llamar a las distintas funciones y librerías que hemos utilizado.



### 3. CRIPTOMONEDAS PRINCIPALES <a id='CRIPTOMONEDAS_PRINCIPALES'></a>

Dibujo de los gráficos de las criptomonedas que vamos a comparar y visualizar a través de la librería matplotlib.

Introduciremos la función **obtener_velas** y **obtener_velas_inicio** para poder comprobar cada uno de los gráficos en ticks de 1 día en diferentes gráficas.


### 4. FILTRO DE CRIPTOMONEDAS <a id='FILTRO_DE_CRIPTOMONEDAS'></a>

Filtraremos nuestras criptomonedas a través de la siguiente variable: **cryptocurrencies = ['BNB-USD','BTC-USD', 'ETH-USD', 'ADA-USD']** y a continuación filtraremos la fecha de inicio y final para comprobar rangos de fecha distintos para realizar un análisis técnico de cada criptomoneda **data = yf.download(cryptocurrencies, start='2020-01-01',end='2022-03-01') data.info()**. 


### 5. HISTOGRAMAS DE CRIPTOMONEDAS PRINCIPALES <a id='HISTOGRAMAS_DE_CRIPTOMONEDAS_PRINCIPALES'></a>

Una vez filtradas las criptomonedas que deseamos visualizar, las introduciremos en los histogramas a través de **Plotly**.

Las llamaremos con el siguiente formato, por ejemplo: **axs[0,0].hist(returns['BTC-USD'], bins=50, range=(-0.2, 0.2))**


### 6. DATOS EN PANDAS <a id='DATOS_EN_PANDAS'></a>

Con todos los datos preparados para tratar, en este apartado se realizan los gráficos comparativos de los datos del volumen, precio inicial, precio al cierre y máximo y mínimo precio del día. 


### 7. COMPROBACIÓN DE CORRELACIONES <a id='COMPROBACION_DE_CORRELACIONES'></a>

En este apartado se realizan los estudios de correlación de las principales criptomonedas que hemos elegido.

Utilizaremos **returns.corr()** para comprobar qué tipo de correlación encontramos.


### 8. MEDIAS MÓVILES <a id='MEDIAS_MÓVILES'></a>

Comprobaremos con un indicador de análisis técnico que personalmente me gusta bastante y se puede configurar con diferentes variables que serían los días de la media móvil que se quiera implementar en el gráfico.

Llamaríamos a la media móvil de 50 días en el notebook de la siguiente manera: 

**MA50 = adj_close.rolling(50).mean()**

**axs[0,1].plot(adj_close['BTC-USD'], label= 'closing')**
**axs[0,1].plot(MA50['BTC-USD'], label= 'MA50')**
**axs[0,1].set_title('BTC')**
**axs[0,1].legend()**


### 9. ICO (INITIAL COIN OFFERING) <a id='ICO_INITIAL_COIN_OFFERING'></a>

Aquí expondremos como podremos obtener rentabilidad con criptomonedas poco comunes y comprobaremos en un análisis técnico exhaustivo que todas las criptos, en el momento de su salida en la fase de la ICO a través de Tokens, se pueden alcanzar rentabilidades por encima del 500% en muchos casos.

Pondremos ejemplos de las siguientes Criptomonedas:

**- AVA**
**- GALA**



### 10. OBTENCIÓN DE INFORMACIÓN E HIPÓTESIS FINAL CON SU CONCLUSIÓN <a id='OBTENCIÓN_DE_INFORMACIÓN_E_HIPÓTESIS_FINAL_CON_SU_CONCLUSIÓN'></a>

Nuestra hipótesis fundamental es realmente preguntarnos cómo es posible que haya tanta volatilidad en el mercado de las criptomonedas cuando el volumen en los últimos 5 años se ha disparado y aumentado casi un 1000%. Aún así vemos caídas notables,  todas precedidas por factores fundamentales que hacen que el mercado de las Criptos estén también relacionadas por el entorno macro y por las diferentes economías políticas.


<img src="https://i.pinimg.com/originals/d5/18/05/d51805b6101cbae3dbcdea213caf5c3d.jpg" alt="drawing" width="600"/>
