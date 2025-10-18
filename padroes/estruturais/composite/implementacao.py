#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementação do Padrão de Projeto Composite."""

from abc import ABC, abstractmethod
from typing import List


class ComponenteSistemaArquivos(ABC):
    """
    A interface Componente declara um método comum para objetos simples e complexos
    da composição. Isso permite que o cliente trate todos os objetos na árvore
    de composição de maneira uniforme.
    """

    @abstractmethod
    def exibir(self, nivel: int = 0):
        """Método que será implementado por folhas e compostos para exibir a estrutura.

        Args:
            nivel (int, optional): O nível de indentação. Defaults to 0.
        """
        pass


class Arquivo(ComponenteSistemaArquivos):
    """
    A classe Folha (Leaf) representa os objetos finais de uma composição.
    Uma folha não pode ter filhos. Ela faz o trabalho real do sistema.
    """

    def __init__(self, nome: str):
        """Inicializa o arquivo com um nome.

        Args:
            nome (str): O nome do arquivo.
        """
        self.nome = nome

    def exibir(self, nivel: int = 0):
        """Exibe o nome do arquivo com indentação para mostrar a hierarquia.

        Args:
            nivel (int, optional): O nível de indentação. Defaults to 0.
        """
        print("  " * nivel + f"- [Arquivo] {self.nome}")


class Pasta(ComponenteSistemaArquivos):
    """
    A classe Composto (Composite) representa os componentes complexos que podem
    ter filhos. Geralmente, os objetos Compostos delegam o trabalho real
    para seus filhos e, em seguida, "somam" o resultado.
    """

    def __init__(self, nome: str):
        """Inicializa a pasta com um nome.

        Args:
            nome (str): O nome da pasta.
        """
        self.nome = nome
        self._filhos: List[ComponenteSistemaArquivos] = []

    def adicionar(self, componente: ComponenteSistemaArquivos) -> None:
        """Adiciona um componente (arquivo ou outra pasta) a esta pasta.

        Args:
            componente (ComponenteSistemaArquivos): O componente a ser adicionado.
        """
        self._filhos.append(componente)

    def remover(self, componente: ComponenteSistemaArquivos) -> None:
        """Remove um componente desta pasta.

        Args:
            componente (ComponenteSistemaArquivos): O componente a ser removido.
        """
        self._filhos.remove(componente)

    def exibir(self, nivel: int = 0):
        """
        Exibe a estrutura da pasta e, em seguida, chama recursivamente o método
        exibir() de cada um de seus filhos. A recursão é a chave aqui.

        Args:
            nivel (int, optional): O nível de indentação. Defaults to 0.
        """
        print("  " * nivel + f"+ [Pasta] {self.nome}/")
        for filho in self._filhos:
            filho.exibir(nivel + 1)
