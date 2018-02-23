function f1(event) {
    var t=$(event.target.parentNode)
 alert(t.children().first().text())
}
function f2() {
    var t=$(event.target).text()
    alert(t)

}
$(document).ready(function () {
    $("td").dblclick(f1);
    $("th").dblclick(f2);
    
})