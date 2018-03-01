<?php
/*
Template Name: About us
*/
?>
<?php get_header(); ?>

<!-- Header -->
<section id="page-title" class="page-title-bg" style="background-image: url(<?php echo get_template_directory_uri(); ?>/assets/images/project-methodology.jpg);">
    <div class="row">
        <div class="wrap-page-title-content">
            <div class="container">
                <div class="page-title-content text-center">
                    <h1 class="os-animation" data-os-animation="fadeInUp"><?php the_title(); ?></h1>
                    <hr class="hr-title">
                </div>
            </div>
        </div>
    </div>
</section>

<!-- mission -->
<?php if (have_posts()): while (have_posts()): the_post(); ?>
<section class="mission">
    <div class="container">
        <div class="section-title mb-50">
            <div class="subtitle">Mission</div>
            <h2 class="text-center">Our <span class="gradient-text-02">Mission</span></h2>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <div class="mission__content"><?php the_content(); ?></div>
            </div>
        </div>
    </div>
</section>
<?php endwhile; endif;?> 

<!-- Values -->
<section class="values">
    <div class="container">
        <div class="row">
            <div class="col-sm-12 text-center">
                <div class="section-title mb-50">
                    <div class="subtitle">Values</div>
                    <h2 class="text-center">Our <span class="gradient-text-02">Values</span></h2>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-10 col-sm-offset-1">
                <div class="row values__items-wrapper">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">Respect for each other</h3>
                            <p>Everyone is an individual</p>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v4.png"></div>
                </div>
                <img class="vulues__down" src="<?php echo get_template_directory_uri(); ?>/assets/images/down-left.svg">
                <div class="row values__items-wrapper values__item-wrapper-revers">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">Education</h3>
                            <p>Personal and corporate</p>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v2.png"></div>
                </div>
                <img class="vulues__down" src="<?php echo get_template_directory_uri(); ?>/assets/images/down-right.svg">
                <div class="row values__items-wrapper">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">Labour organisation</h3>
                            <p>To come at work in time and to go home in time</p>
                            <p>Comfort in an office</p>
                            <p>Goals, objectives, planning</p>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v5.png"></div>
                </div>
                <img class="vulues__down" src="<?php echo get_template_directory_uri(); ?>/assets/images/down-left.svg">
                <div class="row values__items-wrapper values__item-wrapper-revers">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">Trust-based relationship</h3>
                            <p>Between partners, clients and colleagues</p>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v6.png"></div>
                </div>
                <img class="vulues__down" src="<?php echo get_template_directory_uri(); ?>/assets/images/down-right.svg">
                <div class="row values__items-wrapper">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">Labour as a performance of divine service</h3>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v7.png"></div>
                </div>
                <img class="vulues__down" src="<?php echo get_template_directory_uri(); ?>/assets/images/down-left.svg">
                <div class="row values__items-wrapper values__item-wrapper-revers">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">Team</h3>
                            <p>Family, support, relaxation</p>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v1.png"></div>
                </div>
                <img class="vulues__down" src="<?php echo get_template_directory_uri(); ?>/assets/images/down-right.svg">
                <div class="row values__items-wrapper">
                    <div class="col-xs-10 values__item-wrapper">
                        <div class="values__item">
                            <h3 class="valuel__title">We help our clients to develop and grow their business</h3>
                        </div>
                    </div>
                    <div class="col-xs-2"><img src="<?php echo get_template_directory_uri(); ?>/assets/images/v3.png"></div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php
    $args = array(
        'post_type' => 'history',
        'post_status' => 'publish',
        'posts_per_page' => 9,
        'order' => 'ASC'
    );
    $history_first = new WP_Query($args);
    $count_year2 = 0;
    $years2 = count($history_first->posts);
?>
<section id="download" class="download faq bg-image-2 parallax">
    <div class="wrap-download-content">
        <div class="download-content">
            <div class="container">
                <div class="row">
                    <div class="section-title">
                        <h2>The history of our success</h2>
                    </div>
                    <div class="years">
                        <canvas id="canvas"></canvas>
                        <?php while( $history_first->have_posts() ): ?>
                            <?php $history_first->the_post(); ?>
                            <?php $count_year2++; ?>
                            <div data-year="<?php the_title(); ?>" class="years__item-wrapper <?php echo ($count_year2 == $years2) ? 'active' : ''; ?>">
                                <div class="years__item"><?php the_title(); ?></div>
                            </div>
                        <?php endwhile; ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<?php wp_reset_query(); ?>



<?php
    $args = array(
        'post_type' => 'history',
        'post_status' => 'publish',
        'posts_per_page' => 9,
        'order' => 'ASC'
    );
    $history = new WP_Query($args);
    $count_year = 0;
    $years = count($history->posts);
?>
<?php while( $history->have_posts() ): ?>
<?php $history->the_post(); ?>
<?php $count_year++; ?>
<section class="years-content-<?php the_title(); ?> animated fadeIn years-content" style="display: <?php echo ($count_year == $years) ? 'block' : 'none'; ?>;">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="section-title mb-50">
                    <div class="subtitle"><?php the_title(); ?></div>
                    <h2 class="text-center">Year <span class="gradient-text-02"><?php the_title(); ?></span></h2>
                </div>
                <?php the_content(); ?>
            </div>
        </div>
    </div>
</section>
<?php endwhile; ?>
<?php wp_reset_query(); ?>

