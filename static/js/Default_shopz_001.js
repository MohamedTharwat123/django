$('.view_details').click( function() {
  Get_Id(this);
});




function Get_Id(button)
{
    var productRow = $(button).parent();
    var myDataaa = productRow.data('name');
    window.location = "productDescPage.html";
}
