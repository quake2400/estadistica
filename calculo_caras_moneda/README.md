# Probabilidad de obtener caras en lanzamientos de monedas

Este script en Python calcula la probabilidad de obtener un número específico de caras en una serie de lanzamientos de monedas.

## Cómo ejecutar el script

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

2. Clona este repositorio en tu máquina local o descarga el archivo `app.py`.

3. Abre una terminal o un símbolo del sistema y navega al directorio donde se encuentra el archivo `app.py`.

4. Ejecuta el siguiente comando para ejecutar el script:


5. Sigue las instrucciones en pantalla para ingresar el número de lanzamientos de monedas y la probabilidad de obtener cara en un solo lanzamiento.

## Ejemplo

Supongamos que queremos calcular la probabilidad de obtener exactamente 12 caras en 20 lanzamientos de monedas, con una probabilidad de cara de 0.6.

1. Ejecutamos el script `app.py`:


El script calculará la probabilidad y mostrará el resultado en porcentaje.

## Fórmula

La probabilidad de obtener exactamente \( k \) caras en \( n \) lanzamientos de monedas está dada por la fórmula de la distribución binomial:

\[
P(X = k) = \binom{n}{k} \times p^k \times (1 - p)^{n - k}
\]

Donde:
- \( n \) es el número total de lanzamientos de monedas.
- \( k \) es el número de caras deseadas.
- \( p \) es la probabilidad de obtener cara en un solo lanzamiento.

## Vista matemática de la fórmula

La fórmula matemática se presenta de la siguiente manera:

\[
P(X = k) = \frac{{n!}}{{k! \times (n - k)!}} \times p^k \times (1 - p)^{n - k}
\]

## Notas adicionales

- Este script es para fines educativos y de demostración. No se garantiza su precisión o adecuación para ningún propósito específico.
- Si tienes alguna pregunta o problema, no dudes en [crear un problema](https://github.com/tuusuario/turepositorio/issues) en el repositorio.
