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
