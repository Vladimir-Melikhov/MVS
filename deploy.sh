echo "=== MVS Portfolio Deployment ==="

echo "Pulling latest changes..."
git pull origin main

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Restarting gunicorn..."
sudo systemctl restart gunicorn

echo "=== Deployment complete ==="