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

  $('#customer_form').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        url: form.attr('action'),
        method: 'post',
        data: form.serialize(),

        success: function (json) {
            console.log('Hello!');
            $('#success').text(json.success);
            form.each(function(){
            this.reset();
            });
        }
    });
  });

});