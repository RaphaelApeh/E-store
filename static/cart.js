const cartBtn = document.getElementById("cart-btn")
const slug = location.pathname.split("/")[2]
const csrf = document.currentScript.dataset.csrf
document.addEventListener("DOMContentLoaded", handleAddToCart)

function handleAddToCart(event){
    cartBtn.addEventListener("click", (e)=>{
        e.preventDefault()
        fetch(`/add-cart/${slug}/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrf,
            }
        })
        .then(response=> response.json())
        .then(data=> {
            if(data.added){
                cartBtn.textContent = "Remove from Cart"
                cartBtn.style.backgroundColor = "black"
            }else{
                cartBtn.textContent = "Add to Cart"
                cartBtn.removeAttribute("style")
            }
        })
    })
}