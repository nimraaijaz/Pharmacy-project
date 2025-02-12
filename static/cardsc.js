let totalItems = 0;
let totalAmount = 0;

function addToCart(itemName, itemPrice) {
    totalItems += 1;
    totalAmount += itemPrice;

    // Update cart info display
    document.getElementById('total-items').textContent = `Total Items: ${totalItems}`;
    document.getElementById('total-amount').textContent = `Total Amount: Rs. ${totalAmount.toFixed(2)}`;

    console.log(`${itemName} added to the cart.`);
}

// Toggle cart visibility when "Cart" is clicked
document.getElementById('cart-toggle').addEventListener('click', function() {
    const cartContainer = document.getElementById('cart-container');
    // Toggle the cart container visibility
    if (cartContainer.style.display === 'none') {
        cartContainer.style.display = 'block';
    } else {
        cartContainer.style.display = 'none';
    }
});

