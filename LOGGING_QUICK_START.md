# 🚀 Logging Quick Start Guide

## 5-Minute Setup

### Step 1: Add to settings.py (Development - Console Output)

```python
# Add this to your settings.py file

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[{levelname}] {asctime} - {name}: {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

### Step 2: Run Server

```bash
python manage.py runserver
```

### Step 3: View Logs

Logs appear in your terminal! Example:
```
[INFO] 2024-06-19 10:30:45 - students.views: GET /students/dashboard/ - Dashboard request from 127.0.0.1
[INFO] 2024-06-19 10:30:45 - students.views: Retrieved 12 students from database
```

---

## Production Setup (File Output)

### Step 1: Create logs directory

```bash
mkdir logs
chmod 755 logs
```

### Step 2: Add to settings.py

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} - {name} - {funcName}: {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/school_management.log',
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'students': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'teachers': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'school_management': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
```

### Step 3: View logs

```bash
tail -f logs/school_management.log
```

---

## What's Being Logged

### All Views Log:
- ✅ Request type (GET, POST, DELETE)
- ✅ Request URL/path
- ✅ Client IP address
- ✅ Database operations (count, filter, save)
- ✅ Form data received
- ✅ Validation results
- ✅ File uploads
- ✅ Data changes
- ✅ Success/failure outcomes

---

## 🔍 Search Examples

```bash
# Find all student creations
grep "Student created" logs/school_management.log

# Find all validation failures
grep "Validation failed" logs/school_management.log

# Find all deletions
grep "deleted" logs/school_management.log

# Find activity from specific IP
grep "127.0.0.1" logs/school_management.log

# Count total requests
wc -l logs/school_management.log

# Real-time monitoring
tail -f logs/school_management.log
```

---

## 📊 Example Log Messages

### Adding Student
```
[INFO] POST /students/add-student/ - Request from 127.0.0.1
[INFO] Processing POST request for add student
[INFO] Student form data - Name: John Doe, Email: john@example.com, Class: 1
[INFO] Profile image uploaded: john_profile.jpg
[INFO] Student created successfully - ID: 5, Name: John Doe
```

### Viewing Class
```
[INFO] GET /students/class/1/ - Student list request for class 1
[INFO] Retrieved 3 students for class 1
[INFO] Class 1 teacher: Anitha
[INFO] Student list context prepared with 3 students
```

### Updating Teacher
```
[INFO] POST /teachers/edit/2/ - Edit teacher request for ID: 2
[INFO] Editing teacher: Ramesh (Current Email: ramesh@school.com)
[INFO] Changes - Name: Ramesh → R. Ramesh, Email: ramesh@school.com → r.ramesh@school.com
[INFO] Teacher 2 updated successfully
```

### Deleting Student
```
[INFO] DELETE /students/delete/3/ - Request from 127.0.0.1
[INFO] Deleting student: Jane Doe (ID: 3, Email: jane@example.com)
[INFO] Student Jane Doe deleted successfully
```

---

## ⚙️ Common Settings

### Info Level Only (Recommended)
```python
'level': 'INFO',  # See normal operations
```

### Debug Level (Development Only)
```python
'level': 'DEBUG',  # See everything including SQL queries
```

### Warning Level (Errors Only)
```python
'level': 'WARNING',  # Only errors and warnings
```

---

## 🛠️ Disable Logging Temporarily

```python
# To turn off logging temporarily, comment out handlers:
# 'handlers': [],  # Empty handlers = no logging
```

---

## 📁 File Organization

```
your_project/
├── logs/
│   └── school_management.log  ← Log file created here
├── students/
│   ├── views.py  ← Has logging
│   └── ...
├── teachers/
│   ├── views.py  ← Has logging
│   └── ...
├── school_management/
│   ├── urls.py  ← Has logging
│   ├── settings.py  ← Add LOGGING config here
│   └── ...
└── manage.py
```

---

## ✅ Verify Logging Works

1. Run server: `python manage.py runserver`
2. Open browser: `http://localhost:8000`
3. Visit any page (e.g., `/students/dashboard/`)
4. Check terminal/logs for output
5. You should see lines like:
   ```
   [INFO] GET /students/dashboard/ - Dashboard request from 127.0.0.1
   ```

---

## 🚨 Troubleshooting

### No logs appearing?
- [ ] Check if LOGGING config is in settings.py
- [ ] Restart Django server
- [ ] Check DEBUG = True for development
- [ ] Look for Python errors in terminal

### Logs file not created?
- [ ] Create logs directory: `mkdir logs`
- [ ] Check directory permissions: `chmod 755 logs`
- [ ] Verify path in settings matches actual directory

### Too many logs?
- [ ] Increase log level to WARNING
- [ ] Use RotatingFileHandler (already configured)
- [ ] Archive old logs regularly

---

## 📝 All Logging Added To

| Module | File | Functions | Status |
|--------|------|-----------|--------|
| Students | views.py | 9 | ✅ Done |
| Teachers | views.py | 8 | ✅ Done |
| Main | urls.py | 1 | ✅ Done |
| **Total** | - | **18** | ✅ **Done** |

---

## 📖 Full Documentation

See **LOGGING_GUIDE.md** for:
- Complete configuration examples
- Multiple handler types
- Security considerations
- Advanced filtering
- Troubleshooting steps

---

## 💡 Tips

1. **For Development**: Use console output to see logs immediately
2. **For Production**: Use file output with rotation to manage disk space
3. **For Debugging**: Increase log level to DEBUG to see SQL queries
4. **For Monitoring**: Set up log aggregation tool (ELK, Splunk, etc.)
5. **For Security**: Don't log passwords or API keys

---

**Ready to go!** Your logging is already configured in the code. Just add the LOGGING config to settings.py and you're all set! 🎉
