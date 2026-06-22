# 🔧 School Management System - Troubleshooting Guide

## Common Issues & Solutions

### 1. Navbar Shows 0 Students/Teachers

**Problem**: The navbar always displays 0 for student and teacher counts even though records exist.

**Solution**:
```python
# Ensure get_context_data() is being called in views
from students.models import Student
from teachers.models import Teachers

def get_context_data():
    return {
        'total_students': Student.objects.count(),
        'total_teachers': Teachers.objects.count(),
    }

# Make sure views use it
context = get_context_data()
```

**Check**:
- [ ] Migrations are run: `python manage.py migrate`
- [ ] Records exist in database
- [ ] Database connection is working

---

### 2. Class List Shows 0 Students in All Classes

**Problem**: All class cards show 0 students even though students exist.

**Solution**:
```python
# Verify class_stats context in class_list view
class_stats = [
    {'class_no': i, 'count': Student.objects.filter(student_class=str(i)).count()}
    for i in range(1, 11)
]
```

**Check**:
- [ ] Student class field matches range(1-10)
- [ ] Student records have student_class set
- [ ] Filter is using string conversion: `str(i)`

---

### 3. Student Images Not Displaying

**Problem**: Profile images show placeholder instead of actual images.

**Solution**:
```python
# In settings.py ensure
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# In urls.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create media folder if missing
```

**Check**:
- [ ] `/media/` folder exists
- [ ] `/media/students/` subfolder exists
- [ ] Images are uploaded to this folder
- [ ] File permissions allow reading

**Test**:
```bash
python manage.py check
python manage.py runserver
# Visit http://localhost:8000/media/students/[image-name]
```

---

### 4. Edit Forms Not Pre-populating

**Problem**: When editing, form fields don't show existing data.

**Solution**:
```html
<!-- Correct approach -->
<input type="text" name="name" value="{{ student.name }}">

<!-- Not working? Check -->
{{ student }}  <!-- Debug: print student object -->
{{ student.name }}  <!-- Debug: print name field -->
```

**Check**:
- [ ] View passes `student` in context
- [ ] Variable name matches: `{{ student.name }}`
- [ ] Student object exists in database

---

### 5. CSRF Token Errors on Form Submit

**Problem**: "Forbidden (403) CSRF token missing or incorrect"

**Solution**:
```html
<!-- Must be in every form -->
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

**Check**:
- [ ] `{% csrf_token %}` is present in form
- [ ] Form method is POST
- [ ] Middleware includes CSRF: `CsrfViewMiddleware`

---

### 6. Images Upload But Don't Display

**Problem**: Images upload successfully but don't show in templates.

**Solution**:
```html
<!-- Correct approach -->
{% if student.profile_image %}
    <img src="{{ student.profile_image.url }}" alt="{{ student.name }}">
{% else %}
    <div>No image</div>
{% endif %}
```

**Check**:
- [ ] `.url` is used (not just field name)
- [ ] Image file actually exists in media folder
- [ ] MEDIA_URL is correct in settings
- [ ] File permissions are readable

---

### 7. Forms Redirect to Wrong Page

**Problem**: After saving, redirects to unexpected URL.

**Solution**:
```python
# Check redirect in view
return redirect(f'/students/{student.id}/')  # Correct
# OR
return redirect('student_detail', id=student.id)  # Better
```

**Check**:
- [ ] Redirect URL is correct
- [ ] Student/Teacher ID is being saved
- [ ] URL pattern matches route
- [ ] Name references are correct

---

### 8. Page Header Not Showing in Templates

**Problem**: Page header section displays incorrectly.

**Solution**:
```html
<!-- Include in template -->
<div class="page-header">
    <div class="container-fluid">
        <h1>Page Title</h1>
        <p>Description</p>
    </div>
</div>
```

**Check**:
- [ ] Template extends base.html
- [ ] Content is in {% block content %}
- [ ] CSS is loaded from base.html

---

### 9. Dropdown Not Showing Classes

**Problem**: Class dropdown in add_student form is empty.

**Solution**:
```python
# View must pass classes
context['classes'] = range(1, 11)

