const url_base = "http://127.0.0.1:5000";
async function createAccount(event) {
    event.preventDefault(); // Impede o comportamento padrão do formulário

    // Coletar os dados do usuário
    const userData = {
        username: document.getElementById('username').value,
        ra: document.getElementById('ra').value,
        birthDate: document.getElementById('birthDate').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
    };

    // Configurar a requisição HTTP
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url_base, true); // Substitua pela URL do seu back-end
    xhr.setRequestHeader("Content-Type", "application/json");

    // Enviar a requisição com os dados do usuário
    xhr.send(JSON.stringify(userData));

    // Tratar a resposta do servidor
    xhr.onload = function() {
        if (xhr.status == 200) {
            alert("Conta criada com sucesso!");
            // Redirecionar para a página de login ou outra página
            window.location.href = "../Login/login.html";
        } else {
            alert("Erro ao criar a conta. Tente novamente.");
        }
    };
}