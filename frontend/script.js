const API_URL = "http://localhost:8000";


// Listar todos os livros
async function listarLivros() {
    try {
        const resposta = await fetch(`${API_URL}/livros`);
        const livros = await resposta.json();

        mostrarLivros(livros);
    } catch (erro) {
        console.error("Erro ao listar livros:", erro);
    }
}


// Buscar livro pelo título
async function buscarLivro() {
    const titulo = document.getElementById("buscarLivro").value;

    try {
        const resposta = await fetch(
            `${API_URL}/livros/buscar?titulo=${titulo}`
        );

        const livros = await resposta.json();

        mostrarLivros(livros);
    } catch (erro) {
        console.error("Erro na busca:", erro);
    }
}


// Adicionar um novo livro
async function adicionarLivro() {
    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;


    if (!titulo || !autor) {
        alert("Preencha todos os campos!");
        return;
    }


    const novoLivro = {
        titulo: titulo,
        autor: autor
    };


    try {
        await fetch(`${API_URL}/livros`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(novoLivro)
        });


        document.getElementById("titulo").value = "";
        document.getElementById("autor").value = "";

        listarLivros();

    } catch (erro) {
        console.error("Erro ao adicionar livro:", erro);
    }
}


// Alterar disponibilidade
async function alterarStatus(id, statusAtual) {
    try {
        await fetch(`${API_URL}/livros/${id}/status?disponivel=${!statusAtual}`, {
            method: "PUT"
        });

        listarLivros();

    } catch (erro) {
        console.error("Erro ao alterar status:", erro);
    }
}


// Excluir livro
async function excluirLivro(id) {

    const confirmar = confirm(
        "Tem certeza que deseja excluir este livro?"
    );

    if (!confirmar) {
        return;
    }


    try {
        await fetch(`${API_URL}/livros/${id}`, {
            method: "DELETE"
        });

        listarLivros();

    } catch (erro) {
        console.error("Erro ao excluir livro:", erro);
    }
}


// Mostrar livros na tela
function mostrarLivros(livros) {

    const lista = document.getElementById("listaLivros");

    lista.innerHTML = "";


    if (livros.length === 0) {
        lista.innerHTML = "<p>Nenhum livro encontrado.</p>";
        return;
    }


    livros.forEach(livro => {

        const card = document.createElement("div");

        card.className = "livro";


        card.innerHTML = `
            <h3>${livro.titulo}</h3>

            <p><strong>Autor:</strong> ${livro.autor}</p>

            <p class="${
                livro.disponivel
                ? "disponivel"
                : "indisponivel"
            }">

            ${
                livro.disponivel
                ? "Disponível"
                : "Indisponível"
            }

            </p>

            <button onclick="alterarStatus(${livro.id}, ${livro.disponivel})">
                Alterar status
            </button>

            <button onclick="excluirLivro(${livro.id})">
                Excluir
            </button>
        `;


        lista.appendChild(card);

    });

}


// Carregar os livros automaticamente
window.onload = listarLivros;