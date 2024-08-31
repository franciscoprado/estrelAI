from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
estrela_tag = Tag(
    name="Estrela", description="Predição de tipo de estrela")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/estrela', tags=[estrela_tag],
          responses={"200": EstrelaViewSchema, "400": ErrorSchema, "422": ErrorSchema})
def predict(form: EstrelaSchema):
    """Retornará uma predição do tipo de estrela a partir de dados como temperatura e tamanho.

    Args:
        form (EstrelaSchema): Os dados da estrela.

    Returns:
        EstrelaViewSchema: O tipo da estrela.
    """
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = './MachineLearning/pipelines/cart_estrelas_pipeline.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    type = int(Model.preditor(modelo, X_input)[0])

    return {"type": type}, 200


if __name__ == '__main__':
    app.run(debug=True)
