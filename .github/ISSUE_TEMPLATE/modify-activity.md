---
name: ✏️ Modify Existing Activity
about: Request changes to an existing extracurricular activity
title: "Modify activity: [Activity Name]"
labels: ["enhancement", "modify-activity"]
assignees: []
---

## Activity to Modify

**Current Activity Name:** 
<!-- Example: Drama Club, Math Club, Art Class -->

## Requested Changes

### What needs to be changed?
<!-- Check all that apply -->
- [ ] Activity name
- [ ] Description
- [ ] Schedule (days/times)
- [ ] Maximum participants
- [ ] Category
- [ ] Teacher/supervisor
- [ ] Location
- [ ] Other (specify below)

### Change Details

**New Activity Name (if changing):** 
<!-- Leave blank if not changing -->

**New Description (if changing):** 
<!-- Leave blank if not changing -->

**New Schedule (if changing):** 
- Days: <!-- Example: Monday, Wednesday, Friday -->
- Start Time: <!-- Example: 3:30 PM -->
- End Time: <!-- Example: 5:00 PM -->

**New Maximum Participants (if changing):** 
<!-- Example: 20 students -->

**New Category (if changing):** 
<!-- Sports, Arts, Academic, Community, Technology -->

**Other Changes:** 
<!-- Describe any other modifications needed -->

## Reason for Change

**Why is this change needed?** 
<!-- Example: Schedule conflict with other activities, room change, teacher change, etc. -->

**Impact on Current Participants:** 
<!-- Will current students be affected? Do they need to be notified? -->

## Timeline

**When should this change take effect?** 
<!-- Example: Immediately, next semester, after current session ends -->

**Priority Level:** 
<!-- High/Medium/Low -->

---

## For Copilot Agent

### Technical Requirements
- [ ] Locate the activity in `src/backend/database.py` within the `initial_activities` dictionary
- [ ] Update the specified fields while preserving existing participant data
- [ ] Ensure any schedule changes use correct 24h format in `schedule_details`
- [ ] Verify category changes are compatible with frontend filtering
- [ ] Test that existing registrations remain intact after changes
- [ ] Update both the display `schedule` string and structured `schedule_details` object

### Acceptance Criteria
- [ ] Modified activity displays updated information in the activities list
- [ ] All existing participant registrations are preserved
- [ ] Activity can still be filtered correctly if category was changed
- [ ] Schedule display shows the new times correctly formatted
- [ ] Registration functionality continues to work properly
- [ ] Changes take effect immediately when the server restarts

### Implementation Hints
- The activity key in the dictionary should not be changed unless the name is changing
- If changing the activity name, you'll need to update the dictionary key and ensure participant data follows
- Schedule changes require updating both `schedule` (display string) and `schedule_details` (structured data)
- Always preserve the `participants` array to maintain existing registrations
- Use the existing `formatSchedule` function patterns for display formatting