const click_here = document.body.querySelector("#add_item")
const parent = document.body.querySelector(".my_list")


click_here.addEventListener("click", () => {
  li = parent.appendChild(document.createElement("li"));
  li.textContent = "Item"
})