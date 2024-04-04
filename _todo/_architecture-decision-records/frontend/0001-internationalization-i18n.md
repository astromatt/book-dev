# Frontend apps internationalization (i18n) approach

* Status: accepted
* Deciders: ...
* Date: ...

## Context and Problem Statement

We need a way to provide intarnationalization and localization (language, datetime, number format, etc.) for our Angular frontend projects.

## Decision Drivers

* Runtime language change (without reload of the app) (?)
* Extracted text should be available to translate in external files
* Each lib/module should have its own translation files
* There should be a way to add context for translators
* Easy to maintain and use by developers
* Usable in HTML templates and in code-behind
* Pluralization
* Lazy loading of translations
* Support for localization (date, currency & number formats)

## Considered Options

* @angular/localize
* ngx-translate
* I18next (by angular-i18next)
* Locl
* Transloco

## Decision Outcome

Chosen option: "**Transloco**". It has all the features we need, it looks future-proof and community sentiment is positive.

### Positive Consequences

* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
* …

### Negative Consequences

* [e.g., compromising quality attribute, follow-up decisions required, …]
* …

## Pros and Cons of the Options

### [@angular/localize](https://angular.io/guide/i18n)

"Native" angular i18n mechanism.

* Good, "native" mechanism that will be maintained
* Bad, no per module translations
* Bad, no easy runtime language change

### [ngx-translate](https://github.com/ngx-translate/core)

* Good, it looks like it has all the mechanisms we need (but with plugins)
* Neutral, the creator of the library moved to Angular team so it may become depracated at some point
* Bad?, https://github.com/ngx-translate/core/issues/783

### [I18next (by angular-i18next)](https://github.com/Romanchuk/angular-i18next)

* Good, it has all the mechanisms

### [Locl](https://www.locl.app/)

* Bad, hard to find info about it online, there is no documentation (?)
* Bad, it looks like they want to be a paid solution
* Bad, it is still in Beta
* Good, it looks like it should have all the mechanisms we need

### [Transloco](https://github.com/ngneat/transloco)

* Good, it has all the mechanisms
* Good, it supports Server Side Rendering
* Good, it supports unit-testing
* Good, it has keys manager https://github.com/ngneat/transloco-keys-manager

## Links

* https://phrase.com/blog/posts/best-libraries-for-angular-i18n/
* https://informatykzakladowy.pl/grosza-daj-tlumaczowi
* https://angular.fun/post/2020-01-11-angular-ivy-localize/
