const display_list = document.body.querySelector("#list_movies");

async function fetchTitles() {
  const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  let data = await response.json();
  return data
}

async function display_titles() {

  let data = await fetchTitles();
  for (let i = 0; i < data.results.length; i++) {
    li = display_list.appendChild(document.createElement("li"));
    li.textContent = data.results[i].title;
  }
}

display_titles();