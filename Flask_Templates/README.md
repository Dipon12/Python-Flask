# TEMPLATE

## Why Template?

When something like a string is returned from a function and open it in browser, browser automatically converts it to html file and shows the result. To avoid this bad practice, we can create .html files (many html pages) in a separate folder named templates and use _flask.render_template()_ function to render pages from there

`render_template("something.html")`


## Template Variable

You can pass variables through template in the .html file.

`render_template("something.html",html_name = name)`

here _html_name_ is the name of the variable you will use inside html file and _name_ is the name of the variable you are passing. So inside html file the html code will look like this- 

`<h1>Hello {{ html_name }} ! You are in the Home Page!!! </h1>`

But you won't want two separate name for the same variable in two places so you should use- 

`render_template("something.html",html_name = name)` 

and inside html page-

`<h1>Hello {{ name }} ! You are in the Home Page!!! </h1>`