# Template
<select name="student_class">
    <option value="">-- Select --</option>
    {% for cls in classes %}
        <option value="{{ cls }}">Class {{ cls }}</option>
    {% endfor %}
</select>
```

**Check**:
- [ ] `classes` is in context
- [ ] Template loops through classes
- [ ] Value is numeric/string consistently

---

### 10. Delete Doesn't Require Confirmation

**Problem**: Clicking delete immediately removes record.

**Solution**:
```html
<!-- Add confirmation -->
<a href="{% url 'delete_student' student.id %}" 
   onclick="return confirm('Are you sure?');">
    Delete
</a>
```

**Check**:
- [ ] `onclick="return confirm(...)"` is present
- [ ] User sees confirmation dialog

---

## Database Issues

### Migration Errors

**Problem**: "No such table: students_student"

**Solution**:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb  # If issues persist
```

### Foreign Key Errors

**Problem**: "RelatedObjectDoesNotExist"

**Solution**:
- Use `get_object_or_404()` in views
- Handle missing objects gracefully

---

## Template Issues

### Syntax Errors

**Problem**: Template syntax errors in browser console

**Check**:
- [ ] All `{%` have matching `%}`
- [ ] All `{{` have matching `}}`
- [ ] Block names match: `{% block name %}...{% endblock %}`
- [ ] Indentation is correct

### Loading Static Files

**Problem**: CSS/JavaScript not loading

**Solution**:
```html
<!-- Must have in base.html -->
<link href="path/to/style.css" rel="stylesheet">
<script src="path/to/script.js"></script>
```

**Check**:
- [ ] Paths are correct
- [ ] Files exist
- [ ] Paths are relative or absolute correctly

---

## Performance Issues

### Slow Page Loading

**Problem**: Pages load slowly

**Solution**:
- Optimize images (use WebP or compressed JPEG)
- Check for N+1 queries
- Use `.select_related()` or `.prefetch_related()` if joining tables
- Cache expensive queries

### High Memory Usage

**Problem**: Server uses too much memory

**Solution**:
- Paginate large lists
- Use `queryset[:limit]` to limit results
- Close database connections properly

---

## Browser Issues

### Not Responsive on Mobile

**Problem**: Page doesn't adapt to mobile screens

**Check**:
- [ ] Base template has: `<meta name="viewport" ...>`
- [ ] Bootstrap classes are used correctly
- [ ] Images have max-width set
- [ ] Test on actual mobile device

### Old Cache Causing Issues

**Problem**: Changes don't show after deployment

**Solution**:
```javascript
// Clear browser cache
// Or use hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
```

**Check**:
- [ ] Browser cache is cleared
- [ ] CDN cache is cleared
- [ ] Server is restarted

---

## Testing Checklist

### Before Going Live

- [ ] All CRUD operations work
- [ ] Images upload and display
- [ ] Forms validate inputs
- [ ] Navigation links work
- [ ] Mobile responsive design works
- [ ] No JavaScript errors in console
- [ ] No broken links
- [ ] Database backups are working
- [ ] Error pages are handled gracefully
- [ ] Performance is acceptable

---

## Debug Mode Tips

### Enable Detailed Error Messages

```python
# settings.py
DEBUG = True  # Only in development!
ALLOWED_HOSTS = ['*']  # Only in development!
```

### Print Debug Info

```html
<!-- In template -->
{{ object }}  <!-- Print entire object -->
{{ object.field }}  <!-- Print specific field -->
{{ request.GET }}  <!-- Print query parameters -->
{{ request.POST }}  <!-- Print form data -->
```

### Server Side Debugging

```python
# In view
import logging
logger = logging.getLogger(__name__)
logger.info(f"Student count: {Student.objects.count()}")
```

---

## Contact & Support

If issues persist:
1. Check Django logs
2. Review browser console (F12)
3. Test in fresh browser/incognito
4. Verify database connection
5. Check file permissions
6. Review template syntax

---

## Version Compatibility

- Django: 6.0+
- Bootstrap: 5.3.3
- Python: 3.8+
- Font Awesome: 6.4.0

---

**Last Updated**: 2024  
**Status**: ✅ Troubleshooting Guide Complete
