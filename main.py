
import streamlit as st
import pandas as pd
import openpyxl


# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .card {
        background: linear-gradient(135deg, #4A90E2, #007AFF);
        color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
    }
    .card:hover {
        transform: scale(1.02);
    }
    .card img {
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.5);
        transition: opacity 0.3s;
    }
    .card img:hover {
        opacity: 0.9;
    }
    .card h3 {
        font-size: 20px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .card p {
        font-size: 14px;
        margin: 5px 0;
        color: #E6E6E6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📄 Archivo Marta Traba")

# Cargar archivo Excel
archivo = "mt.xlsx"

try:
    df = pd.read_excel(archivo)

    # Verificar columnas disponibles
    columnas_requeridas = [
        "Código", "Código BADAC", "Imagen", "Caja", "Expediente", "Documento",
        "Título", "Descripción", "Autor", "Fecha inicial", "Fecha final",
        "Medio/técnica", "Observaciones", "Tipo documental", "Tema", "Archivo digitalizado en alta"
    ]

    columnas_faltantes = [col for col in columnas_requeridas if col not in df.columns]

    if columnas_faltantes:
        st.warning(f"")

    # Sidebar para filtros
    st.sidebar.header("🔍 Filtros de búsqueda")

    # Buscar por Código BADAC
    codigo_filtro = st.sidebar.text_input("Buscar por Código BADAC") if "Código BADAC" in df.columns else None

    # Filtro de palabra clave
    palabra_clave = st.sidebar.text_input("🔎 Buscar por palabra clave (Título o Descripción)")

    # Multiselección en filtros
    autor_filtro = st.sidebar.multiselect(
        "Filtrar por Autor",
        options=df["Autor"].dropna().unique() if "Autor" in df.columns else []
    )
    tipo_doc_filtro = st.sidebar.multiselect(
        "Filtrar por Tipo Documental",
        options=df["Tipo documental"].dropna().unique() if "Tipo documental" in df.columns else []
    )
    tema_filtro = st.sidebar.multiselect(
        "Filtrar por Tema",
        options=df["Tema"].dropna().unique() if "Tema" in df.columns else []
    )

    # Aplicar filtros
    df_filtrado = df.copy()
    if codigo_filtro:
        df_filtrado = df_filtrado[
            df_filtrado["Código BADAC"].astype(str).str.contains(codigo_filtro, case=False, na=False)
        ]

    # Aplicar filtro de palabra clave en "Título" y "Descripción"
    if palabra_clave:
        df_filtrado = df_filtrado[
            df_filtrado["Título"].astype(str).str.contains(palabra_clave, case=False, na=False) |
            df_filtrado["Descripción"].astype(str).str.contains(palabra_clave, case=False, na=False)
            ]

    if autor_filtro:
        df_filtrado = df_filtrado[df_filtrado["Autor"].isin(autor_filtro)]
    if tipo_doc_filtro:
        df_filtrado = df_filtrado[df_filtrado["Tipo documental"].isin(tipo_doc_filtro)]
    if tema_filtro:
        df_filtrado = df_filtrado[df_filtrado["Tema"].isin(tema_filtro)]

    st.write(f"📌 Mostrando {len(df_filtrado)} resultados")

    # Mostrar datos en formato CardView
    for _, row in df_filtrado.iterrows():
        codigo = str(row.get("Código BADAC", ""))
        imagen_url = f"https://badac.uniandes.edu.co/files/lt_mt/{codigo}.jpg" if codigo else ""

        st.markdown(
            f"""
            <div class="card">
                <div style="display: flex; align-items: center;">
                    <div style="flex: 1; text-align: center;">
                        {'<img src="' + imagen_url + '" width="120">' if codigo else '<p>No hay imagen disponible</p>'}
                    </div>
                    <div style="flex: 3; padding-left: 15px;">
                        <h3>{row.get("Título", "Título no disponible")}</h3>
                        <p><strong>Código:</strong> {row.get("Código", "No disponible")}</p>
                        <p><strong>Código BADAC:</strong> {codigo}</p>
                        <p><strong>Descripción:</strong> {row.get("Descripción", "Sin descripción")}</p>
                        <p><strong>Autor:</strong> {row.get("Autor", "Desconocido")}</p>
                        <p><strong>Fecha:</strong> {row.get("Fecha inicial", "No disponible")} - {row.get("Fecha final", "No disponible")}</p>
                        <p><strong>Medio/Técnica:</strong> {row.get("Medio/técnica", "No especificado")}</p>
                        <p><strong>Observaciones:</strong> {row.get("Observaciones", "Sin observaciones")}</p>
                        <p><strong>Tipo documental:</strong> {row.get("Tipo documental", "No definido")}</p>
                        <p><strong>Tema:</strong> {row.get("Tema", "No especificado")}</p>
                        <p><strong>Archivo digitalizado en alta:</strong> {row.get("Archivo digitalizado en alta", "No disponible")}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


except FileNotFoundError:
    st.error(f"❌ No se encontró el archivo '{archivo}'. Verifica que está en el directorio correcto.")
except Exception as e:
    st.error(f"⚠️ Error al cargar el archivo: {e}")
