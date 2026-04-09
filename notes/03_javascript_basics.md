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

## Arrays

Arrays hold ordered lists of values and come with many built-in methods for transforming data.

```javascript
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const total = numbers.reduce((sum, n) => sum + n, 0);

console.log(doubled); // [2, 4, 6, 8, 10]
console.log(evens);   // [2, 4]
console.log(total);   // 15
```

`map` transforms each element, `filter` keeps elements matching a condition, and `reduce` combines all elements into a single value.

## Objects

Objects store key-value pairs and model real-world entities.

```javascript
const person = {
  name: "Sam",
  age: 30,
  greet() {
    return `Hi, I'm ${this.name}`;
  },
};

console.log(person.name);   // "Sam"
console.log(person.greet()); // "Hi, I'm Sam"
```

Destructuring lets you pull values out of objects or arrays concisely.

```javascript
const { name, age } = person;
const [first, second] = [10, 20];
```

## Conditionals and Loops

`if`/`else` branches based on a condition; loops repeat code.

```javascript
const score = 85;

if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else {
  console.log("C");
}

for (let i = 0; i < 3; i++) {
  console.log(i);
}

for (const num of [10, 20, 30]) {
  console.log(num);
}
```

## Asynchronous JavaScript
