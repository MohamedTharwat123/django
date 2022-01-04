/* Set rates + misc */
var taxRate = 0.05;
var shippingRate = 15.00; 
var fadeTime = 300;

var subtotal;
var num=1;
var CartNumber= 4;
//increase text Number

$('.minus-btn').click( function() {
  Remove_Quantity(this);
});
//decrease text Number
$(' .plus-btn').click( function() {
  ADD_Quantity(this);
});
$('.remove-product svg').click( function() {
  removeItem(this);
});


/* Recalculate cart */
function recalculateCart()
{
   subtotal = 0;
  
  /* Sum up row totals */
  $('.product').each(function () {
    subtotal += parseFloat($(this).children('.product-line-price').text());
  });
  
  /* Calculate totals */
  var tax = subtotal * taxRate;
  var shipping = (subtotal > 0 ? shippingRate : 0);
  var total = subtotal + tax + shipping;
  
  /* Update totals display */
  $('.totals-value').fadeOut(fadeTime, function() {
    $('#cart-subtotal').html(subtotal.toFixed(2));
    $('#cart-tax').html(tax.toFixed(2));
    $('#cart-shipping').html(shipping.toFixed(2));
    $('#cart-total').html(total.toFixed(2));
    if(total == 0){
      $('.checkout').fadeOut(fadeTime);
    }else{
      $('.checkout').fadeIn(fadeTime);
    }
    $('.totals-value').fadeIn(fadeTime);
  });
}

/* Update quantity */
function ADD_Quantity(button)
{
  var productRow = $(button).parent();
     num = productRow.children('.QI').val() ;
    num++;
     var parentDIVprice = productRow.parent().children('#div_price');
  var price = parseFloat(parentDIVprice.children('.product-price').text());
    productRow.children('.QI').val(num) ;
  var quantity =  productRow.children('.QI').val();
  var linePrice = price * quantity;

    
  productRow.parent().children('.product-line-price').each(function () {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });  
}
function Remove_Quantity(button)
{
  var productRow = $(button).parent();
     num = productRow.children('.QI').val() ;
    if(num == 1){}
    else{num--;}
    
//  var price = parseFloat(productRow.parent().children('.product-price').text());
//    productRow.children('.QI').val(num) ;
//  var quantity =  productRow.children('.QI').val();
//  var linePrice = price * quantity;
      var parentDIVprice = productRow.parent().children('#div_price');
  var price = parseFloat(parentDIVprice.children('.product-price').text());
    productRow.children('.QI').val(num) ;
  var quantity =  productRow.children('.QI').val();
  var linePrice = price * quantity;
  
  productRow.parent().children('.product-line-price').each(function () {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });  
}
/* Update quantity */
function updateQuantity(quantityInput)
{
//    document.getElementById('QI').value = num;
  /* Calculate line price */
  var productRow = $(quantityInput).parent().parent();
  var price = parseFloat(productRow.children('.product-price').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;
  
  /* Update line price display and recalc cart totals */
  productRow.children('.product-line-price').each(function () {
    $(this).fadeOut(fadeTime, function() {
      $(this).text(linePrice.toFixed(2));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });  
}


/* Remove item from cart */
function removeItem(removeButton)
{
  /* Remove row from DOM and recalc cart total */
  var productRow = $(removeButton).parent().parent();
  productRow.slideUp(fadeTime, function() {
    productRow.remove();
    recalculateCart();
  });
    
    CartNumber=CartNumber-1;
    if(CartNumber == 0)
    {
       $(document).ready(function() {
       $('.totals-item').css('display', 'none');
       $('.column-labels').css('display', 'none');
        $('.checkout').css('display', 'none');   
        $('.dev-list').css('display', 'block');
       });
    }
}