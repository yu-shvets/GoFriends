

$('document').ready(function(){
//   var swiper = new Swiper('.swiper-container', {
//     pagination: {
//       el: '.swiper-pagination',
//       dynamicBullets: true,
//       clickable: true
//     },
//   });
//   particlesJS.load('particles-js', '../libs/particles.js/demo/particles.json', function() {
//     console.log('callback - particles.js config loaded');
//   });
//   var count_particles, stats, update;
// stats = new Stats;
// stats.setMode(0);
// stats.domElement.style.position = 'absolute';
// stats.domElement.style.left = '0px';
// stats.domElement.style.top = '0px';
// document.body.appendChild(stats.domElement);
// count_particles = document.querySelector('.js-count-particles');
// update = function() {
//   stats.begin();
//   stats.end();
//   if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) {
//     count_particles.innerText = window.pJSDom[0].pJS.particles.array.length;
//   }
//   requestAnimationFrame(update);
// };
// requestAnimationFrame(update);
  $('#owl').owlCarousel({
    items: 4,
    dots: true,
    loop: true,
    margin: 30,
    responsive:{
      0:{
        items:1
      },
      550: {
        items: 2
      },
      950: {
        items: 3
      },
      1200:{
          items:4
      },
      1800: {
        items: 5
      }

    }
  });
  $('#owl1').owlCarousel({
    items: 3,
    dots: true,
    loop: true,
    margin: 30
  });

});

var onMouse = document.querySelectorAll('.cases__work'),
    cases   = document.querySelectorAll('.cases__wrapper');


onMouse.forEach((element,index,array) => {
  if(element) {
    element.onmouseenter = scrollBottom;
    element.onmouseleave = returnScroll;
  }
})

function scrollBottom(event) {
  event.target.firstElementChild.classList.add("animatedBottom");
  setTimeout(() => {
    event.target.firstElementChild.classList.remove("animatedBottom");
  }, 10000)
}

function returnScroll() {

}


// function scrollBottom(obj) {
//   let thisImg = obj.target.firstElementChild.firstElementChild,
//       thisFullSCroll = obj.target.firstElementChild,
//       heightImg = thisImg.offsetHeight,
//       stepScroll = heightImg / 400;
//   var timerId = setInterval(() => {
//     thisFullSCroll.scrollTop += stepScroll;
//     console.log('Hello');
//   }, 25);
//   setTimeout(() => {
//     clearInterval(timerId);
//     thisFullSCroll.scrollTop = 0;
//   }, 10000);
// }

// function returnScroll () {
//   clearInterval(timerId);
// }


// function preventDefault(e) {
//   e = e || window.event;
//   if (e.preventDefault)
//       e.preventDefault();
//   e.returnValue = false;  
// }

// function disableScroll() {

//   document.body.style.overflow = 'hidden';
// }

// function enableScroll() {

//   document.body.style.overflow = 'auto';  
// }