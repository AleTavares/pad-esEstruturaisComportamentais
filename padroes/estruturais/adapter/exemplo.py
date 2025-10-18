#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Arquivo de exemplo para demonstrar o uso do Padrão Adapter."""

from .implementacao import APIAntigaEnvio, AdaptadorEnvio, NovaAPIEnvio


def client_code(api: NovaAPIEnvio, dados: dict):
    """
    O código cliente que interage com a API através da interface moderna (NovaAPIEnvio).
    Ele não sabe (e não precisa saber) se está usando a API nova de verdade ou um adaptador.
    """
    print("\n(Código Cliente) Utilizando a API para enviar dados...")
    api.enviar_dados(dados)


def main():
    """Função principal que executa a demonstração do padrão Adapter."""
    # Dados que o nosso sistema moderno gera
    dados_modernos = {
        "usuario": "Alice",
        "mensagem": "Olá, mundo!",
        "timestamp": 1678886400
    }

    # 1. O sistema legado que não podemos modificar
    api_antiga = APIAntigaEnvio()
    print("API Antiga instanciada.")
    # Se tentássemos usar a API antiga diretamente no nosso código cliente, daria erro:
    # client_code(api_antiga, dados_modernos) # -> AttributeError

    # 2. Criamos um adaptador, envolvendo a API antiga
    adaptador = AdaptadorEnvio(api_antiga)
    print("Adaptador envolvendo a API Antiga foi criado.")

    # 3. O código cliente usa o adaptador como se fosse a API nova, sem perceber a diferença.
    client_code(adaptador, dados_modernos)


if __name__ == "__main__":
    main()
