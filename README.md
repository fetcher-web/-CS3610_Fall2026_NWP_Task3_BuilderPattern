# Task 3 - Builder Design Pattern 

## Assignment Overview

Design Patterns Module - Assignment 1: Creational Patterns

This project demonstrates the implementation of the Builder
Design Pattern in Python by constructing Customer objects
with mandatory and optional fields.

## Implementation

The project contains the following components:

- Customer - The product containing customer information.
- CustomerBuilder - The abstract builder interface.
- WebAppBuilder - Constructs customers with all seven fields.
- MobileAppBuilder - Constructs customers with mandatory fields only.
- Director - Manages the construction process.
- Client (main.py) - Demonstrates both concrete builders.

## Customer Fields

| Field | WebAppBuilder | MobileAppBuilder |
|---|---|---|
| First Name | Yes | Yes |
| Middle Name | Optional | No |
| Last Name | Yes | Yes |
| Primary Email | Yes | Yes |
| Secondary Email | Optional | No |
| Primary Mobile Number | Yes | Yes |
| Secondary Mobile Number | Optional | No |

## Construction Order

1. firstName
2. middleName
3. lastName
4. primaryEmail
5. secondaryEmail
6. primaryMobileNumber
7. secondaryMobileNumber

## UML Class Diagram

Unfortunately, I ran into some issues while installing png of my UML class diagram, but I have completeversion of it in PDF version that is going to be attatched to this Lab assignment as separate file.

## How to Run

Python 3 is required. No external libraries are necessary.

```bash
python main.py
```

## Testing

The implementation was tested for:

- Construction using both concrete builders.
- Automatic builder reset.
- Missing optional fields.
- Missing mandatory fields.
- Abstract interface enforcement.