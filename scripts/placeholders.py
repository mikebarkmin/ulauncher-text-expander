# pylint: skip-file
"""
This script parses the text expansion file contents and displays a dialog to ask the user to fill in any placeholders
defined in the text snippet.
"""

import sys
import gi
import re
import json
import dateparser

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

RE_INPUT_PLACEHOLDERS = re.compile(r"@input\(([^)]+)\)", re.IGNORECASE)

RE_SELECT_PLACEHOLDERS = re.compile(r"@select\(([^)]+)\)", re.IGNORECASE)

RE_DATE_PLACEHOLDERS = re.compile(r"@date\(([^)]+)\)", re.IGNORECASE)

GTK_STYLE = """
* {
    -GtkDialog-content-area-spacing: 20;
}

#content-area {
 padding: 50px;
}

#content-area label {
    font-weight: bold;
}
"""


def parse_date_placeholders(contents):
    """ Parses the date type placeholders """

    placeholders = RE_DATE_PLACEHOLDERS.findall(contents)

    for placeholder in placeholders:

        try:
            value, dt_format = placeholder.split('|')

            dt = dateparser.parse(value)

            if dt is not None:
                formatted_dt = dt.strftime(dt_format)

                contents = re.sub('@date\(%s\)' % re.escape(placeholder),
                                  formatted_dt.title(), contents, 1)
        except ValueError:
            pass

    return contents


class PlaceholdersDialog(Gtk.Dialog):
    """ Dialog window that asks for the values of the required placeholders for the text snippet """

    def __init__(self, content, input_placeholders=[], select_placeholders=[]):

        Gtk.Dialog.__init__(self,
                            "Fill in the placeholder values",
                            None,
                            0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                Gtk.STOCK_OK, Gtk.ResponseType.OK),
                            use_header_bar=True)
        self.content = content
        self.inputs = []
        self.selects = []

        # configure window size and position
        #self.set_default_size(350, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_keep_above(True)

        self.box = self.get_content_area()
        self.box.set_name("content-area")  # needed, so we can apply styles.

        self.build_widgets_for_input_placeholders(input_placeholders)
        self.build_widgets_for_select_placeholders(select_placeholders)

        self.load_styles()

        self.show_all()

    def load_styles(self):
        """ Loads CSS """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(GTK_STYLE)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def build_widgets_for_input_placeholders(self, placeholders=[]):
        """ Parses the text, extract any input placeholders variables and builds the ui to ask for the placeholders values """

        for ph in placeholders:
            data = json.loads(ph)

            key = data['name']

            row = Gtk.HBox(spacing=20)
            row.set_homogeneous(True)

            label = Gtk.Label(data['label'])
            label.set_line_wrap(True)

            entry = Gtk.Entry()

            if 'default' in data:
                entry.set_text(data['default'])

            row.add(label)
            row.add(entry)

            self.inputs.append({'key': key, 'widget': entry})
            self.box.add(row)

    def build_widgets_for_select_placeholders(self, placeholders=[]):
        """  Parses the text, extract any select placeholders variables and builds the ui to ask for the placeholders values """

        # iterates over all the placeholders and builds the form to insert its values
        for ph in placeholders:
            data = json.loads(ph)
            key = data['name']

            row = Gtk.HBox(spacing=20)
            row.set_homogeneous(True)

            label = Gtk.Label(data['label'])
            label.set_line_wrap(True)

            widget = Gtk.ComboBoxText()

            for option in data['options']:
                widget.append_text(option)

            row.add(label)
            row.add(widget)

            self.selects.append({'key': key, 'widget': widget})
            self.box.add(row)

    def get_processed_content(self):
        """ Replaces the variables and returns the final content """

        for item in self.inputs:
            placeholder_value = item['widget'].get_text()
            self.content = re.sub('@input\({"name":"%s"[^}]+}\)' % item['key'],
                                  placeholder_value, self.content, 1)

        for item in self.selects:
            placeholder_value = item['widget'].get_active_text()
            if placeholder_value is None:
                placeholder_value = ""

            self.content = re.sub(
                '@select\({"name":"%s"[^}]+}\)' % item['key'],
                placeholder_value, self.content, 1)

        return self.content


file_path = sys.argv[1]

if file_path is None:
    print("Please specify a valid file path")
    sys.exit(-1)

# Read the contents from the snippet file.
with open(file_path, 'r') as f:
    contents = f.read().decode('utf-8')

# Parse Date placeholders
contents = parse_date_placeholders(contents)

select_placeholders = RE_SELECT_PLACEHOLDERS.findall(contents)
input_placeholders = RE_INPUT_PLACEHOLDERS.findall(contents)

if input_placeholders or select_placeholders:
    dialog = PlaceholdersDialog(contents, input_placeholders,
                                select_placeholders)
    dialog.connect("destroy", Gtk.main_quit)

    result = dialog.run()

    if result == Gtk.ResponseType.OK:
        contents = dialog.get_processed_content()

print(contents.encode('utf-8'))

sys.exit(0)
