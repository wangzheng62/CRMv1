function f1(event) {
    var t=$(event.target.parentNode)
 alert(t.children().first().text())
}
function f2() {
    var t=$(event.target).text()
    str=" "+"<input type='text' class='form-text' placeholder="+t+">"
    $("#fliter").append(str)


}
function f3() {
    var t=$(event.target).val()
    alert(t)

}
function f4() {

  $(event.target).remove()

}
function selected(event) {

     var t=$(event.target.parentNode);
     t.toggleClass("selected")

}
function page(event) {

    var t=$(event.target).text();
    $("tr").addClass("selected");
    $("tr:first").removeClass("selected");
    $('tr').eq(t).removeClass("selected")

}
$(document).ready(function () {

    $("body").on("dblclick","td",f1);
    $("body").on("click","td",selected);
    $("body").on("dblclick","th",f2);
    $("body").on("change",":text",f3);
    $("body").on("dblclick",":text",f4);
    $("body").on("click","li",page);
    $("tr").addClass("selected");
    $("tr:first").removeClass("selected");

    
})