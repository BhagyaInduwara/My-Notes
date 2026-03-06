# CSS Basics

CSS (Cascading Style Sheets) controls how HTML elements look: colors, spacing, fonts, layout, and animation. HTML says *what* something is; CSS says *how it should appear*.

## Adding CSS to a Page

There are three ways to attach CSS to HTML: inline (on the element itself), internal (a `<style>` block in the `<head>`), and external (a separate `.css` file, which is the recommended approach for real projects).

```html
<link rel="stylesheet" href="styles.css" />
```

```css
/* styles.css */
body {
  font-family: sans-serif;
  margin: 0;
}
```

## Selectors

A selector decides which elements a rule applies to. The most common are the type selector (`p`), the class selector (`.highlight`), and the id selector (`#header`).

```css
p {
  color: #333;
}

.highlight {
  background-color: yellow;
}

#header {
  font-weight: bold;
}
```

Classes are the workhorse of everyday CSS because you can reuse the same class on many elements, while an id should only be used once per page.

## The Box Model

Every element is a rectangular box made of four layers, from inside out: content, padding, border, and margin. Understanding this model is essential for controlling spacing.

```css
.card {
  width: 200px;
  padding: 16px;
  border: 1px solid #ccc;
  margin: 8px;
}
```

By default, `width` only sets the content area's width, and padding/border are added on top of it. Setting `box-sizing: border-box;` makes `width` include padding and border, which is usually far less confusing.

```css
* {
  box-sizing: border-box;
}
```

## Colors and Units
