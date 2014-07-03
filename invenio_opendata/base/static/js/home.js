

$(document).ready($(function(){
    /////////////////////////////////
    /*****THINGS FOR ALL PAGES******/
    /////////////////////////////////
    // $('.dropdown-toggle').dropdown();
    // $(".acc-panel").hover(function(e){
    //     e.preventDefault();
    //     $(".pnl-title").fadeOut("fast");
    //     //$(".pnl-details").fadeOut("fast");
        
    //     $(this).siblings().stop().animate({width:'10%'}, "fast");
    //     $(this).stop().animate({width: '69%'}, "fast", function(){
    //         //$(".pnl-details").fadeIn(); //css("background-color", "red");
    //         $(this).children().children().children(".pnl-details").fadeIn("fast");//css("visibility", "visible");
    //     });



    // }, function(){
    //     //$(".pnl-details").css("visibility", "hidden");
    //     $(this).children().children().children(".pnl-details").fadeOut("fast");
    //     $(".acc-panel").stop().animate({width: '25%'}, "fast", function(){

    //         $(".pnl-title").fadeIn(200);
    //     });
    // });    


    $(".fix-overflow a").hover(function(){
        $(".rltd-links ul").slideUp();
    });

    // $("textarea.extlink-sub").tagify({addTagPrompt: 'Add links'});
        // $("textarea.extlink-sub").();

    // jQuery(".tagify").tagsManager();
    // $(".fix-overflow").readmore({
    //     moreLink: '<a href="#">Read more</a>',
    //     lessLink: '<a href="#">Close</a>',
    //     embedCSS: true,
    // });
    /////////////////////////////////
    /**THINGS FOR SUBMISSION PAGES**/
    /////////////////////////////////
    

    var MaxInputs = 10;
    var AddButton = $(".add-more");
    var InputsWrapper = $(".add-more").parent();
    var x = InputsWrapper.length+2;
    var FieldCount=1;

    $(".add-more").click(function(e){
        e.preventDefault();
        if(x <= MaxInputs){
            FieldCount++;
            $(InputsWrapper).append('<div><input type="text" placeholder="Insert Data Title" name="sub-analysis-title[]"><input type="text" placeholder="Upload Data or URL" name="sub-analysis-url[]"><input type="text" placeholder="Upload Data Documentation" name="sub-analysis-doc[]"><span class="remove-me glyphicon glyphicon-remove"></span></div>');
            x++;
            $(".content").css("height", "+=50px;");
        }
        return false;
    });

    $(document).on("click",".remove-me", function(e){
        e.preventDefault();
        $(this).css("background-color", "red");
        if (x > 1){
            $(this).parent('div').remove();
            x--;
            $(".content").css("height", "-=50px;");
        }
        return false;
    });

    // jQuery(".tagify").tagsManager();

    /////////////////////////////////
    /****THINGS FOR RECORD PAGES****/
    /////////////////////////////////
    
}));

