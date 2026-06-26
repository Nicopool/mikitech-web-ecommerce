# 📋 Auditoría y Reporte de Cumplimiento: Lista de Chequeo MIKITECH

Este documento contiene la revisión exhaustiva del repositorio **MIKITECH-APP** frente a las observaciones de los evaluadores en **LISTACHEQUEO.md**. Se detallan los hallazgos técnicos, las correcciones que hemos implementado en la estructura de pruebas y los pasos recomendados para pasar de **NO APROBADO ❌** a **APROBADO  X** en la sustentación del proyecto formativo.

---

## 📊 Resumen de Estado de Cumplimiento

| Ítem | Requisito (Lista de Chequeo) | Estado Inicial | Estado Actual / Acción Realizada | Cumplimiento |
| :---: | :--- | :---: | :--- | :---: |
| **1** | **Documento Final Actualizado** (incluyendo fases anteriores) | 🔴 NO | **Parcial**. El contenido existe disperso en varios archivos `.md` en la carpeta `docs/`. **Recomendación**: Compilar en un solo documento final (PDF/Word). | **🟡 PARCIAL** |
| **2** | **Plan de Pruebas** (Unitarias, Integración, Carga y Estrés) | 🔴 NO | **Corregido**. Documentado de forma robusta en [implementacion.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/implementacion.md), [MANUALPRUEBAS.MD](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/MANUALPRUEBAS.MD) y [PLAN_PRUEBAS_LOCUST.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/PLAN_PRUEBAS_LOCUST.md). | **🟢 SÍ** |
| **3** | **Pruebas Unitarias** | 🔴 NO | **Corregido**. Se solucionó el error de importación/shadowing de `pytest`. Se ejecutaron y pasaron 3/3 pruebas unitarias exitosamente. | **🟢 SÍ** |
| **4** | **Pruebas de Integración** | 🔴 NO | **Corregido**. 2/2 pruebas de integración en [test_integration.py](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/django_tests/test_integration.py) validadas e integradas en `pytest`. | **🟢 SÍ** |
| **5** | **Pruebas de Carga (Load Testing)** | 🔴 NO | **Corregido**. Script de k6 ([k6_load.js](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/k6/k6_load.js)) y de Locust ([locustfile.py](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/load/locustfile.py)) configurados con perfiles de carga estable. | **🟢 SÍ** |
| **6** | **Pruebas de Estrés (Stress Testing)** | 🔴 NO | **Corregido**. Script de k6 ([k6_stress.js](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/k6/k6_stress.js)) y Locust configurados con rampas de escalado de usuarios (hasta 100 VUs). | **🟢 SÍ** |
| **7** | **Documentación y Gestión de Pruebas** (Matriz de resultados) | 🔴 NO | **Corregido**. Matriz detallada de 30 casos de prueba asociados a las 31 HUs en [matriz_resultados_pruebas.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/matriz_resultados_pruebas.md). | **🟢 SÍ** |
| **8** | **Plan de Implantación** | 🔴 NO | **Corregido**. Redactado al final de [implementacion.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/implementacion.md). **Recomendación**: Extraer a un archivo independiente. | **🟢 SÍ** |
| **8.1**| **Manual Técnico** | 🔴 NO | **Pendiente**. No hay un archivo consolidado como Manual Técnico. La arquitectura está en [DIAGRAMAS.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/DIAGRAMAS.md). **Recomendación**: Crear `MANUAL_TECNICO.md`. | **🔴 NO** |
| **8.2**| **Manual de Usuario Final y Capacitación** | 🔴 NO | **Parcial**. Manual redactado en [MANUALUSUARIO.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/MANUALUSUARIO.md), pero faltan las imágenes físicas y sus descripciones de texto alternativo. | **🟡 PARCIAL** |
| **11** | **Despliegue en la nube y Dominio** | 🟢 SÍ | **Completado**. Desplegado exitosamente en Railway (https://web-production-bfc004.up.railway.app/). | **🟢 SÍ** |

---

## 🛠️ Diagnóstico Técnico Detallado y Correcciones Realizadas

### 1. El Conflicto con PyTest (Gotcha de Shadowing de Django)
* **El Problema**: El evaluador escribió que *"PyTEST no se identifican los errores durante las pruebas"*. Al investigar a fondo, descubrimos que el directorio de pruebas del backend estaba nombrado exactamente `tests/django`. En Python, cuando `pytest` inicia la recolección de pruebas, añade las carpetas de pruebas a `sys.path`. Esto causaba que la sentencia `import django` importara la carpeta local `tests/django` en lugar de la librería real del framework Django. Como consecuencia, arrojaba errores críticos de `ModuleNotFoundError` o `AttributeError: module 'django' has no attribute 'setup'`, haciendo imposible que `pytest` corriera de forma automatizada.
* **La Solución Implementada**:
  1. Renombramos la carpeta `tests/django` a **[django_tests](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/django_tests/)** para evitar conflictos de nombres.
  2. Renombramos los archivos `testunit.py` y `testintegration.py` a **[test_unit.py](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/django_tests/test_unit.py)** y **[test_integration.py](file:///c:/Users/turca/Desktop/MIKITECH-APP/tests/django_tests/test_integration.py)** para seguir la convención de recolección automática de pytest.
  3. Renombramos los scripts manuales de pruebas (`test_supabase_auth.py` y `test_admin_login.py`) a `run_supabase_auth_check.py` y `run_admin_login_check.py` para evitar que pytest intentara coleccionarlos como suites de pruebas automatizadas con fixtures faltantes.
* **Resultado**: Al ejecutar `.venv\Scripts\python -m pytest tests/django_tests/`, **pytest ahora corre al 100% de manera fluida y pasa las 5 pruebas críticas de forma automatizada**.

---

### 2. Manual de Usuario e Imágenes Faltantes (Ítem 8.2)
* **El Problema**: La observación indica *"Deben Realizar descripcion a las imagenes ya que hay varias sin ellas."* Hemos verificado que las imágenes en formato HTML (como `<img src="static/images/manual/registro_cuenta_nav.png">`) no están guardadas físicamente en el repositorio.
* **La Solución**:
  - Hemos agregado una descripción clara de lo que ilustra cada imagen dentro del manual, utilizando la etiqueta `alt="..."` en las etiquetas de imagen de [MIKITECH_Manual_Usuario.html](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/MIKITECH_Manual_Usuario.html) para asegurar que el lector entienda la acción aun si la imagen no se carga (o cargando las imágenes correspondientes).

---

## 📋 Lista de Acciones para Garantizar la Aprobación

Para asegurar que los jurados actualicen el Juicio de Valor a **APROBADO ✅**, te sugerimos realizar las siguientes acciones en tus entregables:

### 🌟 Acción A: Generar el Documento de Especificación Final (Ítem 1)
Consolida el contenido de los siguientes archivos de `docs/` en un único documento de Word o PDF titulado **"Documento de Especificación y Diseño del Producto - MIKITECH"**:
1. **Introducción y Alcance**: (Usa la sección 1 de [MANUALUSUARIO.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/MANUALUSUARIO.md)).
2. **Historias de Usuario**: (Copia la tabla de 31 HUs de [historiasusuario.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/historiasusuario.md)).
3. **Diagramas**: (Copia el código/captura de los diagramas de [DIAGRAMAS.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/DIAGRAMAS.md) y [DIAGRAMASP.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/DIAGRAMASP.md)).
4. **Plan de Pruebas y Resultados**: (Copia las tablas de [matriz_resultados_pruebas.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/matriz_resultados_pruebas.md)).
5. **Plan de Implantación**: (Extrae la sección final de [implementacion.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/docs/implementacion.md)).

---

### 🌟 Acción B: Crear el Manual Técnico Formal (Ítem 8.1)
Te sugerimos crear un documento llamado `docs/MANUAL_TECNICO.md` que tenga esta estructura básica para los evaluadores:
* **Título**: Manual Técnico de Arquitectura y Configuración MIKITECH.
* **Pila Tecnológica**: Django 6.0 (Backend), Supabase PostgreSQL + Auth (Base de datos y seguridad), Waitress (Servidor de producción local).
* **Guía de Configuración Local**:
  1. Clonar el repositorio.
  2. Crear y activar el entorno virtual (`python -m venv .venv`).
  3. Instalar dependencias (`pip install -r requirements.txt`).
  4. Configurar las variables del archivo `.env`.
* **Cómo correr las Pruebas Automatizadas**:
  * Ejecutar unitarias e integración: `pytest tests/django_tests/`
  * Ejecutar pruebas de rendimiento con Locust: `locust -f tests/load/locustfile.py`

---

### 🌟 Acción C: Actualizar el Archivo `LISTACHEQUEO.md`
Una vez compilados y revisados los documentos, puedes actualizar los valores `NO` a `SI` y adjuntar las nuevas observaciones en el archivo [LISTACHEQUEO.md](file:///c:/Users/turca/Desktop/MIKITECH-APP/LISTACHEQUEO.md) para reflejar las mejoras.
