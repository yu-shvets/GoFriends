<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-109823802-1');
</script>
<script>
        var IsDuplicateScrollEvent = 0;
         $(document).ready(function () {
            SetupGoogleAnalyticsTrackEvents();
        });
        function SetupGoogleAnalyticsTrackEvents()
        {
            TrackEventsForMinimumPageScroll();
        }
        function TrackEventsForMinimumPageScroll()
        {
           $(window).scroll(function(){
             var scrollPercent = GetScrollPercent();
             if(scrollPercent > 70)
             {
               if(IsDuplicateScrollEvent == 0)
               {
                 IsDuplicateScrollEvent = 1;
                 //alert("Page Scrolled to 70% in " + document.location.href);
                 TrackEvent("Content Engagement", "Scrolled To 70%", document.location.href);
               }
             }
           });
        }
        function GetScrollPercent()
        {
             var bottom = $(window).height() + $(window).scrollTop();
             var height = $(document).height();
             return Math.round(100*bottom/height);
        }
        function TrackEvent(Category, Action, Label)
        {
           _gaq.push(['_trackEvent', Category, Action, Label]);
        }
</script>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-109823802-1', 'auto');
  ga('send', 'pageview');
  setTimeout("ga('send','event','Engaged users','More than 15 seconds')",15000);
</script>


<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter46683339 = new Ya.Metrika({
                    id:46683339,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
            s = d.createElement("script"),
            f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = "https://mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/46683339" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

