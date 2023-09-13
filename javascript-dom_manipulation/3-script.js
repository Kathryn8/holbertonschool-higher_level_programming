const special_text = document.body.querySelector("#toggle_header");
const header = document.body.querySelector("header");
header.setAttribute("class", "red");

special_text.addEventListener("click", () => {
  if (header.getAttribute("class") == 'red') {
    header.setAttribute("class", "green");
  } else if (header.getAttribute("class") == 'green')
    header.setAttribute("class", "red");
});