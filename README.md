# Screentime Passcode Generator

This is a simple python Flask app that generates (by default) a 4-digit numeric
passcode every week for use with Apple iOS's Screen Time feature. The idea is to
(partially) automate credential rotation on a weekly basis to minimize the blast
radius of nosy kiddos discovering the Screen Time passcode.

A primary goal of this "app" is simplicity, so it doesn't use any kind of
external storages to persist the "secret" passcode. All it does is use the
current week number (since UTC epoch) to seed a PRNG, which should be "good
enough" to foil most kiddos. Obviously, this is not cryptographically secure.
Additionally, there is no authentication for the web page, so you'll need to
keep the URL on which it's hosted as secret as possible.

## Flow

The passcode will rotate once every Thursday at 00:00 UTC, so the first "parent"
to modify a child's Screen Time settings will need to manually update the
passcode with the current contents of the web-app. After that, all "parents"
will be able to refer to the web-app for the remainder of the week.

## Setup

```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ zappa init
$ zappa deploy
```

Then, you can take the URL provided by Zappa and save it as a homescreen widget
on your (i.e. the "parent"'s) phone's homescreen or bookmarks.

[1]: https://github.com/miserlou/zappa
