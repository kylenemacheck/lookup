<?php
	$target = $_REQUEST["target"];
	$connect = new mysqli('localhost', 'student', 'fredfredburger', 'nations');
        if ($connect === FALSE)
        	die('Connection failed when trying to connect to db: ' . $connect->connect_error);
        $result = $connect->query("SELECT pop, name FROM nations WHERE name like '%$target%' ORDER BY pop DESC");
	if (mysqli_num_rows($result) > 0)
        {
		print '<table border = 1>';
		print '<tr style = "color: #1f4889"><th>Name</th><th>Population</th><tr>';
	        while ($row = mysqli_fetch_assoc($result))
                {
			print '<tr style = "color: #b6b8ba">';
                	print '<td colspan=2>' . $row['name'] . '</td>';
			print '<td colspan=2>' . $row['pop'] . '</td>';
			print '</tr>';
                }
        }
        else
        	die('No country in database.');
	print '</table>';
?>
