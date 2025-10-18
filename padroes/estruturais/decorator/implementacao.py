from abc import ABC, abstractmethod

# Componente Abstrato
class Cafe(ABC):
    """Define a interface para os componentes de café."""
    @abstractmethod
    def get_custo(self):
        """Retorna o custo do café."""
        pass

    @abstractmethod
    def get_descricao(self):
        """Retorna a descrição do café."""
        pass

# Componente Concreto
class CafeSimples(Cafe):
    """Componente concreto que representa um café simples."""
    def get_custo(self):
        """Retorna o custo do café simples.

        Returns:
            float: O custo do café.
        """
        return 5.0

    def get_descricao(self):
        """Retorna a descrição do café simples.

        Returns:
            str: A descrição do café.
        """
        return "Café Simples"

# Decorador Abstrato
class DecoradorCafe(Cafe, ABC):
    """Decorador abstrato que envolve um componente de café."""
    def __init__(self, cafe: Cafe):
        """Inicializa o decorador com um componente de café.

        Args:
            cafe (Cafe): O componente de café a ser decorado.
        """
        self._cafe = cafe

    @abstractmethod
    def get_custo(self):
        """Método abstrato para obter o custo."""
        pass

    @abstractmethod
    def get_descricao(self):
        """Método abstrato para obter a descrição."""
        pass

# Decorador Concreto: Leite
class Leite(DecoradorCafe):
    """Decorador concreto que adiciona leite ao café."""
    def get_custo(self):
        """Retorna o custo do café com leite.

        Returns:
            float: O custo do café com leite.
        """
        return self._cafe.get_custo() + 2.0

    def get_descricao(self):
        """Retorna a descrição do café com leite.

        Returns:
            str: A descrição do café com leite.
        """
        return self._cafe.get_descricao() + ", com Leite"

# Decorador Concreto: Açúcar
class Acucar(DecoradorCafe):
    """Decorador concreto que adiciona açúcar ao café."""
    def get_custo(self):
        """Retorna o custo do café com açúcar.

        Returns:
            float: O custo do café com açúcar.
        """
        return self._cafe.get_custo() + 1.0

    def get_descricao(self):
        """Retorna a descrição do café com açúcar.

        Returns:
            str: A descrição do café com açúcar.
        """
        return self._cafe.get_descricao() + ", com Açúcar"
