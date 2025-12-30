# Vercel Deployment Guide for SMS Project

This guide covers deploying the SMS Project (Django + PostgreSQL/Supabase) to Vercel.

## Prerequisites

- Vercel account (free tier available at https://vercel.com)
- GitHub repository with this project
- Supabase database set up and credentials ready
- Domain (optional, Vercel provides `*.vercel.app` domains)

## Step 1: Prepare Your Repository

Ensure the following files exist in your project root:

- ✅ `vercel.json` - Vercel configuration
- ✅ `build.sh` - Build script
- ✅ `requirements.txt` - Python dependencies
- ✅ `.env.example` - Environment variables template

## Step 2: Deploy to Vercel

### Option A: Via GitHub (Recommended)

1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Ready for Vercel deployment"
   git push origin main
   ```

2. Go to https://vercel.com/new
3. Import your GitHub repository
4. Vercel will auto-detect Django configuration
5. Click "Deploy"

### Option B: Via Vercel CLI

```bash
npm i -g vercel
vercel
# Follow the prompts
```

## Step 3: Configure Environment Variables

After deployment, set up environment variables on Vercel:

1. Go to your Vercel project dashboard
2. Click **Settings** → **Environment Variables**
3. Add these variables:

```env
# Django settings
SECRET_KEY=your-secure-key-here
DEBUG=False
DJANGO_SETTINGS_MODULE=sms_prj.settings

# Supabase database credentials
USE_SUPABASE=True
HOST=aws-1-eu-west-3.pooler.supabase.com
PORT=6543
DB_USER=postgres.your-project-ref
DB_NAME=postgres
PASSWORD=your-supabase-password

# Supabase API (optional, for direct API calls)
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_KEY=your-public-anon-key

# Custom domain (optional)
CUSTOM_DOMAIN=yourdomain.com
```

## Step 4: Run Migrations on Vercel

After the first deployment:

1. Connect to Vercel via SSH or use the Vercel CLI:
   ```bash
   vercel env pull .env.vercel
   python manage.py migrate --noinput
   ```

Or trigger migrations via your deployment:
- The `build.sh` script runs migrations automatically during each deployment

## Step 5: Create Superuser (Admin Account)

Vercel deployments are ephemeral, so you need to create an admin via:

### Option A: Django Admin Command (on local machine)

```bash
# Set up local .env with same Supabase credentials
python manage.py createsuperuser
```

### Option B: Programmatic Creation

Create a Django management command or API endpoint to create admins.

## Step 6: Access Your Application

1. Your app will be available at: `https://your-project.vercel.app`
2. Admin panel: `https://your-project.vercel.app/admin`
3. API endpoints: `https://your-project.vercel.app/api/...`

## Important Notes for Vercel

### Static Files
- Static files are collected automatically via `build.sh`
- Serve via CDN by using Vercel's built-in static optimization

### Database Connections
- Vercel's serverless functions have short timeouts
- Use connection pooling (configured in `settings.py`)
- Keep-alive connections via `CONN_MAX_AGE`

### Allowed Hosts
- Vercel automatically adds `*.vercel.app` to `ALLOWED_HOSTS`
- Add custom domains in project settings

### Environment Variables Per Deployment
- Set different environment variables for **Production**, **Preview**, and **Development**
- Production: set `DEBUG=False`

## Troubleshooting

### Build Fails: "requirements.txt not found"
- Ensure `requirements.txt` is in the project root
- Check file permissions: `chmod 644 requirements.txt`

### Deployment Error: "Python version not available"
- Edit `vercel.json` to specify supported Python version (3.11 or 3.12)

### Database Connection Timeout
- Check Supabase host is correct
- Verify firewall allows Vercel IP ranges
- Test connection locally: `psql -h HOST -U USER -d DB_NAME`

### Static Files Not Loading
- Run: `python manage.py collectstatic --noinput`
- Check `STATIC_ROOT` points to `staticfiles/`

### Migrations Not Running
- Check `build.sh` has execute permissions: `chmod +x build.sh`
- View build logs in Vercel dashboard

## Performance Optimization

### For Production:

1. **Enable Caching** in Vercel project settings
2. **Use CDN** for static files (default with Vercel)
3. **Database Optimization**:
   - Add indexes to frequently queried fields
   - Use connection pooling (already configured)
4. **API Optimization**:
   - Enable pagination on list endpoints
   - Add caching headers where appropriate

## Monitoring & Logs

- **Vercel Logs**: https://vercel.com/docs/concepts/observability/logging
- **Django Errors**: Check Vercel Function Logs
- **Database**: Monitor via Supabase dashboard

## Rollback & Redeployment

```bash
# Trigger redeploy from GitHub
git commit --allow-empty -m "Trigger redeploy"
git push origin main

# Or redeploy via Vercel CLI
vercel --prod
```

## Custom Domain Setup

1. Go to **Settings** → **Domains**
2. Add your custom domain
3. Update DNS records (see Vercel dashboard for details)
4. Set `CUSTOM_DOMAIN` environment variable

## Next Steps

- Set up CI/CD with GitHub Actions for automated tests
- Configure error monitoring (Sentry, etc.)
- Set up email service for notifications
- Implement backup strategy for Supabase database

For more help, see:
- Vercel Docs: https://vercel.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- Supabase Docs: https://supabase.com/docs
