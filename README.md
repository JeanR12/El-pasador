
# El pasador

## Descripción

El pasador es una herramienta diseñada para intentar eludir restricciones de acceso 403 en páginas web. Implementa diversas técnicas y métodos para evadir dichas restricciones, incluyendo la manipulación de URL y headers, y el uso de proxies SOCKS para mayor anonimato. En pocas palabras, la bestia la aplicacion pa xd.

## Requisitos

- Python 3.x
- Librerías Python: `requests`, `pysocks`

Podes instalar las librerías necesarias usando el pip c: :
```
pip install requests pysocks
```

## Configuración

Recuerde pa que el archivo `config.json` se utiliza para configurar la URL objetivo y el proxy SOCKS si se desea utilizar uno. Ejemplo de `config.json`:
```json
{
    "url": "http://example.com",
    "proxy": "127.0.0.1:9050"
}
```

Si no deseas usar un proxy, deja el campo `proxy` vacío:
```json
{
    "url": "http://example.com",
    "proxy": ""
}
```

## Uso

Para ejecutar el script, simplemente abra una terminal, navegue al directorio donde se encuentra `el_pasador.py` y ejecutelo, igual si tiene preguntas me dice:
```
python el_pasador.py
```

El script intentará varias permutaciones de la URL y diferentes headers para eludir la restricción 403. Los resultados se guardarán en el archivo `el_pasador_results.txt`.

## Funcionalidades adicionales

- **Permutaciones de URL**: Prueba varias modificaciones comunes de la URL para intentar eludir la restricción.
- **Manipulación de headers**: Añade headers comunes que pueden ayudar a evadir restricciones.
- **Soporte para proxy SOCKS**: Permite la configuración de un proxy SOCKS para mayor anonimato.
- **Multihilo**: Utiliza hilos para acelerar las pruebas de bypass.

## Notas

- **Seguridad**: Asegúrate de tener permiso para realizar pruebas de bypass en las URLs objetivo. El uso indebido de esta herramienta puede ser ilegal.
- **Anonimato**: El uso de proxies puede ayudar a proteger tu anonimato, pero no garantiza total seguridad.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request. Estoy encantado de trabajar por y para la comunidad que el conocimiento debe ser libre segun mis criterios


