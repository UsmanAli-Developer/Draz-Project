
  const checkboxes = document.querySelectorAll('.product-checkbox');
  const totalSpan = document.getElementById('selectedTotal');

  function updateSelectedTotal() {
    let total = 0;
    checkboxes.forEach(cb => {
      if (cb.checked) {
        total += parseFloat(cb.dataset.price);
      }
    });
    totalSpan.innerText = total;
  }

  checkboxes.forEach(cb => {
    cb.addEventListener('change', updateSelectedTotal);
  });


  updateSelectedTotal();

