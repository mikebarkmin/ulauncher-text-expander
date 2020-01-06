# ulauncher-text-expander

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-text-expander)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-text-expander.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-text-expander)
![License](https://img.shields.io/github/license/brpaz/ulauncher-text-expander.svg?style=for-the-badge)

> Expand Text snippets directly from [Ulauncher](https://ulauncher.io/)  with Placeholder support.

## Demo

![demo](demo.gif)

## Requirements

* [Ulauncher](https://ulauncher.io/) > 5
* Python >= 3

Before installing, make sure to install all the needed Python packages for your system.

```pip3 install dateparser glob2 gobject PyGObject```


## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-text-expander```

Where:

* name: its an unique identifier for the placeholder. must by unique in the snippet.
* label: A description of the placeholder. This is the label that will appear on the Dialog window to fill in the placeholder values as the description of the placeholder.
* default: A default value of the placeholder


## Usage

- For your snippets to be loaded by the extension, place then in .txt files in the snippets directory. By default, the extension will look for files in ```"~/.config/ulauncher/text-expander/expansions"```. You can change it the extension settings.
- Type ```tex``` in Ulauncher and select the snippet you want to use. It the snippet has any placeholders, a new window will appear where you can fill the values of that placeholders. After that the final snippet with the placeholders filled in will be copied to the clipboard.


## Placeholders format

* This extension supports, simple text, select box and date placeholders.

#### Text input type placeholders

Text input placeholders allows you to ask for simple text values.

You can define input placeholders in your snippet like this:

```
@input({"name":"hello","label":"This is some placeholder", "default":"Some default value"})
```

#### Select type placeholders

Select placeholders allows you to ask for a value from a list of values

You can define input placeholders in your snippet like this:

```
@select({"name":"hello_s","label":"example select", "options":["option1", "option2"]})
```

The "name" and "value" is the same of input type. This field have an extra "options" key which contains the list of options that will appear in the select box for this placeholder.

#### Date placeholders

You can also have placeholders to specify dates. This will be automatically parsed and dont require the user to fill in any value.

The format is the following:

```@date(':date_expression'|:date_format)```

* The :date_expression can be any format supported by [Date Parser](https://dateparser.readthedocs.io/en/latest/) python library.
* The date_format can be any format supported by python [strftime](http://strftime.org/) function.

**Examples**

```@date('now'|%Y-%M-%d)``` - Render todays date in Year-Month-Day format.

```@date('last month'|%B)``` - Render the name of the last month in the users locale.

```@date('in 2 days'|%Y-%m-%d)``` - Render the date in two days.

```@date('10 days ago'|%Y-%m-%d)``` - Render the date 10 days ago.

## Development

```
make link
make dev
```

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
