
$( document ).ready(function() {
	$('.controls .carousel-control').hide();
});
 
$('.main-icon').click(function() {
    $(this).find('.expand').slideToggle("fast");
});

$('.carousel').carousel({
   interval: 3000
});