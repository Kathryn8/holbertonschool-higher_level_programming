$(document).ready(function () {
  $('#add_item').click(function () {
    const liItem = $('<li></li>').text('Item');
    $('.my_list').append(liItem);
  });

  $('#remove_item').click(function () {
    const $list = $('.my_list');
    if ($list.children().length > 0) {
      $list.children().last().remove();
    }
  });

  $('#clear_list').click(function () {
    const $list = $('.my_list');
    $list.children().remove();
  });
});
