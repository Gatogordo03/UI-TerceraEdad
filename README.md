# Documentación de la Interfaz de Usuario para Personas Mayores

## Descripción

Este proyecto es una interfaz de usuario desarrollada en Python utilizando la biblioteca **Kivy**. Está diseñada para personas mayores o personas de la tercera edad, enfocándose en la accesibilidad, en particular ante deficiencias visuales y la facilidad de comprensión de las acciones a realizar en un teléfono.

La interfaz consta de una serie de pantallas simples con iconos y botones grandes, pensados para facilitar la navegación y hacer las funciones más accesibles.

### Funcionalidades principales:
- Pantallas de contacto con botones de fácil acceso.
- Los botones de llamada no tienen funcionalidad por ahora, pero son interactivos.
- El diseño de la interfaz es vertical, optimizando el espacio y asegurando una presentación clara y legible.

## Instalación

Para ejecutar esta interfaz de usuario, necesitarás instalar las siguientes bibliotecas:

1. **Kivy**: Biblioteca principal para la construcción de la interfaz.
   
   Comando de instalación:
   ```bash
   pip install kivy
   ```
2. **Kivy Garden (para el manejo de gráficos SVG):** Necesaria para el uso de iconos SVG.   
   
   Comando de instalación:
   ```bash
   python -m pip install https://github.com/kivy-garden/graph/archive/master.zip
   ```

## Estructura del Proyecto

- ContactScreen: Pantalla que muestra una lista de contactos con botones para realizar llamadas (sin funcionalidad por el momento).
- Layout Vertical: La interfaz está organizada de manera vertical para facilitar la lectura y la navegación.
- Botones de retroceso: Cada pantalla tiene un botón de "Atrás" que permite volver al menú principal.

## Archivos

`main.py`: Archivo principal que contiene la estructura y configuración del proyecto.

### Ejecución

Para ejecutar el proyecto, simplemente utiliza el siguiente comando:

   ```bash
   python main.py
   ```

Esto ejecutará la aplicación con la interfaz diseñada para personas mayores.

### Notas

Este proyecto está en desarrollo activo. Si bien el botón de llamada aún no tiene una funcionalidad real, se encuentra presente para futuras implementaciones.