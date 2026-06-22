# 🎓 School Management System - Template Quick Reference Guide

## 📚 Template Hierarchy

```
templates/
├── base.html (Master Template - All pages extend this)
│   ├── Navbar with live stats
│   ├── Page header section
│   ├── Main content area (block)
│   └── Footer
│
├── index.html (Home/Landing Page)
│   └── System overview with quick actions
│
students/templates/
├── dashboard.html
│   └── Overview stats and recent students
│
├── class_list.html
│   └── All 10 classes with student counts
│
├── student_list.html (class_no parameter)
│   └── Table of students in a class
│
├── student_detail.html (id parameter)
│   └── Individual student profile
│
├── add_student.html
│   └── Form to create new student
│
└── edit_student.html (id parameter)
    └── Form to update student

teachers/templates/
├── teacher_list.html
│   └── All teachers with action buttons
│
├── teacher_detail.html (id parameter)
│   └── Individual teacher profile
│
├── add_teacher.html
│   └── Form to create new teacher
│
└── edit_teacher.html (id parameter)
    └── Form to update teacher
```

---

## 🔗 URL Routing Map

```
HOME PAGE
    ↓
/ ────────────────────── index.html (Home)
    │
    ├─ Students Section
    │  ├─ /students/dashboard/      ──→ dashboard.html
    │  ├─ /students/classes/        ──→ class_list.html
    │  ├─ /students/class/<no>/     ──→ student_list.html
    │  ├─ /students/<id>/           ──→ student_detail.html
    │  ├─ /students/add-student/    ──→ add_student.html
    │  ├─ /students/edit/<id>/      ──→ edit_student.html
    │  └─ /students/delete/<id>/    ──→ delete (redirect)
    │
    └─ Teachers Section
       ├─ /teachers/list/           ──→ teacher_list.html
       ├─ /teachers/<id>/           ──→ teacher_detail.html
       ├─ /teachers/add-teacher/    ──→ add_teacher.html
       ├─ /teachers/edit/<id>/      ──→ edit_teacher.html
       └─ /teachers/delete/<id>/    ──→ delete (redirect)
```

---

## 📊 Data Flow Diagram

```
DATABASE (db.sqlite3)
    │
    ├─ Student table
    │  │
    │  └─→ Views (students/views.py)
    │      ├─ dashboard() → dashboard.html
    │      ├─ class_list() → class_list.html
    │      ├─ student_list() → student_list.html
    │      ├─ student_detail() → student_detail.html
    │      ├─ add_student_page() → add_student.html
    │      └─ edit_student() → edit_student.html
    │
    └─ Teacher table
       │
       └─→ Views (teachers/views.py)
           ├─ teacher_list() → teacher_list.html
           ├─ teacher_detail() → teacher_detail.html
           ├─ add_teacher_page() → add_teacher.html
           └─ edit_teacher() → edit_teacher.html
```

---

## 🎨 Template Blocks (from base.html)

```html
{% block title %}        - Page title (in browser tab)
{% block breadcrumb %}   - Breadcrumb navigation (if needed)
{% block content %}      - Main page content
{% block extra_css %}    - Additional CSS per page
{% block extra_js %}     - Additional JavaScript per page
```

---

## 📝 Template Variables Reference

### Available in ALL templates (via get_context_data()):
```python
total_students    - Count of all students in DB
total_teachers    - Count of all teachers in DB
```

### Dashboard Context:
```python
total_students
total_teachers
total_classes     - 10 (hardcoded)
recent_students   - Last 5 students added
```

### Class List Context:
```python
total_students
total_teachers
classes           - range(1, 11)
class_stats       - List of dicts with {class_no, count}
```

### Student List Context:
```python
total_students
total_teachers
students          - Filtered by class_no
class_name        - "Class {no}"
class_teacher     - Teacher name for the class
student_count     - Count in this class
```

### Student Detail Context:
```python
total_students
total_teachers
student           - Student object with all fields
```

### Add/Edit Student Context:
```python
total_students
total_teachers
classes           - range(1, 11) for dropdown
student           - (edit only) existing student data
edit_mode         - (edit only) True
```

### Teacher List Context:
```python
total_students
total_teachers
teachers          - All teacher objects
teacher_count     - Count of teachers
```

### Teacher Detail Context:
```python
total_students
total_teachers
teacher           - Teacher object
```

### Home (Index) Context:
```python
total_students    - From home view
total_teachers    - From home view
```

---

## 🎯 Key Features Per Template

### 📍 base.html (Master Template)
- [x] Responsive Bootstrap navbar
- [x] Live statistics in navbar
- [x] Sticky navbar
- [x] Mobile toggle menu
- [x] Professional footer
- [x] Gradient backgrounds
- [x] Font Awesome icons
- [x] Active link highlighting

### 🏠 index.html (Home)
- [x] Dashboard stats cards
- [x] Feature cards
- [x] Quick action buttons
- [x] System information
- [x] Call-to-action buttons

### 📊 dashboard.html
- [x] 4 stat cards
- [x] Quick actions section
- [x] Recent students widget
- [x] All data live from DB

