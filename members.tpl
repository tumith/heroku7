<!DOCTYPE html>
<html lang="is">
<head>
	<meta charset="utf-8">
	<title>members</title>
	<!------------------------------------------------->
	<style>
		body{
			background-color: beige;
			margin: 3em;
		}

		h2{
			color: #a00;
			font-family: sans-serif;
		}
	</style>
	<!------------------------------------------------->
</head>
<body>
	<h1>Félagaskrá</h1>
	<p>The member team are as follows:</p>
	<table border="1">
		%for row in rows:
			<tr>
			%for col in row:
				<td>{{col}}</td>
			%end
			</tr>
		%end
	</table>
	<a href="/">Aftur á skráningarsíðu</a>
</body>
</html>