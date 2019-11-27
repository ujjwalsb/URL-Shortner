
$(function() {
  $('#submitURL').click(function() {
    $.ajax({
      type: "POST",
      url: "/shortlink/",
      data: {
        'url' : $('#url').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
      },
      success: returnSuccess,
      dataType: 'json'
    });
  });
});

function returnSuccess(data, textStatus, jqXHR) {
  if(data.url) {
    $('#url-message').html("<b>Shortened URL - </b>");
    $('#url-result').
      html("<a target='_blank' href='"+data.url+"'>"+data.url+"</a>");
    $('#copy').html("<span class='copy'>Copy URL</span>");
  } else {
    $('#url-result').html("<b>Please enter any URL/Link before clicking Submit</b>"); 
  }
}