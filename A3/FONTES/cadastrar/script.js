window.onload = function() {
  function rolarParaGastronomia() {    
    var gastronomiaElement = document.getElementById("gastronomia");
  
    gastronomiaElement.scrollIntoView({ behavior: 'smooth' });
  }
  
  var culinariaDiv = document.getElementById("culinaria");
  culinariaDiv.addEventListener("click", rolarParaGastronomia);

  function rolarParaHospedagem() {    
    var hospedagemH2 = document.getElementById("hospedagem-heading");
  
    hospedagemH2.scrollIntoView({ behavior: 'smooth' });
  }
  
  var hospedagemSection = document.getElementById("hospedagem");
  hospedagemSection.addEventListener("click", rolarParaHospedagem);

  function rolarParaPontosTuristicos() {    
    var pontoturisticoH2 = document.getElementById("pontos-turisticos-heading");
  
    pontoturisticoH2.scrollIntoView({ behavior: 'smooth' });
  }
  
  var pontoturisticoSection = document.getElementById("pontos-turisticos");
  pontoturisticoSection.addEventListener("click", rolarParaPontosTuristicos);
}


document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    for (let i = 0; i < links.length; i++) {
      links[i].addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
          const targetPosition = targetElement.offsetTop;
          const currentPosition = window.pageYOffset;
          const distance = targetPosition - currentPosition;
          
          const duration = 500; // Duração da animação em milissegundos
          const startTime = performance.now();
          
          function animation(time) {
            const elapsedTime = time - startTime;
            const progress = Math.min(elapsedTime / duration, 1);
            const ease = easeOutQuart(progress);
            
            window.scrollTo(0, currentPosition + distance * ease);
            
            if (elapsedTime < duration) {
              requestAnimationFrame(animation);
            }
          }
          
          requestAnimationFrame(animation);
        }
      });
    }
    
    // Função de animação easeOutQuart para suavizar o movimento
    function easeOutQuart(t) {
      return 1 - (--t) * t * t * t;
    }
  });
  
  function abrirMenuLateral(){
    document.getElementById('menuLateral').style.width = '15%';
    document.getElementById('conteudo').style.marginLeft = '15%'; 
    document.getElementById('cabecalho').style.marginLeft = '15%';
  }
  
  function fecharMenuLateral(){
      document.getElementById('menuLateral').style.width = '0px';
      document.getElementById('conteudo').style.marginLeft = '0px';
      document.getElementById('cabecalho').style.marginLeft = '0px';
  }



