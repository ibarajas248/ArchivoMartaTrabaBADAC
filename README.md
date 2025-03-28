#  Aplicación Streamlit - Archivo Marta Traba

Esta aplicación de Streamlit permite visualizar y filtrar documentos del Archivo Marta Traba a partir de un archivo Excel.

##  Características
- Carga y visualización de documentos desde un archivo Excel (`mt.xlsx`).
- Filtros avanzados por:
  - **Código BADAC**
  - **Palabra clave** (en el título o descripción)
  - **Autor**
  - **Tipo documental**
  - **Tema**
- Visualización de documentos en un diseño tipo "card" con:
  - Imagen asociada al documento
  - Detalles del documento (código, título, descripción, autor, fechas, técnica, observaciones, etc.)
  
##  Requisitos

### Instalación de dependencias
Asegúrate de tener instalado Python y luego ejecuta:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye:

```txt
streamlit
pandas
openpyxl
```

##  Ejecución de la Aplicación
Para ejecutar la aplicación, usa el siguiente comando:

```bash
streamlit run app.py
```

##  Estructura del Archivo Excel (`mt.xlsx`)
El archivo Excel debe contener las siguientes columnas:

- `Código`
- `Código BADAC`
- `Imagen`
- `Caja`
- `Expediente`
- `Documento`
- `Título`
- `Descripción`
- `Autor`
- `Fecha inicial`
- `Fecha final`
- `Medio/técnica`
- `Observaciones`
- `Tipo documental`
- `Tema`
- `Archivo digitalizado en alta`

Si alguna de estas columnas falta, la aplicación mostrará una advertencia.

## Visualización
Cada documento se muestra en un diseño tipo "card" que incluye:
- Imagen del documento (si está disponible en BADAC)
- Detalles clave como título, autor, descripción, fechas y observaciones.

## Búsqueda y Filtrado
Puedes filtrar documentos utilizando la barra lateral:
- **Búsqueda por código BADAC**: Filtra documentos específicos.
- **Palabras clave**: Filtra por título o descripción.
- **Filtros adicionales**: Autor, tipo documental y tema.

##  Errores Comunes
- **Archivo no encontrado**: Verifica que `mt.xlsx` esté en el directorio correcto.
- **Error de lectura**: Confirma que el archivo tiene la estructura esperada.

##  Notas
Esta aplicación está diseñada para facilitar la exploración del Archivo Marta Traba y mejorar el acceso a los documentos digitalizados.



