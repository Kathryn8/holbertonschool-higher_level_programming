function addItem() {
  const liItem = $("<li></li>").text("Item");
  $(".my_list").append(liItem);
}

$("#add_item").click(addItem)