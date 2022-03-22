# Backend apps event scheduling approach

* Status: draft
* Date: ...

## Context and Problem Statement

Application needs to be equipped with a mechanism of scheduling tasks with task persistence
and clustered environment in mind

## Decision Drivers

* Simplicity
* Lightness
* Horizontal scaling

## Considered Options

* [Quartz](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-09.html) with [Spring](https://docs.spring.io/spring-boot/docs/2.1.18.RELEASE/reference/html/boot-features-quartz.html)
* [db-scheduler](https://github.com/kagkarlsson/db-scheduler)

## Decision Outcome

* We've decided to take a stab at db-scheduler, because of lightness and curiosity

### Positive Consequences

* simplicity
* low db schema footprint
* we might discover a simpler alternative for Quartz

### Negative Consequences

* low popularity may mean there might be undiscovered bugs we may run into
* in the long run we might be forced to switch back to Quartz

## Pros and Cons of the Options

### Quartz

* Good, because has all you need and more
* Good, it's popular and reliable support
* Bad, because persistence is heavy (11 tables)
* Bad, unfriendly abstractions - boilerplate code

### db-scheduler

https://github.com/kagkarlsson/db-schedule

* Good, because Light and simple - single table for persistence
* Good, Actively maintained
* Good, has sensible history of issue resolving
* Bad, because of low popularity - not a first choice for most other projects - quartz is the king

## Links

https://github.com/kagkarlsson/db-scheduler#faq
