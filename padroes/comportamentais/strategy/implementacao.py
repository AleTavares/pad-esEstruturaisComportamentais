from abc import ABC, abstractmethod

# Estratégia Abstrata (Interface)
class EstrategiaCalculoFrete(ABC):
    """Define a interface para as estratégias de cálculo de frete."""
    @abstractmethod
    def calcular(self, peso: float) -> float:
        """Calcula o frete com base no peso.

        Args:
            peso (float): O peso do produto.

        Returns:
            float: O valor do frete.
        """

# Estratégias Concretas
class FreteNormal(EstrategiaCalculoFrete):
    """Estratégia de frete normal."""
    def calcular(self, peso: float) -> float:
        """Calcula o frete normal.

        Args:
            peso (float): O peso do produto.

        Returns:
            float: O valor do frete.
        """
        # Custo de R$ 5.0 por kg
        return peso * 5.0

class FreteExpresso(EstrategiaCalculoFrete):
    """Estratégia de frete expresso."""
    def calcular(self, peso: float) -> float:
        """Calcula o frete expresso.

        Args:
            peso (float): O peso do produto.

        Returns:
            float: O valor do frete.
        """
        # Custo de R$ 10.0 por kg + taxa fixa de R$ 10.0
        return peso * 10.0 + 10.0

class FreteRetiradaLocal(EstrategiaCalculoFrete):
    """Estratégia de retirada local."""
    def calcular(self, peso: float) -> float:
        """Calcula o frete para retirada local.

        Args:
            peso (float): O peso do produto.

        Returns:
            float: O valor do frete.
        """
        # Sem custo
        return 0.0

# Contexto (utiliza a Estratégia)
class Pedido:
    """Representa um pedido e utiliza uma estratégia de cálculo de frete."""
    def __init__(self, peso: float, estrategia_frete: EstrategiaCalculoFrete):
        """Inicializa o pedido.

        Args:
            peso (float): O peso do pedido.
            estrategia_frete (EstrategiaCalculoFrete): A estratégia de cálculo de frete.
        """
        self.peso = peso
        self._estrategia_frete = estrategia_frete

    def definir_estrategia_frete(self, estrategia_frete: EstrategiaCalculoFrete):
        """Define a estratégia de frete.

        Args:
            estrategia_frete (EstrategiaCalculoFrete): A nova estratégia de frete.
        """
        self._estrategia_frete = estrategia_frete

    def calcular_custo_total(self):
        """Calcula o custo total do frete.

        Returns:
            float: O custo do frete.
        """
        # Delega o cálculo para o objeto Estratégia
        custo_frete = self._estrategia_frete.calcular(self.peso)
        print(f"Custo do frete ({self._estrategia_frete.__class__.__name__}): R${custo_frete:.2f}")
        return custo_frete
