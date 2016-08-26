$(document).ready(function() {

    //all jQuery code from here

    var flag=true;
    var flag2=true;

    $(".header-intro").addClass('slide');

    $('.automatic-slider').unslider({
    autoplay: true,
    delay: 4000
    });

    $(document).on('click', 'a', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 700);
    });


    $(window).scroll(function(){
      var windowWidth = $(this).width();
      var windowHeight = $(this).height();
      var windowScrollTop = $(this).scrollTop();

    //===HEADER===

    if (windowScrollTop > 150)
    {
    $('.navbar-inverse').addClass('show-menu');
    $('.navbar-inverse').removeClass('hide-menu');
    }
    else
    {
    if ($('.navbar-inverse').hasClass('show-menu'))
    {
    $('.navbar-inverse').removeClass('show-menu');
    $('.navbar-inverse').addClass('hide-menu');
    }
    }

    //===O MNIE===

    if (windowScrollTop > 90)
        {
        var i = 0;
        var rows = $("#about-section").find('.row');
        addClass();

        function addClass() {
            if (i < rows.length) {
                $(rows[i]).addClass('slide-content');
                i++;
                setTimeout(addClass, 400);
            }
        };
    }
    else {
        $("#about-section .row").css('opacity', '0');
    }


    //===STATISTICS===
        if (windowScrollTop > 390 && flag)
        {
            $('.counter1, .counter2, .counter3, .counter4').addClass('slide-numbers');

            $('.counter1').counterUp({
                delay: 50,
                time: 1500
            });
            $('.counter2').counterUp({
                delay: 50,
                time: 1200
            });
            $('.counter3').counterUp({
                delay: 50,
                time: 800
            });
            $('.counter4').counterUp({
                delay: 50,
                time: 400
            });
            flag=false;
        }
        else
        {
        $('.counter1, .counter2, .counter3, .counter4 ').css('opacity', '0');
        }

    //===PRICES===

        if (windowScrollTop > 790) {
            $('#prices-section .table').addClass('slide');
            setTimeout(function(){
            $("#prices-section .pricing").addClass("animated pulse");}, 3500);
        }
        else {
            $("#prices-section .table").css('opacity', '0');
        }

    //===CONTACT===
        if (windowScrollTop > 1190 && flag2) {
            var r = $("#fadeIn");
            r.css({ "opacity":"0"});
            r.fadeTo(6000,1);
            flag2 = false;
            setTimeout(function(){
            $("#contact-section .pulseit").addClass("animated pulse");}, 4500);
        }
        else if (windowScrollTop < 1190 && !flag2) {
            $("#fadeIn").css('opacity', '0');
            }
    });
//to here
});
