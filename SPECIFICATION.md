# Kudos System Specification

## Project Overview

The Kudos System allows employees to recognize and appreciate their colleagues through public messages of appreciation.

Employees can send kudos to coworkers, and all approved kudos will appear on a public dashboard feed.

---

# Functional Requirements

## User Story 1: Send Kudos

As an employee,

I want to select a colleague and send them a message of appreciation,

so that I can publicly recognize their contributions.

### Acceptance Criteria

- User can select another employee from a list.
- User can write a short appreciation message.
- User can submit the kudos.
- Kudos is saved successfully.

---

## User Story 2: View Kudos Feed

As an employee,

I want to view recent kudos on the dashboard,

so that I can see employee achievements and recognition.

### Acceptance Criteria

- Dashboard displays recent kudos.
- Feed displays:
  - Sender Name
  - Recipient Name
  - Message
  - Date Created

---

## User Story 3: Moderate Kudos

As an administrator,

I want to hide or delete inappropriate kudos,

so that the public feed remains professional.

### Acceptance Criteria

- Administrator can view all kudos.
- Administrator can hide a kudos message.
- Administrator can delete a kudos message.
- Hidden kudos do not appear in the public feed.

---

# Non-Functional Requirements

- System must load dashboard feed within 2 seconds.
- System must support at least 1000 kudos entries.
- System must require authenticated users.
- System must record audit timestamps.

---

# Technical Design

## Database Schema

### Users Table

| Field | Type |
|---------|---------|
| id | Integer |
| name | String |
| email | String |

---

### Kudos Table

| Field | Type |
|---------|---------|
| id | Integer |
| sender_id | Integer |
| recipient_id | Integer |
| message | Text |
| created_at | Timestamp |
| is_visible | Boolean (Default True) |

---

# API Endpoints

## Create Kudos

POST

```http
/api/kudos
```

Request:

```json
{
  "recipient_id": 2,
  "message": "Great job helping with the client deployment."
}
```

---

## Get Kudos Feed

GET

```http
/api/kudos
```

Returns all visible kudos ordered by newest first.

---

## Hide Kudos

PATCH

```http
/api/kudos/{id}/hide
```

Sets:

```json
{
  "is_visible": false
}
```

---

## Delete Kudos

DELETE

```http
/api/kudos/{id}
```

---

# Approval

Specification reviewed and approved.

Status: APPROVED



## github repository url
https://github.com/Saifuddink78/datacom-kudos-system