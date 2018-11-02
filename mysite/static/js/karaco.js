$(document).ready(function() {


  $("#btnSearch").click(function() {
    
    
      $("#search").fadeToggle(0, function(){

        if($('#search').is(":visible")){
          
          $('.header_logo').css("margin-top","0px");
        }
        else{
          
          $('.header_logo').css("margin-top","34px");
          
        }


      });


  });


});
