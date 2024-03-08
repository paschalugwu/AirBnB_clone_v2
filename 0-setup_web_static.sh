#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Assign ownership
sudo chown -R $USER:$USER /data/

# Update Nginx configuration
sudo sed -i '/^\s*location \/hbnb_static {/a \\\talias /data/web_static/current/;' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
