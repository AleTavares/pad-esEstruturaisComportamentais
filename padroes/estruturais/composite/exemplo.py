#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Arquivo de exemplo para demonstrar o uso do Padrão Composite."""

from .implementacao import Pasta, Arquivo


def main():
    """Função principal que monta e exibe uma estrutura de sistema de arquivos."""

    print("Criando uma estrutura de sistema de arquivos...")

    # Criando a pasta raiz
    raiz = Pasta("home")

    # Criando subpastas
    documentos = Pasta("Documentos")
    fotos = Pasta("Fotos")

    # Adicionando subpastas à raiz
    raiz.adicionar(documentos)
    raiz.adicionar(fotos)

    # Criando arquivos (folhas)
    arquivo_relatorio = Arquivo("relatorio_final.docx")
    arquivo_tese = Arquivo("tese.pdf")
    foto_ferias = Arquivo("ferias_2024.jpg")
    foto_familia = Arquivo("familia.png")

    # Adicionando arquivos às pastas
    documentos.adicionar(arquivo_relatorio)
    documentos.adicionar(arquivo_tese)
    fotos.adicionar(foto_ferias)
    fotos.adicionar(foto_familia)

    # Criando uma sub-subpasta
    trabalhos_faculdade = Pasta("Faculdade")
    documentos.adicionar(trabalhos_faculdade)
    trabalhos_faculdade.adicionar(Arquivo("eng_software_patterns.pdf"))

    # O código cliente pode agora tratar toda a estrutura de forma uniforme.
    # Ele não precisa saber se está lidando com um arquivo ou uma pasta.
    print("\nExibindo a estrutura completa a partir da raiz:")
    raiz.exibir()

    print("\nExibindo a estrutura a partir de uma subpasta (Documentos):")
    documentos.exibir()


if __name__ == "__main__":
    main()
