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

## Links and Images

A link is created with the anchor tag `<a>` and its `href` attribute. An image uses `<img>` with a `src` attribute and should always include `alt` text for accessibility.

```html
<a href="https://example.com">Visit Example</a>
<img src="cat.jpg" alt="A sleeping orange cat" />
```

Relative paths (`images/cat.jpg`) point to files inside your own project; absolute URLs (`https://...`) point elsewhere on the web.

## Lists

HTML supports ordered lists (`<ol>`, numbered) and unordered lists (`<ul>`, bulleted). Each item goes inside an `<li>` tag.

```html
<ul>
  <li>Milk</li>
  <li>Eggs</li>
  <li>Bread</li>
</ul>

<ol>
  <li>Preheat oven</li>
  <li>Mix ingredients</li>
  <li>Bake for 20 minutes</li>
</ol>
```

## Divs, Spans, and Semantic Tags

`<div>` and `<span>` are generic containers with no meaning of their own — `<div>` is block-level (starts on a new line), `<span>` is inline (stays within a line of text). Modern HTML also offers semantic tags that describe the role of their content: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.

```html
<header>
  <nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
  </nav>
</header>
<main>
  <article>
    <h2>Blog Post Title</h2>
    <p>Post content...</p>
  </article>
</main>
<footer>
  <p>&copy; 2026 My Site</p>
</footer>
```

Using semantic tags instead of only `<div>` everywhere improves accessibility and SEO, because both browsers and assistive technology understand what each section is for.

## Forms

Forms collect input from the user. A form is a `<form>` element wrapping input controls, and each control usually has a matching `<label>`.

```html
<form action="/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" />

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" />

  <button type="submit">Send</button>
</form>
```

The `method` attribute decides how data is sent (`GET` appends it to the URL, `POST` sends it in the request body), and `action` is the URL that receives the submission.

## Attributes

Attributes add extra information to a tag and are written as `name="value"` inside the opening tag. Common ones include `id` (a unique identifier), `class` (a reusable style/behavior hook), `src`, `href`, and `alt`.

```html
<p id="intro" class="highlight">Welcome!</p>
```

`id` should be unique per page (used for a single specific element, e.g. via JavaScript or an anchor link), while `class` can be reused across many elements (used for styling groups of elements the same way).
