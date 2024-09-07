from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "./MachineLearning/data/cleaned_star_data.csv"
colunas = ['temperature', 'luminosity', 'radius', 'absolute_magnitude']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:, 0:4]
y = array[:, 4]
y = y.astype('float')


def test_modelo_cart():
    """Método para testar pipeline CART a partir do arquivo correspondente
    """
    # Importando pipeline de CART
    cart_path = './MachineLearning/pipelines/cart_estrelas_pipeline.pkl'
    modelo_cart = Pipeline.carrega_pipeline(cart_path)

    # Obtendo as métricas do CART
    acuracia_cart = Avaliador.avaliar(modelo_cart, X, y)

    # Testando as métricas do CART
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_cart >= 0.95
    # assert recall_rf >= 0.5
    # assert precisao_rf >= 0.5
    # assert f1_rf >= 0.5
