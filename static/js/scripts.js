// Abrir e fechar o menu lateral
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('menu-btn').addEventListener('click', function() {
        document.getElementById('sidebar').classList.add('open');
    });

    document.getElementById('close-btn').addEventListener('click', function() {
        document.getElementById('sidebar').classList.remove('open');
    });
});
console.log("JavaScript carregado!");

