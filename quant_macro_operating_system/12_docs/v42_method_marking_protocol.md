# V42 Method Marking Protocol

Every new structural service in V42 follows this pattern:
- typed input
- stable return object
- no-op or placeholder execution
- future override point
- no business-side silent failure

This makes the whole system startable before hard implementation is completed.
