
function aee() {
    $.get("test01",function(e){
        $('#addproduct_button').before(e)
  });
}
$(document).ready(function () {
    $('#addproduct_button').click(aee);

})