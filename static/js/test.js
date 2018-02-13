function f1(event) {
    var t=$(event.target.parentNode)
 alert(t.children().first().text())
}
$(document).ready(function () {
    $("tr").click(f1);
    
})