# Fuertafit SOS Project

Este proyecto ha sido desarrollado como parte de una prueba técnica para **Fuertafit**.  
El objetivo es implementar una función llamada `can_form_message` que determine si es posible formar un mensaje utilizando únicamente los caracteres disponibles en un cofre.

La función debe ignorar los espacios, respetar las cantidades de cada carácter y permitir cualquier tipo de carácter (letras, símbolos, números, letras con tilde, etc.).

El proyecto incluye:
- La función principal (`can_form_message`)
- Tests unitarios cubriendo casos básicos y avanzados
- Un análisis técnico de eficiencia, diseño y decisiones tomadas

## Requisitos
Este proyecto ha sido desarrollado con:

- **Python 3.10 o superior**
- Visual Studio Code

No se requiere instalación de librerías externas.

## Estructura del proyecto

├── src/
│ └── check_message.py # Lógica principal
├── tests/
│ └── test_check_message.py # Pruebas unitarias
├── README.md # Documentación del proyecto
├── analysis.md # Análisis técnico del proyecto
└── .gitignore  # Exclusiones de Git

## Instalación y ejecución

Sigue estos pasos para clonar y ejecutar el proyecto localmente:

### 1. Clona el repositorio y accede al directorio raíz del proyecto:
```bash
git clone https://github.com/LorelayWilson/fuertafit_check_message
cd fuertafit_check_message
```
### 2. Probar la función:
- Asegúrate de estar en el directorio raíz del proyecto.
- Ejecuta el siguiente comando en terminal:
```python
python src/check_message.py
```
> Para usar la función con entradas personalizadas, puedes editar directamente el archivo `check_message.py` o importar la función desde otro script.

## Funcionamiento de la función principal

La función `can_form_message(message: str, chest: str) -> tuple[bool, str]` determina si es posible formar un mensaje utilizando solo los caracteres disponibles en un cofre.  

Devuelve una tupla formada por:
- Un `bool` indicando si el mensaje puede formarse (`True` o `False`)
- Un `str` explicativo con el motivo (éxito o los caracteres que faltan)

### Reglas que aplica:
- Ignora espacios del mensaje y del cofre
- No distingue entre mayúsculas y minúsculas (`a` y `A` se tratan igual)
- No transforma letras con tilde ni símbolos: se usan tal cual están, y tampoco se ignoran los símbolos.
- Respeta la cantidad de letras (no se puede usar más veces una letra de lo que hay en el cofre)
- Si el mensaje está vacío, se considera **válido** (no requiere caracteres)

### Ejemplo de uso:
```python
can_form_message("SOS", "PELIGROSOS")
# Resultado: (True, "Mensaje puede formarse correctamente.")

can_form_message("RESCUEA", "RSCU")
# Resultado: (False, "Faltan caracteres: E(2), A(1)")

can_form_message("", "AA")
# Resultado: (True, "Mensaje vacío: no requiere letras para formarse.")
```

## Tests
El proyecto incluye un conjunto de **pruebas unitarias** escritas con el módulo estándar `unittest`, localizadas en el archivo:
```bash
tests/test_check_message.py
```

### ¿Qué cubren los tests?

- Casos básicos de mensajes posibles e imposibles.
- Ignorar espacios en el mensaje y el cofre.
- Uso de símbolos, números y caracteres Unicode (como ñ, é, etc.).
- Manejo de letras repetidas.
- Casos extremos: mensajes vacíos, cofres vacíos, inputs largos.
- Verificación del mensaje explicativo en la salida.

### Cómo ejecutarlos

1. Asegúrate de estar en el directorio raíz del proyecto.
2. Ejecuta el siguiente comando en terminal:
```bash
  python -m unittest discover tests
```
Esto ejecutará automáticamente todos los tests dentro de la carpeta `tests/`.
> Los tests están diseñados para ejecutarse sin necesidad de librerías externas.

## Autora

**Lorelay Pricop Florescu**  
Graduada en Tecnologías Interactivas y Project Manager con experiencia en .NET, Python, Angular, Azure DevOps, IA y metodologías ágiles.  

🔗 [LinkedIn](https://www.linkedin.com/in/lorelaypricop)  
📧 Contacto: lorelay.pricop@gmail.com

# Notas
> Algunas ideas de validación, estilo y estructura han sido revisadas con ayuda de herramientas de inteligencia artificial (IA), como apoyo para acelerar la documentación y validar casos límite.
