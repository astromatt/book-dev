# Application monitoring, logs collection and tracing system for frontend apps

* Status: accepted
* Deciders: ...
* Date: ...

## Context and Problem Statement

We would like to collect error logs from frontend apps that are available for the users in order to automatically detect bugs and issues on production environment

## Decision Drivers

* Self-hosted
* Support for Angular (with proper documentation)
* Allows external integration (message queue systems, Teams, e-mail, etc.)

## Considered Options

* Sentry

## Decision Outcome

Chosen option: "**Sentry**". It has all the features we need and it's the only found solution that is free.

## Pros and Cons of the Options

### [Sentry](https://ngrx.io/guide/store/why)

* Good, has all the features
