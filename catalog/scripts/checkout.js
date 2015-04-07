$(function() {
  $('#charge').click(function () {
    $('#message').text('Charging. . .');
    $.ajax({
      url: 'http://dithers.cs.byu.edu/iscore/api/v1/charges',
      type: 'post', 
      data: { 
        apiKey: 'bd4c3e68deac00a9d76b8646e02eb328', 
        currency: 'usd', 
        amount: $('#chargeId').val(), 
        type: 'Visa', 
        number: '4732817300654', 
        exp_month: '10', 
        exp_year: '15', 
        cvc: '411', 
        name: 'Cosmo Limesandal', 
        description: 'Charge for cosmo@is411.byu.edu',
      }, 
      dataType: 'json', 
      success: function (data) { 
        if (typeof(data['error']) !== 'undefined') {
          $('#message').html('<font style="color: red;">' + 'Failure: ' + data['error'] + '</font>');
          } else {


          $('#message').html('<font style="color: green;">' + 'New charge: ' + JSON.stringify(data) + '</font>');
          window.location.replace("/catalog/thanks");
          }
      }, 
      error: function (data) {
        $('#message').html('<font style="color: red;">' + 'Error: ' + JSON.stringify(data) + '</font>');
      } 
    }); //AJAX
  }); //CHARGE
  $('#queryCharges').click(function () {
    var queryUrl = 'http://dithers.cs.byu.edu/iscore/api/v1/charges';

    if (typeof($('#chargeId').val()) !== 'undefined') {
      queryUrl += '/' + $('#chargeId').val();
    }

    $.ajax({
      url: queryUrl,
      type: 'get', 
      data: { 
        apiKey: 'bd4c3e68deac00a9d76b8646e02eb328', 
      }, 
      dataType: 'json', 
      success: function (data) { 
        if (typeof(data['error']) !== 'undefined') {
          $('#message').html('<font style="color: red;">' + 'Failure: ' + data['error'] + '</font>');
          } else {
          $('#message').html('<font style="color: green;">' + 'New charge: ' + JSON.stringify(data) + '</font>');
          }
      }, 
      error: function (data) {
        $('#message').html('<font style="color: red;">' + 'Error: ' + JSON.stringify(data) + '</font>');
      } 
    }); //AJAX
  }); //QUERY CHARGES
});
