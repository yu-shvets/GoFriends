$('document').ready(function(){
  var swiper = new Swiper('.swiper-container', {
    pagination: {
      el: '.swiper-pagination',
      dynamicBullets: true,
      clickable: true
    },
  });
  $('.owl-carousel').owlCarousel({
    items: 4,
    dots: true,
    loop: true,
    margin: 30
  });
  $('#test').owlCarousel({
    items: 1,
    dots: true,
    loop: true,
    margin: 30
  });
});