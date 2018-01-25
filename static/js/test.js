function cc() {

    ss=$('#customer').val();
    $.post("test01",ss,function(e){
        $('#customer').attr('list',e);
        rr=$('#customer').attr("list")
        $('#customer').before(rr);
        alert("1");
    });
};
function aee() {
    $.get("test01",function(e){
        $('#addproduct_button').before(e)
  });
};
$(document).ready(function () {
    $('#addproduct_button').click(aee);
    $('#customer').change(cc);


});