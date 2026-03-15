# Runtime Scheduler Architecture

The runtime layer determines which registered sources are eligible to execute on a given date.

## Core rule
Source instances do not run because they exist.
They run only when:
- their schedule policy is eligible for the date
- they have a declared pipeline
- they are enabled
- they have a declared contract/family/publish target route

## Runtime cycle
1. load source instances
2. evaluate schedule eligibility
3. filter enabled sources
4. emit execution plan
5. route execution to pipeline layer
6. persist run metadata and audit

## Purpose
This prevents daily over-execution and supports long-horizon maintainability.
