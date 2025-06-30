---
name: 📝 Content/Documentation Update
about: Request updates to text, documentation, or informational content
title: "Content: [Brief description of the update needed]"
labels: ["documentation", "content"]
assignees: []
---

## Content Update Request

**What content needs to be updated?** 
<!-- Select all that apply -->
- [ ] Activity descriptions
- [ ] Page titles or headings
- [ ] Help text or instructions
- [ ] Error messages
- [ ] Documentation files
- [ ] README files
- [ ] Other (specify below)

## Current Content

**Location of content to update:** 
<!-- Example: Drama Club description, login page title, README file, etc. -->

**Current text/content:** 
<!-- Copy the current text that needs to be changed -->

```
[Paste current content here]
```

## Requested Changes

**New/Updated content:** 
<!-- What should the content say instead? -->

```
[Paste new content here]
```

**Reason for change:** 
<!-- Why does this content need to be updated? -->

## Context and Requirements

**Tone and Style:** 
<!-- Should this be formal, friendly, professional, etc.? -->

**Target Audience:** 
<!-- Students, teachers, parents, administrators -->

**Content Guidelines:** 
<!-- Any specific requirements for language, length, formatting? -->

**Urgency:** 
<!-- High/Medium/Low - how soon is this needed? -->

## Quality Assurance

**Accuracy Check:** 
<!-- Is the new content factually correct? -->
- [ ] Information is accurate and up-to-date
- [ ] Contact information is correct
- [ ] Links work properly
- [ ] Spelling and grammar are correct

**Consistency Check:** 
<!-- Does this match other content in the system? -->
- [ ] Tone matches other content
- [ ] Terminology is consistent
- [ ] Formatting follows established patterns

---

## For Copilot Agent

### Content Location Guide
- **Activity descriptions**: `src/backend/database.py` in the `initial_activities` dictionary
- **Page titles/headings**: `src/static/index.html`
- **UI text and labels**: `src/static/index.html` and `src/static/app.js`
- **Error messages**: `src/static/app.js` and `src/backend/routers/`
- **Documentation**: `docs/how-to-develop.md`, `src/README.md`, main `README.md`
- **Form placeholders/help text**: `src/static/index.html`

### Technical Tasks
- [ ] Locate the specific content in the codebase
- [ ] Update the content while preserving formatting and structure
- [ ] Ensure any dynamic content still functions correctly
- [ ] Verify links and references remain valid
- [ ] Check that updated content displays properly in the UI
- [ ] Validate that content changes don't break existing functionality

### Acceptance Criteria
- [ ] Content is updated in the correct location(s)
- [ ] Updated content displays properly in the user interface
- [ ] All links and references work correctly
- [ ] Content maintains consistent tone and style
- [ ] No formatting or display issues are introduced
- [ ] Content is grammatically correct and professional

### Implementation Guidelines
- Preserve existing HTML structure and CSS classes
- Maintain accessibility attributes (alt text, labels, etc.)
- Ensure content fits within existing UI layout constraints
- Test content display on both desktop and mobile devices
- Consider impact on different user types (students vs teachers)
- Verify content changes don't affect translations (if applicable)