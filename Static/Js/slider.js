let images=document.querySelectorAll('.img');
let next=document.querySelector('#next')
let pre=document.querySelector('#pre')
const dots = document.querySelectorAll('.form-check-input');
const slider = document.querySelector('.slider'); 

let count=0;
let slideInterval;

images.forEach((slide,i)=>{
 slide.style.left = ` ${i * 100}% `;
}) ;

function slide_images(){

images.forEach((v)=>{
    v.style.transform=`translateX(-${count * 100}%)`

  dots.forEach((dot, i) => {
    dot.checked =  (i === count); 
   
  });
})
}



next.addEventListener("click",()=>{
    count++;
    slide_images()
if ( count >= images.length ) {
    count--;
    slide_images()
} 
})
pre.addEventListener("click",()=>{
    if (count >= 0) {
        count--;
      slide_images()
    }
 
})



dots.forEach(dot => {
    dot.addEventListener('change', () => {
    count = parseInt(dot.value); 
    slide_images();
  });
});



function startAutoSlide() {
  slideInterval = setInterval(() => {
    if (count < images.length - 1) {
      count++;
    } else {
      count = 0;
    }
    slide_images();
  }, 10000); 
}

function stopAutoSlide() {
  clearInterval(slideInterval);
}


startAutoSlide();



slider.addEventListener('mouseenter', stopAutoSlide);
slider.addEventListener('mouseleave', startAutoSlide);

