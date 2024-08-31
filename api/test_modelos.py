from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "./MachineLearning/data/cleaned_star_data_only_numbers.csv"
colunas = ['temperature', 'luminosity', 'radius', 'absolute_magnitude']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:, 0:-1]
y = array[:, -1]

# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"


# def test_modelo_lr():
#     # Importando o modelo de regressão logística
#     lr_path = './MachineLearning/models/estrelas_lr.pkl'
#     modelo_lr = Model.carrega_modelo(lr_path)

#     # Obtendo as métricas da Regressão Logística
#     acuracia_lr = Avaliador.avaliar(modelo_lr, X, y)

#     # Testando as métricas da Regressão Logística
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_lr >= 0.78
#     # assert recall_lr >= 0.5
#     # assert precisao_lr >= 0.5
#     # assert f1_lr >= 0.5

# Método para testar modelo KNN a partir do arquivo correspondente


# def test_modelo_knn():
#     # Importando modelo de KNN
#     knn_path = './MachineLearning/models/estrelas_knn.pkl'
#     modelo_knn = Model.carrega_modelo(knn_path)

#     # Obtendo as métricas do KNN
#     acuracia_knn = Avaliador.avaliar(modelo_knn, X, y)

#     # Testando as métricas do KNN
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_knn >= 0.68
#     # assert recall_knn >= 0.5
#     # assert precisao_knn >= 0.5
#     # assert f1_knn >= 0.5

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
