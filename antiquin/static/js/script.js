// category filtering
document.addEventListener("DOMContentLoaded", function () {
  const categoryLinks = document.querySelectorAll(".category-link");
  const productItems = document.querySelectorAll(".product-item");

  categoryLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      const selectedCategory = this.getAttribute("data-category");

      // Hide all products
      productItems.forEach((item) => {
        item.style.display = 'none';
      });

      // Show products of the selected category
      const selectedCategoryItems = document.querySelectorAll(
        `.category-${selectedCategory}`
      );
      selectedCategoryItems.forEach((item) => {
        item.style.display = 'block';
      });
    });
  });
});

function setPaymentMethod(method) {
  document.getElementById("payment_method").value = method;
}

function confirmCancel() {
  let res = confirm("Are you sure you want to proceed with this action? This action cannot be undone!");

  if (res) {
    return true;
} else {
    return false;
}
}