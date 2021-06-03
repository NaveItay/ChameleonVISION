var data_global = 0;
var donut_chart = 0;
var create_db_form_flag = 0;
$.fn.jQuerySimpleCounter = function( options ) {
		var settings = $.extend({
				start:  0,
				end:    100,
				easing: 'swing',
				duration: 400,
				complete: ''
		}, options );

		var thisElement = $(this);

		$({count: settings.start}).animate({count: settings.end}, {
		duration: settings.duration,
		easing: settings.easing,
		step: function() {
			var mathCount = Math.ceil(this.count);
			thisElement.text(mathCount);
		},
		complete: settings.complete
	});
};


$('#number1').jQuerySimpleCounter({end: 12,duration: 3000});
$('#number2').jQuerySimpleCounter({end: 55,duration: 3000});
$('#number3').jQuerySimpleCounter({end: 359,duration: 2000});
$('#number4').jQuerySimpleCounter({end: 246,duration: 2500});



	/* AUTHOR LINK */
	 $('.about-me-img').hover(function(){
					$('.authorWindowWrapper').stop().fadeIn('fast').find('p').addClass('trans');
			}, function(){
					$('.authorWindowWrapper').stop().fadeOut('fast').find('p').removeClass('trans');
			});

		function myFunction() {
				var br = document.createElement("br");
				var input = document.getElementById('inputGroupFile01');
				readXlsxFile(input.files[0]).then(function(data) {

				 if(create_db_form_flag == 0){
				 var form = document.createElement("form");
				 form.setAttribute("method", "post");
				 form.setAttribute("action", "save.php");
				 form.setAttribute("class", "save.php");
				 form.setAttribute("id", "db_form");


				 // Create an input element for Full Name
				 var game_name = document.createElement("input");
				 game_name.setAttribute("type", "text");
				 game_name.setAttribute("name", "GameName");
				 game_name.setAttribute("class", "form-control")
				 game_name.value= data[1][0];

					// Create an input element for date of birth
					var team_A = document.createElement("input");
					team_A.setAttribute("type", "text");
					team_A.setAttribute("name", "TeamA");
					team_A.setAttribute("class", "form-control");
					team_A.value= data[1][1];

					// Create an input element for emailID
					var team_B = document.createElement("input");
					team_B.setAttribute("type", "text");
					team_B.setAttribute("name", "TeamB");
					team_B.setAttribute("class", "form-control");
					team_B.value= data[1][2];

					 // Create an input element for password
					 var where_gamed_play = document.createElement("input");
					 where_gamed_play.setAttribute("type", "text");
					 where_gamed_play.setAttribute("name", "where_gamed_play");
					 where_gamed_play.setAttribute("class", "form-control");
					 where_gamed_play.value= data[1][3];

						// Create an input element for retype-password
						var date_of_game = document.createElement("input");
						date_of_game.setAttribute("type", "text");
						date_of_game.setAttribute("name", "date_of_game");
						date_of_game.setAttribute("class", "form-control");
						date_of_game.value= data[1][4];


						// Create an input element for retype-password
						var weather = document.createElement("input");
						weather.setAttribute("type", "text");
						weather.setAttribute("name", "Weather");
						weather.setAttribute("class", "form-control");
						weather.value= data[1][5];

						// Create an input element for retype-password
						var ball_in_acc_team_a = document.createElement("input");
						ball_in_acc_team_a.setAttribute("type", "text");
						ball_in_acc_team_a.setAttribute("name", "ball_in_acc_team_a");
						ball_in_acc_team_a.setAttribute("class", "form-control");
						ball_in_acc_team_a.value= data[1][6];

						// Create an input element for retype-password
						var ball_in_acc_team_b = document.createElement("input");
						ball_in_acc_team_b.setAttribute("type", "text");
						ball_in_acc_team_b.setAttribute("name", "ball_in_acc_team_b");
						ball_in_acc_team_b.setAttribute("class", "form-control");
						ball_in_acc_team_b.value= data[1][7];

						var ball_out_acc_team_a = document.createElement("input");
						ball_out_acc_team_a.setAttribute("type", "text");
						ball_out_acc_team_a.setAttribute("name", "ball_out_acc_team_a");
						ball_out_acc_team_a.setAttribute("class", "form-control");
						ball_out_acc_team_a.value= data[1][8];


						var ball_out_acc_team_b = document.createElement("input");
						ball_out_acc_team_b.setAttribute("type", "text");
						ball_out_acc_team_b.setAttribute("name", "ball_out_acc_team_b");
						ball_out_acc_team_b.setAttribute("class", "form-control");
						ball_out_acc_team_b.value= data[1][9];
							 // create a submit button
						 var s = document.createElement("input");
						 s.setAttribute("type", "submit");
						 s.setAttribute("value", "Submit");
						 s.setAttribute("class", "btn btn-primary");
						 s.setAttribute("onclick", "show_pop_up()")

						 // Append the full name input to the form
						 form.appendChild(game_name);

						 // Inserting a line break
						 form.appendChild(br.cloneNode());

						 // Append the DOB to the form
						 form.appendChild(team_A);
						 form.appendChild(br.cloneNode());

						 // Append the emailID to the form
						 form.appendChild(team_B);
						 form.appendChild(br.cloneNode());

						 // Append the Password to the form
						 form.appendChild(where_gamed_play);
						 form.appendChild(br.cloneNode());

						 // Append the ReEnterPassword to the form
						 form.appendChild(date_of_game);
						 form.appendChild(br.cloneNode());

						 // Append the ReEnterPassword to the form
						 form.appendChild(weather);
						 form.appendChild(br.cloneNode());

						 // Append the ReEnterPassword to the form
						 form.appendChild(ball_in_acc_team_a);
						 form.appendChild(br.cloneNode());

						 // Append the ReEnterPassword to the form
						 form.appendChild(ball_in_acc_team_b);
						 form.appendChild(br.cloneNode());

						 // Append the ReEnterPassword to the form
						 form.appendChild(ball_out_acc_team_a);
						 form.appendChild(br.cloneNode());

						 // Append the ReEnterPassword to the form
						form.appendChild(ball_out_acc_team_b);
						form.appendChild(br.cloneNode());

						 // Append the submit button to the form
						form.appendChild(s);
						document.getElementById("model_body").appendChild(form);
						create_db_form_flag++;
					}
				});
			}

			function show_pop_up(){
				var popup = document.getElementById("myPopup");
				popup.classList.toggle("show");

				if(popup.classList.contains("show")) // Check if the popup is shown
				setTimeout(() => popup.classList.remove("show"), 2500) // If yes hide it after 10000 milliseconds
			}

			window.onload=function(){
				var input = document.getElementById('inputGroupFile01');
				input.addEventListener('change', function() {
					readXlsxFile(input.files[0]).then(function(data) {
						data_global = data;
						var i = 0;
						choose = 'doughnut';
						data.map((row, index) => {
							if (i == 0) { // is the first row, its the headres
								var table = document.getElementById('tbl-data')
								generateTableRows(table, row, i ,choose);
							}
							if (i > 0) {
								var table = document.getElementById('tbl-data');
								generateTableRows(table, row, i, choose);
							}
							++i;
						});
						displayChart(data, choose, 'my_donut_chart');
						$('#number1').jQuerySimpleCounter({
							end: data[1][6],
							duration: 3000
						});
						// var number1 = document.getElementById('number1');
						// number1.innerHTML = number1.value + "%";
						$('#number2').jQuerySimpleCounter({
							end: data[1][8],
							duration: 3000
						});
						$('#number3').jQuerySimpleCounter({
							end: data[1][7],
							duration: 2000
						});
						$('#number4').jQuerySimpleCounter({
							end: data[1][9],
							duration: 2500
						});
						let team_a_ball_in = document.getElementById("team_a_ball_in");
						team_a_ball_in.innerHTML = data[1][1] + " ball in (%)";

						let team_b_ball_in = document.getElementById("team_b_ball_in");
						team_b_ball_in.innerHTML = data[1][2] + " ball in (%)";

						let team_a_ball_out = document.getElementById("team_a_ball_out");
						team_a_ball_out.innerHTML = data[1][1] + " ball out (%)";

						let team_b_ball_out = document.getElementById("team_b_ball_out");
						team_b_ball_out.innerHTML = data[1][2] + " ball out (%)";
						// ctx.fillText(data[1][7].value + "%", 100,100, 200);
						let h1_first_team = document.getElementById("h1_first_team");
						h1_first_team.innerHTML = data[1][1];
						h1_first_team.style.display = "block";
						let h1_second_team = document.getElementById("h1_second_team");
						h1_second_team.innerHTML = data[1][2];
						h1_second_team.style.display = "block";

					});
				});



				function generateTableRows(table, data, i, choose) {
					let id = 1;
					let newRow = table.insertRow(-1);
					data.map((row, index) => {
						if (i != 0) {
							let newcell = newRow.insertCell();
							let newText = document.createTextNode(row)
							newcell.setAttribute("id", id);
							newcell.appendChild(newText);
							id++;
						}
						let canvas = document.getElementById("my_bar_chart");
						if(choose == 'doughnut'){
						 canvas = document.getElementById("my_donut_chart");
						}
						canvas.style.display = "block";
						let stats = document.getElementById("projectFacts");
						stats.style.display = "block";
						let excel_file_table = document.getElementById("tbl-data");
						excel_file_table.style.display = "block";
						let save_data_button = document.getElementById("save_data");
						save_data_button.style.display = "block";
						let list = document.getElementById("list");
						list.style.display = "block";
					});
				}

				function generateTableHead(table, data) {
					let thead = table.createTHead();
					let row = thead.insertRow();
					for (let key of data) {
						let th = document.createElement('thead');
						// th.classList.add("table-dark");
						let text = document.createTextNode(key);
						th.appendChild(text);
						row.appendChild(th);
					}
				}
				function ifChooseChange(lsat_choose, current_choose){
					if(lsat_choose != current_choose){
						return true;
					} else{
						return false;
					}
				}
			}

			function displayChart(data,choose,id){
				let ctx = document.getElementById(id);
				if(choose == "doughnut"){
					var bar_chart = document.getElementById('my_bar_chart');
					bar_chart.style.display = "none";
					var rader_chart = document.getElementById('my_radar_chart');
					rader_chart.style.display = "none";
					ctx.style.display = "block";
					dataArray = [data[1][6], data[1][7], data[1][8], data[1][9]];
				} else{
					if(choose == "bar"){
					var donut_chart = document.getElementById('my_donut_chart');
					donut_chart.style.display = "none";
					var rader_chart = document.getElementById('my_radar_chart');
					rader_chart.style.display = "none";
					ctx.style.display = "block";
					dataArray = [data[1][6], data[1][7], data[1][8], data[1][9] , 0];
				} else {
					var donut_chart = document.getElementById('my_donut_chart');
					donut_chart.style.display = "none";
					var bar_chart = document.getElementById('my_bar_chart');
					bar_chart.style.display = "none";
					ctx.style.display = "block";
				}
				}
				// ctx.style.display = 'none';

				let myChart = new Chart(ctx, {
					title: {
						verticalAlign: "center"
					},
					type: choose,
					data: {
						labels: [data[1][1] +': '+'ball in', data[1][2] +': '+'ball in', data[1][1] +': '+'ball out',data[1][2] +': '+'ball out'],
						datasets: [{
							label: 'Game statistics',
							data: dataArray,
							backgroundColor: [
								'rgba(255, 99, 132,0.9)',
								'rgba(54, 162, 235, 0.9)',
								'rgba(255, 206, 86, 0.9)',
								'rgba(75, 192, 192, 0.9)',
							],
							borderColor: [
								'rgba(255, 99, 132, 1)',
								'rgba(54, 162, 235, 1)',
								'rgba(255, 206, 86, 1)',
								'rgba(75, 192, 192, 1)',
								// 'rgba(153, 102, 255, 0.2)',
								// 'rgba(255, 159, 64, 0.2)'
							],
							borderWidth: 5,
						}]
					},
					options: {
						cutoutPercentage: 60,
						scales: {
							y: {
								beginAtZero: true
							},
							pointLabels: {
							fontSize: 16
							},
						},
						tooltips: {
							callbacks: {
								label: function(tooltipItem, data) {
									return data['labels'][tooltipItem['index']] + ': ' + data['datasets'][0]['data'][tooltipItem['index']] + '%';
								}
							}
						},
						legend: {
							labels: {
								fontSize: 20
							}
						},
					}
				})

		}

			function getChoosenValue(){
				var choose = "";
				var id = "";
				var choose_value = document.getElementById("list");
				if(choose_value.value == "donut_chart"){
					choose = 'doughnut';
					id = "my_donut_chart";
				} else {
					if(choose_value.value == "bar_chart"){
					choose = 'bar';
					id = "my_bar_chart";
				} else{
					choose = 'radar';
					id = "my_radar_chart";
				}
			}
				if(choose !='choose'){
				displayChart(data_global,choose,id);
				}
			}
