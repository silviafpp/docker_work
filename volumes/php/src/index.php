<!DOCTYPE html>
<html lang="en">
<head>
	<title>Registration Page</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="box">
		<div class="container">
			<h1>Registration Page</h1>
			<form action="insert.php" method="post">
				<p>
					<label for="firstName">First Name:</label>
					<input type="text" name="first_name" id="firstName">
				</p>
				<p>
					<label for="lastName">Last Name:</label>
					<input type="text" name="last_name" id="lastName">
				</p>
				<p>
					<label for="emailAddress">Email Address:</label>
					<input type="email" name="email" id="emailAddress">
				</p>
				<div class="input-field">
					<input type="submit" value="Submit">
				</div>
			</form>
		</div>
	</div>
</body>
</html>