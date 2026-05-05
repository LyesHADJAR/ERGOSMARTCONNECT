# ERGOSMARTCONNECT Hosting Phases

This guide is written for a final-project demo deployment of the Django app on Render's free tier.
Do not use this free deployment for real patient data or production medical usage.

## Phase 1: Prepare The Project Locally

Goal: make the Django project ready for a cloud builder.

Files prepared:

- `requirements.txt`: Python dependencies used by Render.
- `Procfile`: process command for platforms that read Procfiles.
- `build.sh`: Render build script.
- `ERGOSMARTCONNECT/settings.py`: production-aware settings using environment variables.
- `.gitignore`: excludes local secrets, local databases, virtual environments, and generated static output.

Run locally:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
DEBUG=False SECRET_KEY=replace-with-a-long-secret ALLOWED_HOSTS=.onrender.com .venv/bin/python manage.py check --deploy
DEBUG=False SECRET_KEY=replace-with-a-long-secret ALLOWED_HOSTS=.onrender.com .venv/bin/python manage.py collectstatic --no-input
DEBUG=False SECRET_KEY=replace-with-a-long-secret ALLOWED_HOSTS=.onrender.com .venv/bin/python manage.py migrate --plan
```

Screenshot ideas:

- Project structure showing `manage.py`, `ERGOSMARTCONNECT/`, `Dashboard/`, `requirements.txt`, `Procfile`, and `build.sh`.
- `.gitignore` showing `.env`, `*.env`, `db.sqlite3`, `.venv/`, and `staticfiles/`.
- Successful terminal output for `collectstatic` or `check --deploy`.

## Phase 2: Push The Project To GitHub

Goal: give Render a repository it can deploy.

Steps:

1. Create a new GitHub repository.
2. Make sure `.env` and `db.sqlite3` are not committed.
3. Commit and push the project.
4. Confirm GitHub shows the deployment files.

Screenshot ideas:

- New GitHub repository page.
- Repository file list after push.
- Commit history showing the deployment-preparation commit.

## Phase 3: Create The Render Database

Goal: use PostgreSQL instead of SQLite online.

Steps:

1. Open Render Dashboard.
2. Click `New +`.
3. Choose `PostgreSQL`.
4. Select the free option if available.
5. Create the database.
6. Copy the internal database URL.

Screenshot ideas:

- Render `New +` menu.
- PostgreSQL creation form.
- Database dashboard after creation.
- Database connection page with secret values hidden.

Important limitation:

- Render free PostgreSQL databases may expire after 30 days. This is acceptable for a demo, but it should be mentioned in the dissertation.

## Phase 4: Create The Render Web Service

Goal: deploy the Django app.

Steps:

1. In Render, click `New +`.
2. Choose `Web Service`.
3. Connect the GitHub repository.
4. Use these values:

```txt
Runtime: Python
Build Command: ./build.sh
Start Command: gunicorn ERGOSMARTCONNECT.wsgi:application
Instance Type: Free
```

5. Add environment variables:

```txt
DEBUG=False
SECRET_KEY=<long-generated-django-secret-key>
DATABASE_URL=<render-internal-postgres-url>
ALLOWED_HOSTS=.onrender.com
CSRF_TRUSTED_ORIGINS=https://*.onrender.com
GROQ_API_KEY=<only if the AI feature is needed>
```

Optional email variables if the app sends email:

```txt
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=<gmail-address>
EMAIL_HOST_PASSWORD=<gmail-app-password>
```

Screenshot ideas:

- Web service setup form.
- Build command and start command fields.
- Environment variables page with values hidden.
- Deployment logs showing dependencies installed, static files collected, and migrations applied.

## Phase 5: Validate The Live App

Goal: prove the hosted project works.

Steps:

1. Open the Render `.onrender.com` URL.
2. Test the landing page.
3. Test login/registration.
4. Test the dashboard.
5. Test one patient workflow.
6. Test the AI page only if `GROQ_API_KEY` is configured.

Screenshot ideas:

- Live URL in the browser address bar.
- Login page.
- Dashboard page.
- Patient detail/workflow page.
- Any final feature that represents the project objective.

## Phase 6: Dissertation Notes

Recommended wording:

> The Django application was deployed on Render using a free web service. The source code was hosted on GitHub, then Render installed dependencies from `requirements.txt`, collected static files, applied database migrations, and launched the application with Gunicorn. Sensitive values such as `SECRET_KEY`, `DATABASE_URL`, and API keys were configured as environment variables instead of being stored in the repository.

Limitations to mention:

- Free web services can sleep after inactivity, so the first request can be slow.
- Free databases can have time or persistence limits.
- This setup is for academic demonstration, not production medical deployment.
- Real patient data would require stronger security, backups, paid persistent infrastructure, and legal/privacy compliance.
