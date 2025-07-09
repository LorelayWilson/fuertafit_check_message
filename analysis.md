# Análisis técnico
Este análisis describe las decisiones técnicas tomadas en la implementación de la función `can_form_message`, evaluando eficiencia, estructura, escalabilidad y cobertura de casos límite.

# Rendimiento

### Complejidad Temporal (CPU)
> La complejidad temporal mide cuántas operaciones realiza el algoritmo en función del tamaño del input.

La función trabaja con dos cadenas: `message` (longitud m) y `chest` (longitud n). Las operaciones se distribuyen así:
- **Preprocesamiento (limpieza de espacios):** O(n + m)  
- **Conteo de caracteres del cofre (con `Counter`):** O(n)
- **Recorrido y verificación del mensaje:** O(m)

No se utilizan bucles anidados ni estructuras costosas. Gracias al uso de `Counter`, cada acceso o modificación de frecuencia es O(1), lo que permite una validación eficiente.

> **Complejidad total:** `O(m + n)`  
> Rendimiento lineal respecto al tamaño de las entradas. Escalable incluso con textos extensos.

### Complejidad Espacial (Memoria)

> Este análisis se enfoca en cuánta memoria adicional utiliza el algoritmo (sin contar los inputs).

La función usa:

- Dos `Counter`: uno para el cofre (`chest_counter`) y otro para letras faltantes (`missing_counter`).
- Variables temporales (`message`, `chest` limpios, y el mensaje de salida).

> **Complejidad total:** `O(k)`, donde `k` es el número de caracteres distintos en `message + chest`.  
> En la práctica, `k` es bajo (alfabeto limitado), por lo que el consumo de memoria es mínimo.

### Escalabilidad

> Evaluamos cómo se comporta el algoritmo frente a entradas grandes

Gracias a su complejidad lineal, la función escala correctamente incluso con cadenas de miles de caracteres. Esto fue verificado en los tests (test_long_inputs) repitiendo frases extensas y demostrando estabilidad en rendimiento y exactitud.

# Decisiones de Diseño

### Estructuras de datos elegidas

Se utilizó `collections.Counter` por ser una estructura especializada para conteo de frecuencias en tiempo lineal, con operaciones de lectura, escritura y decremento en tiempo constante (`O(1)`). Esta decisión permite mantener el código limpio y eficiente, sin comprometer el rendimiento.

**¿Por qué no `dict`?**  
Aunque funcionalmente similar, un diccionario manual requiere inicialización y lógica adicional (`if key in dict`), lo que haría el código más verboso y propenso a errores.

La normalización previa con `str.replace()` y `str.lower()` asegura insensibilidad a mayúsculas y espacios, simplificando la lógica general.

### Trade-offs considerados

En esta implementación se tomaron decisiones conscientes para equilibrar rendimiento, claridad y funcionalidad. A continuación se detallan los principales trade-offs evaluados:

| Factor en conflicto              | Decisión tomada                                                    | Lo que se gana                                       | Lo que se sacrifica                                  |
|----------------------------------|---------------------------------------------------------------------|------------------------------------------------------|-------------------------------------------------------|
| Tiempo de ejecución vs. Memoria | Uso de `Counter` para conteo rápido                                 | Operaciones en O(1), código limpio y eficiente       | Ligero uso extra de memoria (estructura adicional)    |
| Simplicidad vs. Flexibilidad     | No se normalizan acentos ni caracteres Unicode equivalentes         | Lógica más simple, sin dependencias externas         | Comparación literal: `á ≠ a`, `ñ ≠ n`                 |
| Legibilidad vs. Control detallado| Mensaje explicativo generado dinámicamente                          | Facilita entender por qué falla una comprobación     | Añade complejidad a la lógica del return              |
| Completitud vs. Abstracción      | Se ignoraron optimizaciones menores como ordenar el `message`       | Menor tiempo de desarrollo, sin afectar Big O        | Posibles mejoras en ejecución con ciertos inputs      |

Estas decisiones se tomaron considerando que el objetivo principal era crear una función robusta, clara, eficiente y fácil de mantener, sin sobreoptimizar para casos poco comunes.


### Casos extremos manejados

La función está diseñada para comportarse correctamente en los siguientes escenarios límite:

- Mensajes vacíos → se consideran válidos.
- Cofres vacíos → el mensaje no puede formarse.
- Insensibilidad a mayúsculas (`A` = `a`).
- Ignora espacios en ambas cadenas.
- Soporte para letras tildadas, Unicode, números y símbolos.
- Manejo correcto de letras repetidas.
- Soporte para entradas largas, como frases repetidas cientos de veces.

Estas validaciones se reflejan en la suite de pruebas unitarias incluidas.

# Reflexión

### Fortalezas de la solución
- Eficiente en tiempo y memoria.
- Claridad y legibilidad en el código.
- Cobertura completa de casos límite.
- No depende de librerías externas.
- Fácil de mantener y extender.

### Limitaciones identificadas

1. **Comparación literal de caracteres:**
   La función trata cada carácter como único. No considera equivalencias como `á` ≠ `a` o `ñ` ≠ `n`, lo que puede ser problemático en idiomas con tildes o variantes Unicode.

2. **Falta de tolerancia a errores tipográficos:**  
   No se admiten pequeñas variaciones como letras parecidas o números que se parezcan a letras (`3` en vez de `E`, etc.). La validación es estrictamente literal.

3. **Mensajes de error extensos:**  
   Si faltan muchos caracteres, el mensaje explicativo puede hacerse muy largo (`Faltan caracteres: A(5), B(3), C(2), ...`), dificultando la lectura en algunos contextos.

4. **Sin opciones de configuración:**  
   No hay forma de configurar comportamientos como sensibilidad a tildes, distinción entre mayúsculas o símbolos. La lógica está fija y no es parametrizable.

5. **No detecta caracteres invisibles:**  
   Caracteres como espacios duros (`\u00A0`), tabulaciones (`\t`) o saltos de línea (`\n`) no se eliminan ni validan, lo que puede llevar a errores sutiles.

6. **Sin validación anticipada por longitud:**  
   No se hace una verificación rápida para descartar casos obvios (por ejemplo, cuando el mensaje es más largo que el cofre).

### Mejoras futuras posibles
1. **Normalización Unicode:**  
   Usar `unicodedata.normalize()` para tratar equivalencias como `á ≈ a`, mejorando soporte multilingüe.

2. **Resumen del mensaje de error:**  
   Truncar el detalle de letras faltantes si es muy largo, mostrando solo las más relevantes (ej. "Faltan caracteres: A(5), B(3), ... +2 más").

3. **Validaciones preventivas:**  
   Comprobar si `len(message) > len(chest)` para abortar casos imposibles antes del conteo.

4. **Limpieza de caracteres invisibles:**  
   Eliminar espacios duros (`\u00A0`), tabulaciones o saltos de línea que puedan afectar silenciosamente.

5. **Interfaz de usuario o CLI:**  
   Crear una interfaz visual o de consola para permitir probar fácilmente diferentes entradas.

6. **Separación de responsabilidades:**  
   Dividir la lógica en funciones auxiliares (normalización, conteo, validación), facilitando testeo y extensión del código.