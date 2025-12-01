# ✍️ Registro Dinámico de Eventos con Participantes – Django App

Aplicación web desarrollada en Django para la gestión de eventos y la inscripción de múltiples participantes. Este proyecto fue desarrollado con un enfoque en la correcta implementación de la lógica de formularios complejos y la mejora de la experiencia de usuario (UX) mediante la integración de un framework CSS moderno.

## 🚀 Características y Logros del Proyecto

✅ **Formularios Anidados (Formsets):** Implementación de `inlineformset_factory` para gestionar la creación de un `Evento` y múltiples `Participantes` relacionados en una sola vista.
✅ **Validación de Fechas:** Validación personalizada a nivel de formulario para asegurar que la **Fecha del Evento** siempre sea futura.
✅ **Estructura MVT Limpia:** Separación clara de responsabilidades en Modelos, Vistas y Formularios.
✅ **Estilo Profesional:** Integración de **Bootstrap 5** y `django-widget-tweaks` para un diseño responsivo y usable.
✅ **Gestión de Mensajes:** Uso de `django.contrib.messages` para notificaciones de éxito y error en el registro.
✅ **Navegación Intuitiva:** Redirección de la raíz (`/`) a la lista de eventos.

## 🛠 Tecnologías Utilizadas

* **Python:** 3.x
* **Framework:** Django 5.x
* **Estilización:** Bootstrap 5 (vía CDN)
* **Dependencias Adicionales:** `django-widget-tweaks`
* **Base de Datos:** SQLite3 (por defecto)

## ⚙️ Instalación y Puesta en Marcha

### 1. Clonar e Inicializar

# Clonar el repositorio
git clone [https://github.com/pvidal94/-M6_AE4_ABPRO.git](https://github.com/pvidal94/-M6_AE4_ABPRO.git)
cd -M6_AE4_ABPRO
# Si aún no existe el entorno:
# python -m venv venv

# Activación (usar la sintaxis que funcione en tu terminal):
.\venv\Scripts\activate

#Instalar Dependencias
pip install django django-widget-tweaks

#Aplicar Migraciones
python manage.py makemigrations eventos_app
python manage.py migrate

#Iniciar el Servidor
python manage.py runserver

#Acceder en el Navegador
Abre tu navegador y accede a la raíz del proyecto, el cual te redirigirá automáticamente a la lista: http://127.0.0.1:8000

✨ Funcionalidades
🔹 Vista de Registro (/registro/)
Permite la creación de un Evento.

El botón "➕ Agregar Participante" añade un nuevo formulario al Formset mediante JavaScript.

Si la validación de fecha falla, se muestra un mensaje de error claro en el campo.

🔹 Vista de Lista (/lista/)
Muestra todos los Eventos guardados, iterando sobre la relación para listar todos los Participantes asociados a cada evento.

📌 Autora
Patricia Vidal 🔗 GitHub: @pvidal94

📝 Licencia
Este proyecto fue desarrollado con fines educativos y está disponible para uso personal o académico.
