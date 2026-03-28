# JavaScript Basics

JavaScript is the programming language of the web browser. It makes pages interactive: responding to clicks, validating forms, fetching data, and updating content without reloading the page. It also runs outside the browser via Node.js.

## Variables

Modern JavaScript uses `let` for variables that can change and `const` for variables that cannot be reassigned. The older `var` keyword still works but has confusing scoping rules and should generally be avoided.

```javascript
let age = 25;
const name = "Alex";

age = 26; // OK, let can be reassigned
// name = "Sam"; // Error, const cannot be reassigned
```