### 📚 class_list.html
- [x] Class cards with student count
- [x] Interactive hover effects
- [x] Quick navigation to class details
- [x] Add student button

### 👥 student_list.html
- [x] Responsive data table
- [x] Student count display
- [x] Action buttons (View/Edit/Delete)
- [x] Class teacher display
- [x] Empty state handling

### 👤 student_detail.html
- [x] Profile image display
- [x] All student information
- [x] Address section
- [x] Edit/Delete options
- [x] Back navigation

### ➕ add_student.html
- [x] Multi-field form
- [x] Image upload
- [x] Dropdown for class
- [x] Required field indicators
- [x] Form validation

### ✏️ edit_student.html
- [x] Pre-populated form
- [x] Image preview
- [x] All fields editable
- [x] Original image retention

### 👨‍🏫 teacher_list.html
- [x] Card view of teachers
- [x] Table view
- [x] Total count
- [x] Action buttons

### 👨‍🎓 teacher_detail.html
- [x] Teacher profile card
- [x] Contact information
- [x] Designation display
- [x] Edit/Delete options

### ➕ add_teacher.html
- [x] Simple form
- [x] Name and email fields
- [x] Validation

### ✏️ edit_teacher.html
- [x] Pre-populated form
- [x] Editable fields
- [x] Cancel and Update buttons

---

## 🔄 Form Methods

### Add Student
- **Method**: POST
- **Action**: {% url 'add_student' %}
- **Enctype**: multipart/form-data (for image)
- **Required Fields**: name, email, student_class
- **Redirect On Success**: /students/{id}/ (student detail)

### Edit Student
- **Method**: POST
- **Action**: {% url 'edit_student' student.id %}
- **Enctype**: multipart/form-data
- **Pre-filled**: All existing student data
- **Redirect On Success**: /students/{id}/ (student detail)

### Delete Student
- **Method**: GET (with confirmation)
- **Action**: {% url 'delete_student' student.id %}
- **Redirect**: /students/classes/ (class list)

### Add Teacher
- **Method**: POST
- **Action**: {% url 'add_teacher' %}
- **Required Fields**: name, email
- **Redirect On Success**: /teachers/{id}/ (teacher detail)

### Edit Teacher
- **Method**: POST
- **Action**: {% url 'edit_teacher' teacher.id %}
- **Pre-filled**: Existing teacher data
- **Redirect On Success**: /teachers/{id}/ (teacher detail)

### Delete Teacher
- **Method**: GET (with confirmation)
- **Action**: {% url 'delete_teacher' teacher.id %}
- **Redirect**: /teachers/list/ (teacher list)

---

## 🎨 Bootstrap Classes Used

- `.container-fluid` - Full width container
- `.page-header` - Header section with gradient
- `.card` - Card components
- `.btn` - Button styles
- `.table-responsive` - Responsive tables
- `.empty-state` - No data display
- `.table-actions` - Inline action buttons
- `.navbar` - Navigation bar
- `.dropdown` - Dropdown menus
- `.badge` - Status badges
- `.alert` - Alert messages

---

## 🔍 Template Tags Used

```django
{% extends "base.html" %}           - Extend master template
{% block title %}...{% endblock %}  - Override blocks
{% if condition %}                  - Conditionals
{% for item in items %}             - Loops
{% url 'name' arg %}                - URL reversal
{% csrf_token %}                    - CSRF protection
{{ variable }}                      - Variable display
{{ variable|filter }}               - Template filters
{% load static %}                   - Load static files
```

---

## 📱 Responsive Grid System

```
Desktop (md):
- 4 columns for cards
- 6 columns for 2-column layout
- 12 columns for full width

Tablet (sm):
- 6 columns for cards
- 12 columns for 1-column layout

Mobile:
- 12 columns full width
- Single column layout
- Stacked buttons
```

---

## ✅ Testing Checklist

- [ ] All pages load without errors
- [ ] Navbar shows correct counts
- [ ] Student list filters by class correctly
- [ ] Forms submit and create records
- [ ] Edit forms pre-populate with existing data
- [ ] Delete operations work with confirmation
- [ ] Images upload and display correctly
- [ ] Responsive design works on mobile
- [ ] All links navigate correctly
- [ ] Empty states display when no data
- [ ] Hover effects work on cards
- [ ] Forms validate required fields

---

## 🚀 Performance Tips

1. Images should be optimized (< 500KB recommended)
2. Database queries are already optimized
3. Use browser cache for static files
4. Consider pagination for large datasets
5. Add search/filter to tables if needed

---

## 📞 Common Tasks

### To Add a New Field to Student
1. Add field to Student model
2. Run migrations
3. Update add_student_page() view
4. Add form input in add_student.html
5. Add form input in edit_student.html
6. Add display in student_detail.html

### To Add a New Class
Update the range in:
- class_list() view
- student_list() dropdown

### To Customize Colors
Edit the `:root` CSS variables in base.html

### To Add a New Teacher Field
Same process as student field

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: ✅ Complete
