const lang_list = ['ar', 'az', 'be', 'bg', 'bn', 'bs', 'cs', 'da', 'de', 'dz', 'el', 'en', 'en - gb', 'en - us', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'kk', 'km', 'ko', 'lb', 'lo', 'lt', 'lv', 'mk', 'mn', 'ms', 'my', 'ne', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'th', 'tk', 'uk', 'vi', 'zh'];

function translate() {
  const lang = $("#language_code").val()
  console.log(lang)
  if (lang_list.includes(lang)) {
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
      $('#hello').text(data.hello);
    })
  } else if (lang) {
    $('#hello').text("Sorry - not a supported language");
  }
}

$(document).ready(function () {
  $("#btn_translate").click(translate)
  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      translate();
    }
  })
})
