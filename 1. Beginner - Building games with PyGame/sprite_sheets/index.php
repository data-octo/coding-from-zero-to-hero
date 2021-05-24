<?php
include ('../../../document_functions.php');
?>

<!DOCTYPE html >
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
 <title>Computer Science With Python and Pygame</title>

	<!-- Syntax Highlighter -->
	<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/styles/shCore.min.css" />
	<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/styles/shThemeDefault.min.css" />
	<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/scripts/shCore.js"></script>
	<script async type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/scripts/shBrushPython.min.js"></script>
	<script async type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/scripts/shBrushVb.min.js"></script>
	<script async type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/scripts/shBrushCpp.min.js"></script>
	<script async type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/scripts/shBrushPlain.min.js"></script>
	<script async type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/SyntaxHighlighter/3.0.83/scripts/shBrushBash.min.js"></script>


 <link href="../../../css/mainbook.css" rel="stylesheet" type="text/css" />
 <?php include ('../../../metrics.php'); ?>
</head>
<body>
<p><a href="../../../index.php?chapter=example_code">&lt;-- Back to list of examples</a></p>

<h2>Platformer With Sprite Sheets</h2>


<p>Example code for this example can be downloaded here: <a href="spritesheet_example.zip">spritesheet_example.zip</a>

<p>A quick video of our final program is below, and at the bottom of the page is
	a video explanation of the program.

<p><iframe width="480" height="360" src="//www.youtube.com/embed/xQb3w182s7I" frameborder="0" allowfullscreen></iframe>


<p>This example shows a platformer game using <em>sprite sheets</em>. A good 2D game can
	involve a lot of graphics. Rather than create and manage a file for each image, games will
	use a large image made up of several smaller images. For example, this sprite sheet
	has multiple frames of a player character walking all in one image:

<?php figure("fig.p1_walk","p1_walk.png","<kbd>p1_walk.png</kbd> spritesheet",15,"",""); ?>

<p>The sprite sheet was downloaded from the
	``<a href="http://opengameart.org/content/platformer-art-deluxe">Platformer Art Deluxe</a>''
	package at OpenGameArt.org and was created by author
	<a href="http://opengameart.org/users/kenney">Kenney</a>. Here is another sprite sheet that
	our game uses to build the world:

<?php figure("fig.tiles_spritesheet","tiles_spritesheet.png","<kbd>tiles_spritesheet.png</kbd> spritesheet",35,"",""); ?>
<p>In addition, I've created a couple backdrops for my game. You can't interact with the backdrops,
	but I think it is more interesting to have a backdrop than just have a solid color. The backdrop
	was created using the <a href="http://sourceforge.net/projects/tiled/">Tiled Map Editor</a> and Kenney's
	<a href="http://opengameart.org/content/platformer-art-buildings">Buildings</a> sprite sheet.

<?php figure("fig.background","background_01.png","<kbd>background_01.png</kbd>",35,"",""); ?>

<p>This is the backdrop for Level 2.
<?php figure("fig.background","background_02.png","<kbd>background_02.png</kbd>",35,"",""); ?>

<p>Finally, the code! This code builds off the other platformer examples
	on this website. I've divided the code up into several files to make
	it easier to navigate.


<p>The first file just has some variables that represent constant values. It makes
	the code easier to read by using variables like <kbd>WHITE</kbd> and allows
	me to change the screen size easily.

<?php include_python_file('',"constants.py",True); ?>

 <p>This class pulls smaller images out of the large sprite sheet. Create an
 	instance of the class and pass in the file name as a parameter to the constructor. Then
 	call <kbd>getImage</kbd> with the x, y location of the upper left corner of yorur sprite
 	along with its height and width. You can use a drawing program to get the location of the
 	sprite images you are intersted in.

<?php include_python_file('',"spritesheet_functions.py",True); ?>

<p>This next file defines platforms we can jump on or run into.
	At the beginning of the file
	we create lists for each image we want to use. The lists contain the x, y
	location of the sprite, along with the width and height.
    Next is the <kbd>Platform</kbd> class that defines a non-moving platform.
    There isn't much to it. The class passes along the image x, y, width, and height
    and uses the SpriteSheet class to grab the image.

<p>If you want moving sprites, the next class <kbd>MovingPlatform</kbd> adds
	functionality to its parent class <kbd>Platform</kbd>. The class keeps track
	of its boundaries that it stays in, along with the velocity. The update is
	complex because a moving platform can 'bump' the user and move him/her. It also
	needs to keep track of how far the world has scrolled to the left or right.

<?php include_python_file('',"platforms.py",True); ?>

<p>This file defines each level in the game. There is a parent <kbd>Level</kbd> class
	that all levels should inherit from. Things that all levels have (like a list of platforms)
	are defined in this parent <kbd>Level<kbd> class. After that there is a class for each level.

<?php include_python_file('',"levels.py",True); ?>

<p>The player class. This class could be simple, but we will make this player
	have an animation as he/she moves left and right.

<?php include_python_file('',"player.py",True); ?>

<p>This is the main program to run:
<p>
<?php include_python_file('',"platform_scroller.py",True); ?>

<?php include("../../../footer.php"); ?>
</body>
</html>