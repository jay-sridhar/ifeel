QUESTION_FORMAT = """<html>
<head>
    <title>iFeel</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
    <script type="text/javascript" src="js/jquery-3.7.0.min.js"></script>
    <script type="text/javascript" src="js/custom.js"></script>
</head>
<body>   
    <h1> <a href="index.html">iFeel</a> <span class="tagline">- Your opinion matters!</span></h1>
    <h2>{question}</h2>
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Rank</th>
                <th>Answer</th>
                <th class="num">Points</th>
            </tr>
        </thead>
        <tbody>
            {answers}
        </tbody>
    </table>
    <div class="game-mode"><span id="game-mode">Normal mode</span></div>
    <div class="countdown"></div>
    <div class="btn-container"><button id="reset" class="btn btn-primary hidden">Start the timer!</button></div>
    <div class="btn-container"><button id="kill" class="btn btn-danger">Take life</button></div>
    <div id="point">Total points earned: <span id="tot-points" class="points">0</span></div>
    <div class="lives">Lives left: <span id="lives">3</span></div>
    <div id="congrats" class="hidden">Congratulations! You won!!!</div>
</body>
</html>"""
TABLE_ROW_FORMAT = """<tr>
                <td>{rank}</td>
                <td><span class="hidden">{answer}</span></td>
                <td class="num"><span class="hidden ptval">{points}</span></td>
            </tr>
            """
INDEX_HTML_FORMAT = """
<html>
<head>
    <title>iFeel</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
</head>
<body>
    <h1> iFeel <span class="tagline">- Your opinion matters!</span></h1>
    <h2> Game rules </h2>
    <p> Every team will be asked a pre-surveyed question in a round-robin fashion. If you answer all the top listed answers for that question, you win 100 points.
    <p> You have 3 lives. With every wrong answer, you lose a life. If you run out of lives without completing all the listed answers, then the following teams have the option to steal your points (in a round-robin fashion).</p>
    <p> <i> Rules for stealing</i> <br> You do not have any lives when you steal. One wrong answer, and you are out!
        <br> If you successfully complete the other team's challenge, you get 100 points.
        <br> In summary, when you successfully steal, you get 100 points (out of your turn), and the other team loses the points they earned.
        <br> Note: When playing with more than 2 teams, only the team that was asked the original question will lose points when a 'steal' is successful. If no team manages to steal, the original team will keep the points they earned.
    </p>
    <ol>{}
    </ol>
</body>
</html>"""

LIST_TEMPLATE = """\n\t\t<li><a href="{qid}.html">Question # {qid}</a></li>"""
