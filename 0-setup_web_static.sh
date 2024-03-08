#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Update package list
sudo apt -y update

# Install Nginx
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic through firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories for web_static
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a simple HTML test page
echo "<h1>Test Page</h1>" > /data/web_static/releases/test/index.html

# Check if symbolic link already exists for current web_static version
if [ -d "/data/web_static/current" ]; then
    echo "Path /data/web_static/current exists"
    # Remove existing symbolic link
    sudo rm -rf /data/web_static/current;
fi

# Create symbolic link to the current version of web_static
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of web_static directories to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data

# Update Nginx configuration to serve web_static content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Create symbolic link to enable Nginx site configuration
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# Restart Nginx to apply changes
sudo service nginx restart
