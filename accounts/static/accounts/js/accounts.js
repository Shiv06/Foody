
// Login Form
var ShowForm= function(){
var url=$(".customlogin").attr('data-url')
  $.ajax({
    url:url,
    type:'GET',
    beforeSend: function(){
      $("#modal_login_id").modal("show")
    },
    success:function(data){
      console.log(url)
      $('#login_form_id').html(data);
    }
  });

}

// Submit Login Form using Ajax
var SubmitForm=function(e){
  e.preventDefault()
  form=$(this);
  url=form.attr('action');
  console.log(url)
  $.ajax({
    url:url,
    dataType:'json',
    type:form.attr('method'),
    data: form.serialize(),
    success:function(data){
      if(data.form_flag) {
        console.log("success")
        $('#modal_login_id').modal('hide');
      }
      else {

        $('#login_form_id').html(data.html_form);
      }

    }
  });
}

// Registration Form
var ShowRegisterForm= function(){
var url=$(this).attr('data-url')
  $.ajax({
    url:url,
    success:function(data){

      $('#register_form_id').html(data);
    }
  });

}

//  Submit Registration Form using Ajax
var SubmitRegisterForm=function(e){
  e.preventDefault()
  form=$(this);
  url=form.attr('action');

  $.ajax({
    url:url,
    dataType:'json',
    type:form.attr('method'),
    data: form.serialize(),
    success:function(data){
      if(data.form_flag) {

        $('#modal_register_id').modal('hide');
          ShowForm()
      }
      else {

        $('#register_form_id').html(data.html_form);
      }

    }
  });
}

// Assign Event for Login Form
$('.customlogin').click(ShowForm)
$("#modal_login_id").on("submit","#frm_login_id",SubmitForm);

// Assign Event for Registration Form
$('.customregister').click(ShowRegisterForm)
$("#modal_register_id").on("submit","#frm_register_id",SubmitRegisterForm);
