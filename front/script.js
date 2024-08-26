/**
 * A medida em que um range é alterado exibe-se o valor dele.
 */
const atualizarValor = (event) => {
    const range = event.target;
    const elementoId = `#${range.getAttribute("id")}`;
    const parent = document.querySelector(elementoId).parentElement;
    const valor = parent.querySelector(".valor");

    valor.textContent = range.value;
};

const aoEnviar = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const estrelaTipos = document.querySelectorAll(".estrela-tipo");
    const url = 'http://127.0.0.1:5000/estrela';

    estrelaTipos.forEach((estrelaTipo) => {
        estrelaTipo.classList.add('d-none');
    })

    fetch(url, {
        method: 'post',
        body: formData
    })
        .then((response) => response.json())
        .then((json) => {
            const estrelaTipo = document.getElementById(`${json.type}`);

            estrelaTipo.classList.remove('d-none');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

/**
 * Realiza ações no carregamento da página.
 * @param {*} event 
 */
const inicializacao = (event) => {
    const ranges = document.querySelectorAll('input[type=range]');

    ranges.forEach(range => { range.dispatchEvent(new Event("mousemove")) })
};
