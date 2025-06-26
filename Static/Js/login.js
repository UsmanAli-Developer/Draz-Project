const formpassword=document.querySelector("#toggle-password")
const input=document.querySelector("#input");

formpassword.addEventListener("click",()=>{


  input.type=(input.type == "password" ? "text" : "password")

   if (input.type === "password") {
    formpassword.classList.add("fa-eye-slash");
    formpassword.classList.remove("fa-eye");
  } else {
    formpassword.classList.remove("fa-eye-slash");
    formpassword.classList.add("fa-eye");
  }
})

