$(document).ready(function () {
  $("#btn_translate").click(function () {
    const lang = $("#language_code").val()
    console.log(lang)
    if (lang) {
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
        $('#hello').text(data.hello);
      });
    }
  })
})