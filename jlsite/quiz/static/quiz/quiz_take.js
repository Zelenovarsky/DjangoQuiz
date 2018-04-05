$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

$( "form" ).on( "submit", function( event ) {
  event.preventDefault();
   var data1 = $(this).serialize();
   var data2 = data1.substr(data1.indexOf('question'),);
    console.log(data2);
  $.ajax({
  type: 'POST',
  url: 'quiz/results',
  data: {
  quiz_id : '{{quiz.id}}',
  user_id: '{{user.id}}',
  answers: data2
  },
  success:function(response){
    console.log(response);

    }
  });

});



