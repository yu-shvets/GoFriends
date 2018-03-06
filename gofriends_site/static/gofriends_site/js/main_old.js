$('#customer_form').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        url: form.attr('action'),
        method: 'post',
        data: form.serialize(),

        success: function (json) {
            console.log('Hello!');
            $('#success').text(json.success);
            form.each(function(){
            this.reset();
            });
        }
    });
});