<style type="text/css">
    .main-map {
        margin-top: 60px;
    }
    .land {
        fill: #CCCCCC;
        fill-opacity: 1;
        stroke:white;
        stroke-opacity: 1;
        stroke-width:0.5;
        transition: .2s;
    }
    .active-land {
        fill: #33b185;
    }
    .active-land:hover {
        fill: #2c8c6a;
        cursor: pointer;
    }
    .maps {
        padding: 40px 0;
    }
    .maps-title {
        margin-bottom: 60px;
    }
    .pink {
        shape-rendering: crispEdges;
        fill: url(#MyGradient);
    }
    #maps-content {
        overflow: hidden;
        position: relative;
    }
    .map-content {
        transition: .2s ease-in-out;
    }
    #maps-content.map-content {
        transform: translateY(-100%);
    }
    #maps-content.active {
        overflow: auto;
        position: relative;
    }
    #maps-content.active .map-content {
        transform: translateY(0);
    }
</style>

<?php
    $args = array(
        'post_type' => 'case',
        'post_status' => 'publish',
        'posts_per_page' => -1,
    );
    $case = new WP_Query($args);
?>

<?php while( $case->have_posts() ): ?>
    <?php $case->the_post(); ?>
    <?php $countries[] = get_the_terms($case->posts->ID, 'country'); ?>
<?php endwhile; ?>
<?php wp_reset_query(); ?>

<?php
foreach ($countries as $value) {
    if ($value) {
        $arr_countries[] = $value[0]->slug;
    }
}
foreach ( array_unique($arr_countries) as $value ) {
    if($value) {
        $cantries[] = strtoupper($value);
    }
}
?>


<section class="maps">
    <div class="container text-center">
        <div class="section-title maps__title">
            <div class="subtitle">19 contry</div>
            <h2>More then <span class="gradient-text-02"><?php echo count($case->posts); ?> happy clients</span> from <?php echo count($cantries); ?> contries</h2>
        </div>
        <div class="clearfix"></div>
        <?php echo file_get_contents( get_template_directory_uri()."/assets/images/worldLow.svg"); ?>
        <div id="map-data" class="animated">
            <button id="map-data__close"><i class="fa fa-times" aria-hidden="true"></i></button>
            <h4 id="map-title" class="gradient-text-02"></h4>
            <ul id="map-content"></ul>
        </div>
    </div>
</section>


<?php wp_reset_query(); ?>

<style type="text/css">
    #map-title {
        margin-top: 30px;
    }
    #map-content {
        margin-top: 10px;
        padding: 0;
    }
    #map-data {
        display: none;
        width: 300px;
        margin-left: -150px;
        height: 200px;
        position: absolute;
        background: rgba(255, 255, 255, .9);
        border: 3px solid #19abd6;
        border-radius: 4px;
        box-shadow: 0 0 10px rgba(0,0,0,.3);
        transition: .2s ease-in-out;
    }
    #map-data:after {
        content: '';
        display: block;
        position: absolute;
        top: -13px;
        left: 140px;
        width: 0;
        height: 0;
        border-style: solid;
        border-width: 0 10px 10px 10px;
        border-color: transparent transparent #19abd6 transparent;
    }
    #map-data__close {
        position: absolute;
        right: 10px;
        top: 10px;
        width: 30px;
        height: 30px;
        background: #19abd6;
        color: #fff;
        border-radius: 50%;
        box-shadow: 0 0 10px rgba(0,0,0,.3);
        transition: .2s ease-in-out;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        text-center: center;
    }
    #map-data__close:hover {
        background: rgb(245,78,162);
        transform: scale(1.2) rotate(360deg);
    }
    #map-data__close i {
        line-height: 1px;
    }

    #canvas {
        position: absolute;
        /*background: rgba(221, 238, 238, 0.25);*/
    }
    
</style>

<?php get_footer(); ?>
<script type="text/javascript">

    var tempCountry =
    
    [{"title":"Lion&#8217;s Heart","link":"https:\/\/gofriends.pro\/case\/lion-s-heart\/"},{"title":"GoFriends Wi-Fi","link":"https:\/\/gofriends.pro\/case\/english-gofriends-wi-fi\/"},{"title":"Restaurant design","link":"https:\/\/gofriends.pro\/case\/russkij-dizajn-restorana\/"},{"title":"E-schools","link":"https:\/\/gofriends.pro\/case\/e-schools\/"},{"title":"Rosslane Film","link":"https:\/\/gofriends.pro\/case\/rosslane-film\/"},{"title":"Arenda auto &#8211;\u00a0is online car rental service","link":"https:\/\/gofriends.pro\/case\/arenda-auto-car-rental-on-line-service\/"},{"title":"Veronika+","link":"https:\/\/gofriends.pro\/case\/english-veronika\/"},{"title":"OpenBit Platform","link":"https:\/\/gofriends.pro\/case\/english-crypto-mlm\/"},{"title":"Athletic Events","link":"https:\/\/gofriends.pro\/case\/english-athletic-events\/"},{"title":"GoFriends Marketplace","link":"https:\/\/gofriends.pro\/case\/gofriends-marketplace\/"}]



        


    var cantries = <?php echo json_encode($cantries); ?>;
    for (cantry in cantries) {
        $('#'+cantries[cantry]).addClass('active-land');
    }

    var coof = 7;
    var getTopValue;
    $('.years__item-wrapper').each(function(index){
        getTopValue = coof * index * index;
        $(this).css({top: '-' + getTopValue + 'px'});
    });
    if($(window).width() < 768) {
        $('.years').css({paddingTop: getTopValue + 40 + 'px'});
    } else {
        $('.years').css({paddingTop: getTopValue + 100 + 'px'});
    }
    

    $('.years__item-wrapper').click(function(){
        var year = $(this).data('year'),
            title = $(this).find('.years__item'),
            content = $('.years-content-' + year);
        $('.years__item-wrapper').removeClass('active');
        $(this).addClass('active');
        $('.years-content').hide();
        content.show().slideDown({
            duration: 600
        });
        $('html, body').animate({
            scrollTop: content.offset().top
        }, 600);
    });

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
</script>


