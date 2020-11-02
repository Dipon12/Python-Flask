# TEMPLATE

## Why Template?

When something like a string is returned from a function and open it in browser, browser automatically converts it to html file and shows the result. To avoid this bad practice, we can create .html files (many html pages) in a separate folder named templates and use _flask.render_template()_ function to render pages from there

`render_template("something.html")`

html + logic_implmentation = Jinja Engine

**Format To Use Variable for Jinja within HTML**
`{{ x }}`


## Template Variable

You can pass variables through template in the .html file.

`render_template("something.html",html_name = name)`

here _html_name_ is the name of the variable you will use inside html file and _name_ is the name of the variable you are passing. So inside html file the html code will look like this- 

`<h1>Hello {{ html_name }} ! You are in the Home Page!!! </h1>`

But you won't want two separate name for the same variable in two places so you should use- 

`render_template("something.html",html_name = name)` 

and inside html page-

`<h1>Hello {{ name }} ! You are in the Home Page!!! </h1>`

## Template Conditional

To implement condition, following lines is to be written inside .html file.

```
{% if display %}
<h2> This to be displayed </h2>
{% else %}
<h2>This is not being displayed</h2>
{% endif %}

```

Above, _display_ is a boolean variable passed from function. Jinja will execute the above line.

## Template Loop

To implement loop, following lines is to be written inside .html file.

```
{% for x in mylist %}
<h3> {{ x }} </h3>
{% endfor %}

```

The above loop shows each element of the list _mylist_. The Following loop shows elements of a list of dictionary. 

_my_dict = [{'name' : 'Dipon'}, {'name' : 'Srijon'}]_

```
{% for x in my_dict %}
<h4> {{ x.name }} </h4>
{% endfor %}

```

## Adding Static Files (image/JavaScript/CSS File)

For adding Image:

`<img src = "{{ url_for('static', filename='images/image.jpg') }}">`

image is stored within static folder within _image_ subdirectory

## INHERITANCE

TARGET:- Create a base template and add features to it

**Creating Base Template**

Write following line where a block has to be added. Means add this where you will add feature in child files:

`{% block blockname %} {% endblock %}`

Example:- 

```
<html>
    <head>
        <title>{% block title %} {% endblock %}</title>
    </head>

    <body>
        <h1>Base Template</h1>
        {% block content %} {% endblock %}

    </body>
</html>

```
**Creating Child Template**

Add following line to extend base template:-

`{% extends 'base.html' %} `

Use the block variables to add features. Example:- 

```
{% extends 'base.html' %}

{% block title %} The Form {% endblock %}

{% block content %}
<h1>This is a Form</h1>

<form method="POST" action="/theform">    
    <input type ="text" name="name">
    <input type ="text" name ="location">
    <input type ="submit" value = "Submit">
</form>

{% endblock %}

```

**super() Function**

You use super() function inside _{% block %}_ when you want to inherit something that is being overridden by child template. Notation:-

`{{ super }}`

## Including Content of Another Template

To include code this in the html file where you want it to include:

`{% include 'include_this.html' %}`

