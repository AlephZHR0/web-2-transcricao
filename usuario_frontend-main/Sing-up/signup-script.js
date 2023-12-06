function createAccount() {
    var username = document.getElementById('username').value;
    var ra = document.getElementById('ra').value;
    var birthDate = document.getElementById('birthDate').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Validar os dados (adicionar validações personalizadas conforme necessário)
    if (username === '' || ra === '' || birthDate === '' || email === '' || password === '') {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    // Aqui você pode enviar os dados para o backend para processamento e armazenamento.
    // Neste exemplo, apenas exibimos um alerta simulando o envio para o backend.
    alert('Dados enviados para o backend:\nNome de Usuário: ' + username + '\nRa: ' + ra + '\nNascimento: ' + birthDate + '\nE-mail: ' + email + '\nSenha: ' + password);
}