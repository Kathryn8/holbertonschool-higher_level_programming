window.addEventListener("load", () => {

  const add = document.body.querySelector("#add_item");
  const remove = document.body.querySelector("#remove_item");
  const clear = document.body.querySelector("#clear_list");
  const parent = document.body.querySelector(".my_list");


  add.addEventListener("click", () => {
    let li = parent.appendChild(document.createElement("li"));
    li.textContent = "Item";
  })

  remove.addEventListener("click", () => {
    if (parent.hasChildNodes()) {
      parent.removeChild(document.body.querySelector("li"));
    }
  })

  clear.addEventListener("click", () => {
    while (parent.firstChild) {
      parent.removeChild(parent.firstChild);
    }
  })
})