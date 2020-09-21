# SecureThisPass

![SecureThisPass Logo](https://i.imgur.com/VS1tsGY.jpg)

SecureThisPass is a tool that converts your password into a secure password without making it too difficult to memorize! It can also generate random secure passwords.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need the following in order to run the application as it is intended on your machine:

```
Python 3 or above
```

### Installing the application

First clone this repository or download it manually to a working directory on your computer.
Now you need to download word lists for the tool to work as it is intended.
You can download a word list from one of the word lists below . Alternatively, you can use any other word list you want.

WORD LISTS (choose one):

[mit word list](https://www.mit.edu/~ecprice/wordlist.10000)(Copy and paste it in a text file then save it as 'wordlist.txt')

[Oxford word list](https://raw.githubusercontent.com/gokhanyavas/Oxford-3000-Word-List/master/Oxford%203000%20Word%20List%20No%20Spaces.txt) (Copy and paste it in a text file then save it as 'wordlist.txt')

Now place the 'wordlist.txt' in the SecureThisPass directory. Thereafter, open cmd/terminal in the same directory and run the following command.

```
py worldlistgenerator.py
```

Now some new text files should be added to the SecureThisPass directory.
The SecureThisPass directory on your machine should look something like the image below:

![SecureThisPass Directory](https://i.imgur.com/yhT8TSF.png)


### Running the application 

if you have gone throgh the steps of "Installing the application" chapter, you are ready to use the SecureThisPass tool. Open cmd/terminal and run the following command:

```
py SecureThisPass.py
```

Now the tool should prompt you to input a password you want to make more secure.
In case you have a password, fill the input field with the password and press enter. In case you don't have any password in mind, leave the input field blank and press enter.
The tool will now generate a secure password for you (either based on your provided password or totally from the scratch). You can now use the generated secure password wherever you want without any need to worry about its security! 

Examples of a generated password:
![SecureThisPass Example Password](https://i.imgur.com/iUBvYtv.png)

## Contributing

Feel free to fork and expand this project! Send a pull request if you would like to add your code to the project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/WozniakManiac/SecureThisPass/releases). 

## Authors

* **Farzam Madani** - *Creation of the core application* - [WozniakManiac](https://github.com/WozniakManiac)

See also the list of [contributors](https://github.com/WozniakManiac/SecureThisPass/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/WozniakManiac/SecureThisPass/blob/master/LICENSE) file for details

## Acknowledgments

* Big thanks to anyone whose library is used for this project 

