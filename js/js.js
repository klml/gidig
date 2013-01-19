jQuery(document).ready(function() {
 var date = new Date();
 var lemma = $('body').attr('class') ; // what if more then one class TODO
 var lemmasource = 'source/' + lemma + '.md?v=' + Date.parse(date) ; // force reload webserver TODO SOURCEROOT 
 
 var writesource = 'source/' + lemma + '.md' ; // SOURCEROOT TODO
 var writesource = 'gidig/gidig.php' ; // SCRIPTROOT TODO writer.php TODO 
 var httptype = "POST" ;// PUT

 $('#edit').click( function() {
    $('.depot').show(); // normal you should move single depot contents.. but if only one...
    //$('.markdown textarea').val('');
    $('.markdown textarea').load( lemmasource, function() { // ok so?
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
