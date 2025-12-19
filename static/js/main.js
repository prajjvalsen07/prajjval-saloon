(function ($) {
    "use strict";

    /* Spinner */
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    /* WOW JS */
    new WOW().init();


    /* Sticky Navbar */
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-150px');
        }
    });


    /* Back to top button */
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    /* Header Carousel */
    $(".header-carousel").owlCarousel({
        items: 1,
        autoplay: true,
        smartSpeed: 1000,
        loop: true,
        dots: false,
        nav: true,
        navText: [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ]
    });


    /* Counter */
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    /* Testimonial Carousel (FIXED & STABLE) */
    var testimonialCarousel = $(".testimonial-carousel");

    testimonialCarousel.owlCarousel({
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: true,
        dots: true,
        nav: false,
        responsive: {
            0: { items: 1 },
            768: { items: 2 },
            992: { items: 3 }
        }
    });

    /* Recalculate on resize */
    $(window).on('resize', function () {
        testimonialCarousel.trigger('refresh.owl.carousel');
    });

})(jQuery);
