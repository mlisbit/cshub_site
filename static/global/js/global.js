
$( document ).ready(function() {
	$('.controls .carousel-control').hide();
});
 
$('.main-icon').click(function() {
    $(this).find('.expand').slideToggle("fast");
});


$('.carousel').carousel({
   interval: 3000
});

//banner image carousel touchs borders on small screens
var border_touch = 730;
//initial view
if (window.innerWidth < border_touch ) {
  if ($('#myCarousel').parent().attr("class") === 'container') {
    $('#myCarousel').unwrap();
  }
}
//on resize
$(window).resize(function(){
  console.log(window.innerWidth)
  if (window.innerWidth < border_touch ) {
    if ($('#myCarousel').parent().attr("class") === 'container') {
      $('#myCarousel').unwrap();
    }
  }
  else {
    if ($('#myCarousel').parent().attr("class") !== 'container') {
      $('#myCarousel').wrap('<div class="container"></div>');
    }
  }
});