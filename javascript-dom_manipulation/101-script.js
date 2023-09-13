window.addEventListener("load", () => {

  const hello = document.body.querySelector("#hello");
  const button = document.body.querySelector("#btn_translate");
  let select = document.body.querySelector("#language_code");
  let value = select.value;


  async function fetchHello(value) {
    base_url = "https://hellosalut.stefanbohacek.dev/?lang="
    api_url = base_url + value
    let response = await fetch(api_url);
    let data = await response.json();
    return data;
  }

  async function displayHello(value) {
    let data = await fetchHello(value);
    hello.textContent = data.hello
  }

  button.addEventListener("click", () => {
    value = select.value;
    if (value !== "") {
      displayHello(value);
    }
  });
})
