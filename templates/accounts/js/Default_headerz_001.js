var isLogin ;
 var container ;
const menuBtn = document.querySelector(".menu_show");
const menu_hideBtn = document.querySelector(".menu_hide");
const searchBtn = document.querySelector(".search_icon");
const cancelBtn = document.querySelector(".cancel_icon");
const items = document.querySelector(".headerz_tabs");
const form = document.querySelector(".headerz_form");
const userIcon = document.querySelector(".user_icon");
const dropUser = document.querySelector(".drop_user_menu");
const dropUserLOG = document.querySelector(".drop_u_log");
const search_result = document.querySelector(".search_result");


$(document).ready(function () {
   isLogin= window.localStorage.getItem('isLogin');

});
$(".btn_drop_L").click(function(e){
         window.location = "login.html"; 
});
$(".btn_drop_S").click(function(e){
         window.location = "register.html"; 
});

$("#anc_logout").click(function(e){
     window.localStorage.setItem('isLogin', "out");
    location.reload();
});

  $(function() {
      
        var timer,
        checkScreenSize = function(){    
                            

            
        timer = setTimeout(function(){ checkScreenSize(); }, 50);
    };

checkScreenSize();
 });
        $('.user_icon').hover(
             function(){ $(".drop_u_log").addClass('active') },
            function(){ $(".drop_u_log").removeClass('active') }
         )
            $('.drop_u_log').hover(
                    function(){ $(".drop_u_log").addClass('active') },
                                   function(){ $(".drop_u_log").removeClass('active') }
            )
        $('.user_icon').hover(
             function(){ $(".drop_user_menu").addClass('active') },
            function(){ $(".drop_user_menu").removeClass('active') }
         )
         $('.drop_user_menu').hover(
            function(){ $(".drop_user_menu").addClass('active') },
            function(){ $(".drop_user_menu").removeClass('active') }
         )
                     
            if( window.localStorage.getItem('isLogin') == "login")
            {
                { $(".drop_u_log").addClass('hide') }

            }
            else if( window.localStorage.getItem('isLogin') =="out" )
            {
                { $(".drop_user_menu").addClass('hide') }

            }
else{
    { $(".drop_user_menu").addClass('hide') }
}


$(document).click(function(){ 
if( !($(".search_icon").is(":hover"))&&
    !($(".headerz_form button").is(":hover"))&&
    !($(".search_data").is(":hover"))
   )//if any of these elements have the mouse then me know the user didn't click on them
{
    form.classList.remove('active');
    search_result.classList.remove('active');
}
})

         menuBtn.onclick = ()=>{
           items.classList.add("active");
           menuBtn.classList.add("hide");
             form.classList.remove("active");
             menu_hideBtn.classList.add("show");
         }
         menu_hideBtn.onclick = ()=>{
              items.classList.remove("active");
           menuBtn.classList.remove("hide");
           searchBtn.classList.remove("hide");
           cancelBtn.classList.remove("show");
           form.classList.remove("active");
             menu_hideBtn.classList.remove("show");
         }
         cancelBtn.onclick = ()=>{
           items.classList.remove("active");
           menuBtn.classList.remove("hide");
           searchBtn.classList.remove("hide");
           cancelBtn.classList.remove("show");
           form.classList.remove("active");
         }
         searchBtn.onclick = ()=>{
           form.classList.add("active");
           search_result.classList.add("active");
         }
         
         
var slider = document.getElementById('slider'),
    sliderItems = document.getElementById('items'),
    prev = document.getElementById('prev'),
    next = document.getElementById('next');

slide(slider, sliderItems, prev, next);

function slide(wrapper, items, prev, next) {
  var posX1 = 0,
      posX2 = 0,
      posInitial,
      posFinal,
      threshold = 100,
      slides = items.getElementsByClassName('slide'),
      slidesLength = slides.length,
      slideSize = items.getElementsByClassName('slide')[0].offsetWidth,
      firstSlide = slides[0],
      lastSlide = slides[slidesLength - 1],
      cloneFirst = firstSlide.cloneNode(true),
      cloneLast = lastSlide.cloneNode(true),
      index = 0,
      allowShift = true;
  
  // Clone first and last slide
  items.appendChild(cloneFirst);
  items.insertBefore(cloneLast, firstSlide);
  wrapper.classList.add('loaded');
  
  // Mouse and Touch events
  items.onmousedown = dragStart;
  
  // Touch events
  items.addEventListener('touchstart', dragStart);
  items.addEventListener('touchend', dragEnd);
  items.addEventListener('touchmove', dragAction);
  
  // Click events
  prev.addEventListener('click', function () { shiftSlide(-1) });
  next.addEventListener('click', function () { shiftSlide(1) });
  
  // Transition events
  items.addEventListener('transitionend', checkIndex);
  
  function dragStart (e) {
    e = e || window.event;
    e.preventDefault();
    posInitial = items.offsetLeft;
    
    if (e.type == 'touchstart') {
      posX1 = e.touches[0].clientX;
    } else {
      posX1 = e.clientX;
      document.onmouseup = dragEnd;
      document.onmousemove = dragAction;
    }
  }

  function dragAction (e) {
    e = e || window.event;
    
    if (e.type == 'touchmove') {
      posX2 = posX1 - e.touches[0].clientX;
      posX1 = e.touches[0].clientX;
    } else {
      posX2 = posX1 - e.clientX;
      posX1 = e.clientX;
    }
    items.style.left = (items.offsetLeft - posX2) + "px";
  }
  
  function dragEnd (e) {
    posFinal = items.offsetLeft;
    if (posFinal - posInitial < -threshold) {
      shiftSlide(1, 'drag');
    } else if (posFinal - posInitial > threshold) {
      shiftSlide(-1, 'drag');
    } else {
      items.style.left = (posInitial) + "px";
    }

    document.onmouseup = null;
    document.onmousemove = null;
  }
  
  function shiftSlide(dir, action) {
    items.classList.add('shifting');
    
    if (allowShift) {
      if (!action) { posInitial = items.offsetLeft; }

      if (dir == 1) {
        items.style.left = (posInitial - slideSize) + "px";
        index++;      
      } else if (dir == -1) {
        items.style.left = (posInitial + slideSize) + "px";
        index--;      
      }
    };
    
    allowShift = false;
  }
    
  function checkIndex (){
    items.classList.remove('shifting');

    if (index == -1) {
      items.style.left = -(slidesLength * slideSize) + "px";
      index = slidesLength - 1;
    }

    if (index == slidesLength) {
      items.style.left = -(1 * slideSize) + "px";
      index = 0;
    }
    
    allowShift = true;
  }
}



