window.addEventListener("load", () => {
  hello = document.body.querySelector("#hello");

  async function fetchHello() {
    response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
    data = await response.json();
    return data
  }

  async function displayHello() {
    data = await fetchHello()
    hello.textContent = data.hello
  }

  displayHello()
})
