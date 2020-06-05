const url = 'http://127.0.0.1:5060/';


function get (endpoint) {
    $(function() {
         $.ajax({
            url: url.concat(endpoint) ,
            type: "get",
            dataType: "json",
            success: function (res) {
                let social_media = JSON.parse(res.user_data.social_media_accounts);
                let edit_form = {
                    first_name: $('#first_name'),
                    last_name:  $('#last_name'),
                    age:        $('#age-form'),
                    country:    $('#country'),
                    city:       $('#city'),
                    phone_number:$('#phone-number-form'),
                    facebook: $('#facebook-form'),
                    instagram: $('#instagram-form'),
                    skype: $('#skype-form'),
                    whatsapp: $('#whatsapp-form')
                };
                let elements = {
                    fullname :    $('#user_fullname'),
                    location:     $('#location'),
                    age:          $('#age'),
                    phone_number: $('#phone_number'),
                    user_avatar:  $('#user_avatar'),
                    facebook:     $('#facebook'),
                    instagram:    $('#instagram'),
                    skype:        $('#skype'),
                    whatsapp:     $('#whatsapp'),
                };
                elements.fullname.html(res.user_data.first_name + res.user_data.last_name);
                elements.age.html(res.user_data.age);
                elements.location.html(res.user_data.city + ', ' + $( "#country option:selected" ).text());
                elements.phone_number.html(res.user_data.phone_number !== '' ? res.user_data.phone_number:'N/L');
                elements.user_avatar.attr("src", res.user_data.avatar_link);
                social_media["Skype"] !=='' ? elements.skype.attr("href", social_media["Skype"]):elements.skype.parent().remove();
                social_media["Facebook"] !=='' ? elements.facebook.attr("href", social_media["Facebook"]):elements.facebook.parent().remove();
                social_media["Instagram"] !=='' ? elements.instagram.attr("href", social_media["Instagram"]):elements.instagram.parent().remove();
                social_media["WhatsApp"] !=='' ? elements.whatsapp.attr("href", social_media["WhatsApp"]):elements.whatsapp.parent().remove();

                edit_form.first_name.val(res.user_data.first_name);
                edit_form.last_name.val(res.user_data.last_name);
                edit_form.age.val(res.user_data.age);
                edit_form.country.val(res.user_data.country);
                edit_form.city.val(res.user_data.city);
                edit_form.phone_number.val(res.user_data.phone_number);
                edit_form.facebook.val(social_media["Facebook"]);
                edit_form.whatsapp.val(social_media["WhatsApp"]);
                edit_form.skype.val(social_media["Skype"]);
                edit_form.instagram.val(social_media["Instagram"]);

                console.log(res);
                console.log(res);
            },
            error: function(jqXHR, t, e) {
                console.log(t, e);
            }
        });
    })
}



const edit = function (form, endpoint) {
    $(function() {
    $(form).submit(function(e) {
         e.preventDefault();
         $.ajax({
            url: url.concat(endpoint) ,
            type: "put",
            data : $(this).serialize(),
            success: function (res) {
                console.log(res)
            },
            error: function(jqXHR, t, e) {
                console.log(t, e);
            }
        });
    });
})
};


const upload_avatar = function () {
      $(function() {
          $('#profile_picture').change(function(){
                var formdata = new FormData();
                if($(this).prop('files').length > 0)
                {
                    const file = $(this).prop('files')[0];
                    console.log(file);
                    formdata.append("file", file);
                    console.log(formdata)
                }

          $.ajax({
              url: url.concat('upload_avatar'),
              type: "POST",
              data: formdata,
              processData: false,
              contentType: false,
              dataType: "json",
              cache:false,
              success: function (res) {
                    console.log(res);
                    if(res.status_code == 200){
                        $("#user_avatar").attr("src", res.avatar_url)
                        //$('#user_avatar').css('background-image', `url('${res.avatar_url}')`);
                    }
                },
              error: function(jqXHR, t, e) {
                console.log(t, e);
            }
          });
      });


  });
};






