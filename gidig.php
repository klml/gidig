<?php
/* * /
error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('error_reporting', E_ALL);
ini_set('display_startup_errors', '1');
/* */

// define all varibles from config to "$VARIABLE"-form
$ini_array = parse_ini_file("config", TRUE);
foreach ($ini_array as $ini => $value ) {
    $$ini = $value  ;
};


if ( $SCRIPT != php ) {
    header("Status: 503 Service Unavailable");
    die();
}

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

    $alwayscontent = file_get_contents( $SCRIPTROOT. '/tpl_alwaysonsite.md' );  // TODO variabler
    $htmlcontent .= markdown($alwayscontent);
    # __TITLE__ # heading in first line

    $sourcecontent = file_get_contents( $SOURCEROOT . $lemma . $MARKUPEXTENSION , true);
    $htmlcontent .= markdown($sourcecontent); // TODO ? only on generl markdown call for all?
    
    $htmlcontent .= file_get_contents( $SCRIPTROOT. '/tpl_footer.html' , true); 

    $htmlcontent = str_replace( "__LEMMA__" , $lemma , $htmlcontent);

    $writefilehandle = fopen( $WEBROOT . $lemma . $WEBEXTENSION ,"w");
    fwrite($writefilehandle, $htmlcontent); // TODO callback?

};
?>
