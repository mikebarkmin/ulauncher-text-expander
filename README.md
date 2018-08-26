# ulauncher-text-expander

> Expand Text snippets directly from Ulauncher with Placeholder support.

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7
* [Date Parser library](https://dateparser.readthedocs.io/en/latest/) - Used to parse date placeholders.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-text-expander```

Where:

* name: its an unique identifier for the placeholder. must by unique in the snippet.
* label: A description of the placeholder. This is the label that will appear on the Dialog window to fill in the placeholder values as the description of the placeholder.
* default: A default value of the placeholder


## Usage

- For your snippets to be loaded by the extension, place then in .txt files in the snippets directory. By default, the extension will look for files in ```~/.config/ulauncher/ext_preferences/text-expander/expansions```. You can change it the extension settings.
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
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License

MIT
