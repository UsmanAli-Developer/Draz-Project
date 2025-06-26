const plus=document.querySelector(".plus");
const minus=document.querySelector(".minus");
const value=document.querySelector(".value");
 const mainImage = document.getElementById("mainImage");
  const originalSrc = mainImage.src;  


let quantity=1;


plus.addEventListener("click",()=>{
        quantity++;
        value.innerHTML= quantity;
})

minus.addEventListener("click",()=>{
     if (quantity > 1) {
    quantity--;
    value.innerHTML= quantity;
     }
})
 

 
 

  function changeMainImage(element) {
    mainImage.src = element.src;
  }

  function resetMainImage() {
    mainImage.src = originalSrc;
  }