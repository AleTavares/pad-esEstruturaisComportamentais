#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Script principal para executar todos os exemplos de Padrões de Projeto."""

import importlib
import os


def run_all_examples():
    """Encontra e executa a função 'main' de cada arquivo 'exemplo.py' no projeto."""
    
    # Define a ordem de execução para uma apresentação lógica
    patterns_order = [
        # Estruturais
        'estruturais.adapter',
        'estruturais.composite',
        'estruturais.decorator',
        'estruturais.facade',
        # Comportamentais
        'comportamentais.observer',
        'comportamentais.strategy',
    ]

    base_path = 'padroes'

    for pattern_path in patterns_order:
        try:
            module_name = f"padroes.{pattern_path}.exemplo"
            
            # Extrai o nome do padrão para o cabeçalho
            pattern_name = pattern_path.split('.')[-1].upper()
            
            print(f"\n{'='*15} Padrão {pattern_name} {'='*15}\n")
            
            # Importa o módulo dinamicamente
            example_module = importlib.import_module(module_name)
            
            # Executa a função main() do módulo
            if hasattr(example_module, 'main'):
                example_module.main()
            else:
                print(f"Aviso: O módulo {module_name} não possui uma função 'main'.")

        except ImportError as e:
            print(f"Erro ao importar o módulo {module_name}: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao executar o exemplo para {pattern_name}: {e}")

if __name__ == "__main__":
    run_all_examples()
