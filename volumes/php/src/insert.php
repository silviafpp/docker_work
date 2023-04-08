<!DOCTYPE html>
<html>

<head>
	<title>Insert</title>
</head>

<body>
		<?php
		// servername => db
		// username => root
		// password => example
		// database name => user
		$conn = mysqli_connect("db", "root", "example", "user");
		
		// Check connection
		if($conn === false){
			die("ERROR: Could not connect. "
				. mysqli_connect_error());
		}
		
		// Taking all 5 values from the form data(input)
		$first_name = $_REQUEST['first_name'];
		$last_name = $_REQUEST['last_name'];
		$email = $_REQUEST['email'];
		
		// Performing insert query execution
		// here our table name is college
		$sql = "INSERT INTO user (first_name, last_name, email) VALUES ('$first_name',
        '$last_name','$email')";

		
		if(mysqli_query($conn, $sql)){
			echo "<h3>Connected Successfully.</h3>";

			echo nl2br("\n$first_name\n $last_name\n $email");
		} else{
			echo "ERROR: Hush! Sorry $sql. "
				. mysqli_error($conn);
		}
		
		// Close connection
		mysqli_close($conn);
		?>
</body>

</html>