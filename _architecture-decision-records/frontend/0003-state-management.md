# State management library

* Status: accepted
* Deciders: ...
* Date: ...

## Context and Problem Statement

We need to decide which State Management library use for our apps. With State Management we mean a complete approach on how to hold, manage and select all important information in the runtime and allow unidirectional data flow for the app core, but NOT for individual components. Things like "is dropdown open" will be handled by internal state in the components.

## Decision Drivers

* Integrates with RxJS Observables
* Well supported
* Unidirectional flow
* Serves as a "single source of truth"
* Requiring minimal boilerplate code
* (Partial) persistence mechanism support
* DevTools support
* Support for async flows
* Easy of use Entity/CRUD data-like stuff
* Testable

## Considered Options

* NgRx Store
* NGXS
* Akita

## Decision Outcome

Chosen option: "**NGXS**". **Akita** seems not to be a fully-grown solution at the time and it is slow according to the blogposts. ***NgRx*** is much more mature than **NGXS**, it has great community support but the need to use Effects library to achieve asynchronicity makes the whole code much less readable. **NGXS** has the same features but is a newer solution than **NgRx** and it was built with asynchronousness in mind.

## Pros and Cons of the Options

### [NgRx Store](https://ngrx.io/guide/store/why)

* Good, most popular library
* Bad, super-verbose, most boilerplate of all the competitors
* Bad, need to use side-effects lib for async actions

### [NGXS](https://www.ngxs.io/)

* Good, second in popularity
* Good, built-in async actions
* Good, it has all the features
* Bad, not as good support as competitors

### [Akita](https://datorama.github.io/akita/)

* Good, 0 bugs policy
* Good, even less code than competitors (no actions)
* Bad, no async support
* Bad, slowest library

## Links <!-- optional -->

* https://dev.to/abdurrkhalid333/what-is-state-management-and-why-you-should-learn-it-3kai
* https://tsh.io/blog/angular-state-management-with-redux-pattern/
* https://blogs.perficient.com/2020/07/21/choosing-a-state-management-library-for-angular-enterprise-applications/
* https://medium.com/@vpranskunas/deep-comparison-of-state-management-solutions-in-angular-562985d4474e
