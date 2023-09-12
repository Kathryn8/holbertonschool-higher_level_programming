const clicker = document.body.querySelector("#update_header")
const heading = document.body.querySelector("header")

clicker.addEventListener("click", () => {
  heading.innerHTML = "New Header!!!"
})