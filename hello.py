#! /usr/bin/env python3
"""Hello World Multi Linguas.

Dependedo da lingua configurada no ambiente o pragramas exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR
Ou informe atraves do CLI argument `--lang`

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Paulo Cesar"
__license__ = "Unlicense"


import os
import sys

arguments = {"lang": None, "count": 1}
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Chose a language:")

current_language = current_language[:5]    

msg = {
    "en_US": "Hello, world!!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_EP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}
    
print(
    msg[current_language] * int(arguments["count"])
    )

