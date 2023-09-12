const display_character = document.body.querySelector("#character")

async function fetchName() {
  const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
  let data1 = await response.json();
  return data1
}

async function display_character_name() {
  let data2 = await fetchName()
  display_character.textContent = data2.name
}

display_character_name()