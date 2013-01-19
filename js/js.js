jQuery(document).ready(function() {
 var date = new Date();
 var lemma = window.location.pathname.split('/').pop().split('.')[0] ; // http://umija.org/howto:data2css
 var lemmasource = 'source/' + lemma + '.md?v=' + Date.parse(date) ; // force reload webserver TODO SOURCEROOT 
 
 var writesource = 'source/' + lemma + '.md' ; // SOURCEROOT TODO
 var writesource = 'gidig/gidig.php' ; // SCRIPTROOT TODO writer.php TODO 
 var httptype = "POST" ;// PUT

 $('#edit').click( function() {
    $('.depot').show(); // normal you should move single depot contents.. but if only one...
    //$('.markdown textarea').val('');
    $('.markdown textarea').load( lemmasource, function (responseText, textStatus, req) {
        if (textStatus == "error") {
          $('.markdown .lemma').val(lemma); // on 404 pages, you will got no source, its not there, try to create it
        }
    });
 });

    $('.markdown').submit( function(event) {

        event.preventDefault();

        //~ var values =  $('.markdown textarea').val() , //+ '~comment' + $('.markdown input').val()
        var values = $(this).serialize();

        $.ajax({
            url: writesource ,
            type: httptype,
            data: values,
            success: function(){
                $("#result").html('submitted successfully');
                location.reload();
            },
            error:function(){
                $("#result").html('there is error while submit');
            }
        }); 
    });
});
