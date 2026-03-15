# Front-End Source Onboarding Runbook

## Objective
Register a new data source from the Streamlit control plane and drive it through the full pre-setup proof-of-concept chain.

## Required registration objects
1. Source template or source record
2. Data family
3. Canonical contract
4. Schedule policy
5. Publish target
6. Join key policy
7. Pipeline
8. Source instance

## Front-end operational sequence
1. Open the Control Plane UI
2. Seed governance defaults
3. Register or create a source from template
4. Register the pipeline preset or custom pipeline
5. Register the source instance
6. Preview the runtime plan for a valid date
7. Execute the source instance E2E
8. Verify a published artifact exists in Platinum

## Proof-of-concept rule
A fake or placeholder source is acceptable in pre-setup as long as:
- the registration path is complete
- the runtime plan can schedule the source
- the execution can produce a Platinum artifact
- all objects are audited
