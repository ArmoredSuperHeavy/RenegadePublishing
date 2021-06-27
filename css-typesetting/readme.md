# Instructions

*Basic knowledge of html and css is going to be helpful here. [W3Schools](https://www.w3schools.com) has some good (free) stuff if you're a beginner.*

- Copy style.css to your computer (preferably into a dedicated folder for your typesetting project)
- Download a fic from ao3 *as an HTML file* and save it in same folder with style.css
- In example.html, look for ```<!--ADDTHIS-->``` and add code to your html document as shown. Further explanation of each element that needs to be added is below.
	- ```<link rel="stylesheet" href="style.css">``` this is the only step that is completely mandatory. When you do this, you should also delete the existing styles (```<style>...</style>```)
	- ```<div id="firstpage"></div>``` makes the metadata show up on the first *left-hand* page instead of the very first page.
	- ```<div id="titlepage">``` adds a title page. pretty self-explanatory.
	- ```<div id="toc">``` adds a table of contents. this one is a little trickier. In order for this to work, you need to 
		- add ```id="chX"``` to ALL of the chapter headings (where "X" is the chapter number). The chapter headings start out looking like this: ```<h2 class="heading">Chapter 1</h2>``` and when you're done they should look like this: ```<h2 id="ch1" class="heading">Chapter 1</h2>```
		- for each chapter you created an id for, add an entry to the toc that looks like this: ```<li><a href="#ch1">Chapter 1</a></li>```. "href" is the chapter id you created PREFIXED WITH "#". The inner text (here "Chapter 1") is the chapter heading - you can freely change this, it doesn't have to match anything.
- assuming you don't want to use the default system font, follow the instructions near the top of style.css to add your font (or fonts - you can add as many "font-face"s as you want) to the project. where to get font files is outside the scope of this document. (I've included an empty "fonts" folder as an example of where you can put fonts, but use whatever file structure you like)
- make any further adjustments to the html and css that you desire. you can preview most of the formatting by opening the html file in a browser
- once you need to start checking the pagination:
	- download the [vivliostyle](https://vivliostyle.org) command line tool (you will need to install [node.js](https://nodejs.org/en/) first - just the minimal installation is fine)
	- open a command prompt pointed to the folder containing the html and css files for your project
	- type in ```vivliostyle build "Fic File Name.html" -s A4``` and hit enter
		- ```-s A4``` sets the paper size. you can use different paper sizes - refer to the vivliostyle documentation for details.
	- this should generate a file called "output.pdf" in the same folder as the html and css files
	- if the pdf is not acceptable, continue adjusting the html and css and rebuilding until you're happy with it
- use [quantumelephant](http://quantumelephant.co.uk/bookbinder/bookbinder.html) (or whatever method of imposition you choose) to generate signatures for print
- print and bind your book!

*(css and instructions by nianeyna)*
