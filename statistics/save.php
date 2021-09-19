<?php

$servername = "localhost";
$database = "chameleonvisiondatabase";
$username = "root";
$password = "root";


$GameName = $_POST['GameName'];
$TeamA = $_POST['TeamA'];
$TeamB = $_POST['TeamB'];
$where_gamed_play = $_POST['where_gamed_play'];
$date_of_game = $_POST['date_of_game'];
$Weather = $_POST['Weather'];
$ball_in_acc_team_a = $_POST['ball_in_acc_team_a'];
$ball_in_acc_team_b = $_POST['ball_in_acc_team_b'];
$ball_out_acc_team_a = $_POST['ball_out_acc_team_a'];
$ball_out_acc_team_b = $_POST['ball_out_acc_team_b'];

echo $GameName;
echo $TeamA;
echo $TeamB;
echo $where_gamed_play;
echo $date_of_game;
echo $Weather;
echo $ball_in_acc_team_a;
echo $ball_in_acc_team_b;
echo $ball_out_acc_team_a;
echo $ball_out_acc_team_b;

// Create connection

$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
echo "Connected failed";
die("Connection failed: " . $conn->connect_error);
} else{
echo "Connected successfully";
}

$sql= "INSERT INTO statistics(GameName, TeamA, TeamB,WhereGamePlayed,DateOfGame,Weather,AccuracyPercentageOfBallInForTeamA,AccuracyPercentageOfBallInForTeamB, AccuracyPercentageOfBallOutForTeamA,AccuracyPercentageOfBallOutForTeamB) VALUES ('$GameName','$TeamA','$TeamB','$where_gamed_play','$date_of_game','$Weather','$ball_in_acc_team_a','$ball_in_acc_team_b','$ball_out_acc_team_a','$ball_out_acc_team_b')";

$run = mysqli_query($conn ,$sql);
if($run == True){
  echo "inserted";
} else {
  echo "error in insert row";
}

mysqli_close($conn);
?>
