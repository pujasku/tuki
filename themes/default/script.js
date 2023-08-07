function toggleMenu() {
  const sidebar = document.querySelector('.sidebar');
  const main = document.querySelector('.main-wrapper');

  sidebar.classList.toggle('active'); // Agrega o quita la clase "active" al menú
  main.classList.toggle('active'); // Agrega o quita la clase "active" al contenido principal
}
function showContent(section) {
  let articles = document.getElementsByClassName('art');
  let pertinent = document.getElementById(section);
  for(var i = 0; i < articles.length; i++){
    articles[i].classList.add("hidden");
  }
  pertinent.classList.remove("hidden")
}
//auto exec for showing main content when the site is open
document.addEventListener("DOMContentLoaded", function() {
  showContent("initial-content");
});


