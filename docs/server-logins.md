# Server access procedure

As you may have heard, we have two new (actually a little old) servers in the Bentzel-Weg-3 server room. This brief document should help you with setting up your machine in order to access them and to understand a bit what happens when you login. 

The whole login procedure is practically the same as the one used for the MOGON2 access; the seldom differences will be addressed as they come during the procedure.

## 1. Create new ssh key pair

To generate the key-pair, you can basically follow the steps showed in the mogon repository (links below). There is one major difference with what is shown there: **the encryption algorythm that we are using for our login is ed25519 and not RSA** (Robert says because it is safer and the keys are also much shorter).

Therefore, Linux and MacOS users have to specify `-t ed25519` and **not** `-t RSA` in the `ssh-keygen` command; Windows users should have the possibility to just click on the desired option during the generating procedure.

Everything else is the same:

Linux/MacOS : https://mogonwiki.zdv.uni-mainz.de/dokuwiki/start:mogon_cluster:access_from_outside_unix#generating_a_new_ssh-key_using_linux_or_macos

Windows: https://mogonwiki.zdv.uni-mainz.de/dokuwiki/start:mogon_cluster:access_from_outside_windows:creating_sshkeys_on_windows#set_up_ssh-keys_for_mogon_using_windows

## 2. Setup ssh config file

For our servers we are also using a jump host called `sshgate` (to my understanding). It is therefore necessary to setup the ssh `config` file to allow this additional authentication. Below is a template that you can append to the `config` file you already have used for MOGON (if you haven't one, just create a new file named `config` in the same folder where you keep your ssh keys)

```
# Jump host login
Host sshgate
    HostName sshgate.zdv.uni-mainz.de
    User uni-mainz-user
    IdentityFile <path/to/private/key>

# Server 1 login    
Host <custom_server_name_1>
    HostName tchumatchenko-r7610-01.biologie.uni-mainz.de
    User <usename>
    ProxyJump sshgate
    IdentityFile <path/to/private/key>

# Server 2 login 
Host <custom_server_name_2>
    HostName tchumatchenko-r7610-02.biologie.uni-mainz.de
    User <username>
    ProxyJump sshgate
    IdentityFile <path/to/private/key>
```

Change the parameters in the angle brackets with you personal parameters. `<custom_server_name_X>` will be the name you use to login in the server with the command `ssh custom_server_name_X`.

## 3. Upload public key

Once that the key-pair is generated and the config file is set up, the last step is to upload the public key to your personal ZDV account page https://account.uni-mainz.de/.

There, click on **SSH-Key hinzufugen** and copy paste the whole content of your `key_name.pub` file in the first big field. Add a Kommentar to remember what are you using the key for, select `SSHGATE` in the Schlüsselzweck menu, and speich everything.

## 4. Write me an e-mail

Write me an e-mail with your zdv user name so that I can add you to the authorized users.

# User home folder

After ssh-ing into the server you will land into your ZDV home folder, which is automatically mounted on `/uni-mainz.de/homes/your_user_name/`. Despite the homely sense of safety this folder may have, it is not a good idea to work from there as it is actually very far from the server (literally), and, therefore, anything you have installed there will talk pretty slowly with the server.

After logging in, each user can find their own new working directory with the correct ownership and rights under `/tank/data-01/your_user_name/` and is very welcome to setup their environment there (basically this is your home folder on the server). 

**IMPORTANT:** the servers' storage memory is quite limited so **do not use them for storage** - this is what the ZDV home is for: copy the stuff you need from there to the local home, do your calculations, and then move it back on the ZDV. Luckily, in the future, we are getting more storage, so this problem should be solved at least partially.

# Setting up python

Our servers are linux based, and, therefore, C++ is natively available for everyone. Python, on the other hand, needs a bit of tinkering (not too much):

## Option 1: miniconda

Due to the limited storage, I strongly suggest using miniconda instead of the full anaconda

1. go into your local home `/tank/data-01/your_user_name/`

2. download the miniconda installer with:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

3. run the downloaded file with `sh` and install miniconda **in your local home folder on the server** (the default option conda proposes is on your ZDV home). Say yes when it asks you to initialize.

4. miniconda is installed but it won't activate automatically when you login. To activate it run the command 
   
   ```bash
   source /uni-mainz.de/homes/your_user_name/.bashrc
   ```
   
   (you can use the relative path as well of course).

5. once that the environment is active just use conda normally.

## Option 2: pip

The servers have a global installation for both `python` and `pip` and, therefore, anaconda is not really needed (although its a little easier to use in my opinion).

You can then create a new virtual environment for a given project with

```bash
cd project_folder 
python -m venv project_env
```

From what I am finding, everyone suggests to create the virtual environment inside the project folder to which the environment pertains; this looks somewhat different from the anaconda paradigm where you just create environments in the conda location but I have no idea which one is better. You do you.

To activate the environment, you can run 

```bash
source project_folder/project_env/bin/activate
```

and from here you are free to use `pip` to do the things you need. To deactivate simply write `deactivate` and the environment will be deactivated.

For more info about environments and python mechanisms in general (distributions, wheels, ...) this is a nice ref https://virtualenv.pypa.io/en/latest/user_guide.html#introduction

# Matlab

I am aware that a number of people in the lab are using Matlab for their projects and it would be very nice if we managed to run that on the server as well. I have not, however, the slightest idea on how Matlab works, so if any of you guys wants can take a couple hours to help me setup the shared Matlab account it'd be supernice of you. 
