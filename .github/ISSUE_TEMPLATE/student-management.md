---
name: 👥 Student Management
about: Request changes related to student registrations and activity management
title: "Student Management: [Brief description]"
labels: ["enhancement", "student-management"]
assignees: []
---

## Request Type

**What type of student management task is needed?** 
<!-- Select one -->
- [ ] Bulk register students for an activity
- [ ] Transfer students between activities
- [ ] Remove students from activities
- [ ] Update student information
- [ ] Generate activity rosters
- [ ] Other (specify below)

## Activity Information

**Activity Name:** 
<!-- Which activity is this related to? -->

**Current Enrollment:** 
<!-- How many students are currently registered? -->

**Capacity:** 
<!-- What is the maximum capacity for this activity? -->

## Student Details

### For Registration/Transfer Requests:
**Student Emails:** 
<!-- List the email addresses of students involved -->
```
student1@mergington.edu
student2@mergington.edu
student3@mergington.edu
```

### For Bulk Operations:
**How many students:** 
<!-- Number of students affected -->

**Source of student list:** 
<!-- Where is the list of students coming from? -->

## Requested Action

**Detailed Description:** 
<!-- Explain exactly what needs to be done -->

**Target Activity (if transferring):** 
<!-- If moving students, what activity should they be moved to? -->

**Special Requirements:** 
<!-- Any prerequisites or restrictions to consider? -->

## Timeline and Priority

**Deadline:** 
<!-- When does this need to be completed? -->

**Priority Level:** 
<!-- High/Medium/Low -->

**Notification Requirements:** 
<!-- Do students/parents need to be notified of the changes? -->

## Authorization

**Requested by:** 
<!-- Teacher name and position -->

**Principal/Admin Approval:** 
<!-- Has this been approved by administration? -->
- [ ] Yes, approved
- [ ] Pending approval
- [ ] Not required

---

## For Copilot Agent

### Technical Implementation Areas
- [ ] Activity registration logic (`src/backend/routers/activities.py`)
- [ ] Database participant management (`src/backend/database.py`)
- [ ] Frontend registration UI updates (`src/static/app.js`)
- [ ] Capacity validation and error handling
- [ ] Authentication and authorization checks

### Data Validation Requirements
- [ ] Verify all student emails follow the correct format (@mergington.edu)
- [ ] Check activity capacity limits before bulk registrations
- [ ] Validate that students aren't already registered for conflicting activities
- [ ] Ensure proper teacher authentication for student management actions
- [ ] Verify target activities exist and are available

### Implementation Steps
- [ ] Create or modify API endpoints for bulk operations
- [ ] Add proper error handling for capacity violations
- [ ] Implement transaction-like behavior for bulk operations (all succeed or all fail)
- [ ] Update frontend to show appropriate success/error messages
- [ ] Add validation for email formats and duplicate registrations
- [ ] Test edge cases (full activities, invalid emails, etc.)

### Acceptance Criteria
- [ ] Bulk operations complete successfully for valid requests
- [ ] Appropriate error messages for invalid operations
- [ ] Activity capacity limits are respected
- [ ] Student registration data is updated correctly
- [ ] UI reflects the changes immediately after completion
- [ ] System handles concurrent registration attempts gracefully

### Security and Authorization
- [ ] Only authenticated teachers can perform student management operations
- [ ] Validate teacher permissions for the specific activities involved
- [ ] Log all student management actions for audit purposes
- [ ] Prevent unauthorized access to student data
- [ ] Ensure data integrity during bulk operations