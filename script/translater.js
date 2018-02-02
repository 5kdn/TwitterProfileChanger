$(function () {

  var DEFAULTVAL = {};
  DEFAULTVAL.name = $('input.textbox.name').attr('placeholder');
  DEFAULTVAL.description = $('input.textbox.description').attr('placeholder');
  DEFAULTVAL.location = $('input.textbox.location').attr('placeholder');

  // change detector
  $('input.textbox').on('keypress change paste', ()=>{
    if ( DEFAULTVAL.name        != null
      && DEFAULTVAL.description != null
      && DEFAULTVAL.location    != null
      && DEFAULTVAL.name        == $('input.textbox.name').val()
      && DEFAULTVAL.description == $('input.textbox.description').val()
      && DEFAULTVAL.location    == $('input.textbox.location').val()
    ) {
      $('button.button.submit').attr('disabled', true);
    }else{
      $('button.button.submit').removeAttr('disabled');
    }
  });




  function getStatus() {
    $.getJSON('/getStatus', null)
      .then(
      function (data) {
        console.log(data);
        $('input.textbox.name').val(data['nam']);
        $('input.textbox.description').val(data['des']);
        $('input.textbox.location').val(data['loc']);

        $('#screen').text(data['nam']);
        $('#Card-des').text(data['des']);
        $('#Card-location').text(data['loc']);

        DEFAULTVAL.name = data['nam'];
        DEFAULTVAL.description = data['des'];
        DEFAULTVAL.location = data['loc'];
      },
      function (data, status) {
        console.log('取得失敗');
        console.log(status);
      }
    );
  }


  function setStatus() {
    // submit buttonがdisabledのときは実行しない
    if ($('button.button.submit').is(':disabled') ) return false;

    $('button.button.submit').attr('disabled', true);
    // set transrate data
    var data = {};
    if (DEFAULTVAL.name != $('input.textbox.name').val()) data['name'] = $('input.textbox.name').val()
    if (DEFAULTVAL.description != $('input.textbox.description').val()) data['description'] = $('input.textbox.description').val()
    if (DEFAULTVAL.location != $('input.textbox.location').val()) data['location'] = $('input.textbox.location').val()
    if ($('input#allow_tweet').is(':checked')) data['tweet'] = true;


    console.log(JSON.stringify(data));
    $.ajax({
      url: '/setStatus',
      type: 'POST',
      data: JSON.stringify(data),
      dataType: 'json',
      contentType: 'application/json; charset=utf-8'
    })
    .then( (data) => {
      // success
      console.log('送信成功');
      $('input.textbox.name').val(data['nam']);
      $('input.textbox.description').val(data['des']);
      $('input.textbox.location').val(data['loc']);

      $('#screen').text(data['nam']);
      $('#Card-des').text(data['des']);
      $('#Card-location').text(data['loc']);
      DEFAULTVAL.name = data['nam'];
      DEFAULTVAL.description = data['des'];
      DEFAULTVAL.location = data['loc'];
    })
    .catch( () => {console.log('送信失敗')} )
    .then( () =>{
      // allways
      $('button.button.submit').removeAttr('disabled');
    } );
  }

  $('button.button.submit').on('click', () =>
  setStatus());
  return false;
});
