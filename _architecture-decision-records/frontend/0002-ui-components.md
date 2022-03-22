# Angular-compatible UI Components library

* Status: accepted
* Deciders: ...
* Date: ...

## Context and Problem Statement

We need to decide which UI Components library to use across our Angular apps.

## Decision Drivers

* Themeable
* Number and variety of existing components
* Exapandable
* Popular
* Modern

## Considered Options

* Angular Material Design
* PrimeNG

## Decision Outcome

Chosen option: "**PrimeNG**", because it has many components that are not available in **Angular Material Design** and is more elastic.

## Pros and Cons of the Options

### [Angular Material Design](https://material.angular.io/components/categories)

"Native" library supported by the Angular team itself.

* Good, well known
* Good, good documentation
* Bad, difficult themeability
* Bad, extensibility is limited

### [PrimeNG](https://www.primefaces.org/primeng/showcase/#/)

* Good, much more available components than any other library
* Good, easy themeability with CSS variables support
* Good?, advertised as "hackable"
* Good, good documentation
* Bad, worse upgradebility

## Links <!-- optional -->

* https://www.reddit.com/r/angular/comments/lq3y4b/debate_angular_material_vs_primeng/
