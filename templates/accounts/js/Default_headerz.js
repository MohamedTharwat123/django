  $(function() {
      
        var timer,
        checkScreenSize = function(){
        if ($(window).width() > 1084){
            $(".menuz").css({
                "right":"-100%",
                "display": "none"
            });
              $(' .dropdown a').css({
                     "font-family": "Andale Mono, monospace",
                      'font-size': '21px',
                     "font-weight": "400",
              "color":"#fff"});
        }
        else if ($(window).width() <= 370){
             $('.show-menu-btn').click(function() {
              $(".menuz").css({
                  "right":"0",
                  "display": "block"
              
              });
            });
             $(' .dropdown a').css({
                     "font-family": "Andale Mono, monospace",
                     'font-size': '18px'});
        }
        else{
            $('.show-menu-btn').click(function() {
              $(".menuz").css({
                  "right":"0",
                  "display": "block"

              });
            });
        }
        timer = setTimeout(function(){ checkScreenSize(); }, 50);
    };

checkScreenSize();
          
 var sub_ul;
          $(".menuz").css({ "position": "absolute",
                                 "right": "-100%",
                                "width":"100%",
                                 "top": "0",
                              "background": "#d4d090",
                              "height": "100vh",
                               "z-index":"1",
                               "transition":"0.7s",
                              "padding":"80px 0",
                              "margin":"0",
                               "overflow-y":"auto"});
              
         
           $(".menuz").append('<div class="div_login"><a href="#"><i class="fa fa-user"></i> </a><text class="login_name">LOGIN</text></div>');
          $(".menuz").append('<li><a class="active" href="index.html">home</a></li>');
          $(".menuz").append('<li><a href="aboutus.html">about us</a></li>');
//          $(".menuz").append('<li class="submenuz"><a href="#">services</a></li>');
      
//          sub_ul = $('<ul/>').addClass('dropdown');
//          sub_ul.append('<li><a href="#">Desktop applications</a></li>');
//          sub_ul.append('<li><a href="#">Web applications</a></li>');
//          sub_ul.append('<li><a href="#">Custome software</a></li>');
//          $(".submenuz").append(sub_ul);
   
          
                       
          $(".menuz").append('<li><a href="#">how we work</a></li>');
//          $(".menuz").append('<li><a href="#">portoflio</a></li>');
          $(".menuz").append('<li><a href="#">contact us</a></li>');
          
//          $('.menuz input').css({"padding":"0 20px",
//                                             "line-height":"18px",
//                                             "text-decoration":"none",
//                                              "font-size":"20px",
//                                              "font-weight":"600",
//                                               "font-family": "Lucida Console,Monaco",
//                                             "color":"#111",
//                                            "width":"85%"});
      $('.menuz li').css({"list-style":"none",
                                             "position":"relative",
                                             "text-transform":"uppercase",
                                             "font-size":"14px",
                                             "font-weight":"400",
                                             "box-sizing":"border-box",
                                             "transition":"0.4s"});
         
         
          
         $('.menuz li a').css({"padding":"0 20px",
                                             "line-height":"18px",
                                             "text-decoration":"none",
                                              "font-size":"20px",
                                              "font-weight":"600",
                                               "font-family": "Lucida Console,Monaco",
                                             "color":"#016070",
                                            "width":"100%"});
                  
         
          $(".menuz li a:not(:only-child)").append("  ▾");
   
          $('.dropdown').css({"position":"static",
                             "background":"#152f4f",
                             "display":"none",
                             "width":"100%",
                             " line-height":"normal",
                             "text-align":"left",
                             "padding":"10px 10px",
                             "position":"relative",
                             "top":"8px"});
          
          $('.dropdown li').css({});
          
      
        
           $(' .dropdown a').css({
                     "font-family": "Andale Mono, monospace",
                      'font-size': '21px',
                     "font-weight": "400",
                    "width":"100%"});
        
          
        
          
//          $('.hide-menuz-btn').css({"position":"absolute",
//                                   "top":"40px",
//                                   "right":"40px",
//                                   "cursor":"pointer",
//                                   "font-size":"30px"});
       
        
          
          $('.hide-menuz-btn').click(function() {
          $(".menuz").css({"right":"-100%"}); });
          $('.menuz li a:not(:only-child)').click(function(e) {
          $(this).siblings('.dropdown').toggle();
              // Close one dropdown when selecting another
          $('.dropdown').not($(this).siblings()).hide();
              e.stopPropagation();});
            // Scrolling Effect
          $(window).on("scroll", function() {
                if($(window).scrollTop()) {
                      $('.nav_bar').addClass('color');
//                    $('.menu li .menuz_link').addClass("coloring");
                }
                else {
                      $('.nav_bar').removeClass('color');
//                     $('.menu li .menuz_link').removeClass("coloring");
                }
          })
      
    
$(".fa-search").click(function(){
  $("#search").addClass("expand");
});     
      
      
     $(".fa-times-circle").click(function(){
  $("#search").removeClass("expand");
});     
    
      
      
      
      
      
      
      
  
});