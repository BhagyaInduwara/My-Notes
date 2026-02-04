# HTML Basics

HTML (HyperText Markup Language) is the standard language for describing the structure of a web page. It is not a programming language — it has no logic or loops — it just describes what content exists and how it is organized: headings, paragraphs, links, images, forms, and so on.

Every HTML file is made of elements. An element usually has an opening tag, some content, and a closing tag: `<p>Hello</p>`. Some elements are "void" elements and never have a closing tag, like `<img>` or `<br>`.

## The Minimal Document

Every HTML page should start with a doctype declaration and follow a standard skeleton. The doctype tells the browser to render the page in modern "standards mode" instead of a legacy quirks mode.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>My First Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>This is my first web page.</p>
  </body>
</html>
```
