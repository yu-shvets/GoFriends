var tempCountry =
    
[{"title":"Lion&#8217;s Heart","link":"https:\/\/gofriends.pro\/case\/lion-s-heart\/"},{"title":"GoFriends Wi-Fi","link":"https:\/\/gofriends.pro\/case\/english-gofriends-wi-fi\/"},{"title":"Restaurant design","link":"https:\/\/gofriends.pro\/case\/russkij-dizajn-restorana\/"},{"title":"E-schools","link":"https:\/\/gofriends.pro\/case\/e-schools\/"},{"title":"Rosslane Film","link":"https:\/\/gofriends.pro\/case\/rosslane-film\/"},{"title":"Arenda auto &#8211;\u00a0is online car rental service","link":"https:\/\/gofriends.pro\/case\/arenda-auto-car-rental-on-line-service\/"},{"title":"Veronika+","link":"https:\/\/gofriends.pro\/case\/english-veronika\/"},{"title":"OpenBit Platform","link":"https:\/\/gofriends.pro\/case\/english-crypto-mlm\/"},{"title":"Athletic Events","link":"https:\/\/gofriends.pro\/case\/english-athletic-events\/"},{"title":"GoFriends Marketplace","link":"https:\/\/gofriends.pro\/case\/gofriends-marketplace\/"}]


var country = [{'title': 'UA'}, {'title': 'GL'}, {'title': 'FR'}];
    


// var cantries = <?php echo json_encode($cantries); ?>;
country.forEach(function(element,index,array) {
  let sCountry = element.title
  $("#" + sCountry).addClass('active-land');
})
// for (cantry in country) {
//     $('#'+cantry.title).addClass('active-land');
// }

// var coof = 7;
// var getTopValue;
// $('.years__item-wrapper').each(function(index){
//     getTopValue = coof * index * index;
//     $(this).css({top: '-' + getTopValue + 'px'});
// });
// if($(window).width() < 768) {
//     $('.years').css({paddingTop: getTopValue + 40 + 'px'});
// } else {
//     $('.years').css({paddingTop: getTopValue + 100 + 'px'});
// }


// $('.years__item-wrapper').click(function(){
//     var year = $(this).data('year'),
//         title = $(this).find('.years__item'),
//         content = $('.years-content-' + year);
//     $('.years__item-wrapper').removeClass('active');
//     $(this).addClass('active');
//     $('.years-content').hide();
//     content.show().slideDown({
//         duration: 600
//     });
//     $('html, body').animate({
//         scrollTop: content.offset().top
//     }, 600);
// });

// ------------------------- Canvas -------------------------
// var firstBlock = $('.years__item-wrapper:first'),
//     lastBlock = $('.years__item-wrapper:last'),
//     centerBlock = $('.years__item-wrapper:nth-child(3)');

// var x = firstBlock.position().left,
//     y = firstBlock.position().top,
//     x1 = lastBlock.position().left,
//     y1 = lastBlock.position().top,
//     cx = centerBlock.position().left,
//     cy = centerBlock.position().top;

// var canvasWidth = x1 - x,
//     canvasHeight = y - y1;

// $('#canvas').attr('width', canvasWidth);
// $('#canvas').attr('height', canvasHeight);

// var liSize = parseInt($('.years__item').css('width').slice(0, -2)),
//     liMargin = parseInt($('.years__item-wrapper').css('margin-left').slice(0, -2));

// $('#canvas').css({
//     top: y1 + liSize/2 + 10 + 'px',
//     left: '50%',
//     marginLeft: -(canvasWidth/2) + 'px'
// });

// var example = document.getElementById("canvas"),
//     ctx = example.getContext('2d');

// ctx.lineWidth = 3;
// ctx.strokeStyle = '#fff';
// ctx.lineTo(canvasWidth, 0);
// ctx.quadraticCurveTo(cx-x+150, canvasHeight-(y-cy), 0, canvasHeight-6);
// ctx.stroke();
// console.log(x, y, x1, y1, canvasWidth, canvasHeight, cx, cy, liSize, liMargin);


// map
$('.active-land').click(function(e){
    var land = $('.land'),
        title = $(this).attr('title'),
        country_id = $(this).attr('id');
    $('#map-data').addClass('bounceIn');
    $('#map-data').removeClass('bounceOut');
    land.removeClass('pink');
    $(this).addClass('pink');
    $('#map-title').text(title);


    var mapY = e.pageY;
    var mapX = e.pageX;
    var mapData = $('#map-data');
    mapData.css({
        top: mapY + 20,
        left: mapX,
        display: 'block'
    });

    var mapDataClose = mapData.find('#map-data__close');
    mapDataClose.click(function(e) {
        e.preventDefault();
        $('#map-content').empty();
        mapData.removeClass('bounceIn').addClass('bounceOut');
        $('.pink').removeClass('pink');
    });

      $.ajax({
          method: "POST",
          url: "/test_country",
          data: {
              'country_id': country_id
          },
          beforeSend: function(){
          },
          success: function(data){
              var testContent = $('#map-content');
              testContent.empty();
              for (var i = 0; i < data.length; i++) {
                  var title = data[i].title,
                      link = data[i].link;
                  testContent.append('<li><a href="' + link + '" target="_blank">' + title + '</a></li>');
              }
          },
          error: function(){
              console.log('no');
          }
      });
});