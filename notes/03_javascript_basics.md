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

## Data Types

JavaScript has a handful of primitive types: `string`, `number`, `boolean`, `undefined`, `null`, and `symbol`, plus the `object` type (which includes arrays and functions).

```javascript
let city = "Colombo";      // string
let count = 42;            // number
let isActive = true;       // boolean
let missing = null;        // intentional absence of value
let notSet;                // undefined
```

## Functions

A function is a reusable block of code. JavaScript supports classic function declarations, function expressions, and arrow functions.

```javascript
function add(a, b) {
  return a + b;
}

const multiply = (a, b) => a * b;

console.log(add(2, 3));      // 5
console.log(multiply(2, 3)); // 6
```

Arrow functions have a shorter syntax and, importantly, do not create their own `this` binding — they inherit `this` from the surrounding scope, which is useful inside callbacks.
