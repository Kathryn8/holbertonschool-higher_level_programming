const special_text = document.body.querySelector("#toggle_header");
special_text.setAttribute("class", "red");

special_text.addEventListener("click", () => {
  if (special_text.getAttribute("class") == 'red') {
    special_text.setAttribute("class", "green");
  } else if (special_text.getAttribute("class") == 'green')
    special_text.setAttribute("class", "red");
});