---
title: Setting Up an Nginx Web Server on a Debian VPS (Beginner's Guide)
date: 2023-03-28
author: "Andy Jones"
category: "Artifical Intelligence"
---


# A Beginner's Journey: Setting Up an Nginx Web Server on a Debian VPS (Step-by-Step Analogies)

![Nginx and Debian header image](image-placeholder-url)

Welcome to the world of web servers and cloud computing! If you're a beginner looking to learn how to set up an Nginx web server on a Debian VPS, you've come to the right place. In this article, I'll guide you through the process, step by step, using simple analogies to help you understand each stage. By the end, you'll have the knowledge and confidence to host your very own website on a virtual private server.

Setting up an Nginx web server on a Debian VPS may seem daunting at first, but with a little guidance and the right analogies, it's a breeze! In this guide, we'll cover everything from installing Debian Linux on your VPS to configuring Nginx and hosting your first website.
===
So, strap in and get ready to embark on an exciting journey into the world of web servers and cloud computing! 🚀

![Excited beginner image](image-placeholder-url)

[Continue to Installing Debian Linux on Your VPS](#preparation-installing-debian-linux-on-your-vps)

******

## 2. Preparation: Installing Debian Linux on Your VPS

Imagine your VPS as an empty plot of land, and Debian Linux is the solid foundation upon which we will build our web server "house." Laying a strong foundation is crucial for the stability and performance of your website.

![Debian foundation analogy image](image-placeholder-url)

In this section, we'll guide you through installing Debian Linux on your VPS. We'll use Kamatera as an example, but the process should be similar for other VPS providers.

### a. Creating a new VPS instance

1. Log in to your [Kamatera dashboard](https://www.kamatera.com/express/app/login/).
2. Click on "Add Server" to create a new VPS instance.
3. Choose the data center closest to your target audience for better performance.
4. Select "Debian" from the list of available operating systems. For this tutorial, we'll use "Debian 11" as an example.

### b. Configuring your VPS instance

1. Choose the server resources (CPU, RAM, and storage) based on your needs and budget. For a basic web server, 1 CPU, 1 GB RAM, and 20 GB SSD storage should suffice.
2. Assign a hostname and domain name (optional) for your server.
3. Select a password or SSH key for secure access to your VPS.
4. Review your configuration and click "Create" to deploy your new Debian VPS.

### c. Accessing your Debian VPS

1. Check your email for your VPS credentials and IP address.
2. Use an SSH client (e.g., [PuTTY](https://www.putty.org/) for Windows or Terminal for macOS and Linux) to connect to your VPS.
3. Enter the following command, replacing `your_server_ip` with your VPS's IP address:

ssh root@your_server_ip


4. Enter your password or provide your SSH key when prompted.

Congratulations! You have now laid the foundation for your web server house by installing Debian Linux on your VPS. In the next section, we'll cover updating your system and installing the necessary dependencies.

![Debian installed on VPS image](image-placeholder-url)

[Continue to System Updates and Installing Dependencies](#system-updates-and-installing-dependencies)

******

## 3. System Updates and Installing Dependencies

Now that we've laid the foundation for our web server house, it's time to install the necessary components and materials. Think of system updates and dependencies as the bricks, wiring, and plumbing needed to make your house functional and secure.

![House components and materials analogy image](image-placeholder-url)

In this section, we'll update our Debian system and install the necessary dependencies for setting up Nginx. Additionally, we'll create a sudo user to avoid using the root user, ensuring better security for our web server house.

### a. Updating your Debian system

1. Connect to your VPS via SSH, if you haven't already.
2. Update the package index by entering the following command:

apt update


3. Upgrade your system packages to the latest versions with this command:

apt upgrade


### b. Installing sudo

Since sudo isn't installed by default on Debian, we'll install it first to create a sudo user.

1. Install sudo with the following command:

apt install sudo

### c. Creating a sudo user

Using the root user for everyday tasks can be risky, as it has unrestricted access to the entire system. It's like giving a stranger the keys to your house – you wouldn't want them to have access to everything! To maintain security, we'll create a sudo user with limited privileges that can perform administrative tasks when needed.

1. Add a new user by entering the following command, replacing `your_username` with your desired username:

adduser your_username


You will be prompted to create a password and provide some user information. Fill in the details as required.

2. Grant the new user sudo privileges by adding them to the sudo group:

usermod -aG sudo your_username


3. Log out of the root user by entering `exit` or closing the SSH session.

4. Log back in with your new sudo user, replacing `your_server_ip` and `your_username` with your VPS's IP address and the username you created:

ssh your_username@your_server_ip


5. Enter your password or provide your SSH key when prompted.

With your Debian system updated and the necessary dependencies installed, you've got the essential components and materials to start building your web server house. By creating a sudo user, you've ensured better security, like having a trusted friend with a spare key to your home.

![Sudo user and house security analogy image](image-placeholder-url)

In the next section, we'll dive into installing and configuring Nginx, the main structure of our web server house.

[Continue to Installing and Configuring Nginx](#installing-and-configuring-nginx)

*****

## 4. Installing and Configuring Nginx

With the foundation, components, and materials in place, it's time to build the main structure of our web server house: Nginx. Nginx serves as the walls, roof, and doors, making it possible for people to visit and access your website.

![Nginx house structure analogy image](image-placeholder-url)

In this section, we'll guide you through installing Nginx and configuring it for basic website hosting.

### a. Installing Nginx

1. Connect to your VPS via SSH with your sudo user, if you haven't already.
2. Install Nginx by entering the following command:

sudo apt install nginx


3. Start the Nginx service and enable it to run at startup:

sudo systemctl start nginx
sudo systemctl enable nginx


### b. Configuring Nginx for basic website hosting

1. Create a new directory for your website files, replacing `your_domain` with your domain name or a name of your choice:

sudo mkdir -p /var/www/your_domain/html


2. Change the ownership of the newly created directory to your sudo user:

sudo chown -R $USER:$USER /var/www/your_domain/html


3. Set the correct permissions for the directory:

sudo chmod -R 755 /var/www/your_domain


4. Create a new Nginx server block configuration file, replacing `your_domain` with your domain name or chosen name:

sudo nano /etc/nginx/sites-available/your_domain


5. Add the following configuration to the file, replacing `your_domain` with your domain name or chosen name:

server {                        # Begin the server block
    listen 80;                  # Listen for HTTP connections on port 80
    listen [::]:80;             # Listen for IPv6 HTTP connections on port 80

    root /var/www/your_domain/html;      # Set the root directory for website files
    index index.html;           # Set the default index file

    server_name your_domain www.your_domain;  # Set the domain names for this server block

    location / {                # Begin the location block for the root path
        try_files $uri $uri/ =404;       # Attempt to serve files, directories, or return a 404 error
    }                           # End the location block
}                               # End the server block

This Nginx server block configuration listens for HTTP connections on port 80, specifies the root directory for the website files, sets the default index file, and defines the domain names for the server block. The location block attempts to serve files, directories, or return a 404 error if the requested resource is not found.

*Please note that the lines with a "#" are just there as 'comments' to explain what each line is for, you don't need to type those bits (unless you want to!)*

Save and close the file.

7. Create a symbolic link to enable the new server block:

sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/


8. Remove the default server block to avoid conflicts:

sudo rm /etc/nginx/sites-enabled/default


9. Test the Nginx configuration for syntax errors:

sudo nginx -t


If there are no errors, you should see the message: "nginx: configuration file /etc/nginx/nginx.conf test is successful."

10. Restart the Nginx service to apply the changes:

 ```
 sudo systemctl restart nginx
 ```

You have now successfully built the main structure of your web server house by installing and configuring Nginx. Like the walls, roof, and doors, Nginx allows visitors to access and view your website.

![Nginx configured for website hosting image](image-placeholder-url)

In the next section, we'll take care of setting up your domain and SSL certificate to provide a welcoming and secure entrance for your guests.

[Continue to Setting Up Your Domain and SSL Certificate](#setting-up-your-domain-and-ssl-certificate)


******

## 5. Setting Up Your Domain and SSL Certificate

A well-designed entrance and secure locks are essential for a welcoming and secure home. Similarly, setting up your domain and SSL certificate is crucial for a professional website and secure browsing experience for your visitors.

![Domain and SSL certificate analogy image](image-placeholder-url)

In this section, we'll guide you through purchasing a domain using Cloudflare and setting up SSL certificates with their service.

### a. Purchasing a domain with Cloudflare

1. Visit [Cloudflare](https://www.cloudflare.com/) and create an account or sign in if you already have one.
2. Navigate to the [Registrar](https://www.cloudflare.com/products/registrar/) page.
3. Use the search bar to find the desired domain name and check its availability.
4. Follow the on-screen instructions to purchase the available domain name.

### b. Setting up Cloudflare nameservers for your domain

1. Log in to your Cloudflare account.
2. Click on "Add a Site" and enter your newly purchased domain name.
3. Follow the on-screen instructions and select the free plan when prompted.
4. Cloudflare will provide you with a list of nameservers. Note these nameservers as you will need to update them at your domain registrar.
5. Log in to your domain registrar's control panel and update the nameservers with the ones provided by Cloudflare.

### c. Configuring DNS records in Cloudflare

1. Log in to your Cloudflare account and select your domain.
2. Click on the "DNS" tab.
3. Add an A record for your domain by following these steps:
   - Type: A
   - Name: your_domain
   - IPv4 address: your_server_ip
   - TTL: Auto
   - Proxy status: Proxied
4. Add another A record for the www subdomain:
   - Type: A
   - Name: www.your_domain
   - IPv4 address: your_server_ip
   - TTL: Auto
   - Proxy status: Proxied

### d. Setting up SSL certificates with Cloudflare

1. Log in to your Cloudflare account and select your domain.
2. Click on the "SSL/TLS" tab.
3. In the "Overview" section, choose the "Full" SSL/TLS encryption mode.
4. Cloudflare will automatically issue an SSL certificate for your domain.

With your domain set up and SSL certificates in place, you have now created a welcoming and secure entrance for your website visitors.

![Domain and SSL certificate setup complete image](image-placeholder-url)

Congratulations! You have successfully set up an Nginx web server on a VPS running Debian Linux, using Cloudflare to purchase a domain and set up SSL certificates. Your web server house is now complete, providing a secure and professional experience for your guests.

[Back to the Beginning](#introduction)





