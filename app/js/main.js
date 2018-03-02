

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
      1600: {
        items: 4
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
    cases = document.querySelectorAll('.cases__wrapper');

onMouse.forEach(function (element, index, array) {
  if (element) {
    element.onmouseenter = scrollBottom;
  }
});

function scrollBottom(event) {
  event.target.firstElementChild.classList.add("animatedBottom");
  setTimeout(function () {
    event.target.firstElementChild.classList.remove("animatedBottom");
  }, 10000);
}

TweenMax.set(".banner__title");

var titleText = new SplitText(".banner__title"),
    tl = new TimelineLite(),
    numWords = titleText.chars.length;

function initTitle() {
  for (var i = 0; i < numWords; i++) {

      tl.from(titleText.chars[i], 1.5, {
          force3D: true,
          opacity: 0,
          x: -500,
          transformOrigin: "0% 50%",
          ease: Back.easeOut
      }, Math.random());
  }
}

$('#menu').slicknav({
  prependTo: '.header',
  label: ''
});

$('.slicknav_btn').click(function(){
  $('.slicknav_menu').toggleClass("slicknav_menu_color");
})

initTitle();

(function(){
  var firstVal = document.getElementById('a1').innerHTML, 
  secondVal = document.getElementById('a2').innerHTML,
  thirdVal = document.getElementById('a3').innerHTML;
  Cont={val:0};
  TweenLite.to(Cont,2,{val:firstVal,roundProps:"val",onUpdate:function(){
    document.getElementById("a1").innerHTML=Cont.val
  }});
  TweenLite.to(Cont,3,{val:secondVal,roundProps:"val",onUpdate:function(){
    document.getElementById("a2").innerHTML=Cont.val
  }});
  TweenLite.to(Cont,2,{val:thirdVal,roundProps:"val",onUpdate:function(){
    document.getElementById("a3").innerHTML=Cont.val
  }});
})();