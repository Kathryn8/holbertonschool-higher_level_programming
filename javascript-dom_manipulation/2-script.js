const special_text = document.body.querySelector("#red_header");

special_text.addEventListener("click", () => {
  special_text.setAttribute("class", "red");
});