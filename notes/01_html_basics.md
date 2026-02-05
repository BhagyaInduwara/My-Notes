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

The `<head>` holds metadata (title, character encoding, linked stylesheets) that is not shown directly on the page. The `<body>` holds everything the visitor actually sees.

## Headings and Paragraphs

HTML has six levels of headings, `<h1>` through `<h6>`, from most to least important. Use only one `<h1>` per page — it represents the main title.

```html
<h1>Main Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
<p>A paragraph of regular text goes inside a p tag.</p>
```

Search engines and screen readers rely on heading levels to understand a page's outline, so skipping levels (e.g. jumping from `<h1>` straight to `<h4>`) is considered bad practice.
