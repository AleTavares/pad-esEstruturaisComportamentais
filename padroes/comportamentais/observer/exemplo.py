from .implementacao import Editor, Assinante

def main():
    """Função principal para demonstrar o uso do padrão Observer."""
    print("--- Padrão Observer ---")

    # Cria o editor (Subject)
    editor_chefe = Editor()

    # Cria os assinantes (Observers)
    leitor1 = Assinante("Ana")
    leitor2 = Assinante("Bruno")
    leitor3 = Assinante("Carla")

    # Inscreve os assinantes no editor
    editor_chefe.adicionar_assinante(leitor1)
    editor_chefe.adicionar_assinante(leitor2)
    editor_chefe.adicionar_assinante(leitor3)

    # Editor publica uma nova notícia, e todos os assinantes são notificados
    editor_chefe.publicar_noticia("Python 3.14 lançado com novos recursos!")

    # Um assinante cancela a inscrição
    editor_chefe.remover_assinante(leitor2)
    print(f"\nEditor: {leitor2.nome} não está mais seguindo.\n")

    # Editor publica outra notícia
    editor_chefe.publicar_noticia("Padrões de Projeto salvam o dia novamente!")

    print("---------------------\n")
