# estrelAI

O objetivo do projeto é fornecer um sistema capaz de predizer o tipo de uma estrela baseando-se em parâmetros fornecidos.

O dataset contém informações sobre várias estrelas, de vários tipos, com cada registro representando uma estrela. As variáveis incluem características como temperatura, luminosidade e raio. A quinta coluna, Star type, é o tipo de estrela.

Descrição de Cada Coluna:

* Temperature (K): Mergulhe nas propriedades térmicas de estrelas, crucial para entender seu ciclo de vida e energia saída.
* Luminosity (L/Lo): Explore o brilho estelar em relação ao nosso Sol (Lo = 3,828 x 10 ^ 26 Watts), oferecendo informações sobre o tamanho das estrelas e a produção de energia.
* Radius (R/Ro): Compare os tamanhos das estrelas com o nosso Sol (Ro = 6,995 x 10 ^ 8 m), essencial para compreender a evolução e estrutura estelar.
* Absolute magnitude (Mv): Analise o brilho estelar intrínseco, padronizado para estudos comparativos em vastas distâncias cósmicas.

Os tipos de estrela são:

* 0: Anã marrom
* 1: Anã vermelha
* 2: Anã branca
* 3: Sequência principal
* 4: Estrela supergigante
* 5: Estrela hipergigante

## Instalação e execução

Instalando as dependências via pip:

`pip install -r .\requirements.txt`

Para executar a aplicação Flask:

`flask --app app run --debug`