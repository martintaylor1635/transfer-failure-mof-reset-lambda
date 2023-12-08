# What is this Lambda?

This Lambda is designed to enhance the stability of the Orphan Record Continuity (ORC) process and consequently render the end-of-transfer-service obsolete. Its primary function is to ingest messages from the ehr-repo-incoming-queue Dead Letter Queue (DLQ), wherein it parses National Events Management Service (NEMS) events. Subsequently, it executes updates to the Managing Organisation Field (MOF), restoring it to the corresponding General Practitioner (GP) from their prior state.

### Required Libraries

| 📦 Library | ❓ Purpose                                                   |
|------------|-------------------------------------------------------------|
| Loguru     | Used for logging throughout the Lambda.                     |
| Urllib3    | Used for making HTTP requests, i.e. communicating with PDS. |
