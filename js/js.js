jQuery(document).ready(function() {
 var lemma = $('body').attr('class') ; // what if more then one class TODO
 var writesource = 'gidig/writer.php' ; // SCRIPTROOT TODO writer.php TODO 
 var writesource = 'source/' + lemma + '.md' ; // SOURCEROOT TODO


 $('#edit').click( function() {
    $('.depot').show(); // normal you shloud move single depot contents.. but if only one...
    $('.markdown textarea').load( mdsource, function() { // ok so?
    });
 });

    $('.markdown button').click( function(event) {
        safe () ;
    });
    function safe () {
        $.ajax({
            type: "PUT", // TODO
            url: writesource ,
            data: $('.markdown textarea').val() , //+ '~comment' + $('.markdown input').val()
        }).done(function( ) {
           alert( "Data Saved" );
        });
        event.preventDefault();
    }
});
