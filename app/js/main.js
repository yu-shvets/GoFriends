$('document').ready(function(){
  var swiper = new Swiper('.swiper-container', {
    pagination: {
      el: '.swiper-pagination',
      dynamicBullets: true,
      clickable: true
    },
  });
  $('#owl').owlCarousel({
    items: 4,
    dots: true,
    loop: true,
    margin: 30
  });
  $('#owl1').owlCarousel({
    items: 3,
    dots: true,
    loop: true,
    margin: 30
  });
});