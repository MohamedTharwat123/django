var isLogin="";

let txt_Email_log ;
let txt_password_log ;


$(".btn_login_form").click(function(e){

txt_Email_log = $('#txt_Email_log').val();
txt_password_log = $('#txt_password_log').val();
if($('#txt_Email_log').val() == "1111" && $('#txt_password_log').val() == "1111")
 {
           isLogin="login";
           
           
        window.localStorage.setItem('isLogin', isLogin);
     window.location = "UserProfile.html";
}
else
{
     isLogin="out";
 window.localStorage.setItem('isLogin', isLogin);
}
    
});