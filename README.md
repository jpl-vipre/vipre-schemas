# VIPRE Schemas

This repository maintains a collection of data schemas for †he **VIPRE** suite of applications. These data schemas (or
models) are used to initialize the database, build the ORM models, populate features in the `vipre-viz` application, and
track metadata/notes.

## Contents

```text
.
├── README.md                                       This document
├── models/                                         Collection of data model definitions
│   ├── vipre_schema-architecture.json              The schema for the `architecture` data model
│   └── vipre_schema-*.json                         ^ etc.
├── schema.json                                     A standard json schema document defining the data-model schemas
└── sheets/                                         The csv files extracted from collaborative google sheet used to define
    :                                                 initial data models (kept only for archive purposes; no longer used)
    ├── VIPRE Database Values - Architecture.csv    
    └── VIPRE Database Values - *.csv
```

## Schema

The schema files (`vipre_schema-<tablename>.json`) conform to the following structure:

In short:

```json5
{
  "tablename": "name of the table in database for this schema",
  "note": "explanation of this data model and its role in the database/application",
  "fields": [
    {
      "field_name": "the name used to access this field programmatically (ORM attribute, column name, etc.)",
      "key": "PK or FK if this field is used as a primary or foreign key in the db; empty otherwise",
      "short_name": "user-friendly name used to display this field's data",
      "datatype_range": "the colloquial datatype and expected range for this field",
      "sql_datatype": "the SQL datatype used to represent this field in the database",
      "example_value": "an example of the expected values for this field",
      "filtering": "how this field might be used for filtering data in the application/database",
      "computable": "whether this field can be computed \"on-the-fly\" in the backend",
      "description": "a brief description of the data captured by this field"
    }
  ]
}
```

For more detail, see the included [`schema.json`](./schema.json)
