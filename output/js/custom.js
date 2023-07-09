const TIMER = "0:30";
const INIT_TIMER = "0:47";
var livesLeft = 3;
var isPrimaryMode = true;
$(document).ready(function () {
    var currentIntervalHandle;
    $("#kill").click(function () {
        livesLeft --;
        $("#lives").html(livesLeft);
        if(livesLeft == 0){
            $(this).addClass('hidden');
            isPrimaryMode = false;
            $('#game-mode').html('Stealth mode activated');
            $('#game-mode').addClass('text-primary')
            clearInterval(currentIntervalHandle);
            $('#reset').removeClass('hidden');
        } 
    });
    $("#reset").click(function () {
        $('.countdown').removeClass('text-danger');
        $(this).addClass('hidden');
        currentIntervalHandle = startTimer(TIMER);
    });
    $("tbody tr").click(function () {

        $(this).addClass('table-success');
        $(this).find('.hidden').removeClass('hidden');
        if(isPrimaryMode){
            let totalPoints = 0;
            $(".table-success .ptval").each(function () {
                var pointVal = $(this).text();
                if ($.isNumeric(pointVal)) {
                    totalPoints += parseInt(pointVal);
                }
            });
            $("#tot-points").html(totalPoints);
        }
        if($('table .hidden').length === 0){
            $('#congrats').removeClass('hidden');
            clearInterval(currentIntervalHandle);
        } else {
            $('.countdown').removeClass('text-danger');
            currentIntervalHandle = startTimer(TIMER);
        }
    });
    function startTimer(initMinuteSecs){
        var timer2 = initMinuteSecs;
        if(currentIntervalHandle !== undefined){
            clearInterval(currentIntervalHandle);
        }
        var interval = setInterval(function() {
        var timer = timer2.split(':');
        //by parsing integer, I avoid all extra string processing
        var minutes = parseInt(timer[0], 10);
        var seconds = parseInt(timer[1], 10);
        --seconds;
        minutes = (seconds < 0) ? --minutes : minutes;
        if (minutes < 0){
            clearInterval(interval);
            $('.countdown').html("Time's up!");
            $('.countdown').addClass('text-danger');
            $('#reset').removeClass('hidden');
            return;
        } 
        seconds = (seconds < 0) ? 59 : seconds;
        seconds = (seconds < 10) ? '0' + seconds : seconds;
        //minutes = (minutes < 10) ?  minutes : minutes;
        $('.countdown').html(minutes + ':' + seconds);
        timer2 = minutes + ':' + seconds;
        }, 1000);
        return interval;  
    }
    currentIntervalHandle = startTimer(INIT_TIMER);
});