{% extends 'shop/basic.html' %}
{% block title%} Checkout - My Awesome Cart{% endblock %}
{% block body %}
<div class="container">
    <div class="col my-4">
        <h2>Step 1 - My Awesome Cart Express Checkout - Review Your Cart Items</h2>
        <div class="my-4">
            <ul class="list-group" id="items">
            </ul>

            <nav aria-label="breadcrumb">
  <ol class="breadcrumb mt-3">
    <li class="breadcrumb-item active" aria-current="page">Your Cart Total Is <b>Rs. <span id="totalPrice"></span></b>. Enter your details below & place your order. Thanks for using My Awesome Cart!</li>
  </ol>
</nav>



            
        </div>
    </div>
    <div class="col my-4">
        <h2>Step 2 - Enter Address & Other Details:</h2>
        <form method="post" action="/shop/checkout/">{% csrf_token %}
            <input type="hidden" name="itemsJson" id="itemsJson">
            <input type="hidden" name="amount" id="amount">
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputname">Name</label>
                    <input type="text" class="form-control" id="name" name="name" placeholder="Name">
                </div>
                <div class="form-group col-md-6">
                    <label for="inputEmail4">Email</label>
                    <input type="email" class="form-control" id="email" name="email" placeholder="Email">
                </div>
            </div>
            <div class="form-group">
                <label for="inputAddress">Address</label>
                <input type="text" class="form-control" id="address1" name="address1" placeholder="1234 Main St">
            </div>
            <div class="form-group">
                <label for="inputAddress2">Address line 2</label>
                <input type="text" class="form-control" id="address2" name="address2" placeholder="Apartment, studio, or floor">
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputCity">City</label>
                    <input type="text" class="form-control" id="city" name="city">
                </div>
                <div class="form-group col-md-4">
                    <label for="inputState">State</label>
                    <input type="text" class="form-control" id="state" name="state"  placeholder="Enter State">
                </div>
                <div class="form-group col-md-2">
                    <label for="inputZip">Zip</label>
                    <input type="text" class="form-control" id="zip_code" name="zip_code">
                </div>
            </div>
            <div class="form-group">
                <label for="inputZip">Phone Number</label>
                <input type="tel" class="form-control" id="phone" name="phone">
            </div>
            <button type="submit" class="btn btn-primary">Place Order</button>
        </form>
    </div>
</div>
{% endblock %}
{% block js %}
<script>
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}
console.log(cart);
var sum = 0;
var totalPrice = 0;
if ($.isEmptyObject(cart)) {
    //if object is empty
    mystr = `<p>Your cart is empty, please add some items to your cart before checking out!</p>`
    $('#items').append(mystr);
} else {
    for (item in cart) {
        let name = cart[item][1];
        let qty = cart[item][0];
        let itemPrice = cart[item][2];
        sum = sum + qty;
        totalPrice = totalPrice + qty* itemPrice;
        mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
                    ${name}
                    <span class="badge badge-primary badge-pill">${qty}</span>
                </li>`
        $('#items').append(mystr);
    }
}
document.getElementById('cart').innerHTML = sum;
document.getElementById('totalPrice').innerHTML = totalPrice;
$('#itemsJson').val(JSON.stringify(cart));
{% if thank %}
alert('Thanks for ordering with us. Your order is is {{id}}. Use it to track your order using our order tracker');
localStorage.clear();
document.location = "/shop";
{% endif %}
$('#amount').val($('#totalPrice').html())
</script>
{% endblock %}