// get 5kdn's information
function getStatus() {
  $.getJSON('/getStatus')
    .done(function (data) {
      // left side
      $('div#screen').text(data['name']);
      $('span#Card-location').text(data['location']);
      $('p#Card-bio').text(data['description']);

      // input area
      $('input.textbox.name').attr('placeholder', data['name']);
      $('input.textbox.location').attr('placeholder', data['location']);
      $('input.textbox.description').attr('placeholder', data['description']);
    });
}

// ToDo:文字入力の反映
// ToDo:文字数カウント


$(document).ready(function () {
  // get 5kdn's information when page loaded
  getStatus();


  // set 5kdn's information when button clicked
  $('.button-wrapper').on('click', function (event) {
    event.preventDefault();
    // ToDo:2度押し禁止
    var name = '';
    if ($('input.textbox.name').val() != '') {
      name = $('input.textbox.name').val().serialize();
    }else{
      name = $('input.textbox.name').attr('placeholder');
    }

    var location = '';
    if ($('input.textbox.location').serialize() != '') {
      location = $('input.textbox.location').serialize();
    } else {
      location = $('input.textbox.location').attr('placeholder');
    }

    var description = '';
    if ($('input.textbox.description').serialize() != '') {
      description = $('input.textbox.description').serialize();
    } else {
      description = $('input.textbox.description').attr('placeholder');
    }

    var allow_tweet = true;
    if (!$('input#allow_tweet').prop('checked')) {allow_tweet = false;}

    var data = '{"name":"'+ name + '","location":"' + location + '","description":"' + description + '","allow_tweet":'+ allow_tweet + '}';
    alert(data);
    $.POST('/setStatus', data);
  });
});

