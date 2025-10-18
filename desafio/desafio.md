## O Desafio para o Aluno: Refatoração ##
O aluno deve refatorar o código checkout_monolitico.py em múltiplas classes (mantendo a estrutura de classes em um único arquivo, se preferir, ou dividindo em módulos) aplicando os seguintes padrões para remover a rigidez e o acoplamento excessivo:

**Padrão Strategy:** Refatorar a lógica de processar_pagamento e calcular_frete.

**Padrão Decorator:** Refatorar a lógica de aplicar_desconto e a taxa de tem_embalagem_presente.

**Padrão Facade:** Criar uma classe CheckoutFacade para substituir o método finalizar_compra e abstrair as interações com "subsistemas" (como Estoque e Nota Fiscal), que agora serão classes separadas (mesmo que simples).

O resultado final deve permitir adicionar um novo MetodoDePagamento ou EstrategiaDeFrete sem modificar a classe Pedido (ou seu Contexto) e permitir a adição de taxas/descontos como "camadas" no objeto Pedido.