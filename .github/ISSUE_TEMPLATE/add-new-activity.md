---
name: 🎯 Add New Activity
about: Request to add a new extracurricular activity to the system
title: "Add new activity: [Activity Name]"
labels: ["enhancement", "new-activity"]
assignees: []
---

## Activity Details

**Activity Name:** 
<!-- Example: Robotics Club, Art Therapy, Drama Club -->

**Activity Description:** 
<!-- Brief description of what students will do in this activity -->

**Activity Category:** 
<!-- Select one: Sports, Arts, Academic, Community, Technology -->

## Schedule Information

**Days of the Week:** 
<!-- Example: Monday, Wednesday, Friday -->

**Start Time:** 
<!-- Example: 3:30 PM -->

**End Time:** 
<!-- Example: 5:00 PM -->

**Duration (if different from start/end times):** 
<!-- Optional: Example: 1.5 hours -->

## Capacity and Requirements

**Maximum Number of Participants:** 
<!-- Example: 15 students -->

**Prerequisites or Requirements:** 
<!-- Example: Must have completed Art I, or No prerequisites required -->

**Equipment Needed:** 
<!-- Example: Art supplies provided, Students bring laptops, etc. -->

## Teacher Information

**Activity Supervisor/Teacher:** 
<!-- Name and contact of the teacher who will run this activity -->

**Room/Location:** 
<!-- Where the activity will take place -->

## Additional Context

**Priority Level:** 
<!-- High/Medium/Low - how urgently is this needed? -->

**Target Start Date:** 
<!-- When should this activity be available for student registration? -->

**Any Special Considerations:** 
<!-- Anything else the developer should know? Budget constraints, special requirements, etc. -->

---

## For Copilot Agent

### Technical Requirements
- [ ] Add activity data to `src/backend/database.py` in the `initial_activities` dictionary
- [ ] Ensure schedule_details format matches existing activities (days array, start_time, end_time in 24h format)
- [ ] Verify activity category maps to existing filter system in frontend
- [ ] Test activity appears correctly in the web interface
- [ ] Verify registration functionality works for the new activity

### Acceptance Criteria
- [ ] New activity appears in the activities list on the homepage
- [ ] Activity can be filtered by the correct category
- [ ] Students can register for the activity (when logged in as teacher)
- [ ] Activity shows correct schedule, capacity, and participant information
- [ ] Activity data persists correctly in the system

### Implementation Hints
- Look at existing activities in `database.py` for the correct data structure
- The `schedule_details` object should have: `days` (array), `start_time` (24h format), `end_time` (24h format)
- The `getActivityType` function in `app.js` categorizes activities based on name and description keywords
- Test the changes by running the application locally and verifying the UI