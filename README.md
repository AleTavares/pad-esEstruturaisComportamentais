# Engenharia de Software Orientada a Padrões: Exemplos em Python

Este repositório contém exemplos práticos dos Padrões de Projeto Estruturais e Comportamentais, implementados em Python. O objetivo é servir como um material de estudo completo para a aula de Engenharia de Software, detalhando não apenas o código, mas também os conceitos, motivações e mecanismos de cada padrão.

## Como Executar os Exemplos

Para ver todos os padrões em ação, execute o script principal na raiz do projeto:

```bash
python3 run_all_examples.py
```

---

## 1. Padrões Estruturais

Os Padrões Estruturais focam em como classes e objetos podem ser compostos para formar estruturas maiores. O objetivo principal é simplificar a estrutura do sistema, definir relacionamentos claros e garantir que a arquitetura seja flexível para mudanças futuras.

### 1.1. Adapter (Adaptador)
[Ver código](./padroes/estruturais/adapter/)

-   **Conceito:** Atua como uma ponte ou tradutor entre duas interfaces incompatíveis, permitindo que elas trabalhem juntas sem que o código cliente precise ser modificado.
-   **Quando Usar:** É ideal para integrar classes de sistemas legados ou bibliotecas de terceiros, quando a interface da classe existente não corresponde à que o cliente espera.
-   **Mecanismo:** O `Adapter` implementa a interface que o cliente espera e, internamente, delega as chamadas para um objeto da classe que ele está adaptando (`Adaptee`), realizando as traduções necessárias de dados e métodos.

### 1.2. Composite (Composto)
[Ver código](./padroes/estruturais/composite/)

-   **Conceito:** Permite tratar objetos individuais (folhas) e composições de objetos (containers) de maneira uniforme. Essencialmente, compõe objetos em estruturas de árvore para representar hierarquias parte-todo.
-   **Quando Usar:** Quando você tem uma estrutura que pode ser representada como uma árvore (ex: sistema de arquivos, organograma) e precisa que o cliente interaja com todos os elementos (sejam nós simples ou complexos) de forma consistente.
-   **Mecanismo:** Define uma interface comum (`Componente`) para todos os objetos na composição. A `Folha` (Leaf) implementa o comportamento base, e o `Composto` (Composite) armazena filhos (`Componentes`) e delega o trabalho a eles, podendo adicionar sua própria lógica.

### 1.3. Decorator (Decorador)
[Ver código](./padroes/estruturais/decorator/)

-   **Conceito:** É uma alternativa flexível à herança para estender funcionalidades. Permite anexar responsabilidades adicionais a um objeto individual em tempo de execução.
-   **Quando Usar:** Quando você precisa adicionar comportamentos a objetos específicos sem alterar outros objetos da mesma classe, ou quando a herança se torna impraticável devido a um grande número de combinações de funcionalidades.
-   **Mecanismo:** O `Decorator` implementa a mesma interface do objeto que ele envolve (`Componente`). Ele recebe uma instância do componente em seu construtor e adiciona seu próprio comportamento antes ou depois de delegar a chamada ao objeto encapsulado.

### 1.4. Facade (Fachada)
[Ver código](./padroes/estruturais/facade/)

-   **Conceito:** Fornece uma interface simples e unificada para um conjunto complexo de interfaces em um subsistema. Ele atua como um "gerente" que simplifica o acesso.
-   **Quando Usar:** Quando um subsistema é muito complexo ou quando há muitas dependências entre o cliente e as classes internas do subsistema. O Facade desacopla o cliente dessa complexidade.
-   **Mecanismo:** É uma única classe que contém referências às classes do subsistema. Seus métodos de alto nível orquestram as interações entre as classes internas para realizar uma tarefa, escondendo os detalhes do cliente.

---

## 2. Padrões Comportamentais

Os Padrões Comportamentais focam em como a comunicação e a interação entre objetos são gerenciadas. Eles buscam flexibilidade e eficiência na distribuição de responsabilidades, garantindo um baixo acoplamento.

### 2.1. Observer (Observador)
[Ver código](./padroes/comportamentais/observer/)

-   **Conceito:** Define uma dependência um-para-muitos entre objetos. Quando o objeto principal (`Subject`) muda de estado, todos os seus dependentes (`Observers`) são notificados e atualizados automaticamente.
-   **Quando Usar:** Quando uma mudança em um objeto requer que outros objetos sejam alterados, mas você não quer que eles sejam fortemente acoplados. É a base de sistemas de eventos e reatividade.
-   **Mecanismo:** O `Subject` mantém uma lista de `Observers`. Quando seu estado muda, ele itera sobre a lista e chama um método (`atualizar` ou `update`) em cada `Observer`, passando os dados necessários.

### 2.2. Strategy (Estratégia)
[Ver código](./padroes/comportamentais/strategy/)

-   **Conceito:** Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Permite que o algoritmo seja selecionado e trocado em tempo de execução.
-   **Quando Usar:** Quando você tem várias maneiras de fazer a mesma coisa (ex: diferentes métodos de pagamento, cálculos de frete, algoritmos de ordenação) e quer eliminar longas estruturas condicionais (`if/else`).
-   **Mecanismo:** O `Contexto` (a classe que usa o algoritmo) mantém uma referência a uma interface de `Estratégia`. As `Estratégias Concretas` implementam essa interface. O `Contexto` delega a execução do algoritmo para o objeto de estratégia que possui no momento.
