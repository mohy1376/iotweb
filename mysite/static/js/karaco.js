$(document).ready(function() {
  $("#btnSearch").click(function() {
 
    if($("#btnSearch").offset().top < 50){

      $("#search").fadeToggle(0, function() {
        if ($("#search").is(":visible")) {
          $(".header_logo").css("margin-top", "0px");
        } else {
          $(".header_logo").css("margin-top", "34px");
        }
      });

    }
    else{
      $("html, body").animate({ scrollTop: 0 }, "slow", );
      $("#search").show(function(){
        $(".header_logo").css("margin-top", "0px");


      });  
    }


  });
});
