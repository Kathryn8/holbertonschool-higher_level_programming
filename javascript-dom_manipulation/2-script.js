const special_text = document.body.querySelector("#red_header");
const header = document.body.querySelector("header");

special_text.addEventListener("click", () => {
  header.setAttribute("class", "red");
});