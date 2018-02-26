function f1(event) {
    var t=$(event.target.parentNode)
 alert(t.children().first().text())
}
function f2() {
    var t=$(event.target).text();
    var n=$(event.target).attr("name");
    str=" "+"<input type='text' name="+n+"class='form-text' placeholder="+t+">";
    $("#fliter").append(str);


}
function f3() {
    var t=$(event.target).val();
    alert(t)

}
function f4() {

  $(event.target).remove()

}
function selected(event) {

     var t=$(event.target.parentNode);
     t.toggleClass("info")

}
function page(event) {

    var t=$(event.target).text();

    $("li").removeClass('active');
    $(event.target.parentNode).addClass('active');
    $("table").addClass("invisible");
    $('table').eq(t-1).removeClass("invisible");

}
function selectall() {
    $("tr:gt(0)").toggleClass('info');
    
}
$(document).ready(function () {

    $("body").on("dblclick","td",f1);
    $("body").on("click","td",selected);
    $("body").on("dblclick","th:gt(0)",f2);
    $("body").on("change",":text",f3);
    $("body").on("dblclick",":text",f4);
    $("body").on("click","li",page);
    $("body").on("click",":checkbox",selectall);

})