<?php
/* * /
error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('error_reporting', E_ALL);
ini_set('display_startup_errors', '1');
/* */

$ini_array = parse_ini_file("config", TRUE);
$SCRIPTROOT = $ini_array['SCRIPTROOT'] ;  // TODO in array
$SOURCEROOT = $ini_array['SOURCEROOT'] ;
$MARKUPEXTENSION = $ini_array['MARKUPEXTENSION'] ;
$WEBROOT = $ini_array['WEBROOT'] ;
$WEBEXTENSION =$ini_array['WEBEXTENSION'] ;

/*
if ( isset($script) NOT ) die();
*/


include_once "lib/markdown.php";


if ( isset($_POST['lemma']) && isset($_POST['sourcecontent']) ) {

    $lemma = $_POST['lemma'] ;
    $sourcecontent = $_POST['sourcecontent'] ;

    $writefilehandle = fopen( $SOURCEROOT . $lemma . $MARKUPEXTENSION ,"w");
    $written = fwrite($writefilehandle, $sourcecontent);
    // TODO post: commit
    if ( $written != false ) {
        echo $lemma .' with ' . $written . ' bytes was written' ;
    } else {
        header("Status: 503 Service Unavailable");
        echo "not written";
    }
}


if ( isset($lemma) || isset($_GET['lemma']) ) {
    if ( isset($_GET['lemma']) ) $lemma = $_GET['lemma'] ;

    $htmlcontent = file_get_contents( $SCRIPTROOT. '/tpl_header.html' ); 
    # __TITLE__ # heading in first line

    $sourcecontent = file_get_contents( $SOURCEROOT . $lemma . $MARKUPEXTENSION , true);
    $htmlcontent .= markdown($sourcecontent);
    
    $htmlcontent .= file_get_contents( $SCRIPTROOT. '/tpl_footer.html' , true); 

    $htmlcontent = str_replace( "__LEMMA__" , $lemma , $htmlcontent);

    $writefilehandle = fopen( $WEBROOT . $lemma . $WEBEXTENSION ,"w");
    fwrite($writefilehandle, $htmlcontent); // TODO callback?

};
?>