const url_base = "http://127.0.0.1:5000";

document.addEventListener("DOMContentLoaded", function () {
    const enviarBtn = document.getElementById("enviar");
    const enviarUrlBtn = document.getElementById("enviarUrl");
    const textoInput = document.getElementById("texto");
    const chatContainer = document.getElementById("chatContainer");

    enviarBtn.addEventListener("click", function () {
        enviarMensagem();
    });

    enviarUrlBtn.addEventListener("click", function () {
        const url = prompt("Digite a URL:");
        if (url) {
            enviarMensagem(`<a href="${url}" target="_blank">${url}</a>`);
        }
    });

    function enviarMensagem(mensagem = "") {
        if (mensagem.trim() !== "") {
            const novaMensagem = document.createElement("p");
            novaMensagem.innerHTML = mensagem;
            chatContainer.appendChild(novaMensagem);
            chatContainer.scrollTop = chatContainer.scrollHeight;
            textoInput.value = "";
        }
    }
});