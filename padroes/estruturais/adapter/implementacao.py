#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementação do Padrão de Projeto Adapter."""


class NovaAPIEnvio:
    """Define a interface moderna e esperada pelo cliente para envio de dados."""

    def enviar_dados(self, dados: dict):
        """Método padrão para enviar dados.
        
        Args:
            dados (dict): Os dados a serem enviados.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.")


class APIAntigaEnvio:
    """Representa uma classe legada ou de terceiros com uma interface incompatível."""

    def enviar_dados_legado(self, dados_antigos: str):
        """Método da API antiga que envia dados em um formato de string.

        Args:
            dados_antigos (str): Os dados a serem enviados.
        """
        print(f"(API Antiga) Enviando dados legados: '{dados_antigos}'")


class AdaptadorEnvio(NovaAPIEnvio):
    """
    Adapta a APIAntigaEnvio para ser compatível com a interface NovaAPIEnvio.
    Este é o coração do padrão Adapter.
    """

    def __init__(self, api_antiga: APIAntigaEnvio):
        """Inicializa o adaptador com uma instância da API antiga.

        Args:
            api_antiga (APIAntigaEnvio): A instância da API antiga.
        """
        self._api_antiga = api_antiga

    def enviar_dados(self, dados: dict):
        """
        Implementa o método da nova interface, traduzindo a chamada para a API antiga.
        
        Args:
            dados (dict): Os dados a serem enviados no formato novo.
        """
        print("(Adaptador) Recebeu dados no formato novo. Traduzindo para o formato antigo...")
        # Lógica de tradução: converte o dicionário para uma string formatada.
        dados_antigos = f"user:{dados.get('usuario')};msg:{dados.get('mensagem')}"
        self._api_antiga.enviar_dados_legado(dados_antigos)
