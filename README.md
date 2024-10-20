# Setting up Maubot

##   
Installing dependencies

This assumes you are running a supported Ubuntu release.

```
sudo apt install git python3-virtualenv python3-venv libolm-dev python3-dev build-essential
```

## Getting the code

```
git clone https://github.com/nbuechner/maubot-workshop.git  
```

```
cd maubot-workshop
```

## Maubot setup

```
cp config.yaml.example config.yaml
```

Copying the example config to your own local copy

```
python3 -m venv env
```

Creating the Python virtual environment in the directory env

```
. env/bin/activate
```

Entering the Python virtual environment

```
pip3 install -r requirements.txt  
```

Install the requited Python modules for Maubot

```
mkdir -p ~/.config
```

You probably already have the \~/.config directory. The last command makes sure it really exists.

## config.yaml

The default config includes sections for the homeservers ubuntu.com and matrix.org.If your account is on another homeserver add it to the homeservers section.If you want to change the login to the bot you can change the username and/or password in the admins section.  

```
homeservers:
   ubuntu.com:
      url: https://chat-server.ubuntu.com
   matrix.org:
      url: https://matrix.org
      secret:
```

```
admins:
   admin: admin
```

## Starting Maubot

```
python3 -m maubot
```

You can now open [*http://127.0.0.1:28316/\_matrix/maubot*](http://127.0.0.1:28316/_matrix/maubot/) in your browser.  
username: admin  
password: admin  
(or your own credentials from the config.yaml section)

## Logging in at the console and homeserver

### Login to your local instance

```
mbc login -u admin -p admin -s http://127.0.0.1:28316 -a local
```

### Login to you Matrix account

#### Using SSO

```
mbc auth -h ubuntu.com -o
```

#### Login with user and password:

```
mbc auth -s matrix.org -u yourusername -p -s local -h matrix.org --update-client
```

> Successfully created client for @yourusername:matrix.org / maubot_PZ44E2D2

This also updates the device ID for your new bot so it uses the correct encryption keys.

##   
Testing the setup

```
mbc build -u
```

> Plugin dev.summit.workshopbot v1.0.0 uploaded to <http://127.0.0.1:28316> successfully.

## Configuring your bot

![Your interface should look like this](.attachments.615512/image.png)

#### Adding a plugin instance

![Add instance](.attachments.615512/image%20%282%29.png)

You can choose any ID. The user and type of the plugin we want to run in this instance are already selected. Click "Create"

![If you did everything right it should look like this](.attachments.615512/image%20%283%29.png)

## Invite your new bot into the workshop room

Use your Matrix client to invite your bot to the workshop room:  
<https://matrix.to/#/#summit-2024-maubot:ubuntu.com>  
  
After it has successfully joined the room you can try your first command:

```
!welcome
```

> Welcome to the Matrix Workshop!

You can also start a DM with your bot and try the command there.

## 