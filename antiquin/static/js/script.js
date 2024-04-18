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
        item.style.display = "none";
      });

      // Show products of the selected category
      const selectedCategoryItems = document.querySelectorAll(
        `.category-${selectedCategory}`
      );
      selectedCategoryItems.forEach((item) => {
        item.style.display = "block";
      });
    });
  });
});

function confirmCancel() {
  let res = confirm(
    "Are you certain you wish to proceed with this action? All associated items will be permanently removed and cannot be recovered. This action cannot be undone!"
  );

  if (res) {
    return true;
  } else {
    return false;
  }
}
