### pwGen🔐

> mnml password generator 🗝



<p align="center">
  <a href="https://github.com/shagunattri/pwgen/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?longCache=true" alt="Pull Requests">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg?longCache=true" alt="MIT License">
  </a>
</p>

<p align="center">
  <a href="https://twitter.com/sp3ppr" target="_blank">
    <img src="https://img.shields.io/twitter/follow/sp3ppr.svg?logo=twitter">
  </a>
</p>

<div align="center">
  <sub>Created by
  <a href="https://twitter.com/sp3ppr">sp3ppr</a> and
  <a href="https://github.com/shagunattri/pwGen/graphs/contributors">contributors</a>
</div>

<br>

****


## Written in
- python3



## Screenshots
![pwgen](https://user-images.githubusercontent.com/29366864/81793797-7bb5da00-9527-11ea-8da4-ac2403a09b1e.png)

***Libraries used:***
- string
- random
- sys
- pyfiglet
- pyperclip
- math
- functools
- pwnedpasswords

## Installation:
```console
$ git clone https://github.com/shagunattri/pwGen.git

$ cd pwGen/

$ pip install -r requirements.txt

$ python3 pwGen.py
```

### TODO
- [ ] Save password inside an encrypted file whose filename is the title of the website or resource that requires the password.
- [x] Copy to Clipboard support.
- [ ] Maintain a mobile-sync directory inside a git repository.
- [x] Display entropy of generated password.
- [ ] Generate easy to remenber passphrase.
- [x] Check generated passwords against a pwnedpassword database.


### Notes

- To make pwGen generate unique passwords,we compare it against the [pwnedpasswords](https://pypi.org/project/pwnedpasswords/) database using the pwnedpasswords package.
- Using the plain_text flag in the package it hashes the generated password and then checks for a hash in the pwnedpassword database to provide results.


*According to pwnedpassword package documentation:*
> No plaintext passwords ever leave your machine using pwnedpasswords.
> How does that work? Well, the Pwned Passwords v2 API has a pretty cool k-anonymity > implementation.

> From https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/:
>   Formally, a data set can be said to hold the property of k-anonymity, if for every record in a released table, there are k − 1 other records identical to it.

> This allows us to only provide the first 5 characters of the SHA-1 hash of the password in question. The API then responds with a list of SHA-1 hash suffixes with that prefix. On average, that list > contains 478 results.

> People smarter than I am have used math to prove that 5-character prefixes are sufficient to maintain k-anonymity for this database.

> In short: your plaintext passwords are protected if you use this library. You won't leak enough data to identity which passwords you're searching for.

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,before making a change.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
