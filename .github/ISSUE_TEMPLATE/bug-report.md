---
name: 🐛 Bug Report
about: Report a problem with the activities system
title: "Bug: [Brief description of the issue]"
labels: ["bug"]
assignees: []
---

## Bug Description

**What happened?** 
<!-- Clear description of what went wrong -->

**What did you expect to happen?** 
<!-- What should have happened instead? -->

## Steps to Reproduce

1. <!-- First step -->
2. <!-- Second step -->
3. <!-- Third step -->
4. <!-- What you observed -->

## Environment Information

**When did this happen?** 
<!-- Example: During student registration, while viewing activities, etc. -->

**What browser were you using?** 
<!-- Example: Chrome, Firefox, Safari, Edge -->

**What device were you on?** 
<!-- Example: Desktop computer, tablet, smartphone -->

**Were you logged in?** 
<!-- Yes/No, and as what type of user (teacher, student, etc.) -->

## Impact Assessment

**How urgent is this?** 
<!-- Critical (system unusable), High (major functionality broken), Medium (some features affected), Low (minor cosmetic issue) -->

**Who is affected?** 
<!-- Students, teachers, administrators, everyone -->

**Current workaround (if any):** 
<!-- Is there a way to work around this problem temporarily? -->

## Additional Information

**Screenshots or error messages:** 
<!-- If applicable, add screenshots or copy any error messages you saw -->

**Additional context:** 
<!-- Any other information that might be helpful -->

---

## For Copilot Agent

### Investigation Steps
- [ ] Reproduce the issue using the provided steps
- [ ] Check browser developer console for JavaScript errors
- [ ] Verify backend API responses are correct
- [ ] Test the issue across different browsers if relevant
- [ ] Identify the root cause in the codebase

### Technical Areas to Check
- [ ] Frontend JavaScript (`src/static/app.js`)
- [ ] Backend API routes (`src/backend/routers/`)
- [ ] Database operations (`src/backend/database.py`)
- [ ] HTML template structure (`src/static/index.html`)
- [ ] CSS styling issues (`src/static/styles.css`)
- [ ] Authentication flow (`src/backend/routers/auth.py`)

### Acceptance Criteria
- [ ] Bug is reproduced and root cause identified
- [ ] Fix is implemented with minimal code changes
- [ ] Fix is tested to ensure it resolves the issue
- [ ] No new issues are introduced by the fix
- [ ] Similar edge cases are considered and addressed if needed
- [ ] Manual testing confirms the fix works in the browser

### Implementation Guidelines
- Focus on the minimal change needed to fix the issue
- Preserve all existing functionality
- Test edge cases related to the bug
- Consider if this bug might exist in similar areas of the code
- Ensure the fix works for both authenticated and non-authenticated users where applicable