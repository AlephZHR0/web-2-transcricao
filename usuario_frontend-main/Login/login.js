const url_base = "http://127.0.0.1:5000";
async function loginUser(event) {
    
    event.preventDefault(); // Impede o comportamento padrão do formulário

    // Coletar os dados de login
    const loginData = {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
    };

    // Configurar a requisição HTTP
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url_base, true); // Substitua pela URL do seu back-end
    xhr.setRequestHeader("Content-Type", "application/json");

    // Enviar a requisição com os dados de login
    xhr.send(JSON.stringify(loginData));

    // Tratar a resposta do servidor
    xhr.onload = function() {
        if (xhr.status == 200) {
            alert("Login realizado com sucesso!");
            // Aqui você pode redirecionar o usuário para outra página ou fazer outras ações necessárias
        } else {
            alert("Erro no login. Verifique seu nome de usuário e senha.");
        }
    };
}