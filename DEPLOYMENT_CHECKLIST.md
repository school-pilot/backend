# Vercel Deployment Checklist

## Pre-Deployment Verification ✓

### Local Testing
- [ ] Run migrations locally: `python manage.py migrate`
- [ ] Start dev server: `python manage.py runserver`
- [ ] Test API endpoints locally
- [ ] Collect static files: `python manage.py collectstatic --noinput`

### Code Quality
- [ ] No uncommitted changes: `git status`
- [ ] All tests pass (if applicable)
- [ ] No syntax errors: `python -m py_compile sms_prj/settings.py`
- [ ] requirements.txt up to date

## Vercel Configuration Files ✓

The following files are configured and ready:

- ✅ **vercel.json** - Vercel platform configuration
  - Build command: `bash build.sh`
  - Python version: 3.13
  - Install command: `pip install -r requirements.txt`

- ✅ **build.sh** - Build and deployment script
  - Installs dependencies
  - Collects static files
  - Runs migrations

- ✅ **VERCEL_DEPLOYMENT.md** - Complete deployment guide

- ✅ **sms_prj/settings.py** - Production-ready settings
  - CORS configuration
  - Vercel environment detection
  - Supabase database support
  - Static files configuration

## Environment Variables Required ✓

Set these on Vercel Dashboard → Settings → Environment Variables:

```
SECRET_KEY=<generate-a-new-secret-key>
DEBUG=False
USE_SUPABASE=True
HOST=<your-supabase-host>
PORT=<your-supabase-port>
DB_USER=<your-db-user>
DB_NAME=postgres
PASSWORD=<your-db-password>
SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_KEY=<your-public-key>
```

## GitHub Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Configure for Vercel deployment"
git push origin main
```

### 2. Connect to Vercel
1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Select your GitHub repository
4. Click "Import"

### 3. Configure Environment
1. In the "Configure Project" screen, click "Environment Variables"
2. Add all required variables from above
3. Click "Deploy"

### 4. Post-Deployment
1. Wait for deployment to complete
2. Visit your Vercel dashboard to get the deployed URL
3. Test the API: `https://your-project.vercel.app/api/`
4. Access admin: `https://your-project.vercel.app/admin`

## Important Vercel Considerations

### Database
- ✅ Using Supabase (cloud PostgreSQL) - no local SQLite issues
- ✅ Connection pooling configured with `CONN_MAX_AGE=600`
- ✅ Timeout handling with `connect_timeout=10`

### Static Files
- ✅ `STATIC_ROOT` configured to `staticfiles/`
- ✅ Static files collected during build via `build.sh`
- ✅ Vercel automatically serves static files

### CORS
- ✅ django-cors-headers installed and configured
- ✅ Middleware added to support cross-origin requests
- ✅ Vercel domains automatically allowed

### Allowed Hosts
- ✅ `localhost`, `127.0.0.1` for development
- ✅ `*.vercel.app` for all Vercel deployments
- ✅ Custom domain support via `CUSTOM_DOMAIN` env var

## Troubleshooting

### Build Failures
- Check `build.sh` has execute permissions
- View build logs in Vercel dashboard
- Ensure `requirements.txt` includes all dependencies

### Database Connection Issues
- Verify Supabase credentials in environment variables
- Test connection locally first
- Check database user has correct permissions

### Static Files Not Loading
- Run: `python manage.py collectstatic --noinput`
- Verify `STATIC_ROOT` setting
- Check file permissions: `chmod -R 644 staticfiles/`

### Admin Panel Not Accessible
- Ensure admin user created: `python manage.py createsuperuser`
- Check `ALLOWED_HOSTS` includes your domain
- Verify CSRF settings in production

## Monitoring

### Vercel Dashboard
- Deployments tab: view build logs
- Analytics tab: monitor traffic and errors
- Function logs: see real-time application logs
- Environment tab: manage variables and secrets

### Django Admin
- User management at `/admin/auth/user/`
- App activity monitoring
- Check error logs for issues

## Next Steps After Deployment

1. **Security**
   - Change `DEBUG=False` in production
   - Update `SECRET_KEY` to a new secure value
   - Configure allowed hosts for your domain

2. **Optimization**
   - Enable caching headers
   - Set up error monitoring (Sentry)
   - Monitor database performance

3. **Features**
   - Configure email service for notifications
   - Set up backup strategy for Supabase
   - Add monitoring and alerting

## Useful Commands

```bash
# Deploy from CLI
vercel --prod

# View logs
vercel logs <deployment-url>

# Manage environment variables
vercel env ls
vercel env pull .env.vercel

# Redeploy without code changes
vercel --prod --force
```

## Support & Resources

- **Vercel Docs**: https://vercel.com/docs
- **Django Docs**: https://docs.djangoproject.com/
- **Supabase Docs**: https://supabase.com/docs
- **Project Docs**: See `DATABASE_SETUP.md`, `API_DOCUMENTATION.md`, `VERCEL_DEPLOYMENT.md`

---

**Ready to deploy?** Start with the "GitHub Deployment Steps" section above! 🚀
