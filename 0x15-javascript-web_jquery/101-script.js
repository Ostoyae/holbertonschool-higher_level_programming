window.onload = function () {
    let add = document.querySelector("DIV#add_item");
    let remove = document.querySelector("DIV#remove_item");
    let clear = document.querySelector("DIV#clear_list");
    let list = document.querySelector("UL.my_list");
    // let count = 0;

    add.addEventListener("click", () => {
        // alert("why you do that?!");
        let item = document.createElement("li");
        item.innerHTML = "Item";
        // item.value = count++;
        list.appendChild(item);
    });
    remove.addEventListener("click", () => {
        // alert("wait that's mine?!");
        list.removeChild(list.lastChild);
    });
    clear.addEventListener("click", () => {
        // alert("NOOOOoooooooo!!!!");
        list.innerHTML = "";
    });
